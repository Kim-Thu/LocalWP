# T0003 — Tạo project Application

- Status: blocked
- Slice: 1
- Type: feat
- Dependency: T0002
- Branch: `feat/create-application-project-yyyyMMdd-HHmm`

## Mục tiêu
Tạo `src/LocalWP.Application` và thêm vào solution.

## Phạm vi
`src/LocalWP.Application/**`, `LocalWP.sln`, task state.

## Ngoài phạm vi
Không thêm package, interface, use case hoặc project reference.

## Yêu cầu
- Target `net8.0`.
- Xóa class mẫu.
- Build độc lập.

## Acceptance criteria
- [ ] Project có trong solution.
- [ ] Không có code mẫu.
- [ ] Build thành công.

```bash
dotnet build src/LocalWP.Application/LocalWP.Application.csproj
```

## Bàn giao
Task tiếp theo: T0004
