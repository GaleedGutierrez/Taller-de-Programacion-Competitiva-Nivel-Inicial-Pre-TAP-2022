def main () -> None:
    galaxies = input().split()

    a = int(galaxies[0])
    b = int(galaxies[1])
    c = int(galaxies[2])

    result = ['']
    result.pop(0)
    result.append(str(bool(a < b)))
    result.append(str(bool(c > a)))
    result.append(str(bool(a == b)))
    result.append(str(bool(a != c)))
    result.append(str(bool(c <= b)))

    final = ' '.join(result)
    print(final)


if __name__ == '__main__':
    main()