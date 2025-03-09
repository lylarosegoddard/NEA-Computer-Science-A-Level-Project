from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
You will evaluate the full conversation history to determine if the latest message is bullying. 
Always focus solely on the most recent message when making your determination. 
If the latest message is not bullying, return "False" without providing any explanation. 
If the latest message is bullying, return a detailed explanation of why it qualifies as bullying. 
Always consider the context of the conversation history to determine the intent behind the latest message. 
If the context indicates that the latest message is not meant as bullying, return "False" without any explanation. 
If the user has already been notified about a previous bullying comment and the latest message is not bullying, 
simply return "False" without repeating earlier warnings or explanations. 
Do not repeat notifications or explanations for comments that were already flagged as bullying in the past; 
your evaluation should focus only on the latest message. 
If the latest message reflects improvement or is unrelated to earlier bullying behavior, 
return "False" without additional commentary. 
Make sure to avoid redundancy by not revisiting previously flagged messages,
 and ensure your assessment is precise, context-sensitive, and avoids unnecessary repetition.
  """

  def __init__(self):
    self.open_ai = Complete(self.SYSTEM_PROMPT)


  def detect_bullying(self, messages):
    conversation_text = "\n".join(messages)
    response = self.open_ai.complete(conversation_text)
    if response == "False":
        return None
    return response
   
