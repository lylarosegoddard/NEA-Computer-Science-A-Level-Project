#ConversationRunner class

from app.bullycatcher import Bullycatcher
from app.friend import Friend
from app.models.base_model import BaseModel
from app.models.conversation import Conversation
from app.models.message import Message

class ConversationRunner(BaseModel):
  def __init__(self, user, friend):
    self.user = user
    self.friend = friend
    self.messages = []
    self.bullycatcher = Bullycatcher(user.name)
    self.conversation = None
    

  def start_conversation(self, user):
    self.conversation = Conversation.create(user = user)

  def run(self):
    #this is the main loop that runs the conversation
    while True:    
      user_message = input(f"{self.user.name}: ")
      formatted_message = f"{self.user.name} : {user_message}" #string formatting
      self.messages.append(formatted_message)
      #formats the message so it is in the correct format for the database

      if user_message.lower() == "goodbye":
          print("Goodbye!")
          return 
        #allows user to quit during the friend and user conversation 

      explanation = self.bullycatcher.detect_bullying(self.messages)
      if explanation is not None: #Bullycatcher returns None if the message is not bullying and an explanation if it is
        print("WARNING: Bullying detected in your message!")
        print("\n\n" + explanation)
        #prints out the warning message along with the explanation if the users message was bullying
        self.save_message(formatted_message, explanation)
        #formatted so it is in the correct format for the Message table in the database
        continue

      
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
  #saves the message to the database using the Message class


    