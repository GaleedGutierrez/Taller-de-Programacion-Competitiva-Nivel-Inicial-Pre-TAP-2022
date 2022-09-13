# Absoluto

|           Puntos          |<span style="font-weight: normal;">9.77</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Ahora te hemos dado la tarea mas difícil de sumar $\large N$ números.

## Entrada
La primera línea tendrá $\large N$ el número de enteros que tienes que sumar. Cada una de las siguientes $\large N$ líneas tendrá un número $\large A_{i}$

## Salida
Imprime la suma de los $\large N$ números.

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
            <td>
                <p>5</p>
                <p>1</p>
                <p>2</p>
                <p>3</p>
                <p>4</p>
                <p>5</p  >
            </td>
            <td>15</td>
            <td>1 + 2 + 3 + 4 + 5 = 15</td>
        </tr>
        <tr>
            <td>
                <p>3</p>
                <p>10</p>
                <p>20</p>
                <p>30</p>
            </td>
            <td>60</td>
            <td>10 + 20 + 30 = 60</td>
        </tr>
    </tbody>
</table>

## Límites
$$
\begin{align}
  \large 1 \leq N \leq 100
  \\
  \large 1 \leq A_{i} \leq 100
\end{align}
$$

------------

Fuente: Grupo de programación competitiva
Subido por: [Saul de Nova Caballero (lkt345) (COA21)](https://omegaup.com/profile/lkt345/ "Saul de Nova Caballero (lkt345) (COA21)")
Problema subido en: 4/3/2015
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    AMOUNT_NUMBERS = int(input())
    NUMBERS = [1]
    NUMBERS.pop(0)
    counter = 0
    sum = 0

    while counter < AMOUNT_NUMBERS:
        number_user = int(input())
        NUMBERS.append(number_user)
        counter += 1

    for i in range(len(NUMBERS)):
        sum += NUMBERS[i]

    print(sum)


if __name__ == '__main__':
    main()
```