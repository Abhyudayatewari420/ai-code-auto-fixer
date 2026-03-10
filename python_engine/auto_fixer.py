import ast

class AutoFixer(ast.NodeTransformer):

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            if node.func.id == "prnit":
                node.func.id = "print"

        return self.generic_visit(node)


def fix_code(code):

    tree = ast.parse(code)

    fixer = AutoFixer()

    fixed_tree = fixer.visit(tree)

    fixed_code = ast.unparse(fixed_tree)

    return fixed_code


# TEST
if __name__ == "__main__":

    code = 'prnit("Hello World")'

    fixed = fix_code(code)

    print("Original Code:")
    print(code)

    print("\nFixed Code:")
    print(fixed)