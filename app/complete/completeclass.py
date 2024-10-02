from openai import OpenAI
import os

class Complete:
   def __init__(self, system_prompt): 
    self.system_prompt = system_prompt
    self.client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
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
    return chat_completion.choices[0].message.content
