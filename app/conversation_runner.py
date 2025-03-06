#ConversationRunner class

from app.bullycatcher import Bullycatcher
#imports Bullycatcher class to determine if message is bullying
from app.friend import Friend
#imports Friend class to create a virtual friend
from app.models.base_model import BaseModel
#inherits from BaseModel class
from app.models.conversation import Conversation
#imports Conversation class to create a conversation
from app.models.message import Message
#imports Message class to create a message

class ConversationRunner(BaseModel):
  def __init__(self, user, friend):
    self.user = user
    self.friend = friend
    self.messages = []
    self.bullycatcher = Bullycatcher(user.name)
    self.conversation = None
    

  def start_conversation(self, user):
    self.conversation = Conversation.create(user = user)
    #starts the conversation with the user

  def run(self):
    while True:    
      user_message = input(f"{self.user.name}: ")
      formatted_message = f"{self.user.name} : {user_message}"
      self.messages.append(formatted_message)
      #formats the message so it is in the correct format for the database

      if user_message.lower() == "goodbye":
          print("Goodbye!")
          return 
        #allows user to quit during the friend and user conversation 

      explanation = self.bullycatcher.detect_bullying(self.messages)
      if explanation is not None:
        print("WARNING: Bullying detected in your message!")
        print("\n\n" + explanation)
        self.save_message(formatted_message, explanation)
        continue
        #prints out the warning message along with the explanation if the users message was bullying
        #formatted so it is in the correct format for the Message table in the database
      
      self.save_message(formatted_message)
      #if not bullying message then message still gets saved
      
      friend_response = f"{self.friend.name} : {self.friend.respond(user_message) } \n\n"
      self.messages.append(friend_response)
      print(friend_response ,"\n\n")
      #prints the friend response to the users message

      self.save_message(friend_response)
      #saves the friend response to the database
      #no need for the if statement of whether it is bullying or not because the friend is the OpenAI API responding which would never bully 

  def save_message(self, message, explanation = None):
    if self.conversation is not None:
      Message.create(
        message = message,
        explanation = explanation,
        is_bullying = explanation is not None,
        conversation = self.conversation
      )
  #saves the message to the database


    