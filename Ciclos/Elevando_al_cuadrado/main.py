def main () -> None:
    USER_NUMBER = int(input())
    LIMIT = 30000
    repetitions = 0
    final_number = USER_NUMBER

    while final_number < LIMIT:
        final_number = final_number ** 2
        repetitions += 1

    print(f'{final_number} {repetitions}')


if __name__ == "__main__":
    main()
