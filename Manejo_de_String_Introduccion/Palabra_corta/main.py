def is_even (number: int) -> str:
    IS_EVEN = number % 2 == 0
    return 'par' if IS_EVEN else 'impar'

def main () -> None:
    AMOUNT_WORD = int(input())
    WORDS = ['']
    WORDS.pop(0)
    counter = 0

    while counter < AMOUNT_WORD:
        counter += 1
        NEW_WORD = input()
        WORDS.append(NEW_WORD)

    shortest_word_length = len(WORDS[0])
    shortest_word = WORDS[0]

    for i in range(1, len(WORDS)):
        if  len(WORDS[i]) < shortest_word_length:
            shortest_word_length = len(WORDS[i])
            shortest_word = WORDS[i]

    PARITY = is_even(shortest_word_length)
    print(shortest_word)
    print(shortest_word_length)
    print(PARITY)


if __name__ == "__main__":
    main()