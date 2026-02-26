VOWELS = "AEIOUaeiou"
table = str.maketrans("", "", VOWELS)


def main():
    txt = input("Input: ")
    print("Output: ", shorten(txt))


def shorten(txt):
    txt_without_vowels = txt.translate(table)
    return txt_without_vowels


if __name__ == "__main__":
    main()
