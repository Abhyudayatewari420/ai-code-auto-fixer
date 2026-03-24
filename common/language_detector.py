def detect_language(code):
    if "#include" in code:
        return "cpp"
    elif "def " in code or "print(" in code or "prnit(" in code:
        return "python"
    else:
        return "unknown"