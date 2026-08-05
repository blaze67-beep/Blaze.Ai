class Planner:

    def plan(self, prompt: str):

        plan = {
            "goal": prompt,
            "task": "general",
            "steps": [
                "Understand request",
                "Choose provider",
                "Generate response",
                "Evaluate response"
            ]
        }

        return plan