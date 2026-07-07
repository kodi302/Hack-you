import json
import os

SESSION = "session.json"


def save(data):

    with open(SESSION, "w") as f:
        json.dump(data, f, indent=4)


def load():

    if not os.path.exists(SESSION):
        return {}

    with open(SESSION) as f:
        return json.load(f)
