#! python

import json

file = open("ex.json")
content = file.read()
data = json.loads(content)
file.close()

print(data["nickname"])