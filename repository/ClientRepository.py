
from config.MongoConfig import MongoConfig

dbname = MongoConfig.get_database()
collection = dbname['client']

class ClientRepository():

    def getAll():
        return collection.find()