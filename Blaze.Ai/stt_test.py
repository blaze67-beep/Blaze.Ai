from app.voice.microphone import Microphone
from app.voice.speech_to_text import SpeechToText

mic = Microphone()
stt = SpeechToText()

audio = mic.record(5)

print("\nRecognizing...")

text = stt.transcribe(audio)

print("\nYou said:")
print(text)

mic.delete(audio)