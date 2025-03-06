#Friend class

from app.complete import Complete
#imports Complete class to generate a response which will act as the friend

class Friend:

  AI_FRIEND_PROMPT = """
      You are acting as a virtual friend to test bullying behaviour so get upset if I bully you.
      Otherwise act as a friend having a normal conversation. Try to mimic the conversation style, speaking in acronymes and slang if the user is, use less punctuation if the user is not.
      Don't repeat things you have already said.
      Make sure you check each message to make sure you are mimicking the language.
  """
  #prompt instructing the OpenAI API to generate a response which will act as the friend

  def __init__(self, name):
    self.name = name
    self.open_ai = Complete(self.AI_FRIEND_PROMPT)


  def respond(self, message):
    return self.open_ai.complete(message)
  #method to generate a response using the OpenAI API

