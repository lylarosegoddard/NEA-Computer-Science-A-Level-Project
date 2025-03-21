#User class/table

from app.models.base_model import BaseModel
from peewee import CharField
import hashlib


class User(BaseModel):
    name = CharField(unique=True)
    hashed_password = CharField()
    #saves the users name and hashed password to the database
    
    def hash_password(self, password): #password hashing
        return hashlib.sha256(password.encode()).hexdigest()
        #hashes the password

    def check_password(self, password):
        return self.hashed_password == self.hash_password(password)
        #have to hash the password the user gave and compare the hashed passwords
        #as we cant decrypt the hashed password in the database

    def set_password(self, password):
        self.hashed_password = self.hash_password(password)
        self.save()
        #if a user doesnt have a password, this will save the users enterred password as a hashed password

