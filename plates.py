def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return check_len(s) and no_marks(s) and starts_with_letters(s) and check_numbers(s)


def check_len(s):
    return 2 <= len(s) <= 6


def no_marks(s):
    return s.isalnum()


def starts_with_letters(s):
    return s[:2].isalpha()


def check_numbers(s):
    if s.isalpha():
        return True
    else:
        first_number = next((c for c in s if c.isdigit()), None)
        if first_number != "0":
            no_digit_between_letters = False
            for c in s:
                if c in "0123456789":
                    no_digit_between_letters = True
                else:
                    # has a letter after a digit
                    no_digit_between_letters = False
            return no_digit_between_letters
        else:
            return False


main()