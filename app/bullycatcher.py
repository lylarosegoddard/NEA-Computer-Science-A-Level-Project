#Bullycatcher class

#imports Complete class so the bullycatcher class can connect to the OpenAI API
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
#a prompt for the OpenAI API to detect bullying

  def __init__(self, name):
    self.name = name
    self.open_ai = Complete(self.SYSTEM_PROMPT)
#uses the Complete class to connect to the OpenAI API and carry out the SYSTEM_PROMPT

  def detect_bullying(self, messages):
    conversation_text = "\n".join(messages)
    #joins the messages together to create a conversation
    response = self.open_ai.complete(conversation_text)
    #for each message in the conversation, check if the user is bullying
    if response == "False":
        return None
    return response
    #if the user is bullying return the response