def main () -> None:
    numbers = input().split()

    a = int(numbers[0])
    b = int(numbers[1])
    final = 0
    SUM_INITIAL = a + b

    if SUM_INITIAL == 5:
        b += 3
        final = 2 * a + b
    else:
        a -= 1
        SUM_SECOND = 7 * a + b
        if SUM_SECOND % 2 == 0:
            final = a - b
        else:
            final = a * b


    print(final)


if __name__ == '__main__':
    main()