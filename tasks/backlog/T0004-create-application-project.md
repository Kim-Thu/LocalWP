# T0004 — Create application project

## UID bất biến
`BOOT-004`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0003` phải hoàn thành và merge.

## Branch bắt buộc
`feat/create-application-project-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **create Application project** theo BRD, SRS và kiến trúc hiện hành.

## Acceptance criteria
- [x] Application project tồn tại tại `src/LocalWP.Application`.
- [x] Project target `.NET 8` và bật nullable.
- [x] Application project đã được thêm vào `LocalWP.sln`.
- [x] Có marker type tối thiểu, chưa thêm use case hoặc dependency ngoài phạm vi.
- [ ] CI, security scan và format xanh.

## Kiểm tra bắt buộc
```bash
dotnet restore LocalWP.sln
dotnet build LocalWP.sln --configuration Release --no-restore
dotnet test LocalWP.sln --configuration Release --no-build
dotnet format LocalWP.sln --verify-no-changes --no-restore
```

## Rollback
Revert PR; không có dữ liệu runtime hoặc dữ liệu người dùng bị thay đổi.

## Task mở khóa tiếp theo
- `T0005`
