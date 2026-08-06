# T0012 — Add directory.packages.props

## UID bất biến
`BOOT-012`

## Trạng thái
`review`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0011` phải hoàn thành và merge.

## Branch bắt buộc
`feat/add-directory-packages-props-yyyyMMdd-HHmm`

## Mục tiêu
Thêm `Directory.Packages.props` tại thư mục gốc để bật quản lý phiên bản package tập trung cho toàn bộ solution.

## Phạm vi
- Thêm `Directory.Packages.props` tại thư mục gốc.
- Bật `ManagePackageVersionsCentrally`.
- Bật `CentralPackageTransitivePinningEnabled`.
- Không thêm hoặc đổi package trong task này.
- Không thay đổi mã runtime hoặc kiến trúc.

## Ngoài phạm vi
- Không thêm version package cụ thể khi solution chưa có package cần quản lý.
- Không sửa từng file project.
- Không thêm analyzer hoặc framework test.
- Không làm nội dung task kế tiếp.
- Không đổi kiến trúc hoặc package chính.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không thêm dependency ngoài phạm vi.
- Không bỏ qua cảnh báo restore hoặc security scan.

## Acceptance criteria
- [x] `Directory.Packages.props` tồn tại tại thư mục gốc.
- [x] Quản lý phiên bản package tập trung được bật.
- [x] Transitive pinning được bật.
- [x] Không thêm hoặc đổi package.
- [x] Không thay đổi mã runtime hoặc kiến trúc.
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
- `T0013`
