import json

from pymongo import MongoClient

from app.core.config import settings

uri = (
    f"mongodb://{settings.MONGO_INITDB_ROOT_USERNAME}:"
    f"{settings.MONGO_INITDB_ROOT_PASSWORD}@{settings.DB_HOST}:"
    f"{settings.DB_PORT}/?authSource=admin"
)
client = MongoClient(uri)
db = client[settings.DB_NAME]
templates_collection = db["templates"]


if __name__ == "__main__":
    templates_collection.delete_many({})

    with open("data/templates.json", "r", encoding="utf-8") as file:
        templates = json.load(file)

    templates_collection.insert_many(templates)
