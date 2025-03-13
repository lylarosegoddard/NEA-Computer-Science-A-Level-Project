#initialise_database subroutine

from peewee import *
import datetime
from app.models.base_model import db
from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message
#imports all the tables in the database to allow the subroutine to actually initialise and create the database


# initialize the database and create tables
def initialise_database():
    with db:
        db.create_tables([User, Conversation, Message])

#this results in this SQL:

#CREATE TABLE "conversation" (
# "id" INTEGER NOT NULL PRIMARY KEY, 
# "user_id" INTEGER NOT NULL, 
# "created_at" DATETIME NOT NULL, 
# FOREIGN KEY ("user_id") REFERENCES "user" ("id")
#);

#CREATE TABLE "message" (
# "id" INTEGER NOT NULL PRIMARY KEY, 
# "conversation_id" INTEGER NOT NULL, 
# "message" TEXT NOT NULL, 
# "created_at" DATETIME NOT NULL, 
# "bullying" INTEGER NOT NULL DEFAULT 0, 
# "is_bullying" INTEGER NOT NULL DEFAULT 0, 
# "explanation" TEXT
#);

#CREATE TABLE "user" (
# "id" INTEGER NOT NULL PRIMARY KEY, 
# "name" TEXT NOT NULL UNIQUE, 
# "hashed_password" TEXT NOT NULL
#);
        

