def main () -> None:
    AMOUNT_ELEMENTS = int(input())
    FIRST_ARRAY_USER = input().split()
    SECOND_ARRAY_USER = input().split()

    FIRST_ARRAY = list(map(int, FIRST_ARRAY_USER))
    SECOND_ARRAY = list(map(int, SECOND_ARRAY_USER))
    result = 1

    for i in range(len(FIRST_ARRAY)):
        if FIRST_ARRAY[i] <= SECOND_ARRAY[i]:
            result = 0
            break

    print(result)


if __name__ == "__main__":
    main()