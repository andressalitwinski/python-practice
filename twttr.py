def main():
    VOWELS = "AEIOUaeiou"
    txt = input("Input: ")
    # builds a translation table (from, to, delete)
    table = str.maketrans("", "", VOWELS)
    txt_without_vowels = txt.translate(table)
    print(f"Output: {txt_without_vowels}")


if __name__ == "__main__":
    main()


""""
both O(n), but
translate:  Implemented in C
            No Python objects created per character
            No Python if, no Python generator, no Python method calls - avoid Python overhead
            Each character: one table lookup and one copy (or skip). Walks through the string once.
            used because: String may be large, operation is simple and rule is static. (and to practice)

join + generator:   Loop runs in Python
                    For every character: Python iteration, Python if, Python in, Python object handling
                    Same number of characters → much more overhead per character.
                    but more flexible and more readable
                    used in camel.py because the transformations needs logic
"""