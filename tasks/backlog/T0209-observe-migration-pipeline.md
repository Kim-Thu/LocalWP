# T0209 — Observe migration pipeline

## Trạng thái
`backlog`

## Epic
`E03 — Persistence and settings`

## Dependency bắt buộc
- `T0208` phải hoàn thành và merge.

## Branch bắt buộc
`feat/observe-migration-pipeline-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **observe migration pipeline** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi
- Thực hiện thay đổi nhỏ nhất đủ đạt mục tiêu.
- Chỉ sửa file trực tiếp cần thiết.
- Cập nhật test và tài liệu khi hành vi thay đổi.

## Ngoài phạm vi
- Không làm nội dung task kế tiếp.
- Không đổi kiến trúc/package chính nếu chưa có ADR.
- Không refactor ngoài phạm vi.

## Yêu cầu triển khai
- Tuân thủ `AGENTS.md` và `docs/DEVELOPMENT_RULES.md`.
- UI không gọi trực tiếp Infrastructure.
- I/O/process phải async, có cancellation/timeout khi phù hợp.
- Error có ngữ cảnh; log có cấu trúc và không chứa secret.
- Thay đổi dữ liệu rủi ro phải có backup hoặc rollback.

## Yêu cầu bảo mật
- Validate input tại boundary.
- Không ghép shell command từ input thô.
- Không ghi password, token, key hoặc connection secret vào log.
- Chặn path traversal/archive traversal khi có file/path.
- Chỉ yêu cầu quyền nâng cao cho thao tác bắt buộc.

## Acceptance criteria
- [ ] Mục tiêu hoạt động và quan sát được.
- [ ] Không mở rộng ngoài phạm vi.
- [ ] Build không có warning mới.
- [ ] Test phù hợp đã thêm/cập nhật.
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
Revert PR. Thay đổi dữ liệu phải dùng rollback/backup ghi trong PR.

## Task mở khóa tiếp theo
- `T0210`
