import argparse
from scanner.engine import scan_project
from scanner.reporter import (
    print_report,
    calculate_security_score
)
from scanner.exporter import export_json, export_html

def main():
    parser = argparse.ArgumentParser(
        description="Secure Code Scanner - A Python SAST tool for detecting insecure code patterns."
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Path to the project folder to scan."
    )

    parser.add_argument(
        "--json",
        help="Export findings to a json report file."
    )

    parser.add_argument(
        "--html",
        help="Export findings to an HTML report file."
    )

    args = parser.parse_args()

    findings = scan_project(args.path)
    print_report(findings)

    security_score = calculate_security_score(findings)

    if args.json:
        export_json(
            findings,
            args.json,
            args.path,
            security_score
        )
    
    if args.html:
        export_html(
            findings,
            args.html,
            args.path,
            security_score
        )

if __name__ == "__main__":
    main()