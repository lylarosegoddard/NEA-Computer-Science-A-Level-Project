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

prompt = input("Hi there, enter your prompt: ")
print("user:", prompt)
reponse = print("\n","friend:", complete(prompt))
