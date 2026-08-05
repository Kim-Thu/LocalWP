# AGENTS.md

## Mục đích
Tài liệu này là điểm bắt đầu bắt buộc cho mọi người hoặc agent tham gia dự án LocalWP.

## Thứ tự đọc bắt buộc
1. `docs/BRD.md`
2. `docs/SRS.md`
3. `docs/PLAN.md`
4. `docs/BACKLOG.md`
5. `docs/CODING_STANDARDS.md`
6. `SECURITY.md`
7. `CONTRIBUTING.md`
8. Task hiện tại trong `tasks/`

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
- Mỗi PR chỉ xử lý một task nhỏ, có acceptance criteria rõ.

## Branch rule bắt buộc
Format:

`<prefix>/<task-name>-yyyyMMdd-HHmm`

Prefix hợp lệ:
- `feat`
- `fix`
- `refactor`
- `test`
- `docs`
- `ci`
- `maint`
- `security`

Ví dụ: `feat/init-solution-20260806-0542`

## Commit
Dùng Conventional Commits, ví dụ:
- `feat(site): add site aggregate`
- `fix(docker): handle compose timeout`
- `test(domain): add slug validation tests`

## Trước khi code
- Đọc task hiện tại.
- Xác nhận dependency đã hoàn thành.
- Xác nhận phạm vi không trùng task khác.
- Không mở rộng scope.

## Trước khi tạo PR
- Build thành công.
- Test thành công.
- Không có warning mới.
- Không lộ secret.
- Cập nhật docs nếu thay đổi hành vi.
- Điền đầy đủ PR template.
