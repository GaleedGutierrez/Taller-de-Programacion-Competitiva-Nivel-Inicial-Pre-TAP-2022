import math

def main () -> None:
    radio = float(input())
    area = math.pi * radio ** 2
    area = round(area, 2)

    print(area)


if __name__ == '__main__':
    main()