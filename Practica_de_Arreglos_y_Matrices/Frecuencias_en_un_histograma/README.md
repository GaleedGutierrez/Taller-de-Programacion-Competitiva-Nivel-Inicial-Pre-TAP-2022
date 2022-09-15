# Frecuencias en un histograma

|           Puntos          |<span style="font-weight: normal;">12.48</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Dada la representación de un histograma vertical, determinar la altura de cada una de sus barras.

## Entrada
La primera línea contiene dos enteros $\large n$ y $\large m$ . Posteriormente aparecen  líneas, cada una con  dígitos binarios separados por espacios. La representación del histograma se construye como sigue: los dígitos 1 forman parte de una barra vertical mientras que los dígitos **0** representan un espacio vacío en el histograma. Puedes suponer que $\large 3 \leq n, m \leq 20$.

## Salida
Una secuencia de $\large m$ enteros separados por espacios, donde cada entero representa la altura de la $\large i$ -esima barra del histograma.

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
                <p>6 3</p>
                <p>0 0 0</p>
                <p>0 0 0</p>
                <p>0 0 0</p>
                <p>0 1 0</p>
                <p>0 1 0</p>
                <p>1 1 1</p>
            </td>
            <td>1 3 1</td>
        </tr>
        <tr>
            <td>
                <p>3 4</p>
                <p>0 0 1 1</p>
                <p>0 1 1 1</p>
                <p>1 1 1 1</p>
            </td>
            <td>1 2 3 3</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [Luis Pedroza (LuisPedroza)](https://omegaup.com/profile/LuisPedroza/ "Luis Pedroza (LuisPedroza)")
Problema subido en: 23/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
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
```