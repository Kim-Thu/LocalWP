# Branch Rules

## Format bắt buộc
`<prefix>/<task-name>-yyyyMMdd-HHmm`

## Prefix hợp lệ
- feat
- fix
- refactor
- test
- docs
- ci
- maint
- security

## Regex
```regex
^(feat|fix|refactor|test|docs|ci|maint|security)/[a-z0-9][a-z0-9-]*-[0-9]{8}-[0-9]{4}$
```

## Branch protection đề xuất cho `master`
- Require pull request before merging
- Require approvals: 1
- Dismiss stale approvals
- Require status checks: `branch-name`, `docs`, `dotnet`, `docker-config`, `codeql`, `secrets`
- Require conversation resolution
- Block force pushes
- Block deletions
- Không cho push trực tiếp
- Ưu tiên squash merge

Lưu ý: workflow chỉ kiểm tra tên branch. Branch protection phải bật trong GitHub Settings vì đây là thiết lập repository, không phải file code.
