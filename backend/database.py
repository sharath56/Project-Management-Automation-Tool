import pymongo
import os

mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = mongo_client["developer_tasks"]
tasks_collection = db["tasks"]
