# T0011 — Add directory.build.props

## UID bất biến
`BOOT-011`

## Trạng thái
`done`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0010` phải hoàn thành và merge.

## Branch bắt buộc
`feat/add-directory-build-props-yyyyMMdd-HHmm`

## Mục tiêu
Thêm `Directory.Build.props` tại thư mục gốc để áp dụng thống nhất cấu hình build cơ bản cho toàn bộ project .NET.

## Phạm vi
- Target `.NET 8` cho các project kế thừa cấu hình chung.
- Bật nullable và implicit usings.
- Biến warning thành lỗi.
- Bật mức phân tích `latest-recommended`.
- Bật deterministic build.
- Không thay đổi package hoặc mã runtime.

## Ngoài phạm vi
- Không thêm `Directory.Packages.props`.
- Không sửa từng file project để loại bỏ thuộc tính trùng lặp.
- Không thêm analyzer package.
- Không làm nội dung task kế tiếp.
- Không đổi kiến trúc hoặc package chính.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không giảm mức warning hoặc vô hiệu hóa analyzer.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] `Directory.Build.props` tồn tại tại thư mục gốc.
- [x] Nullable và implicit usings được bật thống nhất.
- [x] Warning được xử lý như lỗi.
- [x] Analysis level và deterministic build được cấu hình.
- [x] Không thay đổi mã runtime, package hoặc kiến trúc.
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
- `T0012`
