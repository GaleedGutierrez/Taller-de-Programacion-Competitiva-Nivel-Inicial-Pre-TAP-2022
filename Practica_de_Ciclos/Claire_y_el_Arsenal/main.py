def main () -> None:
    TOTAL_WEAPONS = int(input())
    POWER_EACH_WEAPONS_USER = input().split()

    POWER_EACH_WEAPONS = list(map(int, POWER_EACH_WEAPONS_USER))
    ORDER_POWER = POWER_EACH_WEAPONS.copy()
    POWER_EACH_WEAPONS.sort(reverse=True)


    for i in range(TOTAL_WEAPONS):
        if POWER_EACH_WEAPONS[0] == ORDER_POWER[i]:
            print(f'{POWER_EACH_WEAPONS[0]} {i + 1}')
            break


if __name__ == '__main__':
    main()