# La moda y sus signos

|           Puntos          |<span style="font-weight: normal;">15.56</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |

## Descripción
Dada una secuencia de $\large N$ dígitos del $\large 1$ al $\large 9$ donde cada dígito puede aparecer con signo $\large +$ o $\large -$

## Entrada
Un entero $\large N$ seguido de $\large N$ dígitos del $\large 1$ al $\large 9$ en versiones positivas o negativas. Puedes suponer que $\large 1 \leq N \leq 1000$.

## Salida
Un entero que sea el dígito que apareció más veces, seguido de dos enteros que sean la cantidad de veces que apareció dicho dígito en su forma positiva y negativa. En caso de empate en apariciones, debe dársele preferencia al dígito numéricamente menor (en magnitud).

## Ejemplo
<table style="text-align: center;" >
    <thead>
        <tr>
            <th>Entrada</th>
            <th>Salida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>12</p>
                <p>+1 +4 +4 +9 +7 +7 -9 +7 +4 +7 -4 -4</p>
            </td>
            <td>
                <p>4</p>
                <p>3 2</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>4</p>
                <p>+1 +2 +1 +2</p>
            </td>
            <td>
                <p>1</p>
                <p>2 0</p>
            </td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2018
Subido por: [rcc (rcc)](https://omegaup.com/profile/rcc/ "rcc (rcc)")
Problema subido en: 3/7/2018
Página: omegaup.com

------------

## Solución
### Python
```py
import operator


def repeated_numbers_sorted (number_container: dict[str, int]) -> dict[str, int]:
    REPEAT_NUMBERS = {'': 1}
    REPEAT_NUMBERS.pop('')

    for key in number_container:
        if not key[1] in REPEAT_NUMBERS:
            if key[0] == '+':
                opposite_key = key.replace('+', '-')
            else:
                opposite_key = key.replace('-', '+')
            if opposite_key in number_container:
                REPEAT_NUMBERS[opposite_key[1]] = number_container[opposite_key] + number_container[key]
            else:
                REPEAT_NUMBERS[opposite_key[1]] = number_container[key]

    SORTED_REPEAT_NUMBERS = dict(sorted(REPEAT_NUMBERS.items(), key=operator.itemgetter(1), reverse=True))
    return SORTED_REPEAT_NUMBERS


def the_most_repeat_number (number_container: dict[str, int]) -> str:
    the_most_repeated = list(number_container.keys())[0]

    for key in number_container:
        VALUE = number_container[key]
        if (number_container[the_most_repeated] <= VALUE) and (int(key) < int(the_most_repeated)):
            the_most_repeated = key

    return the_most_repeated


def main () -> None:
    AMOUNT_ELEMENTS = int(input())

    NUMBERS_WITH_SIGN = input().split()
    COUNTER_NUMBERS = {i:NUMBERS_WITH_SIGN.count(i) for i in NUMBERS_WITH_SIGN}

    REPEATED_NUMBER_SORTED = repeated_numbers_sorted(COUNTER_NUMBERS)
    THE_MOST_REPEATED_NUMBER = the_most_repeat_number(REPEATED_NUMBER_SORTED)


    THE_MOST_REPEATED_POSITIVE = f'+{THE_MOST_REPEATED_NUMBER}'
    THE_MOST_REPEATED_NEGATIVE = f'-{THE_MOST_REPEATED_NUMBER}'

    print(THE_MOST_REPEATED_NUMBER)
    THERE_IS_NEGATIVE = THE_MOST_REPEATED_NEGATIVE in COUNTER_NUMBERS
    if THERE_IS_NEGATIVE:
        print(f'{COUNTER_NUMBERS[THE_MOST_REPEATED_POSITIVE]} {COUNTER_NUMBERS[THE_MOST_REPEATED_NEGATIVE]}')
    else:
        print(f'{COUNTER_NUMBERS[THE_MOST_REPEATED_POSITIVE]} 0')


if __name__ == "__main__":
    main()
```