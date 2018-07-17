from mongoengine import *
from models.user import User

class Lover(Document):
    user_id = ReferenceField(User)
    fullname = StringField()
    dob = DateTimeField()
    gender = IntField()
    city = StringField()
    like = ListField()
    hate = ListField()
    description = StringField()