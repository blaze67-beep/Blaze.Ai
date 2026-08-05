import json
import os


class Memory:

    def __init__(self):

        self.file = "app/logs/memory.json"

        os.makedirs("app/logs", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

    def _load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def _save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def remember(self, key, value):

        data = self._load()
        data[key] = value
        self._save(data)

    def recall(self, key):

        data = self._load()
        return data.get(key)

    def all(self):

        return self._load()