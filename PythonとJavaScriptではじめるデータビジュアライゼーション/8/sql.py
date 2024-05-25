import pandas as pd

from pymongo import MongoClient


client = MongoClient()

db = client.nobel_prize

cursor = db.winners.find()
df = pd.DataFrame(list(cursor))
print(df)


def get_mongo_database(
    db_name, host="localhost", port=27017, username=None, password=None
):
    if username and password:
        mongo_url = "mongodb://%s:%s@%s/%s" % (username, password, host, db_name)
        conn = MongoClient(mongo_url)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]


def mongo_to_dataframe(
    db_name,
    collection,
    query={},
    host="localhost",
    port=27017,
    username=None,
    password=None,
    no_id=True,
):
    db = get_mongo_database(db_name, host, port, username, password)
    cursor = db[collection].find(query)

    df = pd.DataFrame(list(cursor))

    if no_id:
        del df["_id"]

    return df


def dataframe_to_mongo(
    df, db_name, collection, host="localhost", port=27017, username=None, password=None
):
    db = get_mongo_database(db_name, host, port, username, password)

    records = df.to_dict("records")
    db[collection].insert(records)
