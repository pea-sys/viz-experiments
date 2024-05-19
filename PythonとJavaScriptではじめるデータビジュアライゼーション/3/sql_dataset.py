import dataset


nobel_winners = [
    {'category':'Physics','name':'Albert Einstein','nationality':'Swiss','sex':'male','year':1921},
    {'category':'Physics','name':'Paul Dirac','nationality':'British','sex':'male','year':1933},
    {'category':'Chemistry','name':'Marie Curie','nationality':'Polish','sex':'female','year':1911}
]

db = dataset.connect('sqlite:///data/nobel_prize.db')

wtable = db['winners']
winners = wtable.find()
winners = list(winners)
print(winners)

wtable = db['winners']
wtable.drop()

wtable = db['winners']
print(wtable.find())

with db as tx:
    for w in nobel_winners:
        tx['winners'].insert(w)

print(db['winners'].count())

winners = db['winners'].find()
print(dataset.__version__)

