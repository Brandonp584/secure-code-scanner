import json

def export_json(findings, output_file):
    report = {
        "scan_summary": {
            "total_findings": len(findings)
        },
        "findings": findings
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"\nJSON report written to {output_file}")