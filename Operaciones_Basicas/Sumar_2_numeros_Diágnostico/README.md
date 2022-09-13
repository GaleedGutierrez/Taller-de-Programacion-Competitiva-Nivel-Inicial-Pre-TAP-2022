# Sumar 2 numeros Diágnostico

|           Puntos          |<span style="font-weight: normal;">11.72</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |
## Descripción
Elaborar un programa que lea dos número enteros, y devuelva la suma de las entradas.

## Entrada
\[
x_{1} \\
x_{2}
\]

## Salida
\[
y = x_{1} + x_{2}
\]

## Ejemplo
<table style="text-align: center;" >
    <thead>
        <tr>
            <th>Entrada</th>
            <th>Salida</th>
            <th>Descripción</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1<br />2</td>
            <td>3</td>
            <td>1 + 2 = 3</td>
        </tr>
        <tr>
            <td>10<br />20</td>
            <td>30</td>
            <td>10 + 20 = 30</td>
        </tr>
    </tbody>
</table>
# Limites
\[
x_{1}+x_{2} \in \mathbb{Z}
\]

------------

Fuente: Diagnostico
Subido por: [AyED (AyED)](https://omegaup.com/profile/AyED/ "AyED (AyED)")
Problema subido en: 8/4/2022
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    a = int(input())
    b = int(input())
    c = a + b
    print(c)


if __name__ == '__main__':
    main()
```