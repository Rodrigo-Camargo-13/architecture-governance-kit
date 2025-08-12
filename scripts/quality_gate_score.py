import json, glob

def has_findings(sarif_path):
    try:
        with open(sarif_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for run in data.get("runs", []):
            for r in run.get("results", []):
                level = (r.get("level") or "").lower()
                if level in {"error","critical","high"}:
                    return True
    except Exception:
        pass
    return False

score = 100
penalties = 0

for sarif in glob.glob("*.sarif"):
    if has_findings(sarif):
        penalties += 20

score = max(0, score - penalties)
print(f"Quality Gate Score: {score}")
