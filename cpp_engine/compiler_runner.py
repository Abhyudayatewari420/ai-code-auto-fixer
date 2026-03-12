import subprocess
import tempfile
import os

def run_cpp_code(code):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp", mode="w") as f:
        f.write(code)
        filename = f.name

    compile_cmd = ["g++", filename, "-o", filename + ".out"]

    result = subprocess.run(
        compile_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    os.remove(filename)

    if result.returncode != 0:
        return False, result.stderr
    else:
        return True, "Compilation successful"