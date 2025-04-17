def format_report(issues):
    report = "\n--- Static Code Analysis Report ---\n"
    for issue in issues:
        report += f"- {issue}\n"
    report += "--- End of Report ---"
    return report
