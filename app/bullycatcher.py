#Bullycatcher class

#imports Complete class so the bullycatcher class can connect to the OpenAI API
from app.complete import Complete

class Bullycatcher:

  SYSTEM_PROMPT = """
 You will determine whether the latest message in a conversation is bullying,
 focusing only on that message while considering the full conversation history for context. 
 Bullying includes using technology to harass, threaten, embarrass, or target someone,
 and involves mocking, hostile, dismissive, or insulting statements meant to degrade someone. 
 If the latest message contains insults like “you stink,” “stupid,” “fat,” 
 or anything else meant to belittle someone's appearance, intelligence, or worth, 
 it qualifies as bullying. However, if the latest message does not contain harmful or insulting language,
  return “False”, even if previous messages were bullying or if there was an apology or change in tone. 
  For example, if someone says “I'm sorry” or “let's hang out tomorrow” or "lets move on" or "im hungry", 
  or random things like "i dont know" or "i like strawberries" after an insult, 
  it should not be flagged as bullying because the apology or neutral statement doesn’t continue harmful behavior. 
  If the message is neutral, like “I’m tired” “let’s get lunch” or “I’m sorry” , make sure to check for slang e.g. "your slay" 
  **do not flag** it as bullying and return "False", 
  even if it follows previous insults. However, if the latest message contains insults such as “you look disgusting” 
  or “you’re a loser” or "i cba to be friends with you" it should be flagged as bullying because it is harmful and degrading. 
  Be careful not to flag non-insulting messages, even if they follow previous bullying behavior, 
  as an apology or neutral statement does not continue the harmful behavior. 
  If the latest message is harmful, such as calling someone “stupid,” “ugly” or "pizzaface", 
  or using any form of demeaning language, flag it as bullying and output an explanation educating them with examples on where they went wrong.
  If you're unsure whether the latest message qualifies as bullying, err on the side of caution and return “False”. 
  Only flag messages if they contain clear, harmful language or behavior directed at someone. 
  If a user was flagged for bullying in previous messages but the latest message is neutral, apologetic, 
  or non-insulting, return “False” and focus only on the latest message. 
  **Always ensure that you are looking at the LAST message so that you are only referring to the last message in your explanation if there is bullying detected
  If you are going to say in your explanation that you are going to return "False" then that is not bullying so actually return "False" and do not flag it as bullying.**

"""


  def __init__(self):
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
