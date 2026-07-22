# implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py,
# or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
# (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.


import sys


def get_file_name():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    return sys.argv[1]


def main():
    file_name = get_file_name()

    try:
        with open(file_name) as file:
            line_count = 0
            for line in file:
                stripped = line.strip()
                # if stripped and not stripped.startswith("#"):
                #     line_count += 1
                if not stripped:
                    continue
                if stripped.startswith("#"):
                    continue

                line_count += 1
            print(line_count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
