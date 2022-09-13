def main () -> None:
    entrada = input().split()

    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])
    d = int(entrada[3])

    op = (a - b) * (c - d)

    print(op)


if __name__ == '__main__':
    main()