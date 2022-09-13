# Tipos de Triangulos

|           Puntos          |<span style="font-weight: normal;">8.96</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Escribe un programa que detecte el tipo de un triángulo dadas las longitudes $\large x, y, z$ de sus tres lados.
- **Equilátero**: triángulo con los tres lados iguales.
- **Isósceles**: triángulo con dos lados iguales.
- **Escaleno**: triángulo con los tres lados desiguales.

## Entrada
Los tres enteros $\large x, y, z$ separados por un espacio. Puedes suponer que $\large x, y, z > 0$ y que existe una forma válida de construir un triángulo con esas longitudes de lados.

## Salida
El tipo de triángulo que se tiene. La cadena a imprimir debe estar en minúscula y no debe incluir acentos.

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
            <td>4 5 5</td>
            <td>isosceles</td>
        </tr>
        <tr>
            <td>7 5 2</td>
            <td>escaleno</td>
        </tr>
        <tr>
            <td>3 3 3</td>
            <td>equilatero</td>
        </tr>
    </tbody>
</table>

------------

Fuente: Alberto Medina
Subido por: [Medina Morales José Alberto (AlbertoMedina) (COA21)](https://omegaup.com/profile/AlbertoMedina/ "Medina Morales José Alberto (AlbertoMedina) (COA21)")
Problema subido en: 12/6/2019
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    measurements = input().split()

    X = int(measurements[0])
    Y = int(measurements[1])
    Z = int(measurements[2])

    if X != Y and X != Z and Y != Z:
        result = 'escaleno'
    elif X == Y and X == Z and Y == Z:
        result = 'equilatero'
    else:
        result = 'isosceles'

    print(result)


if __name__ == '__main__':
    main()
```