# El perrito que quiere un hueso

|           Puntos          |<span style="font-weight: normal;">9.35</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Estás paseando a tu perrito y acaban de pasar enfrente de una tienda de comida para perros. En la vitrina hay dos huesos de olor y tamaño distintos. Tu perro mentalmente le asignó una calificación del $\large 1$ al $\large 10$ al olor de cada hueso y una calificación del $\large 1$ al $\large 10$ al tamaño de cada hueso. Por supuesto, tu perro preferiría que le compraras el hueso que es simultáneamente el más grande y el que huele mejor. ¿Puedes ayudarlo a determinar qué hueso comprar?

## Entrada
Cuatro enteros $\large L_{1}, T_{1}, L_{2}, T_{2}$  que son el olor y el tamaño de los dos huesos, respectivamente. Cada hueso se da en su respectiva línea. Puedes suponer que $\large 1 \leq L_{1}, T_{1}, L_{2}, T_{2} \leq 10$ y que los dos huesos difieren en olor y también difieren en tamaño.

## Salida
El mensaje Hueso 1 o Hueso 2 dependiendo de qué hueso es el que es simultáneamente el más grande y el que huele mejor. En caso de que ninguno de los dos huesos cumpla esta propiedad, imprimir el mensaje Perrito confundido :(.

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
                <p>8 9</p>
                <p>5 8</p>
            </td>
            <td>Hueso 1</td>
        </tr>
        <tr>
            <td>
                <p>3 6</p>
                <p>7 10</p>
            </td>
            <td>Hueso 2</td>
        </tr>
        <tr>
            <td>
                <p>6 9</p>
                <p>8 4</p>
            </td>
            <td>Perrito confundido :(</td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2020
Subido por: [rcc (rcc)](https://omegaup.com/profile/rcc/ "rcc (rcc)")
Problema subido en: 12/7/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    bone1 = input().split()
    bone2 = input().split()

    L1 = int(bone1[0])
    T1 = int(bone1[1])
    L2 = int(bone2[0])
    T2 = int(bone2[1])

    if L1 >= L2 and T1 >= T2:
        message = 'Hueso 1'
    elif L2 >= L1 and T2 >= T1:
        message = 'Hueso 2'
    else:
        message = 'Perrito confundido :('

    print(message);


if __name__ == '__main__':
    main()
```