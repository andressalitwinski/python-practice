import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass
    
    number = random.randint(1, n)

    while True:
        try:
            g = int(input("Guess: "))
            if g > 0:
                if g < number:
                    print("Too small!")
                    pass
                if g > number:
                    print("Too large!")
                    pass
                if g == number:
                    print("Just right!")
                    break
        except ValueError:
            pass


if __name__ == "__main__":
    main()