# Huyendo de las serpientes

|           Puntos          |<span style="font-weight: normal;">11.77</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
En su viaje por Australia, Pepe ha visitado la extraña selva de las letras: en esta selva viven 26 animales, cada uno representado por una letra minúscula. De esta forma, podemos representar un elefante con la letra "e", un jaguar con la letra "j", o una guacamaya con la letra "g".

Pepe le tiene un terrible miedo a las serpientes, y como sabemos, en una selva hay serpientes. Las serpientes se representan con la letra "s". Para evitar encontrarse una de éstas, Pepe compró un detector de animales: éste detecta el animal y le dice qué hacer. Sin embargo, el programa que emite las indicaciones se descompuso y ahora debe componerlo. Como eres un programador de confianza para Pepe, él te ha pedido que escribas el nuevo programa. El indicador funciona de la siguiente manera:

Primero se recibe la letra que representa el animal más cercano, seguido de la distancia a la que se encuentra. Si el animal no es una serpiente, imprime `estas a salvo!" (sin las comillas). Si el animal es una serpiente, verifica la distancia a la que se encuentra de Pepe: si está a 10 metros o más, imprime "retrocede y busca otro camino" (sin las comillas). Pero si la serpiente está a menos de 10 metros de distancia imprime: "corre, corre por tu vida!" (sin las comillas).

## Entrada
Recibirás un caracter indicando el animal que representa, seguido de un entero que representa la distancia a la que se encuentra el animal.

## Salida
La acción más adecuada para Pepe, según lo descrito.

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
            <td>c 10</td>
            <td>estas a salvo!</td>
        </tr>
        <tr>
            <td>s 20</td>
            <td>retrocede y busca otro camino</td>
        </tr>
        <tr>
            <td>s 5</td>
            <td>corre, corre por tu vida!</td>
        </tr>
    </tbody>
</table>

## Observaciones
- El animal nunca estará a más de $\large 10^4$ metros de distancia.
- Tu indicador sólo se basa en buscar la acción más conveniente en caso de haber o no haber una serpiente. Puede que existan otros animales peligrosos en la vida real, pero Pepe no les tiene miedo.

------------

Fuente: :)
Subido por: [Karen Sosa Jácome (karen1536)(COA21)](https://omegaup.com/profile/karen1536/ "Karen Sosa Jácome (karen1536)(COA21)")
Problema subido en: 30/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    user = input().split()

    animal = user[0]
    distance = int(user[1])

    if animal == 's' and distance >= 10:
        message = 'retrocede y busca otro camino'
    elif animal == 's' and distance <= 10:
        message = 'corre, corre por tu vida!'
    else:
        message = 'estas a salvo!'


    print(message)


if __name__ == '__main__':
    main()
```