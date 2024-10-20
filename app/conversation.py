class Conversation:
  def __init__(self, name, friend):
    self.name = name
    self.friend = friend

  def run(self):
    while True:    
      prompt = input(f"{self.name}: ")


      if prompt == "Goodbye.":
          print("Goodbye!")
          return 

      print(self.friend.name, ":", self.friend.respond(prompt),"\n")

