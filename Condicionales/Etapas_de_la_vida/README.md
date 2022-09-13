# Etapas de la vida

|           Puntos          |<span style="font-weight: normal;">9.07</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Dieguito vio en su clase de biología las etapas de la vida, pero aún no las distingue muy bien. Tu tarea es ayudar a Dieguito haciendo un programa el cual, dado un número de entrada $\large L$ , el cual representa una edad, te diga si dicha edad corresponde a un **bebé**, **niño**, **joven**, **adulto** o **adulto de la tercera edad**. Para lograr lo anterior, considera la siguiente clasificación:

- Bebé: De 0 a 3 años, inclusive.
- Niño: De 4 a 14 años, inclusive.
- Joven: De 15 a 18 años, inclusive.
- Adulto: de 19 a 65 años, inclusive.
- Adulto de la tercera edad: de 65 años en adelante.

## Entrada
Un entero $\large L$ , el cual representa la edad de una persona. Puedes suponer que $\large 0 \leq L \leq 99$.

## Salida
Según corresponda:

- Si es un bebé, imprimir "BEBE".
- Si es un niño, imprimir "NINO".
- Si es un joven, imprimir "JOVEN".
- Si es un adulto, imprimir "ADULTO".
- Si es un adulto de la tercera edad, imprimir "ADULTO 3RA".

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
            <td>17</td>
            <td>JOVEN</td>
        </tr>
        <tr>
            <td>23</td>
            <td>ADULTO</td>
        </tr>
        <tr>
            <td>68</td>
            <td>ADULTO 3RA</td>
        </tr>
        <tr>
            <td>2</td>
            <td>BEBE</td>
        </tr>
    </tbody>
</table>

------------

Fuente: BeeHigh 2020
Subido por: [Miguel Ángel Mireles Vázquez (BeeHigh1) (COA21)](https://omegaup.com/profile/BeeHigh1/ "Miguel Ángel Mireles Vázquez (BeeHigh1) (COA21)")
Problema subido en: 16/6/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    L = int(input())

    if L >= 0 and L <= 3:
        message = 'BEBE'
    elif L >= 4 and L <= 14:
        message = 'NINO'
    elif L >= 15 and L <= 18:
        message = 'JOVEN'
    elif L >= 19 and L <= 65:
        message = 'ADULTO'
    else:
        message = 'ADULTO 3RA'

    print(message)



if __name__ == '__main__':
    main()
```