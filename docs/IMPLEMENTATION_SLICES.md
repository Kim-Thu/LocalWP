# Implementation Slices

Mỗi slice phải hoàn thành theo thứ tự. Chỉ mở task của slice sau khi gate của slice trước đạt.

## Slice 0 — Repository governance

Kết quả: tài liệu nguồn chuẩn, task flow, branch rule, CI cơ bản, security scan, Docker Compose validation.

Gate: PR bootstrap merge và CI xanh.

## Slice 1 — Solution foundation

Kết quả: solution .NET 8, Domain, Application, Infrastructure, Desktop Avalonia, UnitTests, project references, package management và build rules.

Gate: `dotnet restore`, `dotnet build --no-restore`, `dotnet test --no-build` thành công trên Windows CI.

## Slice 2 — Domain và persistence

Kết quả: Site aggregate, value objects, settings, atomic JSON repository và schema migration.

Gate: unit test đầy đủ; ứng dụng đọc/ghi site index mà không phụ thuộc Docker.

## Slice 3 — UI shell

Kết quả: main window, site sidebar, empty state, navigation, tabs và trạng thái Docker.

Gate: app mở ổn định, UI không chứa nghiệp vụ hạ tầng.

## Slice 4 — Process và Docker diagnostics

Kết quả: safe process runner, streaming log, cancellation, Docker/Compose diagnostics.

Gate: phát hiện đúng Docker thiếu, daemon tắt và Compose thiếu.

## Slice 5 — Compose generator

Kết quả: sinh Nginx, PHP-FPM, MySQL/MariaDB, WP-CLI và Adminer config.

Gate: snapshot test và `docker compose config` thành công.

## Slice 6 — Provision site

Kết quả: create wizard, provisioning localhost, health check, rollback và lifecycle cơ bản.

## Slice 7 — Domain và SSL

Kết quả: elevated helper, hosts, local CA, certificate và HTTPS.

## Slice 8 — Database và WordPress tools

Kết quả: import/export/search-replace, core/plugin/theme management.

## Slice 9 — Backup, clone và blueprint

Kết quả: backup/restore, clone độc lập và reusable blueprint.

## Slice 10 — Version switching và packaging

Kết quả: đổi PHP/database an toàn, diagnostics, repair và Windows installer.
