# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression 
# and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, 
# wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer

def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    if y == "/" and z == "0":
        return
    result = eval(expression)
    print(float(result))


main()