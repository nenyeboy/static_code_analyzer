import ast

def rule_unused_variable(tree):
    issues = []
    assigned = set()
    used = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assigned.add(target.id)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            used.add(node.id)

    unused = assigned - used
    for var in unused:
        issues.append(f"Unused variable detected: '{var}'")
    return issues

def rule_inconsistent_indentation(lines):
    issues = []
    for idx, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        if not stripped:  # skip empty or whitespace-only lines
            continue

        indent = len(line) - len(stripped)

        if "\t" in line:
            issues.append(f"Line {idx}: Uses tab instead of spaces.")
        elif indent % 4 != 0:
            issues.append(f"Line {idx}: Indentation not a multiple of 4.")
    return issues

def rule_missing_docstrings(tree):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if ast.get_docstring(node) is None:
                issues.append(f"Function '{node.name}' is missing a docstring.")
    return issues

def rule_long_functions(source_code):
    issues = []
    lines = source_code.splitlines()
    tree = ast.parse(source_code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno
            end_line = max(getattr(n, 'lineno', start_line) for n in ast.walk(node))
            length = end_line - start_line + 1
            if length > 20:  # threshold
                issues.append(f"Function '{node.name}' is too long ({length} lines).")
    return issues

def get_nesting_depth(node, current=0):
    if isinstance(node, (ast.If, ast.For, ast.While)):
        child_depths = [get_nesting_depth(child, current + 1) for child in ast.iter_child_nodes(node)]
        return max(child_depths, default=current + 1)
    else:
        return max([get_nesting_depth(child, current) for child in ast.iter_child_nodes(node)], default=current)

def rule_deep_nesting(tree):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            depth = get_nesting_depth(node)
            if depth > 3:
                issues.append(f"Function '{node.name}' has deep nesting (depth {depth}).")
    return issues

