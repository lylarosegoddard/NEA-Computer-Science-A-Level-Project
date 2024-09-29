import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

AI_FRIEND_PROMPT = """
You are acting as a virtual friend to test bullying behaviour so get upset if I bully you.
Otherwise act as a friend having a normal conversation.
"""

def complete(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": AI_FRIEND_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
    )
    return chat_completion.choices[0].message.content
    
name = input("Hi there, enter your name:\n")
friendName = input(f"Hi {name}, who would you like to talk to today? \n")


while True:    
    prompt = input(f"{name}: ")
    

    if prompt == "exit":
        print("Goodbye!")
        break 
        
    print(friendName, ":", complete(prompt),"\n")
     