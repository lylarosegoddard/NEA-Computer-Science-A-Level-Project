
from openai import OpenAI
from app.friend import Friend
from app.conversation_runner import ConversationRunner
from app.peewee import initialise_database 
from app.models.user import User
from app.models.message import Message
from app.banned_query import BannedQuery

initialise_database()

name = input("Hi there, enter your name:\n")
user = User.get_or_none(name = name)
password = input("Enter a password or type 'quit' to exit:\n")
if user is None:
    user = User(name = name)
    user.set_password(password)
elif password.lower() == 'quit':
    print("Goodbye!")
    exit()
else:
    while not user.check_password(password): 
        password = input("Incorrect password please try again or type 'quit' to exit:\n")
        if password.lower() == 'quit':
            print("Goodbye!")
            exit()
    print("Welcome back " + name + "!\n")   

if BannedQuery(user).banned():
    print("You have exceeded the number of bullying offences allowed. You have been banned.")
    exit()

friend_name = input(f"Hi {name}, who would you like to talk to? \n")
friend = Friend(friend_name)
conversation = ConversationRunner(user, friend)

conversation.start_conversation(user)
conversation.run()

