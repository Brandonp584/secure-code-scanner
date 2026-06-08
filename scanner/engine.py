from pathlib import Path
from scanner.rules import RULES

SUPPORTED_EXTENSIONS = {".py", ".js", ".ts", ".jsx", ".tsx"}

def scan_file(file_path):
    findings = []

    try:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception as error:
        return [{
            "rule_id": "READ_ERROR",
            "name": "File read error",
            "severity": "LOW",
            "description": str(error),
            "file": str(file_path),
            "line": 0,
            "code": "",
        }]
    
    for line_number, line in enumerate(lines, start=1):
        for rule in RULES:
            if rule["pattern"].search(line):
                findings.append({
                    "rule_id": rule["id"],
                    "name": rule["name"],
                    "severity": rule["severity"],
                    "description": rule["description"],
                    "file": str(file_path),
                    "line": line_number,
                    "code": line.strip(),
                })
    return findings

def scan_project(project_path):
    path = Path(project_path)

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {project_path}")
    
    findings = []

    for file_path in path.rglob("*"):
        if file_path.is_file() and file_path.suffix in SUPPORTED_EXTENSIONS:
            findings.extend(scan_file(file_path))

    return findings 