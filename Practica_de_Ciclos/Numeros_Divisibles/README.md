# Números Divisibles

|           Puntos          |<span style="font-weight: normal;">12.27</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      6s        |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Juan y Pedro siempre están compitiendo por ver quién es el mejor matemático. En esta ocasión Juan ha retado a Pedro para ver si él puede revisar una lista de números enteros y determinar cuántos de esos números son divisibles por otro número entero, al que llamaremos K.

El reto consiste en lo siguiente; Juan le dicta Pedro una lista de números enteros y además le indica el valor del número K. Pedro tiene que contestar cuántos de los números en la lista de Juan son divisibles por el número K.

Te pedimos ayudarle a Pedro a calcular rápidamente cuántos de los números en una lista son divisibles por K. Para esto deberás escribir un programa.

## Entrada
Tu programa recibirá la siguiente entrada; en la primera línea un número entero positivo N que nos indica la longitud de la secuencia de números, después la segunda línea nos indican el valor de K. Finalmente las siguientes N lineas nos proporciona los números enteros a evaluar.

## Salida
Tu programa deberá generar como salida un solo número entero indicando cuántos números en la lista son divisibles por K.

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
                <p>10</p>
                <p>3</p>
                <p>1</p>
                <p>2</p>
                <p>3</p>
                <p>4</p>
                <p>5</p>
                <p>6</p>
                <p>7</p>
                <p>8</p>
                <p>9</p>
                <p>10</p>
            </td>
            <td>3</td>
            <td>La salida es 3 porque 3, 6, y 9 son los únicos números en la secuencia que son divisibles por 3.</td>
        </tr>
        <tr>
            <td>
                <p>15</p>
                <p>7</p>
                <p>2</p>
                <p>4</p>
                <p>6</p>
                <p>8</p>
                <p>10</p>
                <p>12</p>
                <p>16</p>
                <p>20</p>
                <p>24</p>
                <p>25</p>
                <p>26</p>
                <p>30</p>
                <p>32</p>
                <p>5</p>
                <p>9</p>
            </td>
            <td>0</td>
            <td>La salida es 0 porque ninguno de los números en la secuencia es divisible por 7.</td>
        </tr>
    </tbody>
</table>

## Límites
$$
\begin{align}
  \large 1 \leq N \leq 1000000
  \\
  \large 1 < K < 100
\end{align}
$$

------------

Fuente: Inés Fernando Vega López
Subido por: [Jose Angel Cazares Torres [Coahuilita] (COA21)](https://omegaup.com/profile/OMISinaloaMX/ "Jose Angel Cazares Torres [Coahuilita] (COA21)")
Problema subido en: 12/11/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    PEDROS_AMOUNT_NUMBERS = int(input())
    DIVISOR = int(input())

    counter = 0
    numbers_divisibles = 0

    while counter < PEDROS_AMOUNT_NUMBERS:
        counter += 1
        NUMBER_TO_DIVIDED = int(input())
        IS_DIVISBLE = NUMBER_TO_DIVIDED % DIVISOR == 0
        if IS_DIVISBLE:
            numbers_divisibles += 1

    print(numbers_divisibles)


if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>

using namespace std;

int main()
{
    int PEDROS_AMOUNT_NUMBERS;
    int DIVISOR;
    
    int counter = 0;
    int numbers_divisibles = 0;
    
    cin>>PEDROS_AMOUNT_NUMBERS;
    cin>>DIVISOR;
    
    while (counter < PEDROS_AMOUNT_NUMBERS)
    {
        counter++;
        int NUMBER_TO_DIVIDED;
        cin>>NUMBER_TO_DIVIDED;
        bool IS_DIVISBLE = NUMBER_TO_DIVIDED % DIVISOR == 0;
        if (IS_DIVISBLE) 
        {
            numbers_divisibles++;
        }
    }

    cout<<numbers_divisibles;
    return 0;
}

```