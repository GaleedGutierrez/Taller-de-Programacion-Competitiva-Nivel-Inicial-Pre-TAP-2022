def main () -> None:
    NUMBERS = input().split()
    FIRST_NUMBER = int(NUMBERS[0])
    SECOND_NUMBER = int(NUMBERS[1])
    FIRST_LIMIT = FIRST_NUMBER
    SECOND_LIMIT = SECOND_NUMBER + 1

    for dividend in range(FIRST_LIMIT, SECOND_LIMIT):
        EVEN_NUMBER = dividend % 2
        if EVEN_NUMBER == 0:
            print(dividend)

if __name__ == "__main__":
    main()