def main () -> None:
    bone1 = input().split()
    bone2 = input().split()

    L1 = int(bone1[0])
    T1 = int(bone1[1])
    L2 = int(bone2[0])
    T2 = int(bone2[1])

    if L1 >= L2 and T1 >= T2:
        message = 'Hueso 1'
    elif L2 >= L1 and T2 >= T1:
        message = 'Hueso 2'
    else:
        message = 'Perrito confundido :('

    print(message);


if __name__ == '__main__':
    main()