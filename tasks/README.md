# Tasks

Mỗi task là một đơn vị thay đổi nhỏ nhất có thể review và merge độc lập.

## Cấu trúc
```text
tasks/
├── README.md
├── TEMPLATE.md
├── ready/
├── in-progress/
├── review/
└── done/
```

## Quy tắc
- Tên file: `T-xxxx-short-name.md`.
- Mỗi task phải có mục tiêu, phạm vi, ngoài phạm vi, dependency, acceptance criteria, test và rủi ro.
- Agent chỉ được thực hiện task trong `ready/`.
- Khi bắt đầu, chuyển sang `in-progress/` trong cùng PR hoặc cập nhật trạng thái rõ ràng.
- Không gộp task khác vào PR hiện tại.
- Task hoàn thành chỉ chuyển `done/` sau khi merge.
