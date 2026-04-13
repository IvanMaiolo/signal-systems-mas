# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.4",
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
    # Clase 1: Ejercicios Practicos
    ## El Punto de Partida

    Resuelve cada ejercicio en la celda indicada. Cada ejercicio tiene una descripcion y un espacio para tu codigo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Total de muestras

    Calcula el **numero total de muestras** para un audio de **3 segundos** grabado a **48000 Hz**.
    Guarda el resultado en una variable llamada `total_muestras` e imprimi el resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    duracion = 3 #segundos
    sample_rate = 48000 #Hz
    total_muestras = duracion * sample_rate
    print(total_muestras)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Tamano de archivo WAV

    Calcula el **tamano en MB** de un archivo WAV con las siguientes caracteristicas:
    - Estereo (2 canales)
    - Bit depth: 16 bits
    - Sample rate: 44100 Hz
    - Duracion: 5 segundos

    Formula: `tamano_bytes = sample_rate * duracion * canales * (bit_depth / 8)`

    Guarda el resultado en `tamano_mb` e imprimi con 2 decimales.
    """)
    return


@app.cell
def _():
    # EJERCICIO 2: Tu codigo aca
    _duracion = 5 #segundos
    bit_depth = 16 #bits
    _sample_rate = 44100 #Hz
    canales = 2
    tamano_bytes = _sample_rate * _duracion * (bit_depth / 8) * canales
    tamano_mb = tamano_bytes / (1024 * 1024)
    print (round(   tamano_mb,  2))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Convertir segundos a mm:ss

    Dada una duracion en segundos (`duracion_seg = 197`), convertila al formato **mm:ss** usando los operadores `//` y `%`.

    El resultado debe ser un string como `"3:17"`.
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca
    duracion_seg = 197
    minutos = duracion_seg // 60
    segundos = duracion_seg % 60
    texto = f"{minutos}:{segundos}"
    print (texto)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Extraer extension de archivo

    Dado el nombre de archivo `nombre = "mi_cancion_final_v2.wav"`, extraer:
    1. La **extension** (sin el punto): `"wav"`
    2. El **nombre sin extension**: `"mi_cancion_final_v2"`

    Usa metodos de strings (`.split()`, slicing, etc.).
    """)
    return


