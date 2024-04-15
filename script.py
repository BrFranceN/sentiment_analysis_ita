

import json

data = []
with open("haspeede3-task1-test-data.jsonl", 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

# Now the 'data' list contains the data from the .jsonl file


print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
