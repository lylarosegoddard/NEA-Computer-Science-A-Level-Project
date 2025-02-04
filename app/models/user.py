from app.models.base_model import BaseModel
from peewee import CharField, IntegerField, BooleanField

class User(BaseModel):
    name = CharField(unique=True)
    escalated = BooleanField(default=False)
