# T0010 — Cập nhật CI build solution

- Status: blocked
- Slice: 1
- Type: ci
- Dependency: T0009
- Branch: `ci/update-solution-build-yyyyMMdd-HHmm`

## Mục tiêu
Chuyển CI từ chế độ bootstrap sang restore/build/test/format solution thật.

## Phạm vi
`.github/workflows/ci.yml`, `.github/workflows/security.yml`, task state.

## Ngoài phạm vi
Không thêm release, installer hoặc Docker integration test.

## Yêu cầu
- Dùng action version hiện hành không phụ thuộc Node runtime đã bị ngừng hỗ trợ.
- Setup .NET theo `global.json`.
- Cache NuGet an toàn.
- Chạy restore, build Release, test và format check.
- CodeQL build bằng lệnh rõ ràng, không dùng autobuild.
- Permissions tối thiểu.
- Có concurrency để hủy run cũ cùng branch.

## Bảo mật
Không dùng `pull_request_target`; không chạy script không tin cậy với secret.

## Acceptance criteria
- [ ] CI chạy xanh trên pull request.
- [ ] CodeQL phân tích C# thành công.
- [ ] Không còn workaround Node không an toàn.
- [ ] Build failure làm PR check fail.

## Bàn giao
Slice 1 foundation hoàn tất; mở task đầu tiên của Slice 2.
