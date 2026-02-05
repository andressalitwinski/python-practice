months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def main():
    while True:
        date = input("Date: ")
        parsed_date = parse_numeric_date(date) or parse_str_date(date)

        if parsed_date:
            y, m, d = parsed_date
            print(f"{y:04}-{m:02}-{d:02}")
            break


def parse_numeric_date(date):
    try:
        m, d, y = map(int, date.split("/"))
        if  0 < m < 13 and 0 < d < 32 and 0 <= y <= 9999:
            return y, m, d
    except ValueError:
        pass
    return None


def parse_str_date(date):
    try:
        month_name, rest = date.split(" ", 1)
        d, y = map(int, rest.split(", "))
        m = months.index(month_name) + 1
        if  0 < d < 32 and 0 <= y <= 9999:
            return y, m, d
    except (ValueError, IndexError):
        pass
    return None


if __name__ == "__main__":
    main()