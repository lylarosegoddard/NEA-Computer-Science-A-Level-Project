#BannedQuery class

#imports from message to get all messages from a user's conversations
from app.models.message import Message

class BannedQuery:
    def __init__(self, user):
        self.user = user

    def banned(self):
        bullying_count = 0
        #sets bullying count to 0
        for conversation in self.user.conversations:
            bullying_count += conversation.messages.where(Message.is_bullying == True).count()
        return bullying_count >= 3
        #loops through each message in a users conversations and if the message is bullying, meaning the is_bullying field
        #is 1 then the bullying count is incremented by 1