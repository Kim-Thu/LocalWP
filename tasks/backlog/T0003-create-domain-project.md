# T0003 — Create domain project

## UID bất biến
`BOOT-003`

## Trạng thái
`done`

## Epic
`E00 — Repository Bootstrap and Engineering Foundation`

## Dependency bắt buộc
- `T0002` phải hoàn thành và merge.

## Branch bắt buộc
`feat/create-domain-project-yyyyMMdd-HHmm`

## Mục tiêu
Hoàn thành duy nhất phần **create Domain project** theo BRD, SRS và kiến trúc hiện hành.

## Acceptance criteria
- [x] Domain project tồn tại tại `src/LocalWP.Domain`.
- [x] Project target `.NET 8` và bật nullable.
- [x] Domain project đã được thêm vào `LocalWP.sln`.
- [x] Có marker type tối thiểu, không thêm domain entity ngoài phạm vi.
- [x] CI, security scan và format xanh.

## Task mở khóa tiếp theo
- `T0004`
