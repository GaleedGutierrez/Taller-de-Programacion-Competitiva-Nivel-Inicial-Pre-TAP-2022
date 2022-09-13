# Imprime pares en rango

|           Puntos          |<span style="font-weight: normal;">9.13</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Escriba un programa que imprima todos los números PARES que hay entre N y M.

## Entrada
Dos enteros N y M.

NOTA IMPORTANTE: El dato de entrada M siempre será mayor o igual a N.

## Salida
Imprima todos los números pares que hay entre N y M, uno por renglón.

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
            <td>3 20</td>
            <td>
                <p>4</p>
                <p>6</p>
                <p>8</p>
                <p>10</p>
                <p>12</p>
                <p>14</p>
                <p>16</p>
                <p>18</p>
                <p>20</p>
            </td>
        </tr>
        <tr>
            <td>40 50</td>
            <td>
                <p>40</p>
                <p>42</p>
                <p>44</p>
                <p>46</p>
                <p>48</p>
                <p>50</p>
            </td>
        </tr>
        <tr>
            <td>1 5</td>
            <td>
                <p>2</p>
                <p>4</p>
            </td>
        </tr>
    </tbody>
</table>

------------

Fuente: LGGT
Subido por: [GUTIERREZ TORRES LUIS GERMAN (licgerman) (COA21)](https://omegaup.com/profile/licgerman/ "GUTIERREZ TORRES LUIS GERMAN (licgerman) (COA21)")
Problema subido en: 6/3/2016
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    NUMBERS = input().split()
    FIRST_NUMBER = int(NUMBERS[0])
    SECOND_NUMBER = int(NUMBERS[1])
    FIRST_LIMIT = FIRST_NUMBER
    SECOND_LIMIT = SECOND_NUMBER + 1

    for dividend in range(FIRST_LIMIT, SECOND_LIMIT):
        EVEN_NUMBER = dividend % 2
        if EVEN_NUMBER == 0:
            print(dividend)

if __name__ == "__main__":
    main()
```