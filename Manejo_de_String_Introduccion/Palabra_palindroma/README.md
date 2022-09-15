# Palabra palindroma

|           Puntos          |<span style="font-weight: normal;">10.94</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Los palíndromos son palabras o frases que al leerse de izquierda a derecha y viceversa expresan o tienen el mismo sentido. A este vocablo también se le puede llamar palíndromas. Deberá leer una palabra  e indicar si es o no una palabra palíndroma.

## Entrada
Una palabra $\large p$.

## Salida
Si la palabra es palíndroma deberá imprimir SI. Si la palabra **no** es palíndroma deberá imprimir NO.

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
                reconocer
            </td>
            <td>SI</td>
        </tr>
    </tbody>
</table>

------------

Fuente: Strings
Subido por: [Luis Arango (luisestebanas)](https://omegaup.com/profile/luisestebanas/ "Luis Arango (luisestebanas)")
Problema subido en: 1/6/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    WORD = input().replace(' ', '').lower()
    IS_PALINDROMO = WORD == WORD[::-1]
    RESULT = 'SI' if IS_PALINDROMO else 'NO'
    print(RESULT)

if __name__ == "__main__":
    main()
```