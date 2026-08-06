# T0008 — Create integrationtests project

## UID bất biến
`BOOT-008`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0007` phải hoàn thành và merge.

## Branch bắt buộc
`feat/create-integrationtests-project-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **create IntegrationTests project** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi
- Tạo project `LocalWP.IntegrationTests` target `.NET 8`.
- Bật nullable và implicit usings.
- Tắt đóng gói.
- Thêm marker type tối thiểu.
- Thêm project vào solution.

## Ngoài phạm vi
- Không bật `IsTestProject` khi chưa có `Microsoft.NET.Test.Sdk`; phần test SDK thuộc task package management.
- Không cài test framework hoặc test SDK.
- Không thêm project reference hoặc test case.
- Không làm nội dung task kế tiếp.
- Không đổi kiến trúc hoặc package chính nếu chưa có ADR.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] IntegrationTests project tồn tại tại `tests/LocalWP.IntegrationTests`.
- [x] Project target `.NET 8`, bật nullable và không đóng gói.
- [x] IntegrationTests project đã được thêm vào `LocalWP.sln`.
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
- `T0009`
