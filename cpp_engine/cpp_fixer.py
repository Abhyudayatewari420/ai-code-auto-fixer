def fix_cpp_code(code):

    lines = code.split("\n")

    fixed_lines = []

    for line in lines:

        if (
            line.strip() != ""
            and not line.strip().endswith(";")
            and "cout" in line
        ):
            line = line + ";"

        fixed_lines.append(line)

    return "\n".join(fixed_lines)