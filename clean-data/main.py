import json
import re

with open("data.json", "r") as text:
    data = json.load(text)

# removes extra data ".mw-parser-output .nobold{font-weight:normal}(EX)\u00a0" from data.json for clarity.
for item in data:
  item["Category"] = re.compile(" [\.(]").split(item["Category"])[0]

print(data)