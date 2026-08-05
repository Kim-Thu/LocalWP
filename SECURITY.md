# Security Policy

## Nguyên tắc
- Không commit secret, token, certificate private key hoặc password thật.
- Không ghi secret vào log, exception message hoặc diagnostic bundle.
- Mọi tham số process phải truyền qua argument list, không nối chuỗi shell.
- Validate domain, slug, path và archive entry.
- Chặn path traversal và zip slip.
- Quyền Administrator chỉ dùng trong `LocalWP.SystemHelper` cho hosts/certificate.
- Database password phải sinh ngẫu nhiên và bảo vệ bằng cơ chế hệ điều hành khi lưu.
- Backup/restore phải kiểm tra integrity trước khi dùng.
- Docker image phải pin theo version hoặc digest trong release ổn định.

## Báo lỗi bảo mật
Không tạo issue công khai cho lỗ hổng có thể khai thác. Gửi báo cáo riêng cho maintainer kèm bước tái hiện và mức ảnh hưởng.

## Security checks trong CI
- CodeQL
- Dependency review trên PR
- NuGet vulnerability audit
- Secret scanning bằng Gitleaks
- Không build release khi có lỗi mức high/critical
