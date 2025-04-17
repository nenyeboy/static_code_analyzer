import ast
import json
from rules import (
    rule_unused_variable,
    rule_inconsistent_indentation,
    rule_missing_docstrings,
    rule_long_functions,
    rule_deep_nesting
)

def load_config():
    """
    Loads the config.json file to determine which rules are enabled.
    If the file is missing, all rules default to enabled.
    """
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "unused_variable": True,
            "inconsistent_indentation": True,
            "missing_docstring": True,
            "long_function": True,
            "deep_nesting": True
        }

def analyze_code(source_code):
    """
    Analyzes the provided source code using AST-based and line-based rules.
    Returns a list of issues found.
    """
    issues = []
    config = load_config()

    try:
        # Parse source code into an AST (Abstract Syntax Tree)
        tree = ast.parse(source_code)
        lines = source_code.splitlines()

        # Apply enabled rules
        if config.get("unused_variable"):
            issues.extend(rule_unused_variable(tree))
        if config.get("inconsistent_indentation"):
            issues.extend(rule_inconsistent_indentation(lines))
        if config.get("missing_docstring"):
            issues.extend(rule_missing_docstrings(tree))
        if config.get("long_function"):
            issues.extend(rule_long_functions(source_code))
        if config.get("deep_nesting"):
            issues.extend(rule_deep_nesting(tree))

        # Return list of issues or a clean message
        return issues if issues else ["No issues detected."]

    except SyntaxError as e:
        return [f"Syntax Error: {e}"]
