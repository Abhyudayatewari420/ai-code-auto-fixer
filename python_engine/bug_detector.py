import ast

class BugDetector(ast.NodeVisitor):
    def __init__(self):
        self.defined_functions = set(dir(__builtins__))  # built-in functions
        self.errors = []

    def visit_Call(self, node):
        # Check if function name exists
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name not in self.defined_functions:
                self.errors.append(
                    f" Undefined function '{func_name}' at line {node.lineno}"
                )
        self.generic_visit(node)


def detect_bugs(tree):
    detector = BugDetector()
    detector.visit(tree)
    return detector.errors


# TEST
if __name__ == "__main__":
    code = 'prnit("Hello")'
    tree = ast.parse(code)

    bugs = detect_bugs(tree)
    if bugs:
        print("Bugs found:")
        for b in bugs:
            print(b)
    else:
        print("No bugs found")
