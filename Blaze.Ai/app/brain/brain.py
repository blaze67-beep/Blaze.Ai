from app.brain.router import Router
from app.brain.planner import Planner
from app.brain.evaluator import Evaluator
from app.brain.memory import Memory


class Brain:

    def __init__(self):

        self.router = Router()
        self.planner = Planner()
        self.evaluator = Evaluator()
        self.memory = Memory()

    def ask(self, prompt: str):

        prompt_lower = prompt.lower()

        # ==========================
        # MEMORY COMMANDS
        # ==========================

        if prompt_lower.startswith("remember "):

            try:

                _, key, value = prompt.split(" ", 2)

                self.memory.remember(key, value)

                return f"I'll remember that {key} = {value}"

            except ValueError:

                return "Usage: remember <key> <value>"

        if prompt_lower.startswith("recall "):

            try:

                _, key = prompt.split(" ", 1)

                value = self.memory.recall(key)

                if value is None:
                    return "I don't remember that."

                return f"{key} = {value}"

            except ValueError:

                return "Usage: recall <key>"

        # ==========================
        # BUILD MEMORY CONTEXT
        # ==========================

        memory_context = self.memory.context()

        full_prompt = f"""
{memory_context}

User:
{prompt}

Blaze:
"""

        # ==========================
        # NORMAL PIPELINE
        # ==========================

        print("\n========== BLAZE BRAIN ==========")

        print("[Planner]")
        plan = self.planner.plan(prompt)
        print(plan)

        print("\n[Router]")
        provider = self.router.select(prompt)
        print(type(provider).__name__)

        print("\n[Provider]")
        response = provider.chat(full_prompt)
        print(response)

        print("\n[Evaluator]")
        result = self.evaluator.evaluate(response)
        print(result)

        print("=================================\n")

        return result["response"]