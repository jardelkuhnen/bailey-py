

from flask_restful import Resource
from config.MongoConfig import MongoConfig
from bson.json_util import dumps
import json

from service.ClientService import ClientService

dbname = MongoConfig.get_database()
collection = dbname['client']

class ClientResource(Resource):
    
    def get(self):
        list_user = ClientService.getAll()
        
        json_data = json.loads(dumps(list_user))

        return {"status": 'success', 'data': json_data}, 200
