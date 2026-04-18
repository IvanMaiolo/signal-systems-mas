# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.1",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 2: Ejercicios Practicos
    ## Hablar en Python

    Resuelve cada ejercicio en la celda indicada.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Clasificar frecuencias

    Escribi un condicional que clasifique una frecuencia en las siguientes categorias:

    | Rango (Hz) | Categoria |
    |-----------|-----------|
    | 20 - 60 | Sub-bass |
    | 60 - 250 | Bass |
    | 250 - 4000 | Mid |
    | 4000 - 12000 | Treble |
    | 12000 - 20000 | Ultra-treble |

    Proba con `freq = 880` y con `freq = 35`. Imprimi el resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    _freq = 1000 #Hz
    if _freq >20 and _freq <60:
        print (f"{_freq} Hz - categoria: Sub-Bass")
    elif _freq >60 and _freq <250:
        print (f"{_freq} Hz - categoria: Bass")
    elif _freq >250 and _freq <4000:
        print (f"{_freq} Hz - categoria: Mid")
    elif _freq >4000 and _freq <12000:
        print (f"{_freq} Hz - categoria: Treble")
    elif _freq >12000 and _freq <20000:
        print (f"{_freq} Hz - categoria: ultra Treble")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Primeros 10 armonicos

    Dado un `fundamental = 220` Hz (A3), crea un bucle `for` que genere e imprima los primeros **10 armonicos**.

    Recordatorio: el armonico N tiene frecuencia = fundamental * N.

    Formato de salida: `"Armonico 1: 220 Hz"`
    """)
    return


@app.cell
def _():
    # EJERCICIO 2: Tu codigo aca
    fundamental = 220 #Hz
    armonicos = [1,2,3,4,5,6,7,8,9,10]
    for i in armonicos:
        freq_ = fundamental * i
        print(f"armonico {i}: {freq_} Hz") 
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Amplitudes a dB (list comprehension)

    Dada la lista `amplitudes = [1.0, 0.707, 0.5, 0.25, 0.1, 0.01]`, crea una list comprehension que convierta cada valor a dB usando la formula:

    $$dB = 20 \times \log_{10}(amplitud)$$

    Necesitas importar `math` y usar `math.log10()`.

    Imprimi cada par (lineal, dB) con formato.
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca
    import math
    amplitudes = [1, 0.707, 0.5, 0.25, 0.1, 0.01]
    dB = [20*math.log10(a) for a in amplitudes] #dB
    # Usamos un for para recorrer ambas listas al mismo tiempo
    for amp, decibel in zip(amplitudes, dB):
        print(f"({amp:<6},{decibel:.2f} dB)")
    return (math,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Diccionario de bandas de octava

    Crea un diccionario que mapee las frecuencias centrales de las bandas de octava estandar a su **ancho de banda**. El ancho de banda de una banda de octava es: `bw = fc * (sqrt(2) - 1/sqrt(2))` donde `fc` es la frecuencia central.

    Frecuencias centrales: `[125, 250, 500, 1000, 2000, 4000, 8000]`

    Imprimi el diccionario con formato: `"125 Hz: BW = XX.X Hz"`
    """)
    return


@app.cell
def _(math):
    # EJERCICIO 4: Tu codigo aca

    Frecuencias_centrales = [125, 250, 500, 1000, 2000, 4000, 8000, 16000] #Hz
    diccionario_bw = {fc: fc * (math.sqrt(2) - 1/math.sqrt(2)) for fc in Frecuencias_centrales}
    for fc, bw in diccionario_bw.items():
        print(f"{fc} Hz: BW = {bw:.1f} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Filtrar archivos de audio por metadata

    Dada la siguiente lista de diccionarios:

    ```python
    archivos = [
        {"nombre": "voz.wav", "sr": 44100, "bits": 16, "duracion": 30.0},
        {"nombre": "guitarra.wav", "sr": 22050, "bits": 16, "duracion": 120.0},
        {"nombre": "master.wav", "sr": 96000, "bits": 32, "duracion": 240.0},
        {"nombre": "borrador.wav", "sr": 8000, "bits": 8, "duracion": 5.0},
        {"nombre": "drums.wav", "sr": 48000, "bits": 24, "duracion": 60.0},
    ]
    ```

    Usando list comprehension, filtra los archivos que tengan `sr >= 44100`.
    Imprimi los nombres de los archivos que pasan el filtro.
    """)
    return


@app.cell
def _():
    # EJERCICIO 5: Tu codigo aca
    lista_original= [
        {"nombre": "voz.wav", "sr": 44100, "bits": 16, "duracion": 30.0},
        {"nombre": "guitarra.wav", "sr": 22050, "bits": 16, "duracion": 120.0},
        {"nombre": "master.wav", "sr": 96000, "bits": 32, "duracion": 240.0},
        {"nombre": "borrador.wav", "sr": 8000, "bits": 8, "duracion": 5.0},
        {"nombre": "drums.wav", "sr": 48000, "bits": 24, "duracion": 60.0},
    ]
    list_comprension = [archivo["nombre"] for archivo in lista_original if archivo["sr"] >= 44100]
    print (list_comprension)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Tabla frecuencia x armonico

    Usando bucles anidados, crea una tabla donde:
    - Las filas son frecuencias fundamentales: `[100, 200, 440]`
    - Las columnas son numeros de armonico: `[1, 2, 3, 4, 5]`
    - Cada celda muestra `fundamental * armonico`

    Formato de salida (con alineacion):
    ```
         |     x1     x2     x3     x4     x5
    -----|------------------------------------
     100 |    100    200    300    400    500
     200 |    200    400    600    800   1000
     440 |    440    880   1320   1760   2200
    ```
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Tu codigo aca
    frecuencias_fundamentales = [100, 200, 440] #Hz
    numeros_de_armonicos = [1, 2, 3, 4, 5]
    header= "      |"
    for n in numeros_de_armonicos:
        header += f"  x{n}"
    print (header)
    print ("------|" + "-" * (6 * len(numeros_de_armonicos)))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Track listing con enumerate

    Dada la lista:
    ```python
    album = ["Speak to Me", "Breathe", "On the Run", "Time",
             "The Great Gig in the Sky", "Money", "Us and Them",
             "Any Colour You Like", "Brain Damage", "Eclipse"]
    ```

    Usa `enumerate` para imprimir un listado numerado empezando en 1:
    ```
    01. Speak to Me
    02. Breathe
    ...
    ```
    """)
    return


