def main () -> None:
    AMOUNT_NUMBERS = int(input())
    NUMBER_SEARCH = int(input())

    counter = 0
    repetitions = 0

    while counter < AMOUNT_NUMBERS:
        counter += 1
        NEW_NUMBER = int(input())
        if NEW_NUMBER == NUMBER_SEARCH:
            repetitions += 1
    print(repetitions)

if __name__ == '__main__':
    main()

