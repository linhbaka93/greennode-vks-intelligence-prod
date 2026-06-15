# prompts/ — Agent specs

Mỗi file là một **agent spec chi tiết** (persona + scope + responsibilities + output
contract + constraints + collaboration), đồng thời là system prompt mà runtime nạp.
`Specialist.prompt_file` trỏ tới file ở đây; runtime nạp `_output_policy.md` và
`_social_sources.md` làm header chung rồi nối với spec riêng của agent.

Tách spec khỏi code để chỉnh giọng điệu/scope/policy mà không cần đổi Python.

## Chuẩn spec

Kế thừa chuẩn agent definition chi tiết, thích ứng cho runtime multi-agent:

1. Header — role, trigger, workload, ngôn ngữ
2. Role — agent là ai, hoạt động như vai trò nào
3. Scope — In-scope / Out-of-scope rõ ràng
4. Hành vi mỗi lần được gọi + tri thức domain (bảng đối thủ/trend/component...)
5. **Output Contract** — JSON `AgentResult` (hoặc verdict) mà agent phải trả về
6. Constraints — ràng buộc dữ liệu/phân tích/legal
7. Collaboration — phối hợp qua supervisor + shared memory (không gọi trực tiếp agent khác)
8. Performance bar / Initialization
9. Ví dụ + Ghi chú quan trọng

Cadence (hằng tuần/tháng) **không** nằm trong spec — đó là việc của n8n. Spec chỉ mô tả
hành vi từng lần được gọi.

## Danh sách

| File | Agent | Milestone |
|---|---|---|
| `_output_policy.md` | header chung mọi agent (nhãn nguồn inline, so-what, data-gap honesty) | 1 |
| `_social_sources.md` | social allowlist chung cho agent specs, kèm URL page/post và citation rule | 1 |
| `_report_templates.md` | cấu trúc weekly/monthly cho synthesis | 1 |
| `qa_agent.md` | Q&A | 1 |
| `daily_intelligence_agent.md` | Daily Intelligence | 1 |
| `market_trend_agent.md` | Market Trend | 1 |
| `competitor_agent.md` | Competitor | 1 |
| `pricing_agent.md` | Pricing | 1 |
| `quality_critic_agent.md` | Quality Critic | 1 |
| `battlecard_agent.md` | Battlecard | 1 |
| `memory_curator_agent.md` | Memory Curator | 1 |
| `regulatory_agent.md` | Regulatory | sau |
| `positioning_agent.md` | Positioning | sau |
