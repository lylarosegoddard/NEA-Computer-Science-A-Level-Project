from app.models.base_model import BaseModel
from peewee import CharField, BooleanField
import hashlib


class User(BaseModel):
    name = CharField(unique=True)
    hashed_password = CharField()
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
        
    def check_password(self, password):
        return self.hashed_password == self.hash_password(password)

    def set_password(self, password):
        self.hashed_password = self.hash_password(password)
        self.save()

