# Vector Dominante

|           Puntos          |<span style="font-weight: normal;">9.42</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción

Escribe un programa que lea dos secuencias de $\large n$ enteros cada una y determine si cada elemento de la primera secuencia es mayor que el elemento respectivo de la segunda secuencia.

## Entrada

Un entero seguido de una línea con los enteros de la primera secuencia y de otra línea con los enteros de la segunda secuencia. Los enteros de las secuencias aparecen separados por espacios. Puedes suponer que todos los enteros están en el rango de $\large 1$ a $\large 100$.

## Salida
El valor $\large 1$ si se cumple la propiedad descrita o el valor $\large 0$ en otro caso.

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
            <td>5 <br /> 9 7 7 7 7 <br  /> 8 3 4 5 6 </td>
            <td>1</td>
        </tr>
        <tr>
            <td>5 <br /> 9 7 7 7 7 <br /> 8 3 4 7 6 </td>
            <td>0</td>
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
    AMOUNT_ELEMENTS = int(input())
    FIRST_ARRAY_USER = input().split()
    SECOND_ARRAY_USER = input().split()

    FIRST_ARRAY = list(map(int, FIRST_ARRAY_USER))
    SECOND_ARRAY = list(map(int, SECOND_ARRAY_USER))
    result = 1

    for i in range(len(FIRST_ARRAY)):
        if FIRST_ARRAY[i] <= SECOND_ARRAY[i]:
            result = 0
            break

    print(result)


if __name__ == "__main__":
    main()
```