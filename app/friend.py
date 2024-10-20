from app.complete import Complete

class Friend:

  AI_FRIEND_PROMPT = """
      You are acting as a virtual friend to test bullying behaviour so get upset if I bully you.
      Otherwise act as a friend having a normal conversation.
  """

  def __init__(self, name):
    self.name = name
    self.open_ai = Complete(self.AI_FRIEND_PROMPT)

  def respond(self, message):
    return self.open_ai.complete(message)

