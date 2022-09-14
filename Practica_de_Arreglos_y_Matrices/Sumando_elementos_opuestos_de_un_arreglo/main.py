def main () -> None:
    AMOUNT_ELEMENTS = int(input())
    ELEMENTS = list(map(int, input().split()))
    last = len(ELEMENTS) - 1

    for i in range(len(ELEMENTS) // 2):
        SUM_ELEMENTS = ELEMENTS[i] + ELEMENTS[last]
        print(SUM_ELEMENTS)
        last -= 1


if __name__ == "__main__":
    main()