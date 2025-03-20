import os
from pydub import AudioSegment

sound = AudioSegment.from_ogg("audio.ogg")

sound.export("temp.wav", format="wav")

r = sr.Recognizer()

with sr.AudioFile('temp.wav') as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio, language='es-ES')
    print("n El texto generado para el archivo es: n" + text)
except:
    print("Lo siento, no he podido reconocer la voz del archivo")
os.remove('temp.wav')
