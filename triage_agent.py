import json

def triage_bandit_report(report_path="bandit-report.json"):
    with open(report_path) as f:
        report = json.load(f)

    issues = []
    for result in report["results"]:
        issue = {
            "issue": result["test_name"],
            "severity": result["issue_severity"],
            "confidence": result["issue_confidence"],
            "file": result["filename"],
            "line": result["line_number"],
            "details": result["issue_text"]
        }
        issues.append(issue)
    
    return issues

if __name__ == "__main__":
    issues = triage_bandit_report()
    for i, issue in enumerate(issues, 1):
        print(f"Issue {i}:")
        print(f"  Type       : {issue['issue']}")
        print(f"  Severity   : {issue['severity']}")
        print(f"  Confidence : {issue['confidence']}")
        print(f"  File       : {issue['file']}:{issue['line']}")
        print(f"  Details    : {issue['details']}")
        print("-" * 50)
