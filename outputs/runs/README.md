# outputs/runs/ — Artifact store

Mỗi run sinh một thư mục `<run_id>/` để audit. Nội dung run bị gitignore (chỉ giữ
README + .gitkeep). Dashboard đọc `metadata.json` ở đây.

```
outputs/runs/
  2026-06-05_weekly-digest/
    request.json          input đã nhận
    plan.json             TaskPlan supervisor dựng
    market_trend_agent.json
    competitor_agent.json
    pricing_agent.json
    synthesis.md          output gộp thô
    quality.json          verdict + score
    final.md              bản sẵn sàng publish/preview
    metadata.json         model/agent, token, quality, publish, approval
    fallback_trace.json   các bước fallback đã đi
    errors.json           lỗi/retry history
```

`run_id` quy ước: `<YYYY-MM-DD>_<task-type>` cho run định kỳ, hậu tố thời gian khi
chạy nhiều lần trong ngày.
