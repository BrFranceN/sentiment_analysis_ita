

import json

data = []
with open("haspeede3-task1-test-data.jsonl", 'r', encoding='utf-8') as f:
    for line in f:
        sample = json.loads(line)
        text = sample['text']
        choices = sample['choices']
        index_label = int(sample['label'])
        label = choices[index_label]
        label = 0 if (label=='neutrale') else 1
        data.append((text,label))
# Now the 'data' list contains the data from the .jsonl file


for elem in data[:10]:
    print('======')
    print(elem)
    print('======')


