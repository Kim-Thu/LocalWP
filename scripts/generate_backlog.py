from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "planning" / "EPIC_CATALOG.json"
BACKLOG = ROOT / "tasks" / "backlog"
MASTER = ROOT / "MASTER_TASK_PLAN.md"
EPICS = ROOT / "planning" / "epics"
TOTAL_TASKS = 1220

ACTIONS = ["define", "validate", "model", "implement", "test", "document", "integrate", "harden", "observe", "review"]
TOPICS = {
    "E01": ["site identity", "site slug", "site domain", "runtime state", "environment config", "WordPress config", "database config", "backup metadata", "operation result", "domain validation"],
    "E02": ["site repository", "settings repository", "atomic JSON write", "schema version", "migration pipeline", "index recovery", "path provider", "secret storage", "configuration validation", "persistence diagnostics"],
    "E03": ["main window", "sidebar", "site list", "site search", "navigation service", "dialog service", "toast service", "progress overlay", "theme resources", "view model lifecycle"],
    "E04": ["process request", "argument escaping", "stdout streaming", "stderr streaming", "cancellation", "timeout", "secret redaction", "Docker CLI detection", "Docker daemon detection", "Compose detection"],
    "E05": ["compose model", "image catalog", "service naming", "network naming", "volume naming", "Nginx config", "PHP config", "database config", "health checks", "config snapshots"],
    "E06": ["create-site request", "wizard validation", "site directory", "config generation", "image pull", "container startup", "database readiness", "WP-CLI install", "HTTP verification", "provision rollback"],
    "E07": ["hosts entry", "elevated helper", "IPC contract", "root CA", "certificate trust", "domain certificate", "Nginx TLS", "trust status", "certificate renewal", "SSL repair"],
    "E08": ["site start", "site stop", "site restart", "site delete", "container status", "health status", "last-started state", "quick actions", "log streaming", "orphan detection"],
    "E09": ["connection details", "Adminer", "SQL import", "GZip import", "SQL export", "GZip export", "database reset", "search replace", "database shell", "import rollback"],
    "E10": ["WP-CLI wrapper", "core status", "core update", "plugin list", "plugin install", "plugin activation", "plugin update", "theme list", "theme install", "theme update"],
    "E11": ["backup request", "database dump", "source archive", "backup metadata", "integrity hash", "backup listing", "backup deletion", "restore preflight", "restore execution", "restore rollback"],
    "E12": ["clone request", "source copy", "database snapshot", "new site identity", "new domain", "new environment", "URL replacement", "new SSL", "clone verification", "clone rollback"],
    "E13": ["blueprint schema", "blueprint metadata", "config blueprint", "full blueprint", "plugin manifest", "theme manifest", "source template", "database template", "blueprint creation", "blueprint provisioning"],
    "E14": ["runtime catalog", "compatibility matrix", "PHP preflight", "PHP switch", "PHP rollback", "database preflight", "database upgrade", "downgrade guard", "version health check", "version audit log"],
    "E15": ["port conflict", "container drift", "missing config", "hosts mismatch", "SSL mismatch", "broken index", "config rebuild", "diagnostic bundle", "secret scrub", "repair report"],
    "E16": ["Windows publish", "self-contained build", "installer", "uninstaller", "release workflow", "artifact signing", "release notes", "upgrade path", "end-to-end suite", "stability gate"],
}

E00_TASKS = [
    "initialize .NET 8 solution", "create Desktop project", "create Domain project", "create Application project", "create Infrastructure project", "create SystemHelper project", "create UnitTests project", "create IntegrationTests project", "configure project references", "verify clean build",
    "add Directory.Build.props", "add Directory.Packages.props", "add global.json", "enable nullable", "enable implicit usings", "treat warnings as errors", "configure analyzers", "configure StyleCop", "configure EditorConfig", "verify analyzer rules",
    "install Avalonia", "install CommunityToolkit.Mvvm", "install Serilog", "install FluentValidation", "install Polly", "install Docker.DotNet", "install test packages", "verify package restore",
    "configure build workflow", "configure test workflow", "configure CodeQL", "configure Gitleaks", "configure Dependabot", "configure release workflow", "configure Docker validation", "verify CI pipeline",
    "update README", "define repository metadata", "update contribution guide", "finalize branch rules", "finalize coding standards", "write architecture overview", "create ADR structure", "finalize agent rules", "verify documentation",
    "create Docker base structure", "create Docker Compose template", "define PHP image catalog", "define MySQL image catalog", "define Nginx image catalog", "verify Docker Compose",
    "create assets folder", "create scripts folder", "verify docs folder", "verify planning folder", "verify epics folder", "verify tasks folder", "verify repository structure",
    "create issue template", "create bug template", "create feature template", "finalize pull request template", "create CODEOWNERS", "define labels", "define milestones", "write branch protection checklist",
    "verify release build", "verify test suite", "verify all CI checks", "open Avalonia MainWindow",
]


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower().replace("wp-cli", "wpcli")).strip("-")[:56]


def title(epic_id: str, offset: int) -> str:
    if epic_id == "E00":
        return E00_TASKS[offset]
    topics = TOPICS[epic_id]
    return f"{ACTIONS[offset % len(ACTIONS)]} {topics[(offset // len(ACTIONS)) % len(topics)]}"


def task_uid(epic: dict, offset: int) -> str:
    return f"{epic['code']}-{offset + 1:03d}"


