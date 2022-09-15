def main () -> None:
    WORD = input().replace(' ', '').lower()
    VOWELS = [0, 0, 0, 0, 0]

    for i in WORD:
        if i == 'a':
            VOWELS[0] += 1
        elif i == 'e':
            VOWELS[1] += 1
        elif i == 'i':
            VOWELS[2] += 1
        elif i == 'o':
            VOWELS[3] += 1
        elif i == 'u':
            VOWELS[4] += 1

    RESULT = ' '.join(list(map(str,VOWELS)))
    print(RESULT)


if __name__ == "__main__":
    main()