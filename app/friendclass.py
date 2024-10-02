import os
from openai import OpenAI
from app.complete import Complete

class Friend:
  def __init__(self):
    self.name = self.get_name()
    self.friendName = self.get_friendName(self.name)
    self.complete = self.Complete()

  def get_name(self):
    return input("Hi there, enter your name:\n")

  def get_friendName(self, name):
    return input(f"Hi {name}, who would you like to talk to today? \n")

  def chat(self):
    while True:    
      prompt = input(f"{self.name}: ")


      if prompt == "exit":
          print("Goodbye! It was fun chatting with you.")
          break 

      print(self.friendName, ":", self.complete.complete(prompt),"\n")
