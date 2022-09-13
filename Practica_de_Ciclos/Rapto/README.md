# Rapto

|           Puntos          |<span style="font-weight: normal;">13.22</span>|  Tamaño límite de entrada (bytes)  |<span style="font-weight: normal;">32 MiB</span>|
|      :------------:       |               :------------:                  |           :------------:           | :------------: |
|**Límite de tiempo (caso)**|                     1s                        |    **Límite de tiempo (total)**    |      1m0s      |
|     **Entrada/Salida**    |                  Consola                      |**Tamaño límite de entrada (bytes)**|     10 KiB     |


## Descripción
Aldo está determinado a practicar canciones en guitarra para tocar con su banda en los ensayos, sabe que cada canción cuenta con cierta cantidad de minutos, durante los ensayos con la banda Aldo quisiera saber el mínimo de canciones que lograrán ensayar en "n" minutos por ensayo. Previo a cada ensayo se hace una lista de posibles canciones a tocar y los minutos disponibles que se tendrán para practicar en la sala de ensayos, en la lista cada canción tendrá los minutos que dura, ayuda a Aldo realizando un programa que dependiendo el tiempo de las canciones y tiempo de ensayo determine si es posible o no tocarlas todas.

## Entrada
La primera entrada será un entero "T" que es el tiempo que se tendrá disponible en la sala de ensayos, el tiempo está en indicado en minutos, la segunda entrada será un entero "N" que es el número de canciones que se espera tocar, seguido de "n" valores que serán las canciones representadas en minutos.

## Salida
Deberás imprimir un texto (sin comillas) "Es posible" si el tiempo que duran las canciones no rebasa al tiempo que se tiene disponible en la sala de ensayos, o imprimir "Es exacto" en el caso en que el tiempo de la sala sea igual al tiempo de las canciones, o imprimir "No es posible" en caso de que el tiempo de las canciones rebase al tiempo disponible en la sala.

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
                <p>28</p>
                <p>7</p>
                <p>1 3 2 5 6 10 7</p>
            </td>
            <td>No es posible</td>
        </tr>
        <tr>
            <td>
                <p>34</p>
                <p>8</p>
                <p>2 3 2 5 4 3 4 4</p>
            </td>
            <td>Es posible</td>
        </tr>
        <tr>
            <td>
                <p>30</p>
                <p>6</p>
                <p>5 5 5 5 5 5</p>
            </td>
            <td>Es exacto</td>
        </tr>
    </tbody>
</table>

------------

Fuente: http://codigoprogramacion.com/cursos/tutoriales-c/ciclo-for-en-c-y-ejemplos.html
Subido por: [Aldo Pérez (mitno13) (COA21)](https://omegaup.com/profile/mitno13/ "Aldo Pérez (mitno13) (COA21)")
Problema subido en: 16/8/2018
Página: omegaup.com

------------

## Solución
### Python
```py
def main () -> None:
    TIME = int(input())
    AMOUNT_SONGS = int(input())
    TIME_EACH_SONG_USER = input().split()
    TIME_EACH_SONG = list(map(int, TIME_EACH_SONG_USER))
    TOTAL_TIME_SONGS = sum(TIME_EACH_SONG)
    message_final = 'Es exacto'

    if TIME > TOTAL_TIME_SONGS:
        message_final = 'Es posible'
    if TIME < TOTAL_TIME_SONGS:
        message_final = 'No es posible'

    print(message_final)


if __name__ == '__main__':
    main()
```