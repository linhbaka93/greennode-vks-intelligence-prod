"""Rubric chấm điểm output trong eval — giảm regression khi đổi model/prompt.

Tách thành các tiêu chí có trọng số; điểm tổng quy về [0,1] để so với ngưỡng
publish/approval. Dùng cho cả test tự động lẫn review thủ công.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Criterion:
    key: str
    weight: float
    description: str


RUBRIC: tuple[Criterion, ...] = (
    Criterion("sourced_claims",    0.30, "Mọi claim factual có nguồn và nhãn"),
    Criterion("vietnamese_output", 0.15, "Output tiếng Việt, executive-readable"),
    Criterion("required_sections", 0.20, "Đủ section theo template loại task"),
    Criterion("actionability",     0.15, "Có recommendation/next action cụ thể"),
    Criterion("balance",           0.10, "Thừa nhận điểm yếu, không cherry-pick"),
    Criterion("format_safety",     0.10, "Telegram split an toàn, không placeholder"),
)


def score(criteria_results: dict[str, float]) -> float:
    """Gộp điểm từng tiêu chí (0..1) theo trọng số thành điểm tổng [0,1].

    Tiêu chí không có trong criteria_results tính là 0.
    Trọng số tổng không nhất thiết phải == 1 — normalize theo tổng weight thực tế.
    """
    total_weight = sum(c.weight for c in RUBRIC)
    if total_weight == 0:
        return 0.0
    weighted_sum = sum(
        c.weight * max(0.0, min(1.0, criteria_results.get(c.key, 0.0)))
        for c in RUBRIC
    )
    return round(weighted_sum / total_weight, 3)
