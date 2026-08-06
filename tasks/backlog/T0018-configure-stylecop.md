# T0018 — Configure stylecop

## UID bất biến
`BOOT-018`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0017` phải hoàn thành và merge.

## Branch bắt buộc
`feat/configure-stylecop-yyyyMMdd-HHmm`

## Mục tiêu
Cấu hình StyleCop Analyzers thống nhất ở cấp repository bằng Central Package Management.

## Phạm vi
- Dùng package ổn định `StyleCop.Analyzers` phiên bản `1.1.118`.
- Khai báo version trong `Directory.Packages.props`.
- Áp dụng analyzer cho toàn bộ project qua `Directory.Build.props`.
- Đặt `PrivateAssets` là `all` để package không truyền sang consumer.
- Chỉ nạp analyzer/build assets cần thiết.

## Ngoài phạm vi
- Không cấu hình rule chi tiết trong `.editorconfig`; phần đó thuộc `T0019`.
- Không sửa mã runtime chỉ để né cảnh báo.
- Không đổi kiến trúc hoặc project references.
- Không thêm analyzer khác.

## Yêu cầu bảo mật
- Package chỉ dùng lúc build và không trở thành dependency runtime.
- Không thêm secret, credential hoặc process call.
- Không tắt cảnh báo bảo mật.

## Acceptance criteria
- [x] `StyleCop.Analyzers` có version tập trung, ổn định và xác định rõ.
- [x] StyleCop áp dụng thống nhất cho toàn bộ project.
- [x] Package được đánh dấu `PrivateAssets=all`.
- [x] Không thay đổi mã runtime, kiến trúc hoặc project references.
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
- `T0019`
