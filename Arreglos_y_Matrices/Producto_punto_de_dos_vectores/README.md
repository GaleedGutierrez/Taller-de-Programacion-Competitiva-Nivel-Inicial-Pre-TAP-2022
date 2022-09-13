# Producto punto de dos vectores

|           Puntos          |<span style="font-weight: normal;">9.49</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción

Escribe un programa que calcule el producto de dos vectores $\large a$ y $\large b$ de $\large n$ elementos cada uno. El producto punto de los vectores está dado por $\large \sum_{i = 0}^{n - 1} a_{i} b_{i}$ 

## Entrada

Un entero $\large n$ seguido de una línea con los $\large n$ enteros de $\large a$ y de otra línea con los $\large n$ enteros de $\large b$. Los enteros de los vectores aparecen separados por espacios. Puedes suponer que $\large 1 \leq n, a_{i}, b_{i} \leq 100$.

## Salida
Un entero que sea el valor del producto punto.

## Ejemplo

<table style="text-align: center;" >
    <thead>
        <tr>
            <th>Entrada</th>
            <th>Salida</th>
            <th>Descripción</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>3</p>
                <p>1 2 3</p>
                <p>4 5 6</p>
            </td>
            <td>32</td>
            <td>(1*4) + (2*5) + (3*6) = 32</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [rcc (rcc)](https://omegaup.com/profile/rcc/ "rcc (rcc)")
Problema subido en: 12/7/2020
Página: omegaup.com


------------

## Solución
### Python
```py
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
```