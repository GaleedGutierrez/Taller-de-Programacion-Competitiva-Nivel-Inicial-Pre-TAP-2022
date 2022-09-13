# Suma de la diagonal

|           Puntos          |<span style="font-weight: normal;">11.77</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Dada una matriz de $N \times N$ elementos, imprimir la suma de su diagonal.

## Entrada
La primera línea contiene un entero $\large n$. Posteriormente aparecen $\large n$ líneas con $\large n$ enteros por línea separados por espacios, los cuales denotan los elementos de la matriz. Puedes suponer que $\large 3 \leq n \leq 20$ y que los elementos de la matriz están entre $\large -10^6$ y $\large +10^6$.

## Salida
Un entero que corresponda con la suma de la diagonal de la matriz ingresada.

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
                <p>3</p>
                <p>8 3 9</p>
                <p>8 6 8</p>
                <p>1 4 6</p>
            </td>
            <td>20</td>
        </tr>
        <tr>
            <td>
                <p>5</p>
                <p>8 5 5 5 2</p>
                <p>4 9 8 5 2</p>
                <p>6 9 2 1 7</p>
                <p>8 9 9 3 8</p>
                <p>7 7 3 3 6</p>
            </td>
            <td>28</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [ Luis Pedroza (LuisPedroza)](https://omegaup.com/profile/LuisPedroza/ " Luis Pedroza (LuisPedroza)")
Problema subido en: 22/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    AMOUNT_ARRAYS = int(input())
    diagonal_sum = 0
    counter = 0

    while counter < AMOUNT_ARRAYS:
        NEW_ARRAY = list(map(int, input().split()))
        diagonal_sum += NEW_ARRAY[counter]
        counter += 1

    print(diagonal_sum)


if __name__ == "__main__":
    main()
```