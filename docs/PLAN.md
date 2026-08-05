# LocalWP — Kế hoạch triển khai

## Nguyên tắc
Mỗi task phải nhỏ, độc lập, có acceptance criteria và merge được. Không làm UI giả. Không mở rộng scope ngoài task.

## Milestone
1. Repository bootstrap
2. Domain model và persistence
3. UI shell
4. Safe process runner và Docker diagnostics
5. Compose/config generator
6. Provision site bằng localhost
7. Domain và SSL
8. Site lifecycle và logs
9. Database tools
10. WordPress tools
11. Backup/restore
12. Clone
13. Blueprint
14. Version switching
15. Diagnostics/repair
16. Packaging Windows
17. Stabilization

## Flow cho mỗi task
1. Chọn task trạng thái `ready`.
2. Tạo branch đúng format.
3. Đọc dependency và tài liệu liên quan.
4. Chỉ sửa phạm vi đã ghi.
5. Viết test trước hoặc cùng code.
6. Chạy format, build, test, security checks.
7. Tạo PR theo template.
8. Chỉ merge khi CI xanh.

## Definition of Done
- Acceptance criteria đạt.
- Build và test xanh.
- Không warning mới.
- Không secret trong code/log.
- Có rollback cho thay đổi dữ liệu nguy hiểm.
- Docs cập nhật nếu hành vi thay đổi.
- PR không chứa thay đổi ngoài scope.
