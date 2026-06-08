from collections import Counter

SEVERITY_ORDER = {
    "CRITICAL": 1,
    "HIGH": 2,
    "MEDIUM": 3,
    "LOW": 4,
}

def print_report(findings):
    if not findings:
        print("\nNo security findings detected.")
        return
    
    findings = sorted(
        findings,
        key=lambda finding: SEVERITY_ORDER.get(finding["severity"], 99)
    )

    severity_counts = Counter(
        finding["severity"] for finding in findings
    )

    print("\nScan Summary")
    print("=" * 50)

    print(f"CRITICAL: {severity_counts.get('CRITICAL', 0)}")
    print(f"HIGH: {severity_counts.get('HIGH', 0)}")
    print(f"MEDIUM: {severity_counts.get('MEDIUM', 0)}")
    print(f"LOW: {severity_counts.get('LOW', 0)}")

    print(f"\nTotal Findings: {len(findings)}")

    print("\nSecure Code Scanner Report:")
    print("=" * 50)

    for finding in findings:
        print(f"\n[{finding['severity']}] {finding['name']}")
        print(f"Rule: {finding['rule_id']}")
        print(f"File: {finding['file']}")
        print(f"Line: {finding['line']}")
        print(f"Code: {finding['code']}")
        print(f"Why it matters: {finding['description']}")

    print("\nScan complete.")