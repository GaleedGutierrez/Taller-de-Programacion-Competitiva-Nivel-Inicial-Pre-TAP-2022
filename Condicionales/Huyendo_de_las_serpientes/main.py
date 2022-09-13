def main () -> None:
    user = input().split()

    animal = user[0]
    distance = int(user[1])

    if animal == 's' and distance >= 10:
        message = 'retrocede y busca otro camino'
    elif animal == 's' and distance <= 10:
        message = 'corre, corre por tu vida!'
    else:
        message = 'estas a salvo!'


    print(message)


if __name__ == '__main__':
    main()