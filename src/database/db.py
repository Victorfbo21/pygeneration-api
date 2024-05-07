import pymongo as mongo
from dotenv import load_dotenv

import os
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

client = mongo.MongoClient(MONGO_URL)
db = client[MONGO_DB_NAME]