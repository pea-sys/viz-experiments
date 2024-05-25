import pandas as pd
from io import StringIO
import numpy as np

df = pd.read_json("data/nobel_winners.json")
print(df.columns)
df = df.set_index("name")
print(df.loc["Albert Einstein"])

df.reset_index(inplace=True)
print(df.iloc[2])

sex_col = df.sex
print(type(sex_col))
print(sex_col.head())

print(df.groupby("category").count())
print(sum(df.category == "Physics"))

df_dict = pd.DataFrame(
    {
        "name": ["Albert Einstein", "Marie Curie", "William Faulkner"],
        "category": ["Physics", "Chemistry", "Literature"],
    }
)
print(df_dict)
df = pd.DataFrame(
    [
        {"name": "Albert_Einstein", "category": "Physics"},
        {"name": "Marie Curie", "category": "Chemistry"},
        {"name": "William Faulkner", "category": "Literature"},
    ]
)
print(df)

data = "`Albert Einstein` | Physics \n`Marie Curie` | Chemistry"

df = pd.read_csv(
    StringIO(data),
    sep="|",
    names=["name", "category"],
    skipinitialspace=True,
    quotechar="`",
)
print(df)

s = pd.Series([1, 2, 3, 4])
print(s)

s = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s)
s = pd.Series({"a": 1, "b": 2, "c": 3})
print(s)
print(np.sqrt(s))

# Panel廃止
# df1 = pd.DataFrame({"foo": [1, 2, 3]})
# df2 = pd.DataFrame({"baz": [7, 8, 9, 11]})
# pn = pd.Panel.to_frame({"item1": df1, "item2": df2})
