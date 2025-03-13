# base model class

from peewee import SqliteDatabase, Model

#connects database to file 'db.sqlite'
db = SqliteDatabase('db.sqlite')

#any class/table inherits from this class 
class BaseModel(Model):
    class Meta:
        database = db

#sets up the connection to the database which every other class/table will inherit from