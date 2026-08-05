class Evaluator:

    def evaluate(self, response: str):

        result = {
            "response": response,
            "score": 1.0,
            "approved": True
        }

        return result