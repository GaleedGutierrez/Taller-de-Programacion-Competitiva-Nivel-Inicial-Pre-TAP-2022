def main () -> None:
    USER_NUMBER = int(input())
    numbers = [1]

    for i in range(2, USER_NUMBER + 1):
        numbers.append(i)
    numbers = map(str, numbers)
    numbers_str = list(numbers)
    FIRST = ' '.join(numbers_str )
    SECOND = ' '.join(numbers_str [::-1])
    print(FIRST)
    print(SECOND)


if __name__ == '__main__':
    main()