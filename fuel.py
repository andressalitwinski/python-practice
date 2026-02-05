def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            
            if x < 0 or y < 0 or x > y:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    
    p = round(100 * x/y)
    if p <= 1:
        print('E')
    elif p >= 99:
        print('F')
    else:
        print(f"{p}%")    


if __name__ == "__main__":
    main()