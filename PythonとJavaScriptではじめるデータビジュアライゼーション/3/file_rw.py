nobel_winners = [
    {'category':'Physics','name':'Albert Einstein','nationality':'Swiss','sex':'male','year':1921},
    {'category':'Physics','name':'Paul Dirac','nationality':'British','sex':'malr','year':1933},
    {'category':'Chemistry','name':'Marie Curie','nationality':'Polish','sex':'female','year':1911}
]

csv_path = 'data/nobel_winners.csv'
json_path = 'data/nobel_winners.json'

cols = nobel_winners[0].keys()
cols=sorted(cols)

with open(csv_path,'w') as f:
    f.write(','.join(cols) + '\n')

    for o in nobel_winners:
        row = [str(o[col]) for col in cols]
        f.write(','.join(row) + '\n')


with open(csv_path,'r') as f:
    for line in f.readlines():
        print(line)

import csv

with open(csv_path,'w') as f:
    fieldnames = nobel_winners[0].keys()
    fieldnames = sorted(fieldnames)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)

with open(csv_path) as f:
    reader = csv.DictReader(f)
    nobel_winners = list(reader)
    for row in nobel_winners:
        print(row)

import json

with open(json_path,'w') as f:
    json.dump(nobel_winners,f)

print(open(json_path).read())

with open(json_path) as f:
    nobel_winners = json.load(f)

print(nobel_winners)