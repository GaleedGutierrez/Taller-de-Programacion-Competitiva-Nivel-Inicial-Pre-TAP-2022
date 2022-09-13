# Jorge y el concurso

|           Puntos          |<span style="font-weight: normal;">11.04</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
**Jorge**, es conocido en su escuela por ser capaz de resolver diversos acertijos matemáticos con facilidad y en poco tiempo. Esto se le ha subido un poco a la cabeza y lo ha hecho presumir ciertas habilidades matemáticas que en realidad no ha desarrollado.

**Jorge** participará en un concurso de matemáticas en dónde deberá responder la suma de todos los números naturales de 1 a $\large N$) en el menor tiempo posible. Esta tarea no es fácil por lo que **Jorge** ha acudido a ti para que lo ayudes a hacer trampa, su plan es que desarrolles un programa que se conecte a los lentes de Jorge y le otorgue las respuestas a las distintas preguntas de su concurso.

## Entrada
Un valor entero $\large N$).

## Salida
Un valor entero que sea la suma de 1 a $\large N$ (Inclusiva).

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
            <td>3</td>
            <td>6</td>
        </tr>
        <tr>
            <td>100</td>
            <td>5050</td>
        </tr>
    </tbody>
</table>

## Límites
$$
\begin{align}
  \large -1 \leq n \leq e^8
\end{align}
$$

------------

Fuente: Olimpiada de Informática Jalisco
Subido por: [Rob (rrios7) (COA21)](https://omegaup.com/profile/rrios7/ "Rob (rrios7) (COA21)")
Problema subido en: 28/11/2019

------------

## Solución
### Python
```py
def main () -> None:
    n = int(input())
    op = n * (n + 1) // 2
    print(op)

if __name__ == '__main__':
    main()
```