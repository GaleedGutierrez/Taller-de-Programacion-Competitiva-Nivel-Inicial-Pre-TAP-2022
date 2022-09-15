def main () -> None:
    WORD = input().replace(' ', '').lower()
    IS_PALINDROMO = WORD == WORD[::-1]
    RESULT = 'SI' if IS_PALINDROMO else 'NO'
    print(RESULT)

if __name__ == "__main__":
    main()