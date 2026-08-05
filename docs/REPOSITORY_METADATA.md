# LocalWP — Repository Metadata

## Canonical identity

- **Repository name:** `LocalWP`
- **Product name:** `LocalWP`
- **Repository owner:** `Kim-Thu`
- **Primary language:** C#
- **Runtime:** .NET 8
- **Desktop UI:** Avalonia UI
- **Architecture:** MVVM, layered architecture
- **Container orchestration:** Docker Compose v2
- **Primary platform for MVP:** Windows 10/11 x64
- **Primary application domain:** Local WordPress development environment management
- **Project status:** Pre-alpha / foundation stage
- **License:** Not selected yet

## Repository description

Ứng dụng desktop mã nguồn mở giúp tạo và quản lý nhiều môi trường WordPress cục bộ bằng Docker Compose, gồm PHP-FPM, Nginx, MySQL hoặc MariaDB, domain cục bộ, SSL, WP-CLI, import/export database, clone, blueprint, backup và cập nhật WordPress.

## Suggested GitHub description

```text
Desktop WordPress environment manager built with C#, Avalonia and Docker Compose.
```

## Suggested topics

```text
wordpress
docker
docker-compose
csharp
dotnet
avalonia
mvvm
local-development
php
mysql
nginx
wp-cli
```

## Canonical links inside the repository

- Product requirements: `docs/BRD.md`
- Software requirements: `docs/SRS.md`
- Delivery plan: `docs/PLAN.md`
- Master task sequence: `MASTER_TASK_PLAN.md`
- Agent entry point: `AGENTS.md`
- Development rules: `docs/DEVELOPMENT_RULES.md`
- Security policy: `SECURITY.md`
- Contribution rules: `CONTRIBUTING.md`

## Naming rules

- Dùng `LocalWP` khi nói về sản phẩm và repository.
- Namespace C# dự kiến dùng tiền tố `LocalWP`.
- Không đổi tên sản phẩm hoặc namespace gốc nếu chưa có ADR được duyệt.
- Không dùng tên `LocalBox` trong mã, tài liệu mới hoặc package metadata.

## Metadata ownership

Tài liệu này là nguồn chuẩn cho tên sản phẩm, mô tả, stack chính, trạng thái và topic của repository. Thay đổi metadata phải cập nhật đồng thời README và tài liệu liên quan trong cùng task.
