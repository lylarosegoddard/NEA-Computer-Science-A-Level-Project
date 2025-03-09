from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
     You will be detecting if latest message in the conversation is bullying or not.
     You will be given the full conversation history. 
     Return "False" if you dont detect bullying. 
     If you do detect bullying return a detailed explanation of why this is bullying.
     Make sure to only check the last message, the user has already been notified so do not tell them again if they arent still bullying.
     If the user is not bullying anymore after saying something bullying  ONLY return "False" and DONT return an explanation.
     Make sure to consider the messages before as the context may rule out the comment being meant in a bullying way. If you sense that the context does rule out the comment as bullying 
     then please ONLY return "False" and DONT return an explanation.
     Try not to repeat the same message twice.
     Make sure to understand that after a user has said something bullying you should not tell them again and aim to instead move on from that original comment by returning "False" at 
     other non-bullying comments without giving an explanation.
  """

  def __init__(self):
    self.open_ai = Complete(self.SYSTEM_PROMPT)


  def detect_bullying(self, messages):
    conversation_text = "\n".join(messages)
    response = self.open_ai.complete(conversation_text)
    if response == "False":
        return None
    return response
   
