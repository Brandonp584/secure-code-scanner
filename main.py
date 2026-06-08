import argparse
from scanner.engine import scan_project
from scanner.reporter import print_report
from scanner.exporter import export_json

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

    args = parser.parse_args()

    findings = scan_project(args.path)
    print_report(findings)

    if args.json:
        export_json(findings, args.json)

if __name__ == "__main__":
    main()