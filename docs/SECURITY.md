# Security Engineering Rules

## Bắt buộc

- Không commit secret, token, password thật, private key, database dump hoặc dữ liệu website khách hàng.
- Mọi process phải dùng executable + argument list; không dựng command shell từ input.
- Mọi đường dẫn từ người dùng phải normalize và kiểm tra path traversal.
- Archive import phải kiểm tra entry path trước khi giải nén.
- Log phải redact password, token, connection string và biến môi trường nhạy cảm.
- Quyền Administrator chỉ được gọi qua helper riêng cho hosts/certificate; app chính không chạy elevated.
- Database destructive action phải xác nhận và tạo restore point khi có thể.
- Dependency mới phải có lý do trong PR và không có lỗ hổng mức high/critical đã biết.

## Review bắt buộc

Task liên quan các vùng sau phải dùng prefix `security/` hoặc có security checklist riêng:

- Process execution
- File extraction/import
- Hosts file
- Certificate store
- Secret storage
- Database restore/delete
- Auto-update
- Installer

## Kiểm tra CI

- CodeQL cho C# sau khi solution tồn tại.
- Secret scanning bằng Gitleaks.
- Dependency review khi repository đủ điều kiện.
- Không dùng biến cho phép runtime/action đã bị đánh dấu không an toàn.
