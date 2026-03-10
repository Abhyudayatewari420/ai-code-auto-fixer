from python_engine.parser import parse_code
from python_engine.bug_detector import detect_bugs
from python_engine.auto_fixer import fix_code


def run_system(code):

    print("\nOriginal Code:")
    print(code)

    # Step 1: Parse
    success, tree, error = parse_code(code)

    if not success:
        print("\nSyntax Error:", error)
        return

    # Step 2: Detect Bugs
    bugs = detect_bugs(tree)

    if bugs:
        print("\nBugs Detected:")
        for bug in bugs:
            print(bug)
    else:
        print("\nNo Bugs Found")

    # Step 3: Auto Fix
    fixed = fix_code(code)

    print("\nFixed Code:")
    print(fixed)


if __name__ == "__main__":

    code = 'prnit("Hello World")'

    run_system(code)