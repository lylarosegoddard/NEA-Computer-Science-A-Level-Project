#Complete class

import os
from openai import OpenAI

class Complete:
   def __init__(self, system_prompt): #utilising OpenAI API
    self.system_prompt = system_prompt #injecting the system prompt for reuseability
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
    #formats the message how OpenAI wants them and gets the response
    return chat_completion.choices[0].message.content
    #pulling the message from the object structure returned by OpenAI