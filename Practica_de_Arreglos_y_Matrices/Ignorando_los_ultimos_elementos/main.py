def main () -> None:
    AMOUNT_ELEMENTS = int(input())
    ELEMENTS = list(map(int, input().split()))
    ELEMENTS_IGNORE = int(input())

    for i in range(len(ELEMENTS) - ELEMENTS_IGNORE):
        print(ELEMENTS[i])


if __name__ == "__main__":
    main()