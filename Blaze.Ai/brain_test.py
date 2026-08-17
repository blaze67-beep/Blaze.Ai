from app.brain.brain import Brain

brain = Brain()

print("🔥 Blaze Brain Online")

while True:

    prompt = input("You : ")

    if prompt.lower() in ["exit", "quit"]:
        break

    print("Memory:", brain.memory.all())

    response = brain.ask(prompt)

    print("Blaze :", response)