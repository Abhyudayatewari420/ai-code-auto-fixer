import common.language_detector as ld

from python_engine.parser import parse_code
from python_engine.bug_detector import detect_bugs
from python_engine.auto_fixer import fix_code

from cpp_engine.compiler_runner import run_cpp_code
from cpp_engine.error_parser import parse_error
from cpp_engine.cpp_fixer import fix_cpp_code


def run_system(code):

    print("\n==============================")
    print("Original Code:")
    print(code)

    lang = ld.detect_language(code)
    print("\nDetected Language:", lang)

    # -------- PYTHON --------
    if lang == "python":

        success, tree, error = parse_code(code)

        if not success:
            print("Syntax Error:", error)
            return

        bugs = detect_bugs(tree)

        print("\nBugs:", bugs)

        fixed = fix_code(code)

        print("\nFixed Code:")
        print(fixed)

    # -------- CPP --------
    elif lang == "cpp":

        success, output = run_cpp_code(code)

        if not success:
            parsed = parse_error(output)

            print("\nError:", parsed)

            fixed = fix_cpp_code(code)

            print("\nFixed Code:")
            print(fixed)

        else:
            print("\nCompilation Successful")

    else:
        print("\nUnknown Language")

    print("==============================\n")


if __name__ == "__main__":
    code = 'prnit("Hello World")'
    run_system(code)