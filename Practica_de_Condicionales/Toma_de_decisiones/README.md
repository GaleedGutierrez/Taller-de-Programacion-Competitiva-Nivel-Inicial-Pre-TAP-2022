# Toma de decisiones

|           Puntos          |<span style="font-weight: normal;">9.57</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Una diferencia notable entre una calculadora científica y una computadora, es que la última puede ejecutar código de forma condicional. Esto permite automatizar cálculos complicados donde el siguiente paso depende de la situación actual. Escribe un programa que tome dos enteros $\large A, B$ y que imprima el entero que resulte de la ejecución del siguiente diagrama de flujo:

```flow
st=>start: Inicio
AplusB=>condition: ¿A + B es igual a 5?
3plusB=>operation: Sumar 3 a B
1subtractA=>operation: Restar 1 a A
resultYes=>inputoutput: Imprime 2A + B
isEven=>condition: ¿7A + B es par?
printASubstractB=>inputoutput: Imprime A - B
printAMulB=>inputoutput: Imprime A * B
e=>end: Fin

st->AplusB->3plusB
AplusB(yes)->3plusB
AplusB(no)->1subtractA
3plusB->resultYes->e

1subtractA->isEven
isEven(yes)->printASubstractB->e
isEven(no)->printAMulB->e
```

## Entrada
Dos enteros $\large A, B$ separados por un espacio. Puedes suponer que  $\large 1 \leq A, B \leq 100$.

## Salida
Un entero que sea la respuesta obtenida tras ejecutar el diagrama de flujo.

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
            <td>2 3</td>
            <td>10</td>
        </tr>
        <tr>
            <td>1 6</td>
            <td>-6</td>
        </tr>
        <tr>
            <td>2 4</td>
            <td>4</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [rcc (rcc) (COA21)](https://omegaup.com/profile/rcc/ "rcc (rcc) (COA21)")
Problema subido en: 14/6/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    numbers = input().split()

    a = int(numbers[0])
    b = int(numbers[1])
    final = 0
    SUM_INITIAL = a + b

    if SUM_INITIAL == 5:
        b += 3
        final = 2 * a + b
    else:
        a -= 1
        SUM_SECOND = 7 * a + b
        if SUM_SECOND % 2 == 0:
            final = a - b
        else:
            final = a * b


    print(final)


if __name__ == '__main__':
    main()
```