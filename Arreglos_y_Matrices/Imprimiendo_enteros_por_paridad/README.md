# Imprimiendo enteros por paridad

|           Puntos          |<span style="font-weight: normal;">11.56</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Escribe un programa que lea un arreglo de $\large N$ enteros y un entero $\large P$. Si $\large P = 0$, tu programa deberá imprimir los valores del arreglo que sean pares; si $\large P = 1$, tu programa deberá imprimir los valores del arreglo que sean impares. El orden de aparición debe respetarse.

## Entrada
Un entero $\large N$ seguido de los $\large N$ enteros del arreglo y posteriormente un entero $\large P$. Puedes suponer que $\large 1 \leq N \leq 20$, que $\large 0 \leq P \leq 1$ y que los elementos del arreglo están entre $\large 0$ y $\large 100$ 

## Salida
Una secuencia de enteros separados por espacios que correspondan con lo solicitado en la descripción.

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
                <p>5</p>
                <p>2 5 9 6 1</p>
                <p>0</p>
            </td>
            <td>2 6</td>
        </tr>
        <tr>
            <td>
                <p>5</p>
                <p>2 5 9 6 1</p>
                <p>1</p>
            </td>
            <td>5 9 1</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2022
Subido por: [rcc (rcc)(COA21)](https://omegaup.com/profile/rcc/ "rcc (rcc)(COA21)")
Problema subido en: 14/5/2022
Página: omegaup.com

------------

## Solución
### Python
```py
def even_numbers (numbers: list[int]) -> list[int]:
    EVEN_NUMBERS = [1]
    EVEN_NUMBERS.pop(0)

    for i in numbers:
        if i % 2 == 0:
            EVEN_NUMBERS.append(i)
    return EVEN_NUMBERS

def odd_numbers (numbers: list[int]) -> list[int]:
    EVEN_NUMBERS = [1]
    EVEN_NUMBERS.pop(0)

    for i in numbers:
        if i % 2 != 0:
            EVEN_NUMBERS.append(i)
    return EVEN_NUMBERS


def main () -> None:
    AMOUNT_NUMBERS = int(input())
    NUMBERS_USER = input().split()
    OPTION = int(input())
    NUMBERS = list(map(int, NUMBERS_USER))

    result = [1]
    result.pop(0)

    if OPTION == 0:
        result = even_numbers(NUMBERS)
    if OPTION == 1:
        result = odd_numbers(NUMBERS)

    print(' '.join(list(map(str, result))))


if __name__ == '__main__':
    main()
```