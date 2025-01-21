
##brew install portaudio   #  paso 1 en mac
##pip3 install pyaudio     # paso 2 <<<<-----------------------
#brew install flac #paso 3 en mac

#pip3 install speechRecognition <---------------------------

import speech_recognition as sr
r = sr.Recognizer()

print("Inicia:")
#mic = sr.Microphone() ##toma el "microfono" por defecto
#with sr.Microphone(device_index=1) as source:
#    audio = r.listen(source)
with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source) # listen for 1 second
    # to calibrate the energy threshold for ambient noise levels
    audio = r.listen(source)

print("Registro Generado!")

try:
    #print("Mensaje: " + r.recognize_google(audio)) #normal
    cadena =  r.recognize_google(audio, language="es-MX")  #str
    print("Mensaje: " + cadena) #personalized
except sr.UnknownValueError:
    print("Unknown Value Error")
except sr.RequestError as e:
    print("Request Error: ".format(e))
except Exception as ex:
    print("Error: ".format(ex))

