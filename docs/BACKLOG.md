# Backlog

## Quy ước trạng thái
`blocked` → `ready` → `in-progress` → `review` → `done`

## M0 — Bootstrap
- T-0001 Khởi tạo solution .NET 8
- T-0002 Tạo project Desktop
- T-0003 Tạo project Application
- T-0004 Tạo project Domain
- T-0005 Tạo project Infrastructure
- T-0006 Tạo project WordPress
- T-0007 Tạo project Database
- T-0008 Tạo project SystemHelper
- T-0009 Tạo unit test project
- T-0010 Tạo integration test project
- T-0011 Cấu hình project references
- T-0012 Cấu hình central package management
- T-0013 Cấu hình analyzers và warnings-as-errors
- T-0014 Tạo Avalonia shell
- T-0015 Cấu hình logging
- T-0016 Cấu hình dependency injection
- T-0017 Cấu hình CI build/test/format
- T-0018 Cấu hình CodeQL và dependency review
- T-0019 Tạo Docker development validation stack
- T-0020 Tạo release workflow skeleton

## M1 — Domain/Persistence
- Site aggregate, SiteId, SiteSlug, SiteDomain
- EnvironmentConfig và version value objects
- Validation rules
- Atomic JSON repository
- Settings repository
- Schema versioning và migration

## M2 — Docker foundation
- Safe process runner
- Docker CLI diagnostics
- Compose diagnostics
- Streaming stdout/stderr
- Timeout/cancellation
- Secret redaction
- Compose generator

Các milestone sau được tách tiếp ngay trước khi bắt đầu để giữ task nhỏ, tránh backlog giả quá chi tiết khi kiến trúc chưa được kiểm chứng.
