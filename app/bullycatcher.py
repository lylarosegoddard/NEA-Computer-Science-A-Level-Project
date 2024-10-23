from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
     You will be detecting if latest message in the conversation is bullying or not.
     You will be given the full conversation history. 
     Return "False" if you dont detect bullying. 
     If you do detect bullying return a detailed explanation of why this is bullying.
     Make sure to only check the last message, the user has already been notified so do not tell them again if they arent still bullying.
     If the user is not bullying anymore after saying something bullying  ONLY return "False" and DONT return an explanation
  """

  def __init__(self, name):
    self.name = name
    self.open_ai = Complete(self.SYSTEM_PROMPT)


  def detect_bullying(self, messages):
    conversation_text = "\n".join(messages)
    response = self.open_ai.complete(conversation_text)
    if response == "False":
        return None
    return response
   
