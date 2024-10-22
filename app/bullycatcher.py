from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
     You will be detecting if messages are bullying or not.
     You will be given the full conversation history. 
     Return "False" if you dont detect bullying. 
     If you do detect bullying return a detailed explanation of why this is bullying.
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
   
#need two functions one that is binary is it bullying or not and the other will be the explanation