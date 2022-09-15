def main () -> None:
    USER_INPUT = input().split()
    WORD = USER_INPUT[0]
    LETTER = USER_INPUT[1]
    counter = 0

    for i in WORD:
        if i == LETTER:
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()