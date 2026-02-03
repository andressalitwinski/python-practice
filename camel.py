def main():
    camel = input("camelCase: ")
    snake = "".join("_" + c.lower() if c.isupper() else c for c in camel).lstrip("_")
    # result = []
    # for c in camel:
    #     if c.isupper():
    #         result.append("_")
    #         result.append(c.lower())
    #     else:
    #         result.append(c)
    # snake = "".join(result).lstrip("_")
    print(f"snake_case: {snake}")


if __name__ == "__main__":
    main()