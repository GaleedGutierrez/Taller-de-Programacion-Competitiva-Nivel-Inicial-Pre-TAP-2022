# La moda y sus signos

|           Puntos          |<span style="font-weight: normal;">15.56</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |

## Descripción
Dada una secuencia de $\large N$ dígitos del $\large 1$ al $\large 9$ donde cada dígito puede aparecer con signo $\large +$ o $\large -$

## Entrada
Un entero $\large N$ seguido de $\large N$ dígitos del $\large 1$ al $\large 9$ en versiones positivas o negativas. Puedes suponer que $\large 1 \leq N \leq 1000$.

## Salida
Un entero que sea el dígito que apareció más veces, seguido de dos enteros que sean la cantidad de veces que apareció dicho dígito en su forma positiva y negativa. En caso de empate en apariciones, debe dársele preferencia al dígito numéricamente menor (en magnitud).

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
                <p>12</p>
                <p>+1 +4 +4 +9 +7 +7 -9 +7 +4 +7 -4 -4</p>
            </td>
            <td>
                <p>4</p>
                <p>3 2</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>4</p>
                <p>+1 +2 +1 +2</p>
            </td>
            <td>
                <p>1</p>
                <p>2 0</p>
            </td>
        </tr>
    </tbody>
</table>

------------

Fuente: UAM Azcapotzalco 2018
Subido por: [rcc (rcc)](https://omegaup.com/profile/rcc/ "rcc (rcc)")
Problema subido en: 3/7/2018
Página: omegaup.com

------------

## Solución
### Python
```py

```