@app.cell
def _():
    # EJERCICIO 4: Tu codigo aca
    nombre = "mi_cancion_final_v2.wav"
    nombre_sin_extension = nombre.split(".wav")[0]
    print (nombre_sin_extension)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Frecuencia de una nota MIDI

    La formula para convertir un numero de nota MIDI a frecuencia en Hz es:

    $$f = 440 \times 2^{(midi - 69) / 12}$$

    Calcula la frecuencia de las siguientes notas MIDI:
    - **60** (Do central / Middle C)
    - **69** (La 440 / A4)
    - **72** (Do una octava arriba / C5)

    Imprimi cada resultado con 2 decimales.
    """)
    return


@app.cell
def _():
    # EJERCICIO 5: Tu codigo aca
    nota_midi_1 = 60
    nota_midi_2 = 69
    nota_midi_3 = 72
    nota_en_Hz_1 = 440 * (2**((nota_midi_1 - 69) / 12))
    nota_en_Hz_2 = 440 * (2**((nota_midi_2 - 69) / 12))
    nota_en_Hz_3 = 440 * (2**((nota_midi_3 - 69) / 12))
    print (f"Nota MIDI {nota_midi_1} = {round(nota_en_Hz_1, 2)} Hz")
    print (f"Nota MIDI {nota_midi_2} = {round(nota_en_Hz_2, 2)} Hz")
    print (f"Nota MIDI {nota_midi_3} = {round(nota_en_Hz_3, 2)} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: f-string descriptivo

    Crea las siguientes variables:
    - `titulo = "Bohemian Rhapsody"`
    - `artista = "Queen"`
    - `duracion_seg = 354`
    - `sample_rate = 44100`
    - `bit_depth = 24`

    Usando f-strings, crea un string `info` que muestre:
    ```
    Pista: Bohemian Rhapsody - Queen
    Duracion: 5:54
    Formato: 44,100 Hz / 24 bits
    Total muestras: 15,609,400
    ```
    Imprimi el resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Tu codigo aca
    titulo = "Bohemian Rhapsody"
    artista = "Queen"
    _duracion_seg = 354
    _sample_rate = 44100 #Hz
    _bit_depth = 24 #bits
    _minutos = _duracion_seg // 60
    _segundos = _duracion_seg % 60
    _total_muestras = _duracion_seg * _sample_rate
    info = f"""Pista:'{titulo}' - {artista}"
    Druacion: {_minutos}:{_segundos} 
    Total muestras: {_total_muestras} 
    Formato: {_sample_rate} Hz / {_bit_depth} bits."""
    print (info)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Logica booleana para calidad de audio

    Crea las variables:
    - `sr = 48000` (sample rate)
    - `bits = 24` (bit depth)
    - `canales = 2` (numero de canales)

    Determina (como booleanos):
    1. `es_profesional`: el sample rate es >= 44100 **Y** el bit depth es >= 16
    2. `es_hd`: el sample rate es >= 96000 **O** el bit depth es >= 24
    3. `es_surround`: el numero de canales es > 2
    4. `calidad_ok`: es profesional **Y NO** es surround (estereo profesional)

    Imprimi cada resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 7: Tu codigo aca
    sr = 48000 #Hz
    _bits = 24 #bits
    _canales = 2

    es_prfesional = (sr >= 44100) and (_bits>= 24)
    es_hd = (sr >= 96000) and (_bits >= 24)
    es_surround = (_canales >= 2)
    calidad_ok = es_prfesional and es_surround
    print (f"Es profesional: {es_prfesional}")
    print (f"Es HD: {es_hd}")
    print (f"Es Surround: {es_surround}")
    print (f"Calidad OK: {calidad_ok}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Frecuencia de Nyquist

    La **frecuencia de Nyquist** es la maxima frecuencia que se puede representar con un sample rate dado.
    Se calcula como: `f_nyquist = sample_rate / 2`

    Para los siguientes sample rates, calcula e imprimi la frecuencia de Nyquist:
    - 22050 Hz
    - 44100 Hz
    - 48000 Hz
    - 96000 Hz
    - 192000 Hz

    Imprimi en formato: `"SR: 44100 Hz -> Nyquist: 22050.0 Hz"`
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca
    sr_1 = 22050 #Hz
    sr_2 = 44100 #Hz
    sr_3 = 48000 #Hz
    sr_4 = 96000 #Hz
    sr_5 = 192000 #Hz
    f_nyquist_1 = sr_1 / 2
    f_nyquist_2 = sr_2 / 2    
    f_nyquist_3 = sr_3 / 2
    f_nyquist_4 = sr_4 / 2
    f_nyquist_5 = sr_5 / 2
    print (f"""SR: {sr_1} Hz -> Nyquist: {f_nyquist_1} Hz""")
    print (f"""SR: {sr_2} Hz -> Nyquist: {f_nyquist_2} Hz""")
    print (f"""SR: {sr_3} Hz -> Nyquist: {f_nyquist_3} Hz""")
    print (f"""SR: {sr_4} Hz -> Nyquist: {f_nyquist_4} Hz""")
    print (f"""SR: {sr_5} Hz -> Nyquist: {f_nyquist_5} Hz""")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio BONUS: Calculadora de latencia

    La **latencia** de un buffer de audio se calcula como:

    $$latencia_{ms} = \frac{buffer\_size}{sample\_rate} \times 1000$$

    Calcula la latencia para las siguientes combinaciones:
    - Buffer: 64, SR: 44100
    - Buffer: 128, SR: 44100
    - Buffer: 256, SR: 48000
    - Buffer: 512, SR: 96000

    Imprimi cada resultado con 2 decimales en formato:
    `"Buffer: 64 @ 44100 Hz -> Latencia: X.XX ms"`
    """)
    return


@app.cell
def _():
    # EJERCICIO BONUS: Tu codigo aca
    buffer_1 = 64
    _sr_1 = 44100 #Hz
    buffer_2 = 128 
    _sr_2 = 44100 #Hz
    buffer_3 = 256
    _sr_3 = 48000 #Hz
    buffer_4 = 512
    _sr_4 = 96000 #Hz
    latencia_1 = (buffer_1 / _sr_1) * 1000
    latencia_2 = (buffer_2 / _sr_2) * 1000       
    latencia_3 = (buffer_3 / _sr_3) * 1000
    latencia_4 = (buffer_4 / _sr_4) * 1000
    print (f"Buffer: {buffer_1} @ {_sr_1} Hz -> Latencia: {round((buffer_1 / _sr_1) * 1000, 2)} ms")
    print (f"Buffer: {buffer_2} @ {_sr_2} Hz -> Latencia: {round((buffer_2 / _sr_2) * 1000, 2)} ms")
    print (f"Buffer: {buffer_3} @ {_sr_3} Hz -> Latencia: {round((buffer_3 / _sr_3) * 1000, 2)} ms")
    print (f"Buffer: {buffer_4} @ {_sr_4} Hz -> Latencia: {round((buffer_4 / _sr_4) * 1000, 2)} ms")
    return


if __name__ == "__main__":
    app.run()
