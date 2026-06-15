"""Deterministic quality gate chạy trước Quality Critic LLM.

Bắt lỗi cứng (thiếu section, placeholder chưa fill, thiếu nguồn, pricing không
có ngày) và phân loại output thành 4 trạng thái pass/needs_review/revise/blocked
theo điểm số. Critic LLM chạy thêm trên lớp này, không thay thế nó.
"""

from __future__ import annotations

import re

from vks_intelligence.contracts import QualityResult, QualityVerdict, TaskType

MIN_LENGTH = 800
MAX_LENGTH = 15_000
MIN_SOURCES = 3

REQUIRED_SECTIONS = (
    r"#+\s*TL;DR",
    r"#+\s*(Competitor Moves|Market Signals|Action Items|Động thái|Tín hiệu|Việc cần|Key Findings)",
    r"#+\s*(Sources|Nguồn)",
)

FORBIDDEN_PLACEHOLDERS = (
    r"\[TODO\]",
    r"\[XXX\]",
    r"\[PLACEHOLDER\]",
    r"\[FILL IN\]",
    r"\[INSERT.*?\]",
    r"\.\.\.\.+",
    r"Lorem ipsum",
)

HALLUCINATION_RED_FLAGS = (
    r"\breportedly\b",
    r"\bsources say\b",
    r"\binsider information\b",
    r"\bcompetitor admits\b",
)

THRESHOLDS = {
    "pass": 0.80,
    "needs_review": 0.65,
    "revise": 0.45,
}

# Pricing / date freshness
_PRICING_SECTION = re.compile(
    r"(pricing|giá|tcо|cost)", re.IGNORECASE
)
_DATE_MENTION = re.compile(
    r"\b(20\d\d-\d{2}-\d{2}|\d{1,2}/\d{4}|Q[1-4]/20\d\d|tháng \d+/20\d\d)\b"
)
_URL_MENTION = re.compile(r"https?://\S+", re.IGNORECASE)
_WEB_SOURCE_LINE = re.compile(r"^\s*(?:[-*]\s*)?\[(Search|Scrape|Social)\].*$", re.IGNORECASE)


def validate_output(content: str, task_type: TaskType | None = None) -> QualityResult:
    """Chấm điểm content và trả QualityResult với verdict 4 trạng thái."""
    failures: list[str] = []
    warnings: list[str] = []
    deductions = 0.0

    # --- Hard blockers (deduct heavily) ---

    length = len(content)
    if length < MIN_LENGTH:
        failures.append(f"Output quá ngắn ({length} ký tự, tối thiểu {MIN_LENGTH})")
        deductions += 0.50
    elif length > MAX_LENGTH:
        warnings.append(f"Output rất dài ({length} ký tự); cân nhắc tóm tắt")

    for pattern in FORBIDDEN_PLACEHOLDERS:
        if re.search(pattern, content, re.IGNORECASE):
            failures.append(f"Placeholder chưa fill: {pattern}")
            deductions += 0.30

    # Required sections — chỉ áp với weekly digest / competitor monitor
    if task_type in (TaskType.WEEKLY_DIGEST, TaskType.COMPETITOR_MONITOR, None):
        for section_re in REQUIRED_SECTIONS:
            if not re.search(section_re, content, re.IGNORECASE):
                failures.append(f"Thiếu section bắt buộc: {section_re}")
                deductions += 0.15

    # Source count
    source_matches = re.findall(
        r"\[(?:Workspace|RSS|Search|Scrape|Social|Suy luận|Chưa xác minh)\]", content
    )
    if len(source_matches) < MIN_SOURCES and task_type not in (TaskType.QA,):
        warnings.append(
            f"Ít nhãn nguồn ({len(source_matches)}); khuyến nghị ≥ {MIN_SOURCES}"
        )
        deductions += 0.05

    # Search/scrape claims must be directly citable.
    for line in content.splitlines():
        if not _WEB_SOURCE_LINE.search(line):
            continue
        missing: list[str] = []
        if not _URL_MENTION.search(line):
            missing.append("URL")
        if not _DATE_MENTION.search(line):
            missing.append("ngày")
        if missing:
            failures.append(
                f"{line[:90]}... thiếu {'/'.join(missing)} cho nguồn Search/Scrape/Social"
            )
            deductions += 0.25

    # Pricing without date
    if _PRICING_SECTION.search(content) and not _DATE_MENTION.search(content):
        failures.append("Pricing mention không kèm ngày dữ liệu")
        deductions += 0.20

    # Hallucination red flags (soft)
    for flag_re in HALLUCINATION_RED_FLAGS:
        if re.search(flag_re, content, re.IGNORECASE):
            warnings.append(f"Red flag hallucination: '{flag_re}'")
            deductions += 0.10

    # --- Score & verdict ---
    score = max(0.0, round(1.0 - deductions, 3))

    if score >= THRESHOLDS["pass"]:
        verdict = QualityVerdict.PASS
    elif score >= THRESHOLDS["needs_review"]:
        verdict = QualityVerdict.NEEDS_REVIEW
    elif score >= THRESHOLDS["revise"]:
        verdict = QualityVerdict.REVISE
    else:
        verdict = QualityVerdict.BLOCKED

    return QualityResult(
        verdict=verdict,
        score=score,
        failures=failures,
        warnings=warnings,
    )
