import pandas as pd
import numpy as np
from pymongo import MongoClient
import sqlalchemy


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

    print(db[collection].delete_many({}).deleted_count)
    db[collection].insert_many(records)


def clean_data(df):
    df = df.replace("", np.nan)
    df_born_in = df[df.born_in.notnull()]
    df = df[df.born_in.isnull()]
    df = df.drop("born_in", axis=1)
    df.drop(df[df.year == 1809].index, inplace=True)
    df = df[~(df.name == "Marie Curie")]
    df.loc[
        (df.name == "Marie Sk\u0142odowska-Curie") & (df.year == 1911), "country"
    ] = "France"
    df.drop(df[(df.name == "Sidney Altman") & (df.year == 1990)].index, inplace=True)
    df.loc[df.name == "Ragnar Granit", "gender"] = "male"
    df = df[df.gender.notnull()]
    df.loc[df.name == "Hiroshi Amano", "date_of_birth"] = "11 September 1960"
    df.date_of_birth = pd.to_datetime(df.date_of_birth, errors="coerce")
    df.date_of_death = pd.to_datetime(df.date_of_death, errors="coerce")
    df.date_of_birth = df.date_of_birth.astype(object).where(
        df.date_of_birth.notnull(), None
    )
    df.date_of_death = df.date_of_death.astype(object).where(
        df.date_of_death.notnull(), None
    )

    df["award_age"] = df.year - pd.DatetimeIndex(df.date_of_birth).year
    return df, df_born_in


client = MongoClient()

db = client.nobel_prize
df = pd.read_json("nobel_winners_dirty.json")
df_clean, df_born_in = clean_data(df)
dataframe_to_mongo(df_clean, "nobel_prize", "winners_cleaned")
dataframe_to_mongo(df_born_in, "nobel_prize", "winners_born_in")

df = mongo_to_dataframe("nobel_prize", "winners")

# engine = sqlalchemy.create_engine("sqlite:///data/nobel_prize.db")
# df_clean.to_sql("winners", engine)

df_winners_bios = pd.read_json(open("nobel_winners_biopic.json"))
print(df_clean.columns)
print(df_winners_bios.columns)
df_winners_all = pd.merge(
    df_clean,
    df_winners_bios[
        ["award_age", "link", "text", "bio_image", "image_urls", "mini_bio"]
    ],
    how="outer",
    on="link",
)

df_winners_all = df_winners_all[~df_winners_all.name.isnull()].drop_duplicates(
    subset=["link", "year"]
)
print(df_winners_all.count())
df_winners_all = df_winners_all[df_winners_all.mini_bio.isnull()]
dataframe_to_mongo(df_winners_all, "nobel_prize", "winners_all")

engine = sqlalchemy.create_engine("sqlite:///data/nobel_prize.db")
df_clean.to_sql("winners", engine)
