

from flask import request
from flask_restful import Resource
from entity.UserSchema import UserSchema
from repository.UserRepository import UserRepository

users_schema = UserSchema(many=true)
user_schema = UserSchema()

class UserResource(Resource):
    
    def get(self):
        users = UserRepository.query.all()
        users = users_schema.dump(users).data
        return {"status": 'success', 'data': users}, 200
