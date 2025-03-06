#main.py

#imports to utilise all the features of the program
from openai import OpenAI
from app.friend import Friend
from app.conversation_runner import ConversationRunner
from app.peewee import initialise_database 
from app.models.user import User
from app.models.message import Message
from app.banned_query import BannedQuery

initialise_database()
#creates the database

name = input("Hi there, enter your name:\n")
user = User.get_or_none(name = name)
#gets the user from the database if there is a user with that name
password = input("Enter a password or type 'quit' to exit:\n")
#asks for the password or lets the user quit the program

if password.lower() == 'quit':
    print("Goodbye!")
    exit()
#lets the user quit the program if quit is typed
elif user is None:
    user = User(name = name)
    user.set_password(password)
#if there is no user by the name entered, a new user is created and their password is saved
else:
    while not user.check_password(password): 
        password = input("Incorrect password please try again or type 'quit' to exit:\n")
        if password.lower() == 'quit':
            print("Goodbye!")
            exit()
    print("Welcome back " + name + "!\n")   
#if the users name is in the database it asks for the password 
#if that password entered is wrong then the user can retry as many times as necessary or they can quit

if BannedQuery(user).banned():
    print("You have exceeded the number of bullying offences allowed. You have been banned.")
    exit()
#if the user has exceeded the number of bullying offences allowed they are banned

print("\n\nEnter 'Goodbye' at any point in the conversation to end the conversation. ")
friend_name = input(f"\n\nHi {name}, who would you like to talk to?  \n\n")
friend = Friend(friend_name)
conversation = ConversationRunner(user, friend)
#asks for the name of the friend and assigns the OpenAI APIs responses to user to the friends name

conversation.start_conversation(user)
conversation.run()
#the conversation will start when the user types and end when the user types 'Goodbye'


