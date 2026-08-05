# T-0001 — Khởi tạo solution .NET 8

## Trạng thái
`ready`

## Mục tiêu
Tạo solution rỗng `LocalWP.sln` dùng .NET 8 làm nền tảng cho toàn bộ dự án.

## Phạm vi
- Tạo `global.json` pin .NET SDK 8.
- Tạo `LocalWP.sln`.
- Tạo `Directory.Build.props` với nullable, implicit usings và warnings-as-errors.
- Chưa tạo project ứng dụng.

## Ngoài phạm vi
- Không cài Avalonia.
- Không thêm package.
- Không tạo Domain/Application/Infrastructure.
- Không viết business code.

## Dependency
- Repository bootstrap đã merge.

## Yêu cầu bảo mật
- Không thêm secret hoặc credential.
- Không thêm script tải executable bên ngoài.

## Acceptance criteria
- [ ] `dotnet --version` dùng major 8.
- [ ] `dotnet sln LocalWP.sln list` chạy thành công.
- [ ] Repository không có warning cấu hình mới.

## Test bắt buộc
- `dotnet --info`
- `dotnet sln LocalWP.sln list`

## Branch gợi ý
`feat/init-solution-yyyyMMdd-HHmm`
