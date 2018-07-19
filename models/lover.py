from mongoengine import *
from models.user import User

class Lover(Document):
    user_id = ReferenceField(User)
    fullname = StringField()
    date = DateTimeField()
    year = IntField()
    age = IntField()
    gender = IntField()
    city = StringField()
    like = ListField()
    hate = ListField()
    description = StringField()