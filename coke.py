def main():
    due = 50
    accepts = (5, 10, 25)
    while due > 0:
        print(f"Amount Due: {due}")
        paid = int(input("Insert Coin: "))
        if paid in accepts:
            due -= paid
    print(f"Change Owed: {-due}")

if __name__ == "__main__":
    main()