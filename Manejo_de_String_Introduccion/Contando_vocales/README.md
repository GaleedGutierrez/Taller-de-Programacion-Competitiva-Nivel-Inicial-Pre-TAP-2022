# Contando vocales
|           Puntos          |<span style="font-weight: normal;">11.53</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Codificar un programa que lea una cadena de caracteres e informa la cantidad de ocurrencias de cada vocal en la cadena.

## Entrada
Se ingresa una unica linea que contiene una cadena de hasta 500 caracteres. Los caracteres pueden ser digitos y letras, mayusculas y minusculas.

## Salida
Mostrar en una unica linea 5 numeros enteros separados por un espacio. El primero es la cantidad de veces que aparece la vocal 'a' (en mayusculas o minusculas). El segundo representa la cantidad de veces de la vocal 'e'. Y los tres restantes, la 'i', 'o' y 'u',

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
            <td>Santa Fe</td>
            <td>2 1 0 0 0</td>
        </tr>
    </tbody>
</table>

------------

Fuente: Yael_Montoya
Subido por: [Yael Michell Lopez Montoya (Yael_Montoya_CDMX)](https://omegaup.com/profile/Yael_Montoya_CDMX/ "Yael Michell Lopez Montoya (Yael_Montoya_CDMX)")
Problema subido en: 26/11/2019
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    WORD = input().replace(' ', '').lower()
    VOWELS = [0, 0, 0, 0, 0]

    for i in WORD:
        if i == 'a':
            VOWELS[0] += 1
        elif i == 'e':
            VOWELS[1] += 1
        elif i == 'i':
            VOWELS[2] += 1
        elif i == 'o':
            VOWELS[3] += 1
        elif i == 'u':
            VOWELS[4] += 1

    RESULT = ' '.join(list(map(str,VOWELS)))
    print(RESULT)


if __name__ == "__main__":
    main()
```