def task_content(number: int, epic: dict, name: str, uid: str) -> str:
    previous = f"T{number - 1:04d}" if number > 1 else "Repository bootstrap"
    next_task = f"T{number + 1:04d}" if number < TOTAL_TASKS else "MVP release gate"
    branch = f"{epic['prefix']}/{slug(name)}-yyyyMMdd-HHmm"
    return f'''# T{number:04d} — {name.capitalize()}

## UID bất biến
`{uid}`

## Trạng thái
`backlog`

## Epic
`{epic['id']} — {epic['name']}`

## Dependency bắt buộc
- `{previous}` phải hoàn thành và merge.

## Branch bắt buộc
`{branch}`

## Mục tiêu
Hoàn thành duy nhất phần **{name}** theo BRD, SRS và kiến trúc hiện hành.

## Phạm vi
- Thực hiện thay đổi nhỏ nhất đủ đạt mục tiêu.
- Chỉ sửa file trực tiếp cần thiết.
- Cập nhật test và tài liệu khi hành vi thay đổi.

## Ngoài phạm vi
- Không làm nội dung task kế tiếp.
- Không đổi kiến trúc hoặc package chính nếu chưa có ADR.
- Không refactor ngoài phạm vi.

## Yêu cầu triển khai
- Tuân thủ `AGENTS.md` và `docs/DEVELOPMENT_RULES.md`.
- UI không gọi trực tiếp Infrastructure.
- I/O và process phải async, có cancellation hoặc timeout khi phù hợp.
- Error phải có ngữ cảnh; log có cấu trúc và không chứa secret.
- Thay đổi dữ liệu rủi ro phải có backup hoặc rollback.

## Yêu cầu bảo mật
- Validate input tại boundary.
- Không ghép shell command từ input thô.
- Không ghi password, token, key hoặc connection secret vào log.
- Chặn path traversal và archive traversal khi xử lý file.
- Chỉ yêu cầu quyền nâng cao cho thao tác bắt buộc.

## Acceptance criteria
- [ ] Mục tiêu hoạt động và quan sát được.
- [ ] Không mở rộng ngoài phạm vi.
- [ ] Build không có warning mới.
- [ ] Test phù hợp đã thêm hoặc cập nhật.
- [ ] CI, security scan và format xanh.

## Kiểm tra bắt buộc
```bash
dotnet restore
dotnet build --configuration Release --no-restore
dotnet test --configuration Release --no-build
dotnet format --verify-no-changes
```

Task Docker phải chạy thêm:
```bash
docker compose -f docker/compose.dev.yml config
```

## Rollback
Revert PR. Thay đổi dữ liệu phải dùng rollback hoặc backup ghi trong PR.

## Task mở khóa tiếp theo
- `{next_task}`
'''


def validate_catalog(catalog: list[dict]) -> None:
    expected = 1
    for epic in catalog:
        if epic["start"] != expected:
            raise ValueError(f"Gap or overlap before {epic['id']}: expected {expected}, got {epic['start']}")
        expected = epic["end"] + 1
    if expected - 1 != TOTAL_TASKS:
        raise ValueError(f"Catalog must end at {TOTAL_TASKS}, got {expected - 1}")
    if len(E00_TASKS) != 70:
        raise ValueError(f"E00 must contain 70 explicit tasks, got {len(E00_TASKS)}")


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    validate_catalog(catalog)
    BACKLOG.mkdir(parents=True, exist_ok=True)
    EPICS.mkdir(parents=True, exist_ok=True)

    for old in BACKLOG.glob("T*.md"):
        old.unlink()

    master = [
        "# LocalWP — Master Task Plan",
        "",
        "> Nguồn thứ tự duy nhất. Chọn task số nhỏ nhất chưa hoàn thành và có dependency đã merge.",
        "",
        "## Task hiện tại",
        "",
        "`T0001` — `BOOT-001` — Initialize .NET 8 solution",
        "",
        "## Tổng quan",
        "",
        f"- Tổng task: **{TOTAL_TASKS}**",
        "- Mỗi task có ID thứ tự và UID bất biến theo epic.",
        "- Mỗi task: một branch, một PR, một kết quả nhỏ có thể rollback.",
        "",
    ]

    for epic in catalog:
        rows: list[str] = []
        epic_dir = EPICS / epic["id"]
        epic_dir.mkdir(parents=True, exist_ok=True)
        for number in range(epic["start"], epic["end"] + 1):
            offset = number - epic["start"]
            name = title(epic["id"], offset)
            uid = task_uid(epic, offset)
            filename = f"T{number:04d}-{slug(name)}.md"
            (BACKLOG / filename).write_text(task_content(number, epic, name, uid), encoding="utf-8")
            rows.append(f"- [ ] `T{number:04d}` · `{uid}` — {name.capitalize()} — `tasks/backlog/{filename}`")

        (epic_dir / "README.md").write_text(
            "\n".join([
                f"# {epic['id']} — {epic['name']}",
                "",
                f"Mã UID: `{epic['code']}`.",
                f"Dải task: `T{epic['start']:04d}`–`T{epic['end']:04d}`.",
                "",
                *rows,
                "",
            ]),
            encoding="utf-8",
        )
        master += [
            f"## {epic['id']} — {epic['name']}",
            "",
            f"- UID prefix: `{epic['code']}`",
            f"- Dải: `T{epic['start']:04d}`–`T{epic['end']:04d}`",
            f"- Chi tiết: `planning/epics/{epic['id']}/README.md`",
            "",
        ]

    MASTER.write_text("\n".join(master), encoding="utf-8")
    print(f"Generated {TOTAL_TASKS} task files and epic indexes.")


if __name__ == "__main__":
    main()
