from app.bullycatcher import Bullycatcher

class Conversation:
  def __init__(self, name, friend):
    self.name = name
    self.friend = friend
    self.messages = []
    self.bullycatcher = Bullycatcher(name)

  def run(self):
    while True:    
      prompt = input(f"{self.name}: ")
      self.messages.append(f"{self.name} : {prompt}")

      if prompt == "Goodbye.":
          print("Goodbye!")
          return 

      explanation = self.bullycatcher.detect_bullying(self.messages)
      if explanation is not None:
        print("WARNING: Bullying detected in your message!")
        print(" ")
        print(explanation)
        continue
      
      friend_response = f"{self.friend.name} : {self.friend.respond(prompt) } \n"
      self.messages.append(friend_response)
      print(friend_response ,"\n")

    