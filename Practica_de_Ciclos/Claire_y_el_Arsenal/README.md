# Claire y el Arsenal

|           Puntos          |<span style="font-weight: normal;">11.55</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Raccoon City se encuentra sumida en el caos. Tú eres Claire Redfield y necesitas ir en búsqueda de tu hermano, pero quieres ir preparada ante todo, así que decides llevar tu arma más poderosa. Como tienes muchas, no puedes llevarlas todas a la vez, por lo que necesitas ver cuál es mejor. Escribe un programa que te ayude con la tarea de elegir qué arma llevar contigo.

## Entrada
La primera línea contiene un entero $\large N$ que denota el número de armas que tienes a tu disposición. La segunda línea contiene $\large N$ nteros separados por un espacio que representan el poder de las $\large N$ armas. Las armas se encuentran implícitamente numeradas a partir de $\large 1$

## Salida
El poder del arma más poderosa seguida de su índice.

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
                <p>5</p>
                <p>10 8 15 12 20</p>
            </td>
            <td>20 5</td>
        </tr>
        <tr>
            <td>
                <p>7</p>
                <p>100 15 20 300 41 78 10</p>
            </td>
            <td>300 4</td>
        </tr>
    </tbody>
</table>

------------

Fuente: Resident Evil
Subido por: [TheKingCerberu (TheKingCerberu)(COA21)](https://omegaup.com/profile/TheKingCerberu/ "TheKingCerberu (TheKingCerberu)(COA21)")
Problema subido en: 4/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    TOTAL_WEAPONS = int(input())
    POWER_EACH_WEAPONS_USER = input().split()

    POWER_EACH_WEAPONS = list(map(int, POWER_EACH_WEAPONS_USER))
    ORDER_POWER = POWER_EACH_WEAPONS.copy()
    POWER_EACH_WEAPONS.sort(reverse=True)


    for i in range(TOTAL_WEAPONS):
        if POWER_EACH_WEAPONS[0] == ORDER_POWER[i]:
            print(f'{POWER_EACH_WEAPONS[0]} {i + 1}')
            break


if __name__ == '__main__':
    main()
```