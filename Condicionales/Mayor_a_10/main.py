def main () -> None:
    age = float(input())
    message = 'Es mayor' if age > 10 else 'No es mayor'
    print(message)


if __name__ == '__main__':
    main()