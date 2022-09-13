def main () -> None:
    numbers = input().split()

    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])

    if a > b and a > c:
        message = f'{a}'
    elif b > a and b > c:
        message = f'{b}'
    else:
        message = f'{c}'

    print(message)


if __name__ == '__main__':
    main()