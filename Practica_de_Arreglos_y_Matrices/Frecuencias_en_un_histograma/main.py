from itertools import chain


def main () -> None:
    SPEC = list(map(int, input().split()))

    BINARY_CONTAINER = [[0]]
    BINARY_CONTAINER.pop(0)

    COUNTER_CONTAINER = [[1]]
    COUNTER_CONTAINER.pop(0)

    counter = 0
    counter_counter_container = 0

    while counter_counter_container< SPEC[1]:
        COUNTER_CONTAINER.append([0])
        counter_counter_container += 1

    while counter < SPEC[0]:
        BINARY_CONTAINER.append(list(map(int, input().split())))
        counter += 1

    for i in range(len(BINARY_CONTAINER)):
        for j in range(len(BINARY_CONTAINER[i])):
            if BINARY_CONTAINER[i][j] == 1:
                COUNTER_CONTAINER[j][0] += 1

    PREVIOUS_RESULT = list(chain.from_iterable(COUNTER_CONTAINER))
    RESULT = ' '.join(list(map(str, PREVIOUS_RESULT)))
    print(RESULT)


if __name__ == "__main__":
    main()