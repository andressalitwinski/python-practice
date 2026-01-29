# In a file called faces.py, implement a function called convert that accepts a str as
# input and returns that same input with any :) converted to slightly smiling face and any :( converted
# to a slightly frowning face. All other text should be returned unchanged.
# Then, in that same file, implement a function called main that prompts the user for input,
# calls convert on that input, and prints the result

def main():
    phrase = input("Say something using a happy or sad emoticon: ")
    print(convert(phrase))
    

def convert(phrase):
    return phrase.replace(":)", "\U0001F642").replace(":(", "\U0001F641")


main()