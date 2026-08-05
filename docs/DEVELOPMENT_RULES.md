# Development Rules

## Nguồn chuẩn

Thứ tự ưu tiên khi có mâu thuẫn:

1. Task đang thực hiện.
2. `MASTER_TASK_PLAN.md`.
3. `docs/SRS.md`.
4. `docs/BRD.md`.
5. `docs/PLAN.md`.

Không được tự suy diễn để vượt qua mâu thuẫn.

## Branch

Format bắt buộc:

`<prefix>/<slug>-yyyyMMdd-HHmm`

Prefix hợp lệ: `feat`, `fix`, `refactor`, `test`, `docs`, `ci`, `maint`, `security`.

## Commit

Dùng Conventional Commits. Một commit phải mô tả một thay đổi logic. Không dùng `update`, `changes`, `fix stuff`.

## Phạm vi

- Một task tương ứng một branch và một PR.
- Không thêm chức năng ngoài acceptance criteria.
- Không refactor lan rộng trong task feature.
- Không đổi package/version nếu task không yêu cầu.
- Không commit secret, certificate private key, database dump hoặc file người dùng.

## C#/.NET

- .NET 8.
- Nullable bật toàn solution.
- Warnings as errors.
- Async API phải nhận `CancellationToken` khi có I/O hoặc process.
- Không dùng `async void`, trừ event handler UI.
- Không gọi shell bằng chuỗi ghép từ input.
- Domain không phụ thuộc Avalonia, Docker hoặc hệ điều hành.
- Infrastructure implement interface do Application/Domain định nghĩa.
- UI dùng MVVM, không đặt nghiệp vụ trong code-behind.

## Test

- Validator/generator/value object bắt buộc có unit test.
- Workflow Docker, filesystem, hosts, SSL phải có integration test khi module xuất hiện.
- Bug fix phải có test tái hiện nếu khả thi.

## Definition of Done

- Đúng phạm vi task.
- Build thành công.
- Test thành công.
- Format/analyzer thành công.
- Không lộ secret.
- Docs/task state đã cập nhật.
- CI xanh.
