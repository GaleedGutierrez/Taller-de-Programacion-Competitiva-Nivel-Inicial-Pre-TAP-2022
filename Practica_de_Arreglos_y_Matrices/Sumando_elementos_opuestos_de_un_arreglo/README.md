# Sumando elementos opuestos de un arreglo

|           Puntos          |<span style="font-weight: normal;">9.74</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Dado un arreglo de $\large N$ enteros donde $\large K$ es par, escribe un programa que sume (en parejas) los elementos de lados opuestos del arreglo: el primer elemento con el último, el segundo elemento con el penúltimo, etc.

## Entrada
Un entero $\large N$ seguido de una línea con los $\large N$ enteros del arreglo separados por espacios. Puedes suponer que $\large 2 \leq N \leq 200$ y que $\large N$ es par.

## Salida
Los $\dfrac{N}{2}$ enteros que se obtienen al sumar los elementos de lados opuestos del arreglo, comenzando por los elementos de los extremos.

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
                <p>4</p>
                <p>1 10 100 1000</p>
            </td>
            <td>1001 110</td>
            <td>
                <p>El 1 se suma con el 1000.</p>
                <p>El 10 se suma con el 100.</p>
            </td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [rcc (rcc)](https://omegaup.com/profile/rcc/ "rcc (rcc)")
Problema subido en: 5/7/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    AMOUNT_ELEMENTS = int(input())
    ELEMENTS = list(map(int, input().split()))
    last = len(ELEMENTS) - 1

    for i in range(len(ELEMENTS) // 2):
        SUM_ELEMENTS = ELEMENTS[i] + ELEMENTS[last]
        print(SUM_ELEMENTS)
        last -= 1


if __name__ == "__main__":
    main()
```