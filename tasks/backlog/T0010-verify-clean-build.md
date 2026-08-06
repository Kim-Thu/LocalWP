# T0010 — Verify clean build

## UID bất biến
`BOOT-010`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0009` phải hoàn thành và merge.

## Branch bắt buộc
`feat/verify-clean-build-yyyyMMdd-HHmm`

## Mục tiêu
Xác minh toàn bộ solution có thể restore, build, test và kiểm tra format bằng một bộ lệnh chuẩn, có tài liệu quan sát được.

## Phạm vi
- Chuẩn hóa lệnh kiểm tra trên `LocalWP.sln` với cấu hình `Release`.
- Ghi nhận quy trình và tiêu chí kết quả tại `docs/BUILD_VERIFICATION.md`.
- Không thay đổi mã runtime hoặc dependency.

## Ngoài phạm vi
- Không thêm package hoặc framework test.
- Không sửa kiến trúc hay project references.
- Không làm nội dung task kế tiếp.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không bỏ qua lỗi CI, warning hoặc security scan.
- Không thêm dependency ngoài phạm vi để né lỗi.

## Acceptance criteria
- [x] Có bộ lệnh chuẩn chỉ rõ solution và cấu hình build.
- [x] Có tài liệu mô tả kết quả yêu cầu và cách xử lý khi xác minh thất bại.
- [x] Không thay đổi mã runtime, kiến trúc hoặc dependency.
- [x] Không mở rộng ngoài phạm vi.
- [ ] CI, security scan và format xanh trên PR.

## Kiểm tra bắt buộc
```bash
dotnet restore LocalWP.sln
dotnet build LocalWP.sln --configuration Release --no-restore
dotnet test LocalWP.sln --configuration Release --no-build
dotnet format LocalWP.sln --verify-no-changes --no-restore
```

## Rollback
Revert PR; không có thay đổi dữ liệu runtime.

## Task mở khóa tiếp theo
- `T0011`
