from app.actions.action_manager import ActionManager

manager = ActionManager()

while True:

    command = input("Command: ")

    if command == "exit":
        break

    result = manager.execute(command)

    print(result)