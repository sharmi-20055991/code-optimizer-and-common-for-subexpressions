def parse_expression(line):
    """Split a statement into LHS and RHS"""
    if '=' not in line:
        return None, None
    lhs, rhs = line.split('=')
    lhs = lhs.strip()
    rhs = rhs.strip()
    return lhs, rhs


def common_subexpression_elimination(code_lines):
    """Perform Common Subexpression Elimination (CSE)"""
    expr_map = {}   # Map from expression → variable name
    optimized_code = []

    for line in code_lines:
        lhs, rhs = parse_expression(line)
        if not lhs or not rhs:
            continue

        # Check if this expression has already been computed
        if rhs in expr_map:
            prev_var = expr_map[rhs]
            optimized_code.append(f"{lhs} = {prev_var}")
        else:
            expr_map[rhs] = lhs
            optimized_code.append(f"{lhs} = {rhs}")

    return optimized_code


def main():
    print("=== Common Subexpression Elimination (CSE) ===")
    print("Enter code lines (blank line to finish):")

    code_lines = []
    while True:
        line = input()
        if not line.strip():
            break
        code_lines.append(line)

    optimized = common_subexpression_elimination(code_lines)

    print("\n--- Optimized Code ---")
    for line in optimized:
        print(line)


if __name__ == "__main__":
    main()
