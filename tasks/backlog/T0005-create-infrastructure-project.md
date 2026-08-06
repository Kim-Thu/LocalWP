# T0005 — Create infrastructure project

## UID bất biến
`BOOT-005`

## Trạng thái
`done`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0004` phải hoàn thành và merge.

## Branch bắt buộc
`feat/create-infrastructure-project-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **create Infrastructure project** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi
- Tạo project `LocalWP.Infrastructure` target `.NET 8`.
- Bật nullable và implicit usings.
- Thêm marker type tối thiểu.
- Thêm project vào solution.

## Ngoài phạm vi
- Không thêm package, project reference hoặc implementation hạ tầng.
- Không tạo SystemHelper hoặc test project.
- Không làm nội dung task kế tiếp.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] Infrastructure project tồn tại tại `src/LocalWP.Infrastructure`.
- [x] Project target `.NET 8` và bật nullable.
- [x] Infrastructure project đã được thêm vào `LocalWP.sln`.
- [x] Có marker type tối thiểu, chưa thêm implementation ngoài phạm vi.
- [x] CI, security scan và format xanh.

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
- `T0006`
