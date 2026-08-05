# AGENTS.md

## Mục đích
Tài liệu này là điểm bắt đầu bắt buộc cho mọi người hoặc agent tham gia dự án LocalWP.

## Thứ tự đọc bắt buộc
1. `MASTER_TASK_PLAN.md`
2. `docs/BRD.md`
3. `docs/SRS.md`
4. `docs/PLAN.md`
5. `docs/DEVELOPMENT_RULES.md`
6. `docs/SECURITY.md`
7. Epic hiện tại trong `planning/epics/`
8. Task hiện tại trong `tasks/backlog/`

## Cách chọn task
- Đọc mục `Task hiện tại` trong `MASTER_TASK_PLAN.md`.
- Chỉ thực hiện đúng task đó hoặc task có số nhỏ nhất chưa hoàn thành với dependency đã merge.
- Không tự chọn task khác vì thấy thuận tiện hơn.
- Mỗi task tương ứng đúng một branch và một PR.

## Nguyên tắc bất biến
- Stack: C# + .NET 8 + Avalonia UI + MVVM.
- Docker Compose v2 là cơ chế orchestration chính.
- Windows 10/11 là nền tảng MVP.
- Không dựng nút giả hoặc flow giả.
- Không bypass domain layer để gọi thẳng hạ tầng từ UI.
- Không ghép command shell từ input thô.
- Không ghi secret vào log.
- Mọi thao tác có nguy cơ mất dữ liệu phải có backup hoặc rollback.
- Không tự ý đổi kiến trúc, package chính hoặc convention nếu chưa có ADR.
- Không mở rộng phạm vi task.

## Branch rule bắt buộc
`<prefix>/<task-name>-yyyyMMdd-HHmm`

Prefix hợp lệ: `feat`, `fix`, `refactor`, `test`, `docs`, `ci`, `maint`, `security`.

## Commit
Dùng Conventional Commits.

## Trước khi tạo PR
- Build xanh.
- Test xanh.
- Format xanh.
- Không warning mới.
- Không lộ secret.
- Điền đầy đủ PR template.
- Ghi rõ task ID trong PR.
