import json
import os

HISTORY_FILE = 'search_history.json'


def save_search_history(user_id, song_name):
    history = load_search_history()
    if user_id not in history:
        history[user_id] = []
    history[user_id].append(song_name)
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file)


def load_search_history():
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, 'r') as file:
        return json.load(file)
