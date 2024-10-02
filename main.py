from app.friend.friendclass import Friend

name = input("Hi there, enter your name:\n")
friendName = input(f"Hi {name}, who would you like to talk to today? \n")
print("\n\n")

friend = Friend(friendName)

while True:    
    prompt = input(f"{name}: ")


    if prompt == "exit":
        print("Goodbye!")
        break 

    print(friendName, ":", friend.respond(prompt),"\n")