# LocalWP — Master Task Plan

## Mục đích

Đây là nguồn duy nhất để xác định dự án đang ở đâu, task nào đã xong, task nào đang làm và task nào phải làm tiếp theo.

Mọi agent phải đọc theo thứ tự:

1. `AGENTS.md`
2. `MASTER_TASK_PLAN.md`
3. `docs/DEVELOPMENT_RULES.md`
4. `docs/IMPLEMENTATION_SLICES.md`
5. `docs/SECURITY.md`
6. File task cụ thể trong `tasks/backlog/`

## Trạng thái hiện tại

- Giai đoạn: Bootstrap
- Task đang hoạt động: chưa có
- Task tiếp theo bắt buộc: `T0001-init-dotnet-solution.md`
- Không được tự chọn task khác nếu task này chưa hoàn tất hoặc chưa được đánh dấu `blocked`.

## Quy trình task

1. Chọn đúng task đầu tiên có trạng thái `ready` và mọi dependency đã `done`.
2. Đổi trạng thái task thành `in-progress`.
3. Tạo branch đúng tên ghi trong task.
4. Chỉ thay đổi đúng phạm vi task.
5. Chạy toàn bộ validation ghi trong task.
6. Mở PR.
7. Sau khi merge, đổi task thành `done`, ghi PR và commit SHA.
8. Cập nhật task kế tiếp thành `ready` nếu dependency đã thỏa.

## Quy ước trạng thái

- `blocked`: chưa đủ dependency hoặc đang có trở ngại.
- `ready`: task tiếp theo được phép thực hiện.
- `in-progress`: đang có branch/PR triển khai.
- `review`: PR đã mở, chờ review/CI.
- `done`: đã merge vào nhánh mặc định.

## Thứ tự bootstrap

| Thứ tự | Task | Trạng thái |
|---|---|---|
| 1 | T0001 Khởi tạo solution .NET 8 | ready |
| 2 | T0002 Tạo project Domain | blocked |
| 3 | T0003 Tạo project Application | blocked |
| 4 | T0004 Tạo project Infrastructure | blocked |
| 5 | T0005 Tạo project Desktop Avalonia | blocked |
| 6 | T0006 Tạo project UnitTests | blocked |
| 7 | T0007 Cấu hình project references | blocked |
| 8 | T0008 Cấu hình central package management | blocked |
| 9 | T0009 Cấu hình build rules | blocked |
| 10 | T0010 Cập nhật CI build solution | blocked |

## Luật bắt buộc

- Không gộp nhiều task nhỏ thành một PR.
- Không đổi kiến trúc nếu chưa có ADR.
- Không thêm dependency ngoài task.
- Không sửa file ngoài phạm vi nếu không cần để build.
- Không đánh dấu `done` trước khi PR merge và CI xanh.
- Khi phát hiện tài liệu mâu thuẫn, dừng code và mở task `docs/*` hoặc `maint/*` để sửa nguồn chuẩn trước.
