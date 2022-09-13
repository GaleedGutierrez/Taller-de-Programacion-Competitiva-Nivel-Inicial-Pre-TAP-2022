# Elevando al cuadrado

|           Puntos          |<span style="font-weight: normal;">9.69</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Dado un entero inicial $\large N$ , eleva su valor al cuadrado hasta que deje de ser menor que $\large 30000$. Por ejemplo, si comenzamos en $\large N = 2$ entonces pasamos a $\large 4$, luego a $\large 16$, luego a $\large 256$ y finalmente a $\large 65536$ . Escribe un programa que calcule el valor final $\large N$ y cuántas veces tuviste que elevarlo al cuadrado.

## Entrada
Un entero $\large N$. Puedes suponer que $\large 2 \leq N \leq 10^6$

## Salida
Dos enteros que sean respectivamente el valor final de $\large N$ y la cantidad de veces que se elevó al cuadrado.

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
            <td>2</td>
            <td>65536 4</td>
        </tr>
        <tr>
            <td>50000</td>
            <td>50000 0</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2019
Subido por: [rcc (rcc) (COA21)](https://omegaup.com/profile/rcc/ "rcc (rcc) (COA21)")
Problema subido en: 19/1/2019
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    USER_NUMBER = int(input())
    LIMIT = 30000
    repetitions = 0
    final_number = USER_NUMBER

    while final_number < LIMIT:
        final_number = final_number ** 2
        repetitions += 1

    print(f'{final_number} {repetitions}')


if __name__ == "__main__":
    main()
```