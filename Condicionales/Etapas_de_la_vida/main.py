def main () -> None:
    L = int(input())

    if L >= 0 and L <= 3:
        message = 'BEBE'
    elif L >= 4 and L <= 14:
        message = 'NINO'
    elif L >= 15 and L <= 18:
        message = 'JOVEN'
    elif L >= 19 and L <= 65:
        message = 'ADULTO'
    else:
        message = 'ADULTO 3RA'

    print(message)



if __name__ == '__main__':
    main()