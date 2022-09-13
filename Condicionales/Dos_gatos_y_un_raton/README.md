# Dos gatos y un ratón

|           Puntos          |<span style="font-weight: normal;">10.22</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Dos gatos y un ratón se encuentran en varias posiciones sobre una línea. Como valor de entrada te vamos a dar sus posiciones iniciales. Tu tarea es determinar cuál gato alcanzará al ratón primero, asumiendo que el ratón no se mueve y ambos gatos se mueven a la misma velocidad.

**OJO**: Si ambos gatos llegan al mismo tiempo, el ratón podrá escapar mientras que los dos gatos pelean.

## Entrada
Se te darán como valores de entrada tres enteros $\large A$, $\large B$ y $\large C$ separados por un espacio, los cuales representan respectivamente las posiciones del gato $\large A$, del gato $\large B$ y  del ratón $\large C$. Puedes suponer que $\large 1 \leq A,B,C \leq 100$

## Salida
- Si el gato $\large A$ alcanza primero al ratón, imprimir como salida "gato A".
- Si el gato $\large B$ alcanza primero al ratón, imprimir como salida "gato B".
- Si ambos gatos alcanzan al ratón $\large C$ al mismo tiempo, imprimir como salida "raton C".

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
            <td>1 2 3</td>
            <td>gato B</td>
        </tr>
        <tr>
            <td>1 3 2</td>
            <td>raton C</td>
        </tr>
        <tr>
            <td>gato B</td>
            <td>gato B</td>
        </tr>
        <tr>
            <td>8 3 12</td>
            <td>gato A</td>
        </tr>
    </tbody>
</table>

------------

Fuente: BeeHigh 2020
Subido por: [Miguel Ángel Mireles Vázquez (BeeHigh1)(COA21)](https://omegaup.com/profile/BeeHigh1/ "Miguel Ángel Mireles Vázquez (BeeHigh1)(COA21)")
Problema subido en: 15/6/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    animals = input().split()

    catA = int(animals[0])
    catB = int(animals[1])
    mouse = int(animals[2])

    catA_mouse = abs(mouse - catA)
    catB_mouse = abs(mouse - catB)

    if catA_mouse < catB_mouse:
        message = 'gato A'
    elif catB_mouse < catA_mouse:
        message = 'gato B'
    else:
        message = 'raton C'

    print(message)


if __name__ == '__main__':
    main()
```