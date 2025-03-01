
from openai import OpenAI
from app.friend import Friend
from app.conversation_runner import ConversationRunner
from app.peewee import initialise_database 
from app.models.user import User
from app.models.message import Message

initialise_database()

name = input("Hi there, enter your name:\n")
user = User.get_or_none(name = name)
password = input("Enter a password:\n")
if user is None:
    user = User(name = name)
    user.set_password(password)
else:
    if not user.check_password(password):
        print("Incorrect password")
        exit()

friend_name = input(f"Hi {name}, who would you like to talk to? \n")
friend = Friend(friend_name)
conversation = ConversationRunner(user, friend)

conversation.start_conversation(user)
conversation.run()

