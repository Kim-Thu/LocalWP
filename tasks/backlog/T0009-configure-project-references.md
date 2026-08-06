# T0009 — Configure project references

## UID bất biến
`BOOT-009`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0008` phải hoàn thành và merge.

## Branch bắt buộc
`feat/configure-project-references-yyyyMMdd-HHmm`

## Mục tiêu
Cấu hình dependency giữa các project hiện có theo kiến trúc phân lớp.

## Phạm vi
- `LocalWP.Application` tham chiếu `LocalWP.Domain`.
- `LocalWP.Infrastructure` tham chiếu `LocalWP.Application` và `LocalWP.Domain`.
- `LocalWP.Desktop` tham chiếu `LocalWP.Application` và `LocalWP.Infrastructure` để làm composition root; UI vẫn không gọi trực tiếp hạ tầng.
- `LocalWP.SystemHelper` tham chiếu `LocalWP.Application` và `LocalWP.Infrastructure`.
- UnitTests tham chiếu Domain và Application.
- IntegrationTests tham chiếu Infrastructure và SystemHelper.

## Ngoài phạm vi
- Không thêm package, framework test hoặc mã runtime.
- Không làm nội dung task tiếp theo.
- Không đổi kiến trúc hoặc package chính nếu chưa có ADR.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không tạo dependency vòng.
- Domain không tham chiếu project khác.

## Acceptance criteria
- [x] Project references phản ánh đúng hướng dependency của kiến trúc.
- [x] Domain giữ độc lập.
- [x] Không có dependency vòng.
- [x] Không mở rộng ngoài phạm vi.
- [ ] CI, security scan và format xanh.

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
- `T0010`
