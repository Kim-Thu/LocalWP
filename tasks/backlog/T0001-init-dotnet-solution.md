# T0001 — Khởi tạo solution .NET 8

- Status: ready
- Slice: 1
- Type: feat
- Dependency: none
- Branch: `feat/init-dotnet-solution-yyyyMMdd-HHmm`

## Mục tiêu

Tạo `LocalWP.sln` tối thiểu để các task sau thêm project độc lập.

## Phạm vi được phép

- `LocalWP.sln`
- `global.json`
- cập nhật task state và `MASTER_TASK_PLAN.md`

## Ngoài phạm vi

- Không tạo project.
- Không cài package.
- Không thêm code ứng dụng.

## Yêu cầu triển khai

1. Pin .NET SDK 8 bằng `global.json`, cho phép latest patch trong feature band phù hợp.
2. Tạo solution tên `LocalWP`.
3. Không thêm solution folder hoặc project placeholder.

## Yêu cầu bảo mật

Không phát sinh bề mặt bảo mật mới.

## Acceptance criteria

- [ ] `LocalWP.sln` tồn tại và hợp lệ.
- [ ] `dotnet --version` dùng .NET 8 theo `global.json`.
- [ ] `dotnet sln LocalWP.sln list` chạy thành công và chưa có project.
- [ ] Chỉ các file trong phạm vi bị thay đổi.

## Lệnh kiểm tra

```bash
dotnet --version
dotnet sln LocalWP.sln list
```

## Bàn giao

- Task tiếp theo được mở khóa: T0002
