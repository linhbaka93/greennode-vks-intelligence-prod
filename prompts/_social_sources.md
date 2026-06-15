# Social Sources (shared agent spec)

Danh sách này là social allowlist để agent nhận diện nguồn và cite đúng URL khi
`EvidenceBundle` chứa `[Social]`. Agent **không tự fetch** các URL này; việc fetch do
`source_tool.py` và `evidence_tool.py` thực hiện trước khi supervisor gọi agent.

Nếu social fetch bị chặn, thiếu text public, hoặc chỉ thấy login wall/consent wall,
không tạo claim đã xác nhận. Ghi vào `gaps` hoặc phần "Cần xác minh" với wording rõ:
`không fetch được trang social`.

## GreenNode

- GreenNode Facebook page: https://www.facebook.com/greennode23
- GreenNode Facebook post allowlist: https://www.facebook.com/greennode23/posts/pfbid02k8gseaPDWDWRzXG3KWsRgukfNv7EXq1cvxhgmBj42vnGitw3cBf8s174xycgmFeDl
- GreenNode LinkedIn page: https://www.linkedin.com/company/green-node/

## Vietnam Competitors

- Viettel IDC Facebook page: https://www.facebook.com/viettelidc/
- Viettel IDC LinkedIn page: https://www.linkedin.com/company/viettel-idc/
- FPT Cloud Facebook page: https://www.facebook.com/fptsmartcloud
- FPT Cloud LinkedIn page: https://www.linkedin.com/company/fpt-cloud/
- FPT Cloud X page: https://x.com/FPT_Cloud
- FPT Cloud YouTube channel: https://www.youtube.com/channel/UCJM51jaizo0jSbv35HD2nYA
- Bizfly Cloud Facebook page: https://facebook.com/BizflyCloud.VCCorp
- Bizfly Cloud LinkedIn page: https://www.linkedin.com/company/bizfly-cloud-vccorp/
- Bizfly Cloud X page: https://x.com/bizflycloud
- Bizfly Cloud Telegram channel: https://t.me/s/bizflycloudvn
- Bizfly Cloud YouTube channel: https://www.youtube.com/@giaiphapientoanammaybizfly9256

## Hyperscalers

- AWS LinkedIn page: https://www.linkedin.com/company/amazon-web-services/
- AWS X page: https://x.com/awscloud
- AWS YouTube channel: https://www.youtube.com/user/AmazonWebServices
- Google Cloud Facebook page: https://www.facebook.com/googlecloud/
- Google Cloud LinkedIn page: https://www.linkedin.com/showcase/google-cloud/
- Google Cloud X page: https://x.com/googlecloud
- Google Cloud YouTube channel: https://www.youtube.com/@googlecloudtech
- GKE LinkedIn product page: https://www.linkedin.com/products/google-cloud-google-kubernetes-engine/
- Azure Facebook page: https://www.facebook.com/microsoftazure/
- Azure LinkedIn page: https://www.linkedin.com/showcase/microsoft-azure/
- Azure X page: https://x.com/azure
- Azure YouTube channel: https://www.youtube.com/user/windowsazure

## Citation Rules For Social Evidence

- `[Social]` claim phải ghi account/channel + URL page/post + `fetched_at` hoặc
  `published_at`.
- Nếu chỉ có page URL nhưng không đọc được post/content, đưa vào `gaps`, không đưa vào
  `key_findings` như tin đã xác nhận.
- Nếu nội dung social trùng với RSS/scrape nguồn chính thức, ưu tiên cite nguồn chính
  thức, social chỉ dùng làm tín hiệu phụ.
