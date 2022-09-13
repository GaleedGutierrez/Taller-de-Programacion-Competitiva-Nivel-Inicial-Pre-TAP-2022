# Varias evaluaciones de una función

|           Puntos          |<span style="font-weight: normal;">12.8</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Escribe un programa que evalúe la siguiente función para todos los enteros desde $\large x = 1$ hasta $\large n$.



## Problema
Haz un programa que te de un numero $\large n$ y te saque el $\large |n|$ (valor absoluto de $\large n$).

$$
\large f(x) = e^{2x} - x
$$

## Entrada
Un entero $\large n$ tal que $\large 1 \leq n \leq 15$

## Salida
Un total de $\large n$ lineas, donde cada una contenga dos números $\large x$ y $\large f(x)$ separados por un espacio. El valor de la función evaluada se debe imprimir con tres cifras significativas.

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
            <td>5</td>
            <td>
                <p>1 6.389</p>
                <p>2 52.598</p>
                <p>3 400.429</p>
                <p>4 2976.958</p>
                <p>5 22021.466</p>
            </td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [Luis Pedroza (LuisPedroza) (COA21)](https://omegaup.com/profile/LuisPedroza/ "Luis Pedroza (LuisPedroza) (COA21)")
Problema subido en: 7/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
from math import e


def main () -> None:
    USER_NUMBER = int(input())
    RESULTS = [1.1]
    RESULTS.pop(0)
    for i in range(1, USER_NUMBER + 1):
        f_de_x = e ** (2 * i) - i
        RESULTS.append(round(f_de_x, 3))

    NUMBERS = list(map(str, RESULTS))

    for i in range(len(NUMBERS)):
        print(f'{i + 1} {NUMBERS[i]}')


if __name__ == '__main__':
    main()
```