from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
     #system prompt enginnering on openai playground 
  """

  def __init__(self, name):
    self.name = name
    self.open_ai = Complete(self.SYSTEM_PROMPT)

  def respond(self, messages):
    conversation_text = "\n".join(messages)
    return self.open_ai.complete(conversation_text)

#need two functions one that is binary is it bullying or not and the other will be the explanation