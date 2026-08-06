# T0014 — Enable nullable

## UID bất biến
`BOOT-014`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0013` phải hoàn thành và merge.

## Branch bắt buộc
`feat/enable-nullable-yyyyMMdd-HHmm`

## Mục tiêu
Bật nullable thống nhất cho toàn bộ project .NET thông qua cấu hình build dùng chung tại thư mục gốc.

## Phạm vi
- Xác minh `Directory.Build.props` tại thư mục gốc khai báo `<Nullable>enable</Nullable>`.
- Giữ nullable áp dụng thống nhất cho toàn bộ project kế thừa cấu hình chung.
- Không sửa mã runtime, package, kiến trúc hoặc project references.

## Ngoài phạm vi
- Không làm nội dung task kế tiếp.
- Không sửa từng file project để lặp lại cấu hình nullable.
- Không thêm analyzer hoặc package.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không giảm warning hoặc vô hiệu hóa analyzer.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] `Directory.Build.props` bật nullable bằng `<Nullable>enable</Nullable>`.
- [x] Cấu hình áp dụng ở cấp repository, không lặp trong từng project.
- [x] Không thay đổi mã runtime, package, kiến trúc hoặc project references.
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
- `T0015`
