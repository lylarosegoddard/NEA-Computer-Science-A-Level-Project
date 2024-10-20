from openai import OpenAI
from app.friend import Friend
from app.conversation import Conversation

name = input("Hi there, enter your name:\n")
friendName = input(f"Hi {name}, who would you like to talk to today? \n")
print("\n\n")

friend = Friend(friendName)

conversation = Conversation(name, friend)
conversation.run() 