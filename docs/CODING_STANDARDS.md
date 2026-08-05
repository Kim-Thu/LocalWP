# Coding Standards

## C#
- .NET 8, nullable enabled, implicit usings enabled.
- Warnings là errors trong CI.
- Một type public chính cho mỗi file.
- Ưu tiên immutable model và `required` cho dữ liệu bắt buộc.
- Async method phải nhận `CancellationToken` khi có I/O.
- Không dùng `.Result`, `.Wait()` hoặc `async void` ngoài event handler.
- Không catch `Exception` rồi bỏ qua.
- Không trả `null` khi có thể dùng result type hoặc nullable rõ ràng.

## Kiến trúc
- Desktop chỉ gọi Application.
- Application phụ thuộc Domain và abstraction.
- Domain không phụ thuộc UI, Docker, filesystem hoặc framework.
- Infrastructure implement interface, không chứa business rule.
- Mọi quyết định kiến trúc lớn phải có ADR.

## MVVM
- View không chứa business logic.
- ViewModel không gọi process/filesystem trực tiếp.
- Command phải phản ánh trạng thái CanExecute.
- Thao tác dài phải có progress, cancel và error state.

## Process và Docker
- Dùng `ProcessStartInfo.ArgumentList`.
- Không gọi `cmd /c` hoặc PowerShell với input chưa kiểm soát.
- Mọi command phải có timeout và log đã redact.
- Không hard-code secret hoặc port.

## Test
- Tên test: `Method_State_ExpectedResult`.
- Test hành vi, không test implementation detail.
- Generator dùng snapshot/golden test khi phù hợp.
- Bug fix phải có regression test.

## Formatting
- `dotnet format --verify-no-changes` phải xanh.
- Không tắt analyzer nếu chưa ghi lý do.
