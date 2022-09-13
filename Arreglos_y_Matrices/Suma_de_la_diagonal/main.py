def main () -> None:
    AMOUNT_ARRAYS = int(input())
    diagonal_sum = 0
    counter = 0

    while counter < AMOUNT_ARRAYS:
        NEW_ARRAY = list(map(int, input().split()))
        diagonal_sum += NEW_ARRAY[counter]
        counter += 1

    print(diagonal_sum)


if __name__ == "__main__":
    main()