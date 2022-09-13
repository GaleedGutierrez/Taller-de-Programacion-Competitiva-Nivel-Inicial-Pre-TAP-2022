# Elevando a alguna potencia

|           Puntos          |<span style="font-weight: normal;">10.57</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Dados dos valores $\large a$ y $\large b$, , calcular el valor de $\large a^b$

## Entrada
Dos enteros $\large a, b$ separados por un espacio tales que $\large 1 \leq a, b \leq 9$

## Salida
Un entero que sea el valor de $\large a^b$.

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
            <td>8</td>
        </tr>
        <tr>
            <td>3 5</td>
            <td>243</td>
        </tr>
        <tr>
            <td>8 9 </td>
            <td>134217728</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [Luis Pedroza (LuisPedroza) (COA21)](https://omegaup.com/profile/LuisPedroza/ "Luis Pedroza (LuisPedroza) (COA21)")
Problema subido en: 30/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    USER_NUMBER = input().split()
    A = int(USER_NUMBER[0])
    B = int(USER_NUMBER[1])
    RESULT = A ** B
    print(f'{RESULT}')


if __name__ == "__main__":
    main()
```