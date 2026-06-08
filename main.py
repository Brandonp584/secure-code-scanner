import argparse
from scanner.engine import scan_project
from scanner.reporter import print_report

def main():
    parser = argparse.ArgumentParser(
        description="Secure Code Scanner - A Python SAST tool for detecting insecure code patterns."
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Path to the project folder to scan."
    )

    args = parser.parse_args()

    findings = scan_project(args.path)
    print_report(findings)

if __name__ == "__main__":
    main()