"""Phòng vệ JSON cho output của specialist agent.

Thứ tự xử lý: parse trực tiếp → trích JSON object lớn nhất → 1 lần repair prompt
→ validate theo schema. Nếu vẫn fail, đánh dấu agent result là failed/partial.
Supervisor không được synthesis từ JSON chưa validate.
"""

from __future__ import annotations

import json
import re
from typing import TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)

_CODE_BLOCK = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)


def extract_json(text: str) -> str:
    """Trích JSON object đầu tiên trong code fence, hoặc object lớn nhất trong text."""
    m = _CODE_BLOCK.search(text)
    if m:
        return m.group(1)

    # Tìm cặp { ... } ngoài cùng từ đầu
    start = text.find("{")
    if start == -1:
        raise ValueError("Không tìm thấy JSON object trong text")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    raise ValueError("JSON object không đóng ngoặc hoàn chỉnh")


def parse_into(text: str, schema: type[T]) -> T:
    """Parse + validate; thử trực tiếp trước, rồi trích JSON, raise nếu cả hai fail."""
    stripped = text.strip()
    for candidate in (stripped,):
        try:
            return schema.model_validate_json(candidate)
        except (ValidationError, ValueError, json.JSONDecodeError):
            try:
                return schema.model_validate(_coerce_schema_data(json.loads(candidate), schema))
            except (ValidationError, ValueError, json.JSONDecodeError, TypeError):
                pass
    try:
        extracted = extract_json(stripped)
        try:
            return schema.model_validate_json(extracted)
        except (ValidationError, ValueError, json.JSONDecodeError):
            return schema.model_validate(_coerce_schema_data(json.loads(extracted), schema))
    except (ValidationError, ValueError, json.JSONDecodeError) as exc:
        raise ValueError(f"Không parse được text vào {schema.__name__}: {exc}") from exc


def _stringify_item(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        if {"finding", "source", "impact", "recommendation"} & set(value):
            parts = [
                value.get("source", ""),
                value.get("finding", "") or value.get("claim", ""),
                f"Tác động tới GreenNode: {value.get('impact', '')}" if value.get("impact") else "",
                f"GreenNode nên: {value.get('recommendation', '')}" if value.get("recommendation") else "",
            ]
            return " — ".join(p for p in parts if p)
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def _stringify_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [_stringify_item(item) for item in value]
    return [_stringify_item(value)]


def _coerce_schema_data(data, schema: type[BaseModel]):
    if schema.__name__ != "AgentResult" or not isinstance(data, dict):
        return data

    coerced = dict(data)
    if coerced.get("status") == "success":
        coerced["status"] = "ok"
    if "keyfindings" in coerced and "key_findings" not in coerced:
        coerced["key_findings"] = coerced.pop("keyfindings")
    if "recommendedactions" in coerced and "recommended_actions" not in coerced:
        coerced["recommended_actions"] = coerced.pop("recommendedactions")

    strategic = coerced.pop("strategicimplications", None)
    if strategic:
        coerced.setdefault("key_findings", [])
        coerced["key_findings"].extend(_stringify_list(strategic))

    # memory_curator trả {"patches": [...]} — map sang key_findings để synthesis đọc được
    patches = coerced.pop("patches", None)
    if patches and isinstance(patches, list):
        coerced.setdefault("key_findings", [])
        coerced.setdefault("recommended_actions", [])
        for patch in patches:
            if not isinstance(patch, dict):
                continue
            op = patch.get("op", "update")
            path = patch.get("path", "")
            reason = patch.get("reason", "")
            confidence = patch.get("confidence", "medium")
            if reason or path:
                coerced["key_findings"].append(
                    f"[Patch {op}] {path} (confidence: {confidence}) — {reason}"
                )
                coerced["recommended_actions"].append(
                    f"Áp dụng patch {op} cho {path}: {reason[:120]}"
                )

    for field in ("key_findings", "risks", "gaps", "recommended_actions"):
        if field in coerced:
            coerced[field] = _stringify_list(coerced[field])

    coerced.setdefault("agent", "")
    coerced.setdefault("task_id", "")
    return coerced


def repair_prompt(broken: str, schema: type[BaseModel]) -> str:
    """Prompt yêu cầu model sửa JSON hỏng về đúng schema (gọi tối đa 1 lần)."""
    schema_def = json.dumps(schema.model_json_schema(), indent=2, ensure_ascii=False)
    return (
        "JSON dưới đây bị lỗi hoặc thiếu trường. "
        "Sửa để khớp JSON Schema. Chỉ trả về JSON hợp lệ, không giải thích.\n\n"
        f"Schema:\n{schema_def}\n\n"
        f"JSON lỗi:\n{broken}\n\n"
        "JSON đã sửa:"
    )
