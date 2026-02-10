from pyfiglet import Figlet
import random
import sys

VALID_FIRST_ARGS = {"-f", "--font"}


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    font = parse_args(fonts)

    if font is None:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))


def parse_args(fonts):
    # guard clause
    if len(sys.argv) == 1:
        return random.choice(fonts)
    if len(sys.argv) != 3:
        return None

    # = 3
    f, font = sys.argv[1], sys.argv[2]
    if f not in VALID_FIRST_ARGS or font not in fonts:
        return None

    return font


if __name__ == "__main__":
    main()
