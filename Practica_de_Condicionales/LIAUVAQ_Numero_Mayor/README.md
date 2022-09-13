# LIAUVAQ Numero Mayor

|           Puntos          |<span style="font-weight: normal;">12.78</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
En la ciudad los habitantes estan espantados por no saber diferenciar de tres numeros un numero mayor, debido a un problema generalizado de dislexia ya que durante generaciones se ha ido esparcierdo hasta llegar a todos, ayuda a los habitantes a saber cual es el numero mayor.

## Entrada
La entrada costa de tres numeros enteros

## Salida
El numero mayor de los tres numeros.

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
            <td>1 45 3</td>
            <td>45</td>
            <td>El numero mayor de los tres es 45.</td>
        </tr>
    </tbody>
</table>

------------

Fuente: Personal.
Subido por: [Ever (Exer) (COA21)](https://omegaup.com/profile/Exer/ "Ever (Exer) (COA21)")
Problema subido en: 25/3/2017
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    numbers = input().split()

    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])

    if a > b and a > c:
        message = f'{a}'
    elif b > a and b > c:
        message = f'{b}'
    else:
        message = f'{c}'

    print(message)


if __name__ == '__main__':
    main()
```