# Buscando el Ki

|           Puntos          |<span style="font-weight: normal;">13.2</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |

## Descripción
Miguel ha visto mucho anime últimamente y ha empezado a hacer comparaciones entre las habilidades de los personajes y el mundo real. Al hacer su tarea se dio cuenta de una propiedad en los números que tiene que manejar: un número $\large X$ tiene un ki igual a la cantidad de dígitos que éste posee.

Miguel también notó que cuando un par de números $\large A$ y $\large B$ hacen la fusión se concatenan. Por ejemplo el número 12 tiene un ki de 2 y el número 2 tiene un ki de 1, al hacer la fusión el número resultante es 122 con un ki de 3.

Miguel te dará dos números $\large A$ y $\large B$ y tu tarea es ayudarlo a determinar el ki del número resultante de la fusión de éstos.

**Pista: Los números que está manejando son GIGANTES, entonces puedes leerlos como texto.**

## Entrada
La primera línea contiene el número $\large A$. La segunda línea contiene el número $\large B$

## Salida
Debes decir a Miguel el ki del número resultante al fusionar $\large A$ y $\large B$.

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
                <p>1</p>
                <p>1</p>
            </td>
            <td>2</td>
        </tr>
        <tr>
            <td>
                <p>735</p>
                <p>83</p>
            </td>
            <td>5</td>
        </tr>
    </tbody>
</table>

## Restricciones
$
    \large 1 \leq A, B \leq 10^{100000}
$

------------

Fuente: Coding Rush
Subido por: [CodingRush (CodingRush)](https://omegaup.com/profile/CodingRush/ "CodingRush (CodingRush)")
Problema subido en: 16/10/2015
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    A = input()
    B = input()
    KI = len(A) + len(B)
    print(KI)


if __name__ == "__main__":
    main()
```