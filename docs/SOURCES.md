# Social Source Registry

Danh sach nay la allowlist social public cho `tools/source_tool.py`. Crawler chi fetch
URL nam trong registry; khong crawl lan sang link ngoai.

## Policy

- Social fetch la best-effort. Facebook, LinkedIn, X, YouTube co the tra login wall,
  consent wall, unsupported browser, hoac noi dung render bang JavaScript.
- Neu khong doc duoc noi dung public, evidence layer khong promote thanh `[Social]`
  claim va report se ghi ro: `khong fetch duoc trang social`.
- Chi coi social post la tin da xac nhan khi co URL public + ngay fetch/post + noi
  dung doc duoc.

## GreenNode

- Facebook: `greennode-facebook`
- Facebook post allowlist: `greennode-facebook-post-pfbid02k8gsea`
- LinkedIn: `greennode-linkedin`

## Vietnam Competitors

- Viettel IDC Facebook: `viettel-idc-facebook`
- Viettel IDC LinkedIn: `viettel-idc-linkedin`
- FPT Cloud Facebook: `fpt-cloud-facebook`
- FPT Cloud LinkedIn: `fpt-cloud-linkedin`
- FPT Cloud X: `fpt-cloud-x`
- FPT Cloud YouTube: `fpt-cloud-youtube`
- Bizfly Cloud Facebook: `bizfly-cloud-facebook`
- Bizfly Cloud LinkedIn: `bizfly-cloud-linkedin`
- Bizfly Cloud X: `bizfly-cloud-x`
- Bizfly Cloud Telegram: `bizfly-cloud-telegram`
- Bizfly Cloud YouTube: `bizfly-cloud-youtube`

## Hyperscalers

- AWS LinkedIn: `aws-linkedin`
- AWS X: `aws-x`
- AWS YouTube: `aws-youtube`
- Google Cloud Facebook: `google-cloud-facebook`
- Google Cloud LinkedIn: `google-cloud-linkedin`
- Google Cloud X: `google-cloud-x`
- Google Cloud YouTube: `google-cloud-youtube`
- GKE LinkedIn product page: `gke-linkedin`
- Azure Facebook: `azure-facebook`
- Azure LinkedIn: `azure-linkedin`
- Azure X: `azure-x`
- Azure YouTube: `azure-youtube`
