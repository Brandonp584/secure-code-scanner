from collections import Counter
from datetime import datetime
import json
import html

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

def export_html(findings, output_file, scan_path, security_score):
    severity_counts = Counter(
        finding["severity"] for finding in findings
    )

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    finding_rows = ""

    for finding in findings:
        finding_rows += f"""
        <tr>
            <td>{html.escape(finding["severity"])}</td>
            <td>{html.escape(finding["rule_id"])}</td>
            <td>{html.escape(finding["name"])}</td>
            <td>{html.escape(finding["file"])}</td>
            <td>{finding["line"]}</td>
            <td><code>{html.escape(finding["code"])}</code></td>
            <td>{html.escape(finding["description"])}</td>
        </tr>
        """

    report = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Code Scanner Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            color: #1f2937;
            padding: 24px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: #ffffff;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08);
        }}

        h1, h2 {{
            color: #111827;
        }}

        .metadata {{
            margin-bottom: 24px;
            color: #4b5563;
        }}

        .summary {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 12px;
            margin-bottom: 24px;
        }}

        .card {{
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            padding: 16px;
            border-radius: 10px;
            text-align: center;
        }}

        .card strong {{
            display: block;
            font-size: 24px;
            margin-top: 8px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 16px;
            font-size: 14px;
        }}

        th, td {{
            border: 1px solid #e5e7eb;
            padding: 10px;
            vertical-align: top;
            text-align: left;
        }}

        th {{
            background: #111827;
            color: white;
        }}

        code {{
            background: #f3f4f6;
            padding: 3px 6px;
            border-radius: 6px;
            display: inline-block;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Secure Code Scanner Report</h1>

        <div class="metadata">
            <p><strong>Tool:</strong> Secure Code Scanner</p>
            <p><strong>Version:</strong> 1.0.0</p>
            <p><strong>Generated:</strong> {generated_at}</p>
            <p><strong>Scan Path:</strong> {html.escape(scan_path)}</p>
        </div>

        <h2>Scan Summary</h2>

        <div class="summary">
            <div class="card">Critical<strong>{severity_counts.get("CRITICAL", 0)}</strong></div>
            <div class="card">High<strong>{severity_counts.get("HIGH", 0)}</strong></div>
            <div class="card">Medium<strong>{severity_counts.get("MEDIUM", 0)}</strong></div>
            <div class="card">Low<strong>{severity_counts.get("LOW", 0)}</strong></div>
            <div class="card">Score<strong>{security_score}/100</strong></div>
        </div>

        <h2>Findings</h2>

        <table>
            <thead>
                <tr>
                    <th>Severity</th>
                    <th>Rule</th>
                    <th>Name</th>
                    <th>File</th>
                    <th>Line</th>
                    <th>Code</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                {finding_rows}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"\nHTML report written to {output_file}")