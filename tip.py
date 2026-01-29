# dollars_to_float should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float
# percent_to_float should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float
# Assume that the user will input values in the expected formats.


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d): 
    df = d.replace("$", "")
    return float(df)


def percent_to_float(p): 
    percent = float(p.replace("%", ""))
    return percent/100


main()