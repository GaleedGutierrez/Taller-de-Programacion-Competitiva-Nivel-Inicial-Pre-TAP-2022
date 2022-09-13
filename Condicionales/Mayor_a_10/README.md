# Mayor A 10
|           Puntos          |<span style="font-weight: normal;">11.05</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Después de tantos meses de pandemia mi tio vino de visita a la casa, para mi sorpresa llegó con las manos vendadas. Al parecer por estar todo este tiempo encerrado se puso a entrenar box en su casa y se fracturó ambas manos. Estas cosas suceden cuando te la pasas encerrado todos los días. Se me ocurrió decirle de broma que de seguro ya no sabía si un número era mayor o menor de 10 porque no podía contar con sus dedos, lo cual no le pareció gracioso y me contestó con un "por lo menos me acuerdo de más que los alumnos de tus clases". Así que le dije que se lo iba a comprobar poniéndoles un programa que lo hiciera.

## Entrada
Un número real (flotante).

## Salida
La frase "Es mayor" si el número ingresado es mayor a 10, o la frase "No es mayor" si no lo es.

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
            <td>15</td>
            <td>Es Mayor</td>
        </tr>
    </tbody>
</table>

------------

Fuente: Book
Subido por: [Alejandro Ramos (alxramos) (COA21)](https://omegaup.com/profile/alxramos/ "Alejandro Ramos (alxramos) (COA21)")
Problema subido en: 30/8/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    age = float(input())
    message = 'Es mayor' if age > 10 else 'No es mayor'
    print(message)


if __name__ == '__main__':
    main()
```