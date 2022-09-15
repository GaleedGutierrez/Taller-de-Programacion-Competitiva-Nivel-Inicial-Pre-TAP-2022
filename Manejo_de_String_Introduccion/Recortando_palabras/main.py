def main () -> None:
    WORD_AMOUNT_LETTERS = input().split()

    WORD = WORD_AMOUNT_LETTERS[0]
    AMOUNT_LETTERS = int(WORD_AMOUNT_LETTERS[1])
    WORD_BACKWARDS = WORD[::-1]
    WORD_BACKWARDS_LETTERS = WORD_BACKWARDS[:AMOUNT_LETTERS]

    print(f'{WORD[:AMOUNT_LETTERS]}{WORD_BACKWARDS_LETTERS[::-1]}')


if __name__ == "__main__":
    main()