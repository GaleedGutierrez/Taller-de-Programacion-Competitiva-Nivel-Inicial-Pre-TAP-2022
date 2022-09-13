def main () -> None:
    animals = input().split()

    catA = int(animals[0])
    catB = int(animals[1])
    mouse = int(animals[2])

    catA_mouse = abs(mouse - catA)
    catB_mouse = abs(mouse - catB)

    if catA_mouse < catB_mouse:
        message = 'gato A'
    elif catB_mouse < catA_mouse:
        message = 'gato B'
    else:
        message = 'raton C'

    print(message)


if __name__ == '__main__':
    main()