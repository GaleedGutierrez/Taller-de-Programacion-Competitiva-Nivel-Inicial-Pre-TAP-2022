def main () -> None:
    measurements = input().split()

    X = int(measurements[0])
    Y = int(measurements[1])
    Z = int(measurements[2])

    if X != Y and X != Z and Y != Z:
        result = 'escaleno'
    elif X == Y and X == Z and Y == Z:
        result = 'equilatero'
    else:
        result = 'isosceles'

    print(result)


if __name__ == '__main__':
    main()