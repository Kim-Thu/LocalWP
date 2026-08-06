# T0013 — Add global.json

## UID bất biến
`BOOT-013`

## Trạng thái
`done`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0012` phải hoàn thành và merge.

## Branch bắt buộc
`feat/add-global-json-yyyyMMdd-HHmm`

## Mục tiêu
Thêm `global.json` tại thư mục gốc để khóa dự án vào dòng .NET 8 SDK với chính sách roll-forward có kiểm soát.

## Phạm vi
- Thêm `global.json` tại thư mục gốc.
- Đặt SDK cơ sở là `8.0.100`.
- Cho phép roll-forward tới feature band .NET 8 mới nhất đã cài.
- Không cho phép SDK preview.
- Không thay đổi package, mã runtime hoặc kiến trúc.

## Ngoài phạm vi
- Không đổi workflow CI.
- Không cài hoặc cập nhật package.
- Không sửa từng file project.
- Không làm nội dung task kế tiếp.
- Không đổi kiến trúc hoặc package chính.
- Không refactor ngoài phạm vi.

## Yêu cầu bảo mật
- Không thêm secret, credential hoặc process call.
- Không cho phép SDK preview ngoài ý muốn.
- Không thêm dependency ngoài phạm vi.

## Acceptance criteria
- [x] `global.json` tồn tại tại thư mục gốc.
- [x] Dòng SDK .NET 8 được khai báo rõ ràng.
- [x] Chính sách roll-forward có kiểm soát.
- [x] SDK preview bị vô hiệu hóa.
- [x] Không thay đổi package, mã runtime hoặc kiến trúc.
- [x] CI, security scan và format xanh.

## Kiểm tra bắt buộc
```bash
dotnet --version
dotnet restore LocalWP.sln
dotnet build LocalWP.sln --configuration Release --no-restore
dotnet test LocalWP.sln --configuration Release --no-build
dotnet format LocalWP.sln --verify-no-changes --no-restore
```

## Rollback
Revert PR; không có thay đổi dữ liệu runtime.

## Task mở khóa tiếp theo
- `T0014`
