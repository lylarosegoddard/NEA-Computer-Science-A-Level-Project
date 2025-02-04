from app.models.base_model import BaseModel
from peewee import ForeignKeyField, TextField, DateTimeField, BooleanField
import datetime
from app.models.conversation import Conversation

class Message(BaseModel):
    conversation = ForeignKeyField(Conversation, backref='messages')  # One-to-many relationship
    message = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    bullying = BooleanField(default = False)
    explanation = TextField()