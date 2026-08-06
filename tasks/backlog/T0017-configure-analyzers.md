# T0017 — Configure analyzers

## UID bất biến
`BOOT-017`

## Trạng thái
`done`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0016` phải hoàn thành và merge.

## Branch bắt buộc
`feat/configure-analyzers-yyyyMMdd-HHmm`

## Mục tiêu
Bật và chuẩn hóa bộ phân tích mã nguồn .NET ở cấp repository.

## Phạm vi
- Bật `<EnableNETAnalyzers>true</EnableNETAnalyzers>` trong `Directory.Build.props`.
- Dùng `<AnalysisLevel>latest-recommended</AnalysisLevel>`.
- Dùng `<AnalysisMode>Recommended</AnalysisMode>` để áp dụng bộ rule khuyến nghị ổn định.
- Không thêm package analyzer bên ngoài trong task này.

## Ngoài phạm vi
- Không cấu hình StyleCop; phần đó thuộc `T0018`.
- Không sửa mã runtime để né warning.
- Không đổi kiến trúc, package chính hoặc project references.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không vô hiệu hóa cảnh báo bảo mật.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] .NET analyzers được bật rõ ràng ở cấp repository.
- [x] Analysis level dùng bộ rule mới nhất được khuyến nghị.
- [x] Analysis mode dùng tập rule khuyến nghị.
- [x] Không thêm package analyzer bên ngoài.
- [x] Không mở rộng ngoài phạm vi.
- [x] CI, security scan và format xanh.

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
- `T0018`
