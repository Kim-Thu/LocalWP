# T0016 — Treat warnings as errors

## UID bất biến
`BOOT-016`

## Trạng thái
`done`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0015` phải hoàn thành và merge.

## Branch bắt buộc
`feat/treat-warnings-as-errors-yyyyMMdd-HHmm`

## Mục tiêu
Bắt buộc toàn bộ project .NET xử lý cảnh báo biên dịch như lỗi thông qua cấu hình build dùng chung tại thư mục gốc.

## Phạm vi
- Xác minh `Directory.Build.props` khai báo `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`.
- Giữ chính sách áp dụng thống nhất cho toàn bộ project kế thừa cấu hình chung.
- Không sửa mã runtime, package, kiến trúc hoặc project references.

## Ngoài phạm vi
- Không làm nội dung task kế tiếp.
- Không lặp cấu hình trong từng project.
- Không vô hiệu hóa warning hoặc analyzer để né lỗi.
- Không thêm package hoặc refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không giảm mức warning hoặc vô hiệu hóa analyzer.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] `Directory.Build.props` bật `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`.
- [x] Chính sách áp dụng ở cấp repository, không lặp trong từng project.
- [x] Không thay đổi mã runtime, package, kiến trúc hoặc project references.
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
- `T0017`
