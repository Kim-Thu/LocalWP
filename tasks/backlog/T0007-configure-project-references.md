# T0007 — Cấu hình project references

- Status: blocked
- Slice: 1
- Type: maint
- Dependency: T0006
- Branch: `maint/configure-project-references-yyyyMMdd-HHmm`

## Mục tiêu
Thiết lập dependency direction đúng kiến trúc.

## Phạm vi
Các file `.csproj`, task state.

## Ngoài phạm vi
Không thêm package hoặc code.

## Yêu cầu
- Application tham chiếu Domain.
- Infrastructure tham chiếu Application và Domain.
- Desktop tham chiếu Application và Infrastructure.
- Domain không tham chiếu project nào.
- UnitTests tham chiếu Domain và Application.

## Acceptance criteria
- [ ] Không có circular reference.
- [ ] Solution build thành công.
- [ ] Dependency đúng chiều đã mô tả.

```bash
dotnet build LocalWP.sln
```

## Bàn giao
Task tiếp theo: T0008
