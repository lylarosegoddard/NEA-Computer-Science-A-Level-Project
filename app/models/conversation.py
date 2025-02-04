from app.models.base_model import BaseModel
from app.models.user import User
import datetime
from peewee import ForeignKeyField, DateTimeField

class Conversation(BaseModel):
    user = ForeignKeyField(User, backref='conversations')  # One-to-many relationship
    created_at = DateTimeField(default=datetime.datetime.now)
