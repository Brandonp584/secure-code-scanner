import unittest
from pathlib import Path

from scanner.engine import scan_file
from scanner.reporter import calculate_security_score

class TestSecureCodeScanner(unittest.TestCase):

    def test_detects_eval_usage(self):
        test_file = Path("tests/temp_eval_test.py")
        test_file.write_text("eval(user_input)", encoding="utf-8")

        findings = scan_file(test_file)

        test_file.unlink()

        rule_ids = [finding["rule_id"] for finding in findings]
        self.assertIn("PY001", rule_ids)

    def test_detects_hardcoded_password(self):
        test_file = Path("tests/temp_password_test.py")
        test_file.write_text('password = "admin123"', encoding="utf-8")

        findings = scan_file(test_file)

        test_file.unlink()

        rule_ids = [finding["rule_id"] for finding in findings]
        self.assertIn("SEC001", rule_ids)

    def test_safe_code_has_no_findings(self):
        test_file = Path("tests/temp_safe_test.py")
        test_file.write_text('name = "Brandon"\nprint(name)', encoding="utf-8")

        findings = scan_file(test_file)

        test_file.unlink()

        self.assertEqual(len(findings), 0)

    def test_security_score_calculation(self):
        findings = [
            {"severity": "CRITICAL"},
            {"severity": "HIGH"},
            {"severity": "MEDIUM"},
        ]

        score = calculate_security_score(findings)

        self.assertEqual(score, 65)

if __name__ == "__main__":
    unittest.main()