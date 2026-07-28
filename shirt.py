"""
in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and
cropping the input to be the same size, saving the result as its output.

The program should instead exit via sys.exit:
- if the user does not specify exactly two command-line arguments,
- if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
- if the input’s name does not have the same extension as the output’s name, or
- if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, so that, when they’re resized and cropped,
the shirt appears to fit perfectly.
"""

import os
import sys

from PIL import Image, ImageOps

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png")


def get_file_names():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_extension = os.path.splitext(input_file)[1].lower()
    output_extension = os.path.splitext(output_file)[1].lower()

    if input_extension not in VALID_EXTENSIONS:
        sys.exit("Invalid input")
    if output_extension not in VALID_EXTENSIONS:
        sys.exit("Invalid output")
    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    return input_file, output_file


def main():
    input_file, output_file = get_file_names()

    try:
        with Image.open("shirt.png") as shirt, Image.open(input_file) as photo:
            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, shirt)
            photo.save(output_file)
    except FileNotFoundError as error:
        sys.exit(f"{error.filename} does not exist.")


if __name__ == "__main__":
    main()
