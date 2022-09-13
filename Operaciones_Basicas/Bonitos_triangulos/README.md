# Bonitos triángulos

|           Puntos          |<span style="font-weight: normal;">10.5</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |

## Descripción
¡Brenda ha encontrado un nuevo pasatiempo! Ella encuentra fascinante estudiar sobre los polígonos y sus propiedades. Para esta semana, ella se ha enfocado en los polígonos de tres lados y en cómo calcular su área. Ayuda a Brenda a calcular el área de los triángulos que te pide. Ella te dará la base y la altura, además de que también te asegura que el área de los triángulos siempre será un número entero.

## Entrada
Dos enteros $\large B$ y $\large H$, cada uno en su propia línea, los cuales representan la base y la altura del triángulo, respectivamente.

## Salida
Un entero que representa el área del triángulo. Puedes suponer que su valor cabe en un entero de 32 bits.

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
            <td>5<br />4</td>
            <td>10</td>
        </tr>
        <tr>
            <td>10<br />3</td>
            <td>15</td>
        </tr>
    </tbody>
</table>

------------

Fuente: Coding Rush (Edmundo Gatica + Jorge Chang)
Subido por: [CodingRush (CodingRush)](https://omegaup.com/profile/CodingRush/ "CodingRush (CodingRush)")
Problema subido en: 10/10/2018
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    h = int(input())
    b = int(input())
    area = int(h * b / 2)
    print(area)


if __name__ == '__main__':
    main()
```