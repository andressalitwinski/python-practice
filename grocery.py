def main():
    list = {}
    while True:
        try:
            item = input().lower()
            list[item] += 1
        except KeyError:
            list[item] = 1
        except (EOFError, KeyboardInterrupt):
            for key in sorted(list):
                print(f"{list[key]} {key.upper()}")
            break


if __name__ == "__main__":
    main()