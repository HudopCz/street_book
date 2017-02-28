import json
import re
import os

books = {}

for filename in os.listdir("books"):
    if filename.endswith(".json"):
        with open("books/" + filename) as f:
            content = json.load(f)
            books[filename[:-5]] = content
