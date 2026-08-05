from app.brain.brain import Brain


brain = Brain()

while True:

    prompt = input("You : ")

    if prompt.lower() in ["exit", "quit"]:
        break

    reply = brain.ask(prompt)

    print("Blaze :", reply)