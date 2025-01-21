from google.cloud import speech  ## pip3 install google-cloud-speech

#https://console.cloud.google.com/apis/dashboard?project=api-proyectos-fians

#https://console.cloud.google.com/apis/api/speech.googleapis.com/quotas?hl=es&project=api-proyectos-fians&pli=1

#https://realpython.com/python-speech-recognition/

r = speech.SpeechClient.from_service_account_file('api_key_recognition.json')

file_name = 'Audios/audio_file.wav'
with open(file_name, 'rb') as f:
    mp3_data = f.read()

audio_file = speech.RecognitionAudio(content = mp3_data)

config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16, #speech.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz = 44100,
    #sample_rate_hertz = 24000,
    #audio_channel_count = 2,
    audio_channel_count = 1,
    enable_automatic_punctuation = True,
    language_code = 'es-MX'
)

response = r.recognize(
    config=config,
    audio=audio_file
)

print(response)
#print(response.results[0])
#print(str(response).encode("utf8"))
#
#for result in response.results:
#    print(result.alternatives[0].transcript)

