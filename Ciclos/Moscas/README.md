# Moscas

|           Puntos          |<span style="font-weight: normal;">11.59</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Hola de nuevo :3, como ya saben Pancho es un sapo y gusta de comer moscas. Hoy, Pancho ha encontrado una perfecta línea con $\large n$ moscas numeradas de $\large 1$ a $\large n$, pero ahora Pancho no sabe cómo empezar a comérselas: si de la primera a la última, o de la última a la primera. Pancho necesita de tu ayuda para que le muestres las dos maneras de comer las moscas y así ayudarlo a decidir.

## Entrada
Una único entero $\large n$ que denota la cantidad de moscas de la fila.

## Salida
La salida debe consistir de dos líneas. La primera debe contener una secuencia de enteros separados por espacios que corresponda con el orden de comerse a las moscas de la primera a la última. La segunda debe contener una secuencia de enteros separados por espacios que corresponda con el orden de comerse a las moscas de la última a la primera.

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
            <td>
                <p>1 2 3 4 5</p>
                <p>5 4 3 2 1</p>
            </td>
        </tr>
        <tr>
            <td>8</td>
            <td>
                <p>1 2 3 4 5 6 7 8</p>
                <p>8 7 6 5 4 3 2 1</p>
            </td>
        </tr>
    </tbody>
</table>

## Límites
$$
\begin{align}
  \large 1 \leq n \leq 1000
\end{align}
$$
- Si, a Pancho le pasan muchos problemas.
------------

Fuente: Yop
Subido por: [『 Juan De Dios Moreno Rivera 』 (JDDMR) (COA21)](https://omegaup.com/profile/JDDMR/ "『 Juan De Dios Moreno Rivera 』 (JDDMR) (COA21)")
Problema subido en: 30/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    USER_NUMBER = int(input())
    numbers = [1]

    for i in range(2, USER_NUMBER + 1):
        numbers.append(i)
    numbers = map(str, numbers)
    numbers_str = list(numbers)
    FIRST = ' '.join(numbers_str )
    SECOND = ' '.join(numbers_str [::-1])
    print(FIRST)
    print(SECOND)


if __name__ == '__main__':
    main()
```