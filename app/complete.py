#Complete class

import os
#utilising the OpenAI library by importing
from openai import OpenAI

class Complete:
   def __init__(self, system_prompt): 
    self.system_prompt = system_prompt
    self.client = OpenAI(
    #creates a client for interacting with OpenAI's API
        api_key=os.environ.get("OPENAI_API_KEY"),
        #sets the API key to authenticate with OpenAI
    )
    


   def complete(self, message):   
    chat_completion = self.client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-4o-mini",
    )
    #gives the user message and gets the response from OpenAI's API in the format above using the 4o model
    return chat_completion.choices[0].message.content
    #returns the response from OpenAI's API