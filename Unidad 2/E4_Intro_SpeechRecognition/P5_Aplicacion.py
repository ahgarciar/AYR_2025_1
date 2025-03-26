
##brew install portaudio   #  paso 1 en mac
##pip3 install pyaudio     # paso 2
#brew install flac #paso 3 en mac
import speech_recognition as sr
r = sr.Recognizer()
#audio_file = sr.AudioFile('Audios/audio1.wav')
audio_file = sr.AudioFile('Audios/audio_file.wav')
try:
    with audio_file as source:
        audio = r.record(source)

    var = r.recognize_google(audio,language="es-MX", show_all=False)
    print("Mensaje: " ) #personalized
    print(var)

    palabras = str(var).split()
    print(palabras)

    #if palabras[0] =="debería":
    if "debería" in palabras:
        print("Saludos:D!")


except sr.UnknownValueError as e:
    print("Unknown Value Error", e)
except sr.RequestError as e:
    print("Request Error: ".format(e))
except Exception as ex:
    print(ex)


