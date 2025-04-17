import sys
from analyzer import analyze_code
from report import format_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file.py>")
        return

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as f:
            source_code = f.read()
            issues = analyze_code(source_code)
            report = format_report(issues)
            print(report)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    main()
