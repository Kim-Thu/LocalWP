# Contributing

## Bắt đầu
Đọc `AGENTS.md` và toàn bộ tài liệu bắt buộc trước khi nhận task.

## Branch
Format bắt buộc:

`<prefix>/<task-name>-yyyyMMdd-HHmm`

Prefix hợp lệ: `feat`, `fix`, `refactor`, `test`, `docs`, `ci`, `maint`, `security`.

## Commit
Dùng Conventional Commits.

## Pull request
- Một PR chỉ giải quyết một task.
- Không đổi package, kiến trúc hoặc convention ngoài scope.
- Mô tả rõ cách test.
- PR thay đổi UI phải có ảnh/video.
- PR tác động dữ liệu phải nêu rollback.
- CI phải xanh trước khi merge.

## Merge
Ưu tiên squash merge. Không push trực tiếp vào branch mặc định.
