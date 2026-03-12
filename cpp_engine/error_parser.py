def parse_error(error_msg):

    lines = error_msg.split("\n")

    for line in lines:
        if "error:" in line:
            return line.strip()

    return "Unknown compilation error"