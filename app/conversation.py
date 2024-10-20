class Conversation:
  def __init__(self, name, friend):
    self.name = name
    self.friend = friend
    self.messages = []

  def run(self):
    while True:    
      prompt = input(f"{self.name}: ")
      self.messages.append(f"{self.name} : {prompt}")

      if prompt == "Goodbye.":
          print("Goodbye!")
          return 

      friend_response = f"{self.friend.name} : {self.friend.respond(prompt) } \n"
      self.messages.append(friend_response)
      print(friend_response ,"\n")

    