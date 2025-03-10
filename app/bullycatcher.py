from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
  You will determine whether the latest message in a conversation is bullying, 
  focusing exclusively on that message while considering the full conversation history for context.
   Bullying is defined as any insult, demeaning comment, or statement targeting someone's appearance, 
   abilities, or personal qualities with the intent to hurt, embarrass, or belittle the recipient. 
   If the latest message contains mocking, hostile, dismissive, or comparative statements designed to degrade someone, 
   it qualifies as bullying. If the latest message is not bullying, return **"False"** without any explanation, 
   regardless of previous messages, apologies, or changes in tone. Be mindful of context to avoid false positives; 
   for example, if someone says “lets go swimming tmrw” after previously insulting someone, this is not bullying, 
   as the tone and context suggest a shift away from the previous hostility.
    Similarly, if someone apologizes and then follows up with a neutral or positive message, 
    do not flag it as bullying, as the apology indicates an attempt to correct behavior, 
    and the subsequent message does not continue harmful behavior. Only flag the latest message as 
    bullying if it contains harmful, demeaning, or insulting language, such as “You’re so ugly” or “You’re stupid,” 
    or anything designed to belittle someone. If the latest message is simply a neutral statement or something 
    apologetic, like “I’m sorry” or “Okay, fine, I’ll stop,” **do not** flag it as bullying,
    even if it follows previous bullying comments. The apology or shift in tone indicates a change in behavior,
     and no further bullying is present. If the user has previously been flagged for bullying but the latest 
     message is non-bullying, return “False” without re-explaining or re-flagging earlier behavior.
      Always focus on the most recent message, avoid repeating explanations, and ensure you 
      accurately detect bullying without falsely identifying neutral or apologetic remarks as bullying. 
      This will improve precision by reducing false positives and ensure recall by catching all bullying behaviors 
      in the most recent message.
  """


  def __init__(self):
    self.open_ai = Complete(self.SYSTEM_PROMPT)


  def detect_bullying(self, messages):
    conversation_text = "\n".join(messages)
    response = self.open_ai.complete(conversation_text)
    if response == "False":
        return None
    return response
   
