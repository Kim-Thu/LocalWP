# T0004 — Tạo project Infrastructure

- Status: blocked
- Slice: 1
- Type: feat
- Dependency: T0003
- Branch: `feat/create-infrastructure-project-yyyyMMdd-HHmm`

## Mục tiêu
Tạo `src/LocalWP.Infrastructure` và thêm vào solution.

## Phạm vi
`src/LocalWP.Infrastructure/**`, `LocalWP.sln`, task state.

## Ngoài phạm vi
Không thêm Docker, filesystem, persistence hoặc package.

## Yêu cầu
- Target `net8.0`.
- Xóa class mẫu.
- Chưa thêm project reference.

## Acceptance criteria
- [ ] Project có trong solution.
- [ ] Build thành công.
- [ ] Không có code mẫu.

```bash
dotnet build src/LocalWP.Infrastructure/LocalWP.Infrastructure.csproj
```

## Bàn giao
Task tiếp theo: T0005
