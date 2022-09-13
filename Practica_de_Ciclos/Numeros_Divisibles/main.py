def main () -> None:
    PEDROS_AMOUNT_NUMBERS = int(input())
    DIVISOR = int(input())

    counter = 0
    numbers_divisibles = 0

    while counter < PEDROS_AMOUNT_NUMBERS:
        counter += 1
        NUMBER_TO_DIVIDED = int(input())
        IS_DIVISBLE = NUMBER_TO_DIVIDED % DIVISOR == 0
        if IS_DIVISBLE:
            numbers_divisibles += 1

    print(numbers_divisibles)


if __name__ == '__main__':
    main()
