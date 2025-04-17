
## Static Code Analysis Tool

This Python-based static analysis tool scans source code for:
- Common programming mistakes
- Code style violations
- Deeply nested structures
- Missing docstrings
- Long functions
- And more!

## Features
- AST-based rule engine
- Extensible rules (add your own!)
- Handles syntax errors gracefully
- CLI interface for ease of use
- Configurable rule toggling (via `config.json`)

## Setup

```bash
git clone <your-repo-url>
cd project-folder
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py sample1.py
```

## Sample Files

You can test different issues using the sample files:
- `sample1.py` → Unused variable
- `sample2.py` → Indentation errors
- `sample6.py` → Missing docstrings
- `sample7.py` → Long function
- `sample8.py` → Deep nesting
- `sample9.py` → Combo of all rules

## ⚙️ Rule Configuration (Optional)

Edit `config.json` to enable/disable rules:

```json
{
  "unused_variable": true,
  "inconsistent_indentation": true,
  "missing_docstring": true,
  "long_function": true,
  "deep_nesting": true
}
```

## Architecture

- `main.py` – CLI entry point
- `analyzer.py` – Parses code and applies rules
- `rules.py` – Collection of all analysis rules
- `report.py` – Formats output for CLI or reports
- `config.json` – Optional rule toggle file

## Author

# Chinenyenwa Aso-Ibeh  

