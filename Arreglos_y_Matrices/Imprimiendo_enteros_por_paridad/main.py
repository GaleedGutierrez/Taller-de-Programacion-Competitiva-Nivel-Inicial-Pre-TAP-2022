def even_numbers (numbers: list[int]) -> list[int]:
    EVEN_NUMBERS = [1]
    EVEN_NUMBERS.pop(0)

    for i in numbers:
        if i % 2 == 0:
            EVEN_NUMBERS.append(i)
    return EVEN_NUMBERS

def odd_numbers (numbers: list[int]) -> list[int]:
    EVEN_NUMBERS = [1]
    EVEN_NUMBERS.pop(0)

    for i in numbers:
        if i % 2 != 0:
            EVEN_NUMBERS.append(i)
    return EVEN_NUMBERS


def main () -> None:
    AMOUNT_NUMBERS = int(input())
    NUMBERS_USER = input().split()
    OPTION = int(input())
    NUMBERS = list(map(int, NUMBERS_USER))

    result = [1]
    result.pop(0)

    if OPTION == 0:
        result = even_numbers(NUMBERS)
    if OPTION == 1:
        result = odd_numbers(NUMBERS)

    print(' '.join(list(map(str, result))))


if __name__ == '__main__':
    main()