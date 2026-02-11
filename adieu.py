import inflect


def main():
    names = []
    p = inflect.engine()
    while True:
        try:
            name = input("Name: ").strip()
            if name:
                names.append(name)
        except (EOFError, KeyboardInterrupt):
            if names:
                print(f"\nAdieu, adieu, to {p.join(names)}")
            break


if __name__ == "__main__":
    main()
