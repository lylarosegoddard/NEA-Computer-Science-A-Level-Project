from site import USER_SITE
from openai import OpenAI
from app.friend import Friend
from app.conversation_runner import ConversationRunner
from app.peewee import initialise_database, User, Message

initialise_database()

name = input("Hi there, enter your name:\n")
user, created = User.get_or_create(name = name)

friend_name = input(f"Hi {name}, who would you like to talk to? \n")
friend = Friend(friend_name)
conversation = ConversationRunner(user, friend)

conversation.start_conversation(user)
conversation.run()
