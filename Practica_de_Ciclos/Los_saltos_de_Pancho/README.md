# Los saltos de Pancho

|           Puntos          |<span style="font-weight: normal;">11.36</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Hola de nuevo, Pancho necesita de tu ayuda otra vez. Él está en una laguna con plantas de nenúfares perfectamente alineadas en una línea. Pancho empieza en la primera planta y quiere realizar $\large n$ saltos, pero es muy olvidadizo (es un sapo, por dios) por lo que quiere que le digas cada vez que salta, en qué número de planta se encuentra (las plantas están numeradas a partir de 1).

## Entrada
Un unico entero $\large n$, la cantidad de saltos que Pancho desea hacer.

## Salida
Un total de $\large n$ líneas, cada una con un entero que identifique la planta en la que Pancho se encuentra.

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
            <td>5</td>
            <td>
                <p>1</p>
                <p>2</p>
                <p>3</p>
                <p>4</p>
                <p>5</p>
            </td>
        </tr>
        <tr>
            <td>10</td>
            <td>
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
        </tr>
    </tbody>
</table>

## Límites
$$
\begin{align}
  \large 1 \leq n \leq 1000
\end{align}
$$

------------

Fuente: Yop
Subido por: [『 Juan De Dios Moreno Rivera 』 (JDDMR) (COA21)](https://omegaup.com/profile/JDDMR/ "『 Juan De Dios Moreno Rivera 』 (JDDMR) (COA21)")
Problema subido en: 30/10/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    USER_NUMBER = int(input())

    for i in range(1, USER_NUMBER + 1):
        print(i)

if __name__ == '__main__':
    main()
```