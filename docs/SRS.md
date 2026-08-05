# LocalWP — Software Requirements Specification

## Stack
- C# / .NET 8
- Avalonia UI
- MVVM bằng CommunityToolkit.Mvvm
- Microsoft.Extensions.DependencyInjection
- Serilog
- Docker Compose v2
- Nginx, PHP-FPM, MySQL/MariaDB, WP-CLI, Adminer

## Kiến trúc
```text
LocalWP.Desktop       UI, Views, ViewModels
LocalWP.Application   Use cases, commands, queries, DTOs
LocalWP.Domain        Entities, value objects, validation
LocalWP.Infrastructure Docker, process, filesystem, hosts, SSL, persistence
LocalWP.WordPress     WP-CLI, core, plugin, theme
LocalWP.Database      Import, export, backup, restore
LocalWP.SystemHelper  Tiến trình elevated trên Windows
```

## Yêu cầu chức năng chính
- FR-001: kiểm tra Docker CLI, daemon và Compose v2.
- FR-002: tạo site từ wizard và rollback khi lỗi.
- FR-003: start/stop/restart/delete site.
- FR-004: sinh Compose, Nginx, PHP và database config.
- FR-005: quản lý hosts và domain.
- FR-006: tạo/trust root CA và certificate theo site.
- FR-007: cài WordPress bằng WP-CLI.
- FR-008: import/export SQL và SQL.GZ theo streaming.
- FR-009: clone site và search-replace domain.
- FR-010: blueprint cấu hình hoặc đầy đủ.
- FR-011: backup/restore có metadata và integrity check.
- FR-012: update core/plugin/theme.
- FR-013: đổi PHP/database version có preflight, backup và rollback.
- FR-014: stream logs và tạo diagnostic bundle đã loại secret.

## Yêu cầu phi chức năng
- UI không bị block bởi thao tác dài.
- JSON phải ghi atomic.
- Input dùng argument list, không ghép shell command.
- Password lưu bằng cơ chế bảo vệ của hệ điều hành khi cần.
- Không log secret.
- Import file lớn không nạp toàn bộ vào RAM.
- Có cancellation, timeout và correlation ID.
- Build phải không có warning.

## Cấu trúc dữ liệu trên đĩa
```text
%LOCALAPPDATA%/LocalWP/
├── settings.json
├── sites-index.json
├── certificates/
├── blueprints/
├── logs/
└── sites/{slug}/
    ├── site.json
    ├── docker-compose.yml
    ├── app/public/
    ├── config/
    ├── database/
    ├── backups/
    └── logs/
```

## Test bắt buộc
- Unit: validator, generator, compatibility matrix, secret redaction.
- Integration: Docker, WP-CLI, DB import/export, hosts, SSL.
- End-to-end: create → HTTPS → update → clone → backup → restore → delete.
