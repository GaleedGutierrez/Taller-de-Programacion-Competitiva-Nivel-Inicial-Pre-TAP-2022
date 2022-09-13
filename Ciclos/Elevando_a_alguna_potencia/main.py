def main () -> None:
    USER_NUMBER = input().split()
    A = int(USER_NUMBER[0])
    B = int(USER_NUMBER[1])
    RESULT = A ** B
    print(f'{RESULT}')


if __name__ == "__main__":
    main()