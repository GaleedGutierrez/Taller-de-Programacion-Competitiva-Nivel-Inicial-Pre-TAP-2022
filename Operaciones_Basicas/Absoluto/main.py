def main () -> None:
    a = int(input())

    if a < 0:
        a = a * (-1)

    print(a)


if __name__ == '__main__':
    main()