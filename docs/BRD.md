# LocalWP — Business Requirements

## Mục tiêu
LocalWP là ứng dụng desktop giúp lập trình viên WordPress tạo và quản lý môi trường cục bộ bằng Docker Compose mà không cần tự cấu hình PHP, Nginx, database, domain, SSL hay WP-CLI.

## Người dùng
- WordPress developer
- Frontend/full-stack developer
- Freelancer và agency
- QA/content team cần chạy site cục bộ

## Giá trị
- Tạo site trong vài phút
- Chuẩn hóa môi trường giữa các máy
- Giảm lỗi domain, SSL, database và container
- Hỗ trợ clone, import, blueprint, backup và update

## Phạm vi MVP
- Quản lý nhiều site
- Tạo/start/stop/restart/delete site
- PHP 7.4–8.4
- MySQL/MariaDB nhiều phiên bản
- Nginx + PHP-FPM
- Domain `.local`
- SSL tin cậy trên Windows
- WP-CLI
- Import/export database
- Clone site
- Blueprint
- Backup/restore
- Update WordPress core/plugin/theme
- Logs và diagnostics

## Ngoài phạm vi MVP
- Production hosting
- Cloud sync
- Team realtime
- Kubernetes
- macOS/Linux release đầu tiên
- Apache/Caddy
- WordPress multisite

## Quy tắc nghiệp vụ
1. Mỗi site có `site.json` làm nguồn cấu hình chính.
2. Mỗi site có Docker Compose riêng.
3. Domain không được trùng.
4. Container/network/volume phải namespace theo site ID.
5. Thao tác rủi ro phải backup trước.
6. Clone phải tạo toàn bộ định danh mới.
7. Không lưu secret vào log.
8. Không dùng cổng cố định nếu có thể tránh.
9. Xóa dữ liệu phải xác nhận rõ.
10. Workflow dài phải có progress và log.

## Tiêu chí đạt MVP
Người dùng có thể tạo một site WordPress HTTPS, quản lý vòng đời, import DB, clone, tạo blueprint, backup/restore và update core/plugin/theme mà không cần chạy lệnh thủ công.
