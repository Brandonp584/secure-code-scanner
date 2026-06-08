from datetime import datetime
import json

def export_json(findings, output_file, scan_path, security_score):
    report = {
        "tool": "Secure Code Scanner",
        "version": "1.0.0",
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scan_path": scan_path,
        "scan_summary": {
            "total_findings": len(findings),
            "security_score": security_score
        },
        "findings": findings
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"\nJSON report written to {output_file}")