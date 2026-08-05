# T0009 — Cấu hình build rules

- Status: blocked
- Slice: 1
- Type: maint
- Dependency: T0008
- Branch: `maint/configure-build-rules-yyyyMMdd-HHmm`

## Mục tiêu
Tạo `Directory.Build.props` để áp dụng quy tắc biên dịch đồng nhất.

## Phạm vi
`Directory.Build.props`, task state.

## Ngoài phạm vi
Không thêm analyzer package trong task này.

## Yêu cầu
- `Nullable=enable`.
- `ImplicitUsings=enable`.
- `TreatWarningsAsErrors=true` trong CI/build release.
- `LangVersion` không dùng preview.
- Bật deterministic build.

## Acceptance criteria
- [ ] Toàn solution nhận chung cấu hình.
- [ ] Build thành công không warning.

```bash
dotnet build LocalWP.sln -c Release
```

## Bàn giao
Task tiếp theo: T0010
