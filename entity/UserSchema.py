
from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class UserSchema(ma.Schema):
    id: fields.Integer(dump_only=True)
    name: fields.String(dump_only=True)
    age: fields.Integer(dump_only=True)
    phone: fields.String(dump_only=True)

