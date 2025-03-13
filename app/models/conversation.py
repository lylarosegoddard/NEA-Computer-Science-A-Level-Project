#Conversation class/table

from app.models.base_model import BaseModel
from app.models.user import User
import datetime
from peewee import ForeignKeyField, DateTimeField

#table in database
class Conversation(BaseModel):
    user = ForeignKeyField(User, backref='conversations')  
    #one-to-many relationship between user and conversation
    created_at = DateTimeField(default=datetime.datetime.now)
    #saves date and time when conversation is created
