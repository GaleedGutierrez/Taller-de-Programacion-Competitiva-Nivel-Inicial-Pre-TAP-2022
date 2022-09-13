def main () -> None:
    TIME = int(input())
    AMOUNT_SONGS = int(input())
    TIME_EACH_SONG_USER = input().split()
    TIME_EACH_SONG = list(map(int, TIME_EACH_SONG_USER))
    TOTAL_TIME_SONGS = sum(TIME_EACH_SONG)
    message_final = 'Es exacto'

    if TIME > TOTAL_TIME_SONGS:
        message_final = 'Es posible'
    if TIME < TOTAL_TIME_SONGS:
        message_final = 'No es posible'

    print(message_final)


if __name__ == '__main__':
    main()
