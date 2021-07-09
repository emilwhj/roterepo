import json

f = open('skattemeldinger.json',)
data = json.load(f)
f.close()

print(data['skattemeldinger'])