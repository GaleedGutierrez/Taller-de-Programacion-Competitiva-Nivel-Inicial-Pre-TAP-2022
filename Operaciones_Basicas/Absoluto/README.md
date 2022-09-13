# Absoluto

|           Puntos          |<span style="font-weight: normal;">9.73</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Eres un tutor de matematicas (uno muy malo por cierto) y estas ayudando a Juanito a estudiar para su examen de matematicas para que asi el te ayude con programacion. Como eres un tutor muy malo y no sabes lo que es el valor absoluto, lo buscas en Wikipedia. Te dice la siguiente respuesta: **En matemáticas, el valor absoluto o módulo de un número real es su valor numérico sin tener en cuenta...** bla bla bla. Le preguntas a un amigo lo que es y te dice que es la distancia entre un numero y 0. Tu, comprometido a ayudarle a Juanito, haces un programa que te de el valor absoluto de un numero y asi, presumirle a Juanito tus abilidades matematicas y de programacion.

## Problema
Haz un programa que te de un numero $\large n$ y te saque el $\large |n|$ (valor absoluto de $\large n$).

## Entrada
El numero $\large n$, anteriormente descrito.

## Salida
El valor absoluto de $\large n$.

## Ejemplo
<table style="text-align: center;" >
    <thead>
        <tr>
            <th>Entrada</th>
            <th>Salida</th>
            <th>Descripción</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>-5</td>
            <td>5</td>
            <td>El |5| es 5</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
            <td></td>
        </tr>
    </tbody>
</table>

## Límites
$$
\begin{align}
  \large -10000 \leq n \leq 10000
\end{align}
$$

------------

Fuente: Unknown
Subido por: [Jose Angel Cazares Torres [Coahuilita] (COA21)](https://omegaup.com/profile/COA21/ "Jose Angel Cazares Torres [Coahuilita] (COA21)")
Problema subido en: 8/4/2016
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    a = int(input())

    if a < 0:
        a = a * (-1)

    print(a)


if __name__ == '__main__':
    main()
```