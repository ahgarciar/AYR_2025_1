
##brew install portaudio   #  paso 1 en mac
##pip3 install pyaudio     # paso 2
#brew install flac #paso 3 en mac
import speech_recognition as sr
r = sr.Recognizer()

print("Inicia:")
#with sr.Microphone(device_index=1, sample_rate=44100) as source:
#with sr.Microphone(device_index=1) as source:
with sr.Microphone(sample_rate=44100) as source:
    #r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    audio = r.listen(source)
print("Registro Generado!")

with open("../E3_Intro_SpeechRecognition/Audios/audio_file.wav", "wb") as file:
    file.write(audio.get_wav_data())
print("Archivo Creado!")






