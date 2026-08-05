# T0001 — Initialize .NET 8 solution

## UID bất biến
`BOOT-001`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `Repository bootstrap` đã hoàn thành và merge.

## Branch bắt buộc
`feat/initialize-net-8-solution-20260806-0632`

## Mục tiêu
Khởi tạo solution `.NET 8` tối thiểu làm điểm gốc cho các project của LocalWP.

## Phạm vi
- Tạo `LocalWP.sln`.
- Khai báo cấu hình `Debug` và `Release` cho `Any CPU`.
- Giữ solution chưa chứa project để task sau thêm từng project độc lập.

## Ngoài phạm vi
- Không tạo project.
- Không thêm package.
- Không thêm `global.json`, `Directory.Build.props` hoặc `Directory.Packages.props`.
- Không làm nội dung `T0002`.

## Yêu cầu triển khai
- Solution phải đọc được bởi Visual Studio 2022 và .NET CLI.
- File phải ổn định, không chứa đường dẫn máy cục bộ.
- Không thêm cấu hình ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret hoặc credential.
- Không thêm script tải executable.
- Không thêm đường dẫn tuyệt đối từ máy phát triển.

## Acceptance criteria
- [x] Có file `LocalWP.sln` tại root repository.
- [x] Solution có cấu hình `Debug|Any CPU` và `Release|Any CPU`.
- [x] Solution chưa chứa project.
- [x] Không mở rộng ngoài phạm vi.
- [ ] CI và security scan xanh.

## Kiểm tra bắt buộc
```bash
dotnet sln LocalWP.sln list
dotnet restore LocalWP.sln
dotnet build LocalWP.sln --configuration Release --no-restore
```

## Rollback
Revert PR; task không thay đổi runtime hoặc dữ liệu người dùng.

## Task mở khóa tiếp theo
- `T0002`
