# Clean Build Verification

## Mục đích
Tài liệu này ghi lại lệnh chuẩn để xác minh toàn bộ solution LocalWP có thể restore, build, test và kiểm tra format từ trạng thái sạch.

## Phạm vi
- Solution: `LocalWP.sln`
- Cấu hình: `Release`
- Nền tảng CI hiện tại: Windows runner
- Không cài thêm package hoặc thay đổi mã runtime.

## Lệnh xác minh
```bash
dotnet restore LocalWP.sln
dotnet build LocalWP.sln --configuration Release --no-restore
dotnet test LocalWP.sln --configuration Release --no-build
dotnet format LocalWP.sln --verify-no-changes --no-restore
```

## Kết quả yêu cầu
- Restore kết thúc thành công.
- Build kết thúc thành công và không phát sinh warning mới.
- Test command kết thúc thành công; các test project chưa bật test SDK cho tới task package management.
- Format check không phát hiện thay đổi cần áp dụng.
- CI và Security workflow phải xanh trên PR của task.

## Khi xác minh thất bại
- Không bỏ qua lỗi hoặc warning.
- Sửa đúng nguyên nhân trên branch hiện tại.
- Không mở task mới khi PR hiện tại chưa xanh.
- Không thêm dependency ngoài task chỉ để làm CI xanh.

## Rollback
Xóa tài liệu này bằng cách revert PR; không có dữ liệu runtime bị thay đổi.
