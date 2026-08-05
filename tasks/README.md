# Tasks

`tasks/backlog/` chứa toàn bộ task đã được tách nhỏ theo thứ tự thực hiện. Trạng thái nằm ngay trong từng file để agent không phải đoán theo vị trí thư mục.

## Cấu trúc

```text
tasks/
├── README.md
├── TASK_TEMPLATE.md
└── backlog/
    ├── T0001-....md
    ├── T0002-....md
    └── ...
```

## Cách chọn task

Không chọn theo tên file tùy ý. Luôn đọc `MASTER_TASK_PLAN.md` và thực hiện đúng `Task tiếp theo bắt buộc`.

## Quy tắc tên

- Task ID: `T` + 4 chữ số, ví dụ `T0001`.
- File: `T0001-short-kebab-name.md`.
- Không tái sử dụng ID.
- Không đổi ID sau khi task đã xuất hiện trong PR.

## Vòng đời

`blocked → ready → in-progress → review → done`

Status phải được cập nhật trong file task và bảng trong `MASTER_TASK_PLAN.md`.

## Quy tắc thực hiện

- Một task = một branch = một PR.
- Mỗi file task phải nêu dependency, branch type, phạm vi, ngoài phạm vi, yêu cầu code, bảo mật, acceptance criteria và lệnh kiểm tra.
- Agent không được làm task `blocked`.
- Khi task bị kẹt, giữ status và ghi nguyên nhân; không nhảy sang task sau nếu master plan chưa thay đổi.
- Sau merge phải ghi PR/commit SHA và mở khóa task kế tiếp.
