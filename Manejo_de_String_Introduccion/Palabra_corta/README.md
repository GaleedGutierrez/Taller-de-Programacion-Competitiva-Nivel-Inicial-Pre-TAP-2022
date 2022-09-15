# Palabra corta

|           Puntos          |<span style="font-weight: normal;">12.72</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Realiza un programa que solicite al usuario nn palabras. El programa deberá solicitar las nn palabras y deberá imprimir cuál de ellas tiene menos caracteres, de cuántos caracteres consta dicha palabra y si el número de caracteres de dicha la palabra es impar o par.

## Entrada
Un número entero n seguido de n palabras.

## Salida
La palabra con menos caracteres, cantidad de caracteres de esa palabra y si el número de caracteres de dicha la palabra es impar o par.

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
                <p>3</p>
                <p>Perro</p>
                <p>Gato</p>
                <p>Mandarina</p>
            </td>
            <td>
                <p>Gato</p>
                <p>4</p>
                <p>par</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>4</p>
                <p>barco</p>
                <p>carrito</p>
                <p>camión</p>
                <p>trailer</p>
            </td>
            <td>
                <p>barco</p>
                <p>5</p>
                <p>impar</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>2</p>
                <p>dos</p>
                <p>tres</p>
            </td>
            <td>
                <p>dos</p>
                <p>2</p>
                <p>impar</p>
            </td>
        </tr>
    </tbody>
</table>
Palabra de 0 a 500 caracteres.

------------

Fuente: Arial 12 xd
Subido por: [Yael Michell Lopez Montoya (Yael_Montoya_CDMX)](https://omegaup.com/profile/Yael_Montoya_CDMX/ "Yael Michell Lopez Montoya (Yael_Montoya_CDMX)")
Problema subido en: 6/12/2019
Página: omegaup.com

------------

## Solución
### Python
```py
def is_even (number: int) -> str:
    IS_EVEN = number % 2 == 0
    return 'par' if IS_EVEN else 'impar'

def main () -> None:
    AMOUNT_WORD = int(input())
    WORDS = ['']
    WORDS.pop(0)
    counter = 0

    while counter < AMOUNT_WORD:
        counter += 1
        NEW_WORD = input()
        WORDS.append(NEW_WORD)

    shortest_word_length = len(WORDS[0])
    shortest_word = WORDS[0]

    for i in range(1, len(WORDS)):
        if  len(WORDS[i]) < shortest_word_length:
            shortest_word_length = len(WORDS[i])
            shortest_word = WORDS[i]

    PARITY = is_even(shortest_word_length)
    print(shortest_word)
    print(shortest_word_length)
    print(PARITY)


if __name__ == "__main__":
    main()
```