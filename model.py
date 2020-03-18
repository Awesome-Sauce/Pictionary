import json

def load_db():
    with open("words_db.json") as f:
        return json.load(f)

def save_db():
    with open("words_db.json", 'w') as f:
        return json.dump(wordsDB, f)

wordsDB = load_db()