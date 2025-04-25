from pymongo import MongoClient
from ..config import setting

mongo_client = MongoClient(setting.MONGODB_CONNECTION_STRING)
db = mongo_client[setting.MONGODB_DATABASE]