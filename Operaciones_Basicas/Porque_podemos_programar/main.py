def main () -> None:
    x = float(input())

    op1 = (x + x ** 2)
    op2 = (5 * x + 3)
    op3 = op1 / op2
    y = (op3 + x) * (op3 / (op3 + 2 * x))
    y = round(y, 6)

    print(y)

if __name__ == '__main__':
    main()