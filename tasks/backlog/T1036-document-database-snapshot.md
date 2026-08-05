# T1036 — Document database snapshot

## UID bất biến
`CLONE-026`

## Trạng thái
`backlog`

## Epic
`E12 — Clone Workflow`

## Dependency bắt buộc
- `T1035` phải hoàn thành và merge.

## Branch bắt buộc
`feat/document-database-snapshot-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **document database snapshot** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi
- Thực hiện thay đổi nhỏ nhất đủ đạt mục tiêu.
- Chỉ sửa file trực tiếp cần thiết.
- Cập nhật test và tài liệu khi hành vi thay đổi.

## Ngoài phạm vi
- Không làm nội dung task kế tiếp.
- Không đổi kiến trúc hoặc package chính nếu chưa có ADR.
- Không refactor ngoài phạm vi.

## Yêu cầu triển khai
- Tuân thủ `AGENTS.md` và `docs/DEVELOPMENT_RULES.md`.
- UI không gọi trực tiếp Infrastructure.
- I/O và process phải async, có cancellation hoặc timeout khi phù hợp.
- Error phải có ngữ cảnh; log có cấu trúc và không chứa secret.
- Thay đổi dữ liệu rủi ro phải có backup hoặc rollback.

## Yêu cầu bảo mật
- Validate input tại boundary.
- Không ghép shell command từ input thô.
- Không ghi password, token, key hoặc connection secret vào log.
- Chặn path traversal và archive traversal khi xử lý file.
- Chỉ yêu cầu quyền nâng cao cho thao tác bắt buộc.

## Acceptance criteria
- [ ] Mục tiêu hoạt động và quan sát được.
- [ ] Không mở rộng ngoài phạm vi.
- [ ] Build không có warning mới.
- [ ] Test phù hợp đã thêm hoặc cập nhật.
- [ ] CI, security scan và format xanh.

## Kiểm tra bắt buộc
```bash
dotnet restore
dotnet build --configuration Release --no-restore
dotnet test --configuration Release --no-build
dotnet format --verify-no-changes
```

Task Docker phải chạy thêm:
```bash
docker compose -f docker/compose.dev.yml config
```

## Rollback
Revert PR. Thay đổi dữ liệu phải dùng rollback hoặc backup ghi trong PR.

## Task mở khóa tiếp theo
- `T1037`
