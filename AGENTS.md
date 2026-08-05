# AGENTS.md

## Điểm bắt đầu bắt buộc

Mọi agent tham gia giữa chừng phải đọc theo đúng thứ tự:

1. `MASTER_TASK_PLAN.md`
2. `docs/DEVELOPMENT_RULES.md`
3. `docs/IMPLEMENTATION_SLICES.md`
4. `docs/SECURITY.md`
5. `docs/BRD.md`
6. `docs/SRS.md`
7. `docs/PLAN.md`
8. File task được chỉ định trong `tasks/backlog/`

Không bắt đầu viết mã chỉ từ README hoặc yêu cầu hội thoại cũ.

## Cách xác định task tiếp theo

1. Mở `MASTER_TASK_PLAN.md`.
2. Lấy task được ghi tại `Task tiếp theo bắt buộc`.
3. Mở đúng file tương ứng trong `tasks/backlog/`.
4. Kiểm tra status là `ready` và dependency đã `done`.
5. Nếu không thỏa, dừng và báo mâu thuẫn; không tự chọn task khác.

## Nguyên tắc bất biến

- Stack: C# + .NET 8 + Avalonia UI + MVVM.
- Docker Compose v2 là cơ chế orchestration chính.
- Windows 10/11 là nền tảng MVP.
- Domain không phụ thuộc UI, Docker hoặc hệ điều hành.
- UI không chứa nghiệp vụ hạ tầng.
- Không dựng nút hoặc workflow giả.
- Không ghép shell command từ input.
- Không ghi secret vào log.
- Thao tác có nguy cơ mất dữ liệu phải có backup/rollback.
- Không đổi kiến trúc hoặc package chính nếu chưa có ADR/task riêng.
- Một task = một branch = một PR.

## Branch

`<prefix>/<task-name>-yyyyMMdd-HHmm`

Prefix hợp lệ: `feat`, `fix`, `refactor`, `test`, `docs`, `ci`, `maint`, `security`.

## Khi nhận task

- Đổi status thành `in-progress`.
- Tạo branch đúng format và đúng type trong task.
- Chỉ sửa file thuộc `Phạm vi được phép`.
- Không làm mục trong `Ngoài phạm vi` dù thấy tiện.

## Khi hoàn tất

- Chạy đúng lệnh kiểm tra trong task.
- Đáp ứng toàn bộ acceptance criteria.
- Mở PR và đổi status thành `review`.
- Chỉ sau khi merge mới đổi thành `done`.
- Ghi PR, commit SHA và mở khóa task kế tiếp trong cả task file lẫn `MASTER_TASK_PLAN.md`.

## Khi tài liệu mâu thuẫn

Dừng triển khai. Ưu tiên theo thứ tự: task hiện tại → master plan → SRS → BRD → PLAN. Không tự đoán ý định để tiếp tục code.
