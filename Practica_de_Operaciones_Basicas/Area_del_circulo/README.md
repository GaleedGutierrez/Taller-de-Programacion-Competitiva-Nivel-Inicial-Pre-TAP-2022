# Area del circulo

|           Puntos          |<span style="font-weight: normal;">8.97</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Escribe un programa que calcule el área de un círculo dado su radio.

## Entrada
Un entero $\large R$ que denota el radio del círculo. Puedes suponer que $\large 0 < R < \sqrt{2*10^9}$.

## Salida
Un real impreso con dos cifras decimales que denote el área del círculo.

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
            <td>78.54</td>
        </tr>
    </tbody>
</table>

------------
Fuente: Giovanni de Jesus
Subido por: [Giovanni de Jesús Alejo Calderón (Giovannidb)](https://omegaup.com/profile/Giovannidb/ "Giovanni de Jesús Alejo Calderón (Giovannidb)")
Problema subido en: 5/3/2020
Página: omegaup.com

------------

## Solución
### Python
```py
import math

def main () -> None:
    radio = float(input())
    area = math.pi * radio ** 2
    area = round(area, 2)

    print(area)


if __name__ == '__main__':
    main()
```