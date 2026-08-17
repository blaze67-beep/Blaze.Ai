from app.voice.microphone import Microphone

mic = Microphone()

path = mic.record(5)

print("Audio saved to:", path)

input("Press ENTER to delete the file...")

mic.delete(path)

print("Done.")