# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, 
# or dinner time. breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
# If it’s not time for a meal, don’t output anything at all. 
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, 
# to the corresponding number of hours as a float. (given a time like "7:30", convert should return 7.5.

def main():
    time = input("What time is it? ")
    meal_time = convert(time)
    if 7 <= meal_time <= 8:
        print("Breakfast time")
    elif 12 <= meal_time <= 13:
        print("Lunch time")
    elif 18 <= meal_time <= 19:
        print("Dinner time")


def convert(time):
    h, m = time.split(":")
    return float(h) + float(m) / 60


if __name__ == "__main__":
    main()