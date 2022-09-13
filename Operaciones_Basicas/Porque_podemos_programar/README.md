# Porque podemos programar

|           Puntos          |<span style="font-weight: normal;">9.44</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Antes de que aprendieras a programar, tenías que usar la calculadora científica para realizar todos los cálculos que te dejaban de tarea. Sin embargo, ahora con la computadora sientes que cualquier cálculo se volvió fácil para ti. Tu profesor de matemáticas se enteró de esto y te ha desafiado a calcular lo siguiente:

$$
\begin{align}
    \LARGE
        y =
            \left(
                \dfrac{x + x^2}{5x + 3} + x
            \right)
            \left(
                \dfrac{
                    \dfrac{x + x^2}{5x + 3}
                }
                {
                    \dfrac{x + x^2}{5x + 3} + 2x
                }
            \right)
\end{align}
$$

## Entrada
Un real $\large x$ . Puedes suponer que $\large 1 \leq x \leq 100$.

## Salida
Un real que sea el valor de $\large y$. Tu programa se considerará correcto si el valor calculado es razonablemente cercano a la respuesta exacta.

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
            <td>8.5</td>
            <td>0.971243</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: rcc (rcc)
[rcc (rcc)](https://omegaup.com/profile/rcc/ "rcc (rcc)")
Problema subido en: 31/5/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    x = float(input())

    op1 = (x + x ** 2)
    op2 = (5 * x + 3)
    op3 = op1 / op2
    y = (op3 + x) * (op3 / (op3 + 2 * x))
    y = round(y, 6)

    print(y)

if __name__ == '__main__':
    main()
```