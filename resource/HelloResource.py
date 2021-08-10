from flask_restful import Resource
from service.HelloService import HelloService


class HelloResource(Resource):
    def get(self):
        return HelloService.hello_message()
