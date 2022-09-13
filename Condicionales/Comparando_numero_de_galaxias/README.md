# Comparando número de galaxias

|           Puntos          |<span style="font-weight: normal;">9.74</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                 |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                       |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                     |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
En un telescopio enorme 🔭 se disponen a observar 3 regiones pequeñísimas del espacio a la vez para contar cuantas galaxias se pueden observar en cada región 👽. Nos interesa investigar la relación que existe entre el número de galaxias entre cada una de estas regiones diferentes, para observar si podemos encontrar algún patrón; el problema es que hacerlo a mano es imposible 😨 por lo que han pedido tu ayuda para comparar el número de galaxias.

## Entrada
Tres números enteros $\large a, b$ y  $\large c$ separados por un espacio, cada uno correspondiente al número de galaxias que se encontraron en cada región.

## Salida
Imprime, en una sola línea, separados por un espacio, True si la comparación es verdadera o False si la comparación es falsa, de las siguientes comparaciones en orden:

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
            <td>733 796 881</td>
            <td>True True False True False</td>
            <td>Puedes observar que las comparaciones son correctas 👀, ya que a = 733, b = 796 y c = 881, entonces:
                <ol> 
                    <li>733 menor que 796 = True</li>
                    <li>881 mayor que 733 = True</li>
                    <li>733 igual a 796 = False</li>
                    <li>733 diferente de 881 = True</li>
                    <li>881 menor o igual que 796 = False</li>
                </ol>
            </td>
        </tr>
    </tbody>
</table>

## Límites
$$
\begin{align}
  \large 0 \leq a,b,c \leq 1000
\end{align}
$$

------------

Fuente: Future Lab
Subido por: [ Gabriel Missael Barco (MissaelBarco) (COA21)](https://omegaup.com/profile/MissaelBarco/ " Gabriel Missael Barco (MissaelBarco) (COA21)")
Problema subido en: 9/7/2020
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    galaxies = input().split()

    a = int(galaxies[0])
    b = int(galaxies[1])
    c = int(galaxies[2])

    result = ['']
    result.pop(0)
    result.append(str(bool(a < b)))
    result.append(str(bool(c > a)))
    result.append(str(bool(a == b)))
    result.append(str(bool(a != c)))
    result.append(str(bool(c <= b)))

    final = ' '.join(result)
    print(final)


if __name__ == '__main__':
    main()
```