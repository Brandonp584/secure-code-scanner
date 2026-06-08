import re 

RULES = [
    {
        "id": "PY001",
        "name": "Use of eval() detected",
        "severity": "HIGH",
        "description": "eval() can execute arbitrary code and may lead to code injection.",
        "pattern": re.compile(r"\beval\s*\("),
    },
    {
        "id": "PY002",
        "name": "Use of exec() detected",
        "severity": "HIGH",
        "description": "exec() can execute dynamic Python code and may be dangerous.",
        "pattern": re.compile(r"\bexec\s*\("),
    },
    {
        "id": "SEC001",
        "name": "Possible hardcoded password",
        "severity": "CRITICAL",
        "description": "Hardcoded credentials should not be stored directly in source code.",
        "pattern": re.compile(r"(password|passwd|pwd)\s*=\s*[\"'].+[\"']", re.IGNORECASE),
    },
    {
        "id": "SEC002",
        "name": "Weak hash algorithm detected",
        "severity": "MEDIUM",
        "description": "MD5 and SHA1 are weak hashing algorithms and should be avoided for security-sensitive use.",
        "pattern": re.compile(r"\b(md5|sha1)\s*\(", re.IGNORECASE),
    },
]