@app.cell
def _():
    # EJERCICIO 7: Tu codigo aca
    album = ["Speak to Me", "Breathe", "On the Run", "Time",
             "The Great Gig in the Sky", "Money", "Us and Them",
             "Any Colour You Like", "Brain Damage", "Eclipse"]

    enumerate = list(enumerate(album, start=1))
    for index, track in enumerate:
        print(f"{index:>2}. {track}") 
    return (enumerate,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Stereo pairs con zip

    Dadas las muestras del canal izquierdo y derecho:
    ```python
    left =  [0.5, -0.3, 0.8, -0.6, 0.2, -0.9, 0.4]
    right = [0.3, -0.1, 0.6, -0.4, 0.1, -0.7, 0.3]
    ```

    Usa `zip` para:
    1. Crear una lista de tuplas `stereo_pairs` con los pares (L, R)
    2. Calcular la senal mono (promedio de L y R) para cada muestra
    3. Imprimi cada muestra: `"Muestra 0: L=+0.50, R=+0.30, Mono=+0.40"`
    """)
    return


@app.cell
def _(enumerate):
    # EJERCICIO 8: Tu codigo aca
    left_8= [0.5, -0.3, 0.8, -0.6, 0.2, -0.9, 0.4]
    right_8 = [0.3, -0.1, 0.6, -0.4, 0.1, -0.7, 0.3]

    stereo_pairs = list(zip(left_8, right_8))

    for i, (left, right) in enumerate(stereo_pairs, start=1):
        mono = (left + right) / 2
        print(f"Muestra {i}: Left = {left}, Right = {right}, Mono = {mono}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Operaciones con sets

    Dados los sample rates soportados por dos interfaces de audio:
    ```python
    interface_a = {44100, 48000, 88200, 96000, 176400, 192000}
    interface_b = {44100, 48000, 96000}
    ```

    Calcula e imprimi:
    1. Sample rates soportados por **ambas** interfaces
    2. Sample rates soportados por **al menos una** interfaz
    3. Sample rates que tiene la interfaz A pero **no** la B
    4. Si los SR de la interfaz B son un **subconjunto** de los de la A
    """)
    return


@app.cell
def _():
    # EJERCICIO 9: Tu codigo aca
    interface_a= {44100, 48000, 88200, 96000, 176400, 192000}
    interface_b= {44100, 48000, 96000}

    print(f"Interfaz A: {sorted(interface_a)}")
    print(f"Interfaz B: {sorted(interface_b)}")
    print()

    comunes = interface_a & interface_b
    print (f"1.comunes (A & B):  {sorted(comunes)}")

    ambas= interface_a | interface_b
    print (f"2.ambas (A o B): {sorted(ambas)}")

    solo_en_a= interface_a - interface_b
    print (f"3.solo en A (A - B): {sorted(solo_en_a)}")

    es_subconjunto= interface_b.issubset(interface_a)
    print(f"4.B es subconjunto de A: {es_subconjunto}")


    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Dict comprehension - Notas y frecuencias

    Crea un diccionario usando **dictionary comprehension** que mapee los nombres de las notas de A3 a A5 a sus frecuencias.

    Datos de entrada:
    ```python
    nombres_notas = ["A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5"]
    midi_base = [57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81]
    ```

    Formula MIDI a Hz: `f = 440 * 2**((midi - 69) / 12)`

    El diccionario debe ser: `{"A3": 220.0, "B3": 246.94, ...}`
    """)
    return


@app.cell
def _():
    # EJERCICIO 10: Tu codigo aca

    nombres_notas = ["A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5"]
    midi_base = [57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81]

    nota_freq_10= {nombres: 440 * 2**((midi-69)/12) for nombres, midi in zip(nombres_notas, midi_base)}

    print ("Nota - Frecuencia")
    print ("-" * 30)

    for nota, freq in nota_freq_10.items():
        print (f"{nota:3s} : {freq:<10.2f}Hz")
    return


if __name__ == "__main__":
    app.run()
