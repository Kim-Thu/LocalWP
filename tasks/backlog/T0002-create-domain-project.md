# T0002 — Tạo project Domain

- Status: blocked
- Slice: 1
- Type: feat
- Dependency: T0001
- Branch: `feat/create-domain-project-yyyyMMdd-HHmm`

## Mục tiêu

Tạo class library `src/LocalWP.Domain` và thêm vào solution.

## Phạm vi được phép

- `src/LocalWP.Domain/**`
- `LocalWP.sln`
- task state và master plan

## Ngoài phạm vi

- Không tạo entity, interface hoặc package reference.
- Không sửa project khác.

## Yêu cầu triển khai

1. Target `net8.0`.
2. Bật nullable và implicit usings theo build rules hiện có.
3. Xóa class mẫu do template sinh.
4. Domain không tham chiếu project khác.

## Bảo mật

Không phát sinh bề mặt bảo mật mới.

## Acceptance criteria

- [ ] Project có trong solution.
- [ ] Không có class mẫu.
- [ ] Project build thành công độc lập.

## Lệnh kiểm tra

```bash
dotnet build src/LocalWP.Domain/LocalWP.Domain.csproj
```

## Bàn giao

- Task tiếp theo: T0003
