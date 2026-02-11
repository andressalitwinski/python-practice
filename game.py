import random


def main():

    level = get_positive_int("Level: ")
    number = random.randint(1, level)

    while True:
        g = get_positive_int("Guess: ")

        if g < number:
            print("Too small!")
        elif g > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_positive_int(msg):
    while True:
        try:
            n = int(input(msg))
            if n > 0:
                return n
        except ValueError:
            pass


if __name__ == "__main__":
    main()
