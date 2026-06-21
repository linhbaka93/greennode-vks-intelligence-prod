# Competitor Summary — 2026-06-21

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Blog | https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore | published_at=2026-06-19 — [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore) 2026-06-19 — AWS công bố GA tính năng Web Search trên Amazon Bedrock AgentCore, cho phép các agent AI truy cập web an toàn và tích hợp RAG pipeline doanh nghiệp. Tác động tới GreenNode: ❌ Feature gap về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent mà VKS chưa có. Khách hàng Enterprise muốn triển khai AI nhanh có thể chọn AWS nếu không cần data residency VN. GreenNode nên: Theo dõi thêm xem đối thủ nội địa (FPT/Viettel) có tích hợp tương tự vào K8s hay không để chuẩn bị battlecard.
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMikgFBVV95cUxPX3U0RW9nZ1NDWG9hR2lZZWRrMWpSeFVRTW5pZ3R1eURoLW8wQmRnTTVMQ1hOMkE0OW9PTzdHNjhQRDN5ajdfSVZQM0pMaEluRDQ3YUdxRVhjVVllbkhMb21LQlJMQkRSUmVjbkhWbDlaWmQyRFo4aDJDdkdZa042Vks3c3FHd3A5b2xialhsb2V3Zw?oc=5 | published_at=2026-06-20 — [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxPX3U0RW9nZ1NDWG9hR2lZZWRrMWpSeFVRTW5pZ3R1eURoLW8wQmRnTTVMQ1hOMkE0OW9PTzdHNjhQRDN5ajdfSVZQM0pMaEluRDQ3YUdxRVhjVVllbkhMb21LQlJMQkRSUmVjbkhWbDlaWmQyRFo4aDJDdkdZa042Vks3c3FHd3A5b2xialhsb2V3Zw?oc=5) 2026-06-20 — A10 Networks (nhà cung cấp hạ tầng mạng bảo mật) mua lại TrojAI Inc. để mở rộng lộ trình phát triển AI. Tác động tới GreenNode: ⚠️ Tín hiệu thị trường. Sự kiện này cho thấy xu hướng tích hợp AI vào hạ tầng mạng và bảo mật đang tăng tốc. GreenNode nên: Rà soát lại các đối tác bảo mật và AI hiện tại để đảm bảo VKS có thể hỗ trợ các workload AI-native an toàn, đặc biệt cho phân khúc Gov/Enterprise.
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMiiwFBVV95cUxQU1lNcmpDbkIxdllJVmQycUNHSmwxOXFoTXdqR05lOENMbHFtbmFPZTFSamtONzIyUzNpc3N0Z29fUU5sd21OX1I0a3hoYlJIVEpFdFE3S09WYmhoMllHSjdsdVAtaGV2bEZXSkx2aFpyem93dGdUXzlpTE5ERlJBcWd1WWlpdzRmRnpV?oc=5 | published_at=2026-06-19 — [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQU1lNcmpDbkIxdllJVmQycUNHSmwxOXFoTXdqR05lOENMbHFtbmFPZTFSamtONzIyUzNpc3N0Z29fUU5sd21OX1I0a3hoYlJIVEpFdFE3S09WYmhoMllHSjdsdVAtaGV2bEZXSkx2aFpyem93dGdUXzlpTE5ERlJBcWd1WWlpdzRmRnpV?oc=5) 2026-06-19 — Google tăng cường cạnh tranh với Nvidia trong thị trường chip AI. Tác động tới GreenNode: ⚠️ Tín hiệu gián tiếp. Cạnh tranh chip AI có thể dẫn đến giảm giá hoặc đa dạng hóa lựa chọn phần cứng GPU trong tương lai. GreenNode nên: Theo dõi giá GPU và khả năng tiếp cận chip mới để tối ưu TCO cho khách hàng cần training/inference nặng.

## Risks

- AWS tiếp tục dẫn đầu về AI-native infrastructure (Bedrock AgentCore, Web Search), tạo áp lực cho GreenNode nếu khách hàng ưu tiên tính năng AI mới hơn là data residency.
- Không có thông tin mới về đối thủ Tier 1 nội địa (Viettel, FPT, Bizfly) trong 24h qua, nhưng cần cảnh giác với các động thái M&A hoặc hợp tác chiến lược liên quan đến AI có thể xảy ra bất cứ lúc nào.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa có thông tin mới về vOKS trong 24h qua.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa xác minh được GPU node pool mới nhất.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, cần xác nhận lại SLA và K8s versions.
