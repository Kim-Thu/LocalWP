# T0005 — Tạo project Desktop Avalonia

- Status: blocked
- Slice: 1
- Type: feat
- Dependency: T0004
- Branch: `feat/create-desktop-project-yyyyMMdd-HHmm`

## Mục tiêu
Tạo ứng dụng `src/LocalWP.Desktop` bằng Avalonia và thêm vào solution.

## Phạm vi
`src/LocalWP.Desktop/**`, `LocalWP.sln`, task state.

## Ngoài phạm vi
Không thiết kế giao diện LocalWP, không thêm DI, logging hoặc MVVM Toolkit.

## Yêu cầu
- Target `net8.0`.
- Template Avalonia desktop tối thiểu.
- App mở được MainWindow mặc định.
- Không thêm nghiệp vụ vào code-behind.

## Bảo mật
Không nhúng secret hoặc cấu hình máy cá nhân.

## Acceptance criteria
- [ ] Project có trong solution.
- [ ] Build thành công trên Windows.
- [ ] Ứng dụng khởi động được.

```bash
dotnet build src/LocalWP.Desktop/LocalWP.Desktop.csproj
```

## Bàn giao
Task tiếp theo: T0006
