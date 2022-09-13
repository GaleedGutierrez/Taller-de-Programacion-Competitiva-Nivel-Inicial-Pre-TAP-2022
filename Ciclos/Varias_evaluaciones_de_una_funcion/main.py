from math import e


def main () -> None:
    USER_NUMBER = int(input())
    RESULTS = [1.1]
    RESULTS.pop(0)
    for i in range(1, USER_NUMBER + 1):
        f_de_x = e ** (2 * i) - i
        RESULTS.append(round(f_de_x, 3))

    NUMBERS = list(map(str, RESULTS))

    for i in range(len(NUMBERS)):
        print(f'{i + 1} {NUMBERS[i]}')


if __name__ == '__main__':
    main()
