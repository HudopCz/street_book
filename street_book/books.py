import json
import re
import os

books = {}

this_dir = os.path.dirname(__file__)

for filename in os.listdir(os.path.join(this_dir, "../books")):
    if filename.endswith(".json"):
        with open(os.path.join(this_dir, "../books/") + filename) as f:
            content = json.load(f)
            books[filename[:-5]] = content
