MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_USERNAME = "user"
MONGO_PASSWORD = "user"
URL_PREFIX = "api"
MONGO_DBNAME = "nobel_prize"
X_DOMAINS = "*"
HATEOAS = False
PAFINATION = False
DOMAIN = {
    "winners_full": {
        "item_title": "winners",
        "schema": {
            "country": {"type": "string"},
            "category": {"type": "string"},
            "name": {"type": "string"},
            "year": {"type": "integer"},
            "gender": {"type": "string"},
            "mini_bio": {"type": "string"},
            "bio_image": {"type": "string"},
        },
        "url": "winners",
    }
}
