def main():
    try:
        percentage = convert(input("Fraction: "))
        print(gauge(percentage))
    except ValueError:
        print("Invalid fraction")
    except ZeroDivisionError:
        print("Cannot divide by zero")


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round(100 * (x / y))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
