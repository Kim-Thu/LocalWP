# T0006 — Create systemhelper project

## UID bất biến
`BOOT-006`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0005` phải hoàn thành và merge.

## Branch bắt buộc
`feat/create-systemhelper-project-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **create SystemHelper project** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi
- Tạo project `LocalWP.SystemHelper` target `.NET 8`.
- Bật nullable và implicit usings.
- Thêm marker type tối thiểu.
- Thêm project vào solution.

## Ngoài phạm vi
- Không thêm package, project reference hoặc helper hệ thống.
- Không tạo test project.
- Không làm nội dung task kế tiếp.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] SystemHelper project tồn tại tại `src/LocalWP.SystemHelper`.
- [x] Project target `.NET 8` và bật nullable.
- [x] SystemHelper project đã được thêm vào `LocalWP.sln`.
- [x] Có marker type tối thiểu, chưa thêm helper hoặc implementation ngoài phạm vi.
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
- `T0007`
