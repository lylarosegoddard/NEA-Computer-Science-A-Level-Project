from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
      
  """

  def __init__(self, name):
    self.name = name
    self.open_ai = Complete(self.SYSTEM_PROMPT)

  def respond(self, messages):
    conversation_text = "\n".join(messages)
    return self.open_ai.complete(conversation_text)

