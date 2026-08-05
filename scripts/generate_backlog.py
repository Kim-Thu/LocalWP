from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "planning" / "EPIC_CATALOG.json"
BACKLOG = ROOT / "tasks" / "backlog"
MASTER = ROOT / "MASTER_TASK_PLAN.md"
EPICS = ROOT / "planning" / "epics"

ACTIONS = ["define", "validate", "model", "implement", "test", "document", "integrate", "harden", "observe", "review"]
TOPICS = {
"E00":["repository metadata","branch policy","commit policy","pull request template","issue template","agent onboarding","documentation index","security policy","dependency policy","CI guard"],
"E01":["solution file","SDK pinning","build properties","package management","domain project","application project","infrastructure project","desktop project","test projects","project references"],
"E02":["site identity","site slug","site domain","runtime state","environment config","WordPress config","database config","backup metadata","operation result","domain validation"],
"E03":["site repository","settings repository","atomic JSON write","schema version","migration pipeline","index recovery","path provider","secret storage","configuration validation","persistence diagnostics"],
"E04":["main window","sidebar","site list","site search","navigation service","dialog service","toast service","progress overlay","theme resources","view model lifecycle"],
"E05":["process request","argument escaping","stdout streaming","stderr streaming","cancellation","timeout","secret redaction","Docker CLI detection","Docker daemon detection","Compose detection"],
"E06":["compose model","image catalog","service naming","network naming","volume naming","Nginx config","PHP config","database config","health checks","config snapshots"],
"E07":["create-site request","wizard validation","site directory","config generation","image pull","container startup","database readiness","WP-CLI install","HTTP verification","provision rollback"],
"E08":["hosts entry","elevated helper","IPC contract","root CA","certificate trust","domain certificate","Nginx TLS","trust status","certificate renewal","SSL repair"],
"E09":["site start","site stop","site restart","site delete","container status","health status","last-started state","quick actions","log streaming","orphan detection"],
"E10":["connection details","Adminer","SQL import","GZip import","SQL export","GZip export","database reset","search replace","database shell","import rollback"],
"E11":["WP-CLI wrapper","core status","core update","plugin list","plugin install","plugin activation","plugin update","theme list","theme install","theme update"],
"E12":["backup request","database dump","source archive","backup metadata","integrity hash","backup listing","backup deletion","restore preflight","restore execution","restore rollback"],
"E13":["clone request","source copy","database snapshot","new site identity","new domain","new environment","URL replacement","new SSL","clone verification","clone rollback"],
"E14":["blueprint schema","blueprint metadata","config blueprint","full blueprint","plugin manifest","theme manifest","source template","database template","blueprint creation","blueprint provisioning"],
"E15":["runtime catalog","compatibility matrix","PHP preflight","PHP switch","PHP rollback","database preflight","database upgrade","downgrade guard","version health check","version audit log"],
"E16":["port conflict","container drift","missing config","hosts mismatch","SSL mismatch","broken index","config rebuild","diagnostic bundle","secret scrub","repair report"],
"E17":["Windows publish","self-contained build","installer","uninstaller","release workflow","artifact signing","release notes","upgrade path","end-to-end suite","stability gate"]}

def slug(v: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", v.lower().replace("wp-cli", "wpcli")).strip("-")[:48]

def title(epic: str, offset: int) -> str:
    return f"{ACTIONS[offset % 10]} {TOPICS[epic][(offset // 10) % 10]}"

def task(n: int, epic: dict, name: str) -> str:
    prev = f"T{n-1:04d}" if n > 1 else "Repository bootstrap"
    nxt = f"T{n+1:04d}" if n < 1220 else "MVP release gate"
    branch = f"{epic['prefix']}/{slug(name)}-yyyyMMdd-HHmm"
    return f'''# T{n:04d} — {name.capitalize()}

## Trạng thái
`backlog`

## Epic
`{epic['id']} — {epic['name']}`

## Dependency bắt buộc
- `{prev}` phải hoàn thành và merge.

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
- Không đổi kiến trúc/package chính nếu chưa có ADR.
- Không refactor ngoài phạm vi.

## Yêu cầu triển khai
- Tuân thủ `AGENTS.md` và `docs/DEVELOPMENT_RULES.md`.
- UI không gọi trực tiếp Infrastructure.
- I/O/process phải async, có cancellation/timeout khi phù hợp.
- Error có ngữ cảnh; log có cấu trúc và không chứa secret.
- Thay đổi dữ liệu rủi ro phải có backup hoặc rollback.

## Yêu cầu bảo mật
- Validate input tại boundary.
- Không ghép shell command từ input thô.
- Không ghi password, token, key hoặc connection secret vào log.
- Chặn path traversal/archive traversal khi có file/path.
- Chỉ yêu cầu quyền nâng cao cho thao tác bắt buộc.

## Acceptance criteria
- [ ] Mục tiêu hoạt động và quan sát được.
- [ ] Không mở rộng ngoài phạm vi.
- [ ] Build không có warning mới.
- [ ] Test phù hợp đã thêm/cập nhật.
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
Revert PR. Thay đổi dữ liệu phải dùng rollback/backup ghi trong PR.

## Task mở khóa tiếp theo
- `{nxt}`
'''

def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    BACKLOG.mkdir(parents=True, exist_ok=True)
    EPICS.mkdir(parents=True, exist_ok=True)
    for old in BACKLOG.glob("T*.md"): old.unlink()
    master = ["# LocalWP — Master Task Plan", "", "> Nguồn thứ tự duy nhất. Chọn task số nhỏ nhất chưa hoàn thành và có dependency đã merge.", "", "## Task hiện tại", "", "`T0001`", "", "## Tổng quan", "", "- Tổng task: **1220**", "- Mỗi task: một branch, một PR, một kết quả nhỏ có thể rollback.", ""]
    for epic in catalog:
        rows = []
        d = EPICS / epic["id"]
        d.mkdir(parents=True, exist_ok=True)
        for n in range(epic["start"], epic["end"] + 1):
            name = title(epic["id"], n - epic["start"])
            file = f"T{n:04d}-{slug(name)}.md"
            (BACKLOG / file).write_text(task(n, epic, name), encoding="utf-8")
            rows.append(f"- [ ] `T{n:04d}` — {name.capitalize()} — `tasks/backlog/{file}`")
        (d / "README.md").write_text("\n".join([f"# {epic['id']} — {epic['name']}", "", f"Dải task: `T{epic['start']:04d}`–`T{epic['end']:04d}`.", "", *rows, ""]), encoding="utf-8")
        master += [f"## {epic['id']} — {epic['name']}", "", f"- Dải: `T{epic['start']:04d}`–`T{epic['end']:04d}`", f"- Chi tiết: `planning/epics/{epic['id']}/README.md`", ""]
    MASTER.write_text("\n".join(master), encoding="utf-8")
    print("Generated 1220 task files and epic indexes.")

if __name__ == "__main__": main()
