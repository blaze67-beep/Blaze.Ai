from app.voice.microphone import Microphone
from app.voice.speech_to_text import SpeechToText
from app.voice.text_to_speech import TextToSpeech
from app.voice.wake_word import WakeWord
from app.brain.brain import Brain


def main():

    print("\n================================")
    print("        BLAZE.AI STARTING")
    print("================================\n")

    # -----------------------------
    # INITIALIZE COMPONENTS
    # -----------------------------

    mic = Microphone()
    stt = SpeechToText()
    tts = TextToSpeech()
    brain = Brain()
    wake_word = WakeWord()

    print("[Blaze] All systems ready.")

    # -----------------------------
    # WAIT FOR LOCAL ACTIVATION
    # -----------------------------

    try:

        activated = wake_word.wait()

        if not activated:
            print("[Blaze] Activation cancelled.")
            return

        print("\n================================")
        print("       BLAZE VOICE CHAT")
        print("================================")
        print("Blaze is listening.")
        print("Say 'exit', 'quit', 'stop', or 'goodbye' to stop.\n")

        # -----------------------------
        # MAIN VOICE LOOP
        # -----------------------------

        while True:

            try:

                # Record user speech
                audio = mic.record(5)

                # Convert speech to text
                text = stt.transcribe(audio)

                # Delete temporary WAV file
                mic.delete(audio)

                text = text.strip()

                # Ignore empty transcription
                if not text:
                    continue

                print(f"\nYou: {text}")

                # -----------------------------
                # EXIT COMMAND
                # -----------------------------

                command = text.lower().strip()

                if command in {
                    "exit",
                    "quit",
                    "stop",
                    "goodbye",
                    "shutdown blaze",
                    "stop blaze"
                }:

                    print("\n[Blaze] Shutting down...")

                    tts.speak("Goodbye.")

                    break

                # -----------------------------
                # SEND TO BRAIN
                # -----------------------------

                response = brain.ask(text)

                if response is None:
                    response = "I couldn't generate a response."

                response = str(response).strip()

                # -----------------------------
                # DISPLAY RESPONSE
                # -----------------------------

                print(f"\nBlaze: {response}")

                # -----------------------------
                # SPEAK RESPONSE
                # -----------------------------

                tts.speak(response)

            except KeyboardInterrupt:

                print("\n\n[Blaze] Interrupted.")

                break

            except Exception as e:

                print(f"\n[Voice Error] {e}")

                try:
                    tts.speak(
                        "I encountered an error, but I'm still running."
                    )
                except Exception:
                    pass

    finally:

        # -----------------------------
        # CLEANUP
        # -----------------------------

        try:
            wake_word.close()
        except Exception:
            pass

        print("\n[Blaze] Stopped.")


if __name__ == "__main__":
    main()