"""SpeechRecognition - библиотека для распознования
 pyAudio - для работы с инструментами звукозаписи
 wave """
import speech_recognition as speech_r
from pydub import AudioSegment


def convertToWav(audioPathFrom, AudioPathTo):
    sound = AudioSegment.from_mp3(audioPathFrom)
    sound.export(AudioPathTo, format='wav')


r = speech_r.Recognizer()

harvard = speech_r.AudioFile('Audio/audio_files_harvard.wav')
with harvard as source:
    audio = r.record(source)  # доп аргументы offset- смещение начала записи, duration - доительность записи
    print(r.recognize_google(audio, show_all=True))

mic = speech_r.Microphone()
print(speech_r.Microphone.list_microphone_names())

with mic as source:
    print('mic')
    audio = r.listen(source, phrase_time_limit=7)
    print(r.recognize_google(audio, language='ru'))

