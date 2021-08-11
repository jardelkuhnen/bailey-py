
from config.MongoConfig import MongoConfig
from bson.json_util import dumps
import json

from repository.ClientRepository import ClientRepository

class ClientService():
    def getAll():
        return list(ClientRepository.getAll())