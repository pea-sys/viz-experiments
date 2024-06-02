from flask import Flask, request, abort
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
db = MongoClient().nobel_prize


@app.route("/api/winners")
def get_country_data():
    query_dict = {}
    for key in ["country", "category", "year"]:
        arg = request.args.get(key)
        if arg:
            query_dict[key] = arg

    winners = db.winners_cleaned.find(query_dict)
    if winners:
        return dumps(winners)
    abort(404)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
