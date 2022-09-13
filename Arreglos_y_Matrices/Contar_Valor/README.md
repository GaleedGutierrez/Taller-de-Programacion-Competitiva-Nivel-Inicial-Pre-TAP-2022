# Contar Valor

|           Puntos          |<span style="font-weight: normal;">10.65</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Hacer un programa que diga cuantas veces aparece en un arreglo un valor introducido desde teclado.

## Entrada
Un entero $\large N$ que indica la cantidad de elementos del arreglo.

Las siguientes $\large N$ lineas un entero que indica un elemento del arreglo. Un entero $\large K$ que indica el valor que se quiere contar.

## Salida
La cantidad de veces que aparece el valor.

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
            <td>
                <p>5</p>
                <p>1</p>
                <p>2</p>
                <p>1</p>
                <p>3</p>
                <p>1</p>
                <p>1</p>
            </td>
            <td>3</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UASLP
Subido por: [Victor Yoguel Salazar Alanis (VictorYoguel) (COA21)](https://omegaup.com/profile/VictorYoguel/ "Victor Yoguel Salazar Alanis (VictorYoguel) (COA21)")
Problema subido en: 21/11/2017
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    AMOUNT_NUMBERS = int(input())
    NUMBER_SEARCH = int(input())

    counter = 0
    repetitions = 0

    while counter < AMOUNT_NUMBERS:
        counter += 1
        NEW_NUMBER = int(input())
        if NEW_NUMBER == NUMBER_SEARCH:
            repetitions += 1
    print(repetitions)

if __name__ == '__main__':
    main()
```