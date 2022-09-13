def main () -> None:
    AMOUNT_NUMBERS = int(input())
    A_USER = input().split()
    B_USER = input().split()

    A = list(map(int, A_USER))
    B = list(map(int, B_USER))
    total = 0

    for i in range(AMOUNT_NUMBERS):
        total += A[i] * B[i]

    print(total)

if __name__ == "__main__":
    main()