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
    while True:    
      user_message = input(f"{self.user.name}: ")
      self.messages.append(f"{self.user.name} : {user_message}")

      if user_message == "Goodbye.":
          print("Goodbye!")
          return 

      explanation = self.bullycatcher.detect_bullying(self.messages)
      if explanation is not None:
        print("WARNING: Bullying detected in your message!")
        print(explanation)
        self.save_message(self.user.name, explanation)
        continue
      
      self.save_message(user_message)
      
      friend_response = f"{self.friend.name} : {self.friend.respond(user_message) } \n"
      self.messages.append(friend_response)
      print(friend_response ,"\n")

      self.save_message(friend_response)

  def save_message(self, message, explanation = None):
    print("Saving message...")
    print("Message: ", message)
    print("Explanation: ", explanation)
    print("Is bullying: ", explanation is not None)
    if self.conversation is not None:
      Message.create(
        message = message,
        explanation = explanation,
        is_bullying = explanation is not None,
        conversation = self.conversation
      )
  


    