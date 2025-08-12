import re
import sys
from pathlib import Path

ADR_DIRS = [Path("docs/adr"), Path("architecture/adr")]

HEADER_RE = re.compile(r"^#\s*ADR-(\d+):\s+.+", re.IGNORECASE)
STATUS_RE = re.compile(r"^Status:\s*(Proposed|Accepted|Superseded|Deprecated)", re.IGNORECASE | re.MULTILINE)
TICKET_RE = re.compile(r"(https?://[^\\s]+/(issues|browse)/[A-Z0-9\\-]+)", re.IGNORECASE)

def find_adrs():
    files = []
    for base in ADR_DIRS:
        if base.exists():
            files.extend(base.rglob("*.md"))
    return files

def main():
    adrs = find_adrs()
    if not adrs:
        print("ADR Lint: nenhuma ADR encontrada (docs/adr ou architecture/adr).")
        return

    failures = []
    for f in adrs:
        content = f.read_text(encoding="utf-8")
        if not HEADER_RE.search(content):
            failures.append(f"Falta cabeçalho padrão em {f}")
        if not STATUS_RE.search(content):
            failures.append(f"Falta campo Status em {f}")
        if not TICKET_RE.search(content):
            failures.append(f"Falta link para ticket (Jira/GitHub) em {f}")

    if failures:
        print("ADR Lint: falhas encontradas:")
        print("\n".join(failures))
        sys.exit(1)
    else:
        print("ADR Lint: OK")

if __name__ == "__main__":
    main()
