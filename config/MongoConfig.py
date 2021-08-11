
from pymongo import MongoClient


class MongoConfig():
    def get_database():
        CONNECTION_STRING = 'mongodb://localhost:27017/baylei'

        client = MongoClient(CONNECTION_STRING)

        return client['baylei']
