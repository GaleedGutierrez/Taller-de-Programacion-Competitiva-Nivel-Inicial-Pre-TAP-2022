def main () -> None:
    AMOUNT_NUMBERS = int(input())
    NUMBERS = [1]
    NUMBERS.pop(0)
    counter = 0
    sum = 0

    while counter < AMOUNT_NUMBERS:
        number_user = int(input())
        NUMBERS.append(number_user)
        counter += 1

    for i in range(len(NUMBERS)):
        sum += NUMBERS[i]

    print(sum)


if __name__ == '__main__':
    main()
