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
        "id": "PY003",
        "name": "subprocess with shell=True detected",
        "severity": "HIGH",
        "description": "using shell=True can introduce command injection risks if user input reaches the command.",
        "pattern": re.compile(r"subprocess\.(run|call|Popen)\s*\(.*shell\s*=\s*True"),
    },
    {
        "id": "PY004",
        "name": "Possible command injection risk",
        "severity": "HIGH",
        "description": "os.system() executes shell commands and can be dangerous when combined with user input.",
        "pattern": re.compile(r"\bos\.system\s*\("),
    },
    {
        "id": "PY005",
        "name": "Unsafe pickle deserialization detected",
        "severity": "HIGH",
        "description": "pickle.load() and pickle.loads() can execute malicious code when loading untrusted data.",
        "pattern": re.compile(r"\bpickle\.loads?\s*\("),
    },
    {
        "id": "SQL001",
        "name": "Possible SQL injection risk",
        "severity": "HIGH",
        "description": "Building SQL queries with string formatting or concatenation can allow SQL injection.",
        "pattern": re.compile(
            r"(SELECT|INSERT|UPDATE|DELETE).*(\+|%|\.format\s*\(|f[\"'])",
            re.IGNORECASE
        ),
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
    {
        "id": "SEC003",
        "name": "Possible GitHub token",
        "severity": "CRITICAL",
        "description": "GitHub access token may be exposed.",
        "pattern": re.compile(r"github_pat_[A-Za-z0-9_]{20,}",)
    },
    {
        "id": "SEC004",
        "name": "Possible AWS access key",
        "severity": "CRITICAL",
        "description": "AWS access key detected in source code.",
        "pattern": re.compile(r"AKIA[0-9A-Z]{16}"),
    },
    {
        "id": "SEC005",
        "name": "Possible API key",
        "severity": "HIGH",
        "description": "Potential API key detected.",
        "pattern": re.compile(
            r"(api_key|apikey|secret_key)\s*=\s*[\"'].+[\"']",
            re.IGNORECASE
        ),
    },
    {
        "id": "SEC006",
        "name": "Possible hardcoded JWT secret",
        "severity": "CRITICAL",
        "description": "Hardcoded JWT secrets can allow attackers to forge or tamper with authentication tokens.",
        "pattern": re.compile(
            r"(jwt_secret|secret_key|token_secret)\s*=\s*[\"'].+[\"']",
            re.IGNORECASE
        ),
    },
]