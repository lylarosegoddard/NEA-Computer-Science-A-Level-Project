from peewee import *
import datetime
from app.models.base_model import db
from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message



# Initialize the database and create tables
def initialise_database():
    with db:
        db.create_tables([User, Conversation, Message])
        