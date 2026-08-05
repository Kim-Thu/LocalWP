# T0006 — Tạo project UnitTests

- Status: blocked
- Slice: 1
- Type: test
- Dependency: T0005
- Branch: `test/create-unit-tests-project-yyyyMMdd-HHmm`

## Mục tiêu
Tạo `tests/LocalWP.UnitTests` bằng xUnit và thêm vào solution.

## Phạm vi
`tests/LocalWP.UnitTests/**`, `LocalWP.sln`, task state.

## Ngoài phạm vi
Không thêm test nghiệp vụ hoặc project reference.

## Yêu cầu
- Target `net8.0`.
- Xóa test mẫu vô nghĩa.
- Test project chạy thành công khi chưa có test.

## Acceptance criteria
- [ ] Project có trong solution.
- [ ] `dotnet test` thành công.
- [ ] Không có test giả chỉ để làm xanh CI.

```bash
dotnet test tests/LocalWP.UnitTests/LocalWP.UnitTests.csproj
```

## Bàn giao
Task tiếp theo: T0007
