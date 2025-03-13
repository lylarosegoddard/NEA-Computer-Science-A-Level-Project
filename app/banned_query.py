#BannedQuery class

from app.models.message import Message

class BannedQuery:
    def __init__(self, user):
        self.user = user

    def banned(self):
        bullying_count = 0
        #sets bullying count to 0
        for conversation in self.user.conversations: #for loops and cross-table queries
            bullying_count += conversation.messages.where(Message.is_bullying == True).count() 
        return bullying_count >= 3
        
        #this is using peewee to execute a joined query the SQL will look like: 
        # SELECT COUNT(*) 
        # FROM message 
        # JOIN conversation ON message.conversation_id = conversation.id
        # JOIN user ON conversation.user_id = user.id
        # WHERE message.is_bullying = 1 
        # AND user.id = {self.user.id}
        