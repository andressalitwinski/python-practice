import emoji


def main():
    phrase = input("Input: ")
    print(emoji.emojize(phrase, language="alias"))


if __name__ == "__main__":
    main()
