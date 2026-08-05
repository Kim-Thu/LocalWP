# T0001 — Define repository metadata

## Trạng thái
`review`

## Epic
`E00 — Repository and governance`

## Dependency bắt buộc
- `Repository bootstrap` đã hoàn thành và merge qua PR #1.

## Branch bắt buộc
`maint/define-repository-metadata-20260806-0601`

## Mục tiêu
Hoàn thành duy nhất phần **define repository metadata** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi đã thực hiện
- Tạo `docs/REPOSITORY_METADATA.md` làm nguồn metadata chuẩn.
- Xác định tên sản phẩm, repository owner, stack, nền tảng MVP, trạng thái và mô tả repository.
- Xác định GitHub description và topics đề xuất.
- Đồng bộ `README.md` với metadata chuẩn.
- Chặn việc tái sử dụng tên cũ `LocalBox` trong tài liệu và namespace mới.

## Ngoài phạm vi
- Không thay đổi GitHub repository settings bằng API.
- Không tạo solution hoặc project .NET.
- Không làm nội dung `T0002`.
- Không đổi kiến trúc hoặc package.

## Yêu cầu bảo mật
- Không thêm secret hoặc credential.
- Không thêm script hoặc executable.
- Không ghi dữ liệu nhạy cảm vào metadata.

## Acceptance criteria
- [x] Có nguồn chuẩn xác định repository metadata.
- [x] README dùng đúng tên, stack và trạng thái dự án.
- [x] Tài liệu liên kết đến BRD, SRS, PLAN, master task và agent entry point.
- [x] Không mở rộng ngoài phạm vi.
- [x] Không có secret.

## Kiểm tra bắt buộc
- Kiểm tra Markdown render đúng.
- Kiểm tra toàn bộ liên kết file nội bộ tồn tại.
- CI và security scan phải xanh trên PR.

## Rollback
Revert PR. Không có thay đổi dữ liệu hoặc runtime.

## Task mở khóa tiếp theo
- `T0002`
