''''
implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, 
and outputs a table formatted as ASCII art using tabulate.
Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.
'''

import sys
import csv
from tabulate import tabulate


def get_file_name():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    return sys.argv[1]


def main():
    file_name = get_file_name()

    try:
        with open(file_name) as file:
            table = []
            reader = csv.reader(file)
            table = list(reader)
            # for row in reader:
            #     table.append(row)

            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
