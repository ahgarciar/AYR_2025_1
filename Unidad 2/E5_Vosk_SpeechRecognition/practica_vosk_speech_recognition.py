import sys
import os
from vosk import Model, KaldiRecognizer
import pyaudio

import Lexico as validador_lexico

# Load the Vosk model
if not os.path.exists("model"):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    sys.exit(1)

model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

# Start audio stream
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Listening...")

while True:
    data = stream.read(4000)

    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()  # "PRENDE EL FOCO DE LA COCINA EN EL VALOR CIEN"
        #print(result, end= "")
        tem_cadena = result[14:]
        tem_cadena = tem_cadena[:len(tem_cadena)-3]
        print("Cadena Leida: ",tem_cadena, end="")
        print("\t->\tResultado Lexico: ", validador_lexico.validar_cadena(tem_cadena))


    else:
        pass
        #partial_result = recognizer.PartialResult()
        #print(partial_result)
