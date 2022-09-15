# Recortando palabras

|           Puntos          |<span style="font-weight: normal;">13.33</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |

## Descripción
José esta escribiendo una carta a mano y faltando 25% de la hoja se dio cuenta que todo lo que tiene por escribir no cabria en su única hoja. Ayuda a José a terminar su carta recortando una palabra $\large p$. Para lograrlo deberás usar las primeras $\large n$ letras y las ultimas $\large n$ letras de $\large p$.

## Entrada
Una palabra $\large p$ seguido de un número $\large p (0 < p < 25)$ La longitud de $\large p$ siempre será mayor al doble de $\large n$.

## Salida
Una palabra $\large p$ recortada.

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
            <td>archipielago 3</td>
            <td>arcago</td>
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
    WORD_AMOUNT_LETTERS = input().split()

    WORD = WORD_AMOUNT_LETTERS[0]
    AMOUNT_LETTERS = int(WORD_AMOUNT_LETTERS[1])
    WORD_BACKWARDS = WORD[::-1]
    WORD_BACKWARDS_LETTERS = WORD_BACKWARDS[:AMOUNT_LETTERS]

    print(f'{WORD[:AMOUNT_LETTERS]}{WORD_BACKWARDS_LETTERS[::-1]}')


if __name__ == "__main__":
    main()
```