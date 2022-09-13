# Resta y multiplicación

|           Puntos          |<span style="font-weight: normal;">8.42</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Haz un sencillo programa que lea 4 variables nombradas $\large A, B, C$ y $\large D$. Y calcula e imprima la multiplicación de la diferencia de $\large A$ y $\large B$ con la diferencia de $\large C$ y $\large D$. $\large (A-B)*(C-D)$

## Entrada
Cuatro números enteros.

## Salida
El producto de la diferencia con 4 variables de acuerdo al ejemplo.

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
            <td>10 6 8 3</td>
            <td>20</td>
        </tr>
    </tbody>
</table>

------------

Fuente:
Subido por: [Jorge Fernández Quezada (jofeque)](https://omegaup.com/profile/jofeque/ "Jorge Fernández Quezada (jofeque)")
Problema subido en: 30/10/2013
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    entrada = input().split()

    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])
    d = int(entrada[3])

    op = (a - b) * (c - d)

    print(op)


if __name__ == '__main__':
    main()
```