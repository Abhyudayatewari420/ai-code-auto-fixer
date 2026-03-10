import ast

def parse_code(code: str):
    try:
        tree = ast.parse(code)
        return True, tree, None
    except SyntaxError as e:
        return False, None, str(e)

# TEST CASE
if __name__ == "__main__":
    sample_code = 'prnit("Hello")'

    success, tree, error = parse_code(sample_code)

    if success:
        print("AST generated successfully")
        print(ast.dump(tree, indent=4))
    else:
        print("Syntax Error found:")
        print(error)
