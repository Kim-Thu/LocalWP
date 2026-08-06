# T0007 — Create unittests project

## UID bất biến
`BOOT-007`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0006` phải hoàn thành và merge.

## Branch bắt buộc
`feat/create-unittests-project-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **create UnitTests project** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi
- Tạo project `LocalWP.UnitTests` target `.NET 8`.
- Bật nullable và implicit usings.
- Đánh dấu project là test project và không đóng gói.
- Thêm marker type tối thiểu.
- Thêm project vào solution.

## Ngoài phạm vi
- Không cài test framework hoặc test SDK; phần package thuộc task package management.
- Không thêm project reference hoặc test case.
- Không tạo IntegrationTests project.
- Không làm nội dung task kế tiếp.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] UnitTests project tồn tại tại `tests/LocalWP.UnitTests`.
- [x] Project target `.NET 8`, bật nullable và không đóng gói.
- [x] UnitTests project đã được thêm vào `LocalWP.sln`.
- [x] Có marker type tối thiểu, chưa thêm framework hoặc test case ngoài phạm vi.
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
- `T0008`
