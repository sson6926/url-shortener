import os
from pymongo import MongoClient
from dotenv import load_dotenv


#load file .env
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")


#ket noi db
client = MongoClient(MONGODB_URL)
db = client[MONGODB_DATABASE]
collection = db['urls']