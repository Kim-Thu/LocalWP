# T0008 — Cấu hình central package management

- Status: blocked
- Slice: 1
- Type: maint
- Dependency: T0007
- Branch: `maint/central-package-management-yyyyMMdd-HHmm`

## Mục tiêu
Tạo `Directory.Packages.props` làm nguồn version package duy nhất.

## Phạm vi
`Directory.Packages.props`, các `.csproj`, task state.

## Ngoài phạm vi
Không nâng version package ngoài version template đang dùng; không thêm package chưa cần.

## Yêu cầu
- Bật `ManagePackageVersionsCentrally`.
- Di chuyển mọi package version khỏi `.csproj`.
- Không dùng floating version.

## Bảo mật
Package phải đến từ NuGet chính thức; không thêm feed lạ.

## Acceptance criteria
- [ ] Không còn `Version=` trong `PackageReference`.
- [ ] Restore/build thành công.

```bash
dotnet restore LocalWP.sln
dotnet build LocalWP.sln --no-restore
```

## Bàn giao
Task tiếp theo: T0009
