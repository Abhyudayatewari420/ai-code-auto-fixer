def select_best_fix(bugs, fixes):
    """
    Select the best fix from a list of possible fixes.
    Currently rule-based logic is used.
    """

    if not bugs:
        return None

    # Simple heuristic rules
    for bug in bugs:

        if "Undefined function" in bug:
            return fixes.get("function_fix")

        if "syntax error" in bug.lower():
            return fixes.get("syntax_fix")

        if "missing semicolon" in bug.lower():
            return fixes.get("semicolon_fix")

    return None