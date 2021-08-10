

from flask import Blueprint 
from flask_restful import Api
from resource.HelloResource import HelloResource
from resource.UserResource import UserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(HelloResource, '/hello')
api.add_resource(UserResource, '/user')