#Message class/table 

from app.models.base_model import BaseModel
from peewee import ForeignKeyField, IntegerField, TextField, DateTimeField, BooleanField
import datetime
from app.models.conversation import Conversation

#table in database
class Message(BaseModel):
    conversation = ForeignKeyField(Conversation, backref='messages') 
    #one-to-many relationship between conversation and message
    message = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    bullying = IntegerField(default = 0) 
    is_bullying = BooleanField(default = False)
    explanation = TextField(null = True)
    #saves the message, the date and time the message was created, the bullying score, 
    #whether the message is bullying or not and the explanation if the message is bullying