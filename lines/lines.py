import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if file_name[-3:] != '.py':
    sys.exit("Not a Python file")

def main():
    with open(file_name, "r") as file:
        code = file.readlines()
    lines = 0
    in_docstring = False
    for line in code:
        stripped = line.strip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            if stripped.endswith('"""') and len(stripped) > 6:
                continue
            if stripped.endswith("'''") and len(stripped) > 6:
                continue
            in_docstring = not in_docstring
            continue
        if in_docstring:
            continue
        if stripped == "":
            continue
        if stripped.startswith("#"):
            continue

        lines += 1
    print(lines)




try:
    main()
except FileNotFoundError:
    sys.exit("File does not exist")

