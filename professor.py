import random


def main():
    l = get_level()
    correct = 0
    pairs = [(generate_integer(l), generate_integer(l)) for _ in range(10)]

    for x, y in pairs:
        wrong = 0
        while wrong < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    correct += 1
                    break
            except ValueError:
                pass

            wrong += 1
            print("EEE")

        if wrong == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level < 1 or level > 3:
        raise ValueError

    start = 10 ** (level - 1)
    end = 10**level - 1
    return random.randint(start, end)


if __name__ == "__main__":
    main()