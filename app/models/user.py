#User class/table

#inherits from base model class
from app.models.base_model import BaseModel
#importing from peewee ORM
from peewee import CharField, BooleanField
#importing the password hashing library
import hashlib


class User(BaseModel):
    name = CharField(unique=True)
    hashed_password = CharField()
    #saves the users name and hashed password to the database
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
        #hashes the password

    def check_password(self, password):
        return self.hashed_password == self.hash_password(password)
        #checks if the password entered by the user is the same as the password saved in the database

    def set_password(self, password):
        self.hashed_password = self.hash_password(password)
        self.save()
        #if a user doesnt have a password, this will save the users enterred password as a hashed password

