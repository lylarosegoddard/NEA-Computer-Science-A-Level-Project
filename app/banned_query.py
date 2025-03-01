from app.models.message import Message

class BannedQuery:
    def __init__(self, user):
        self.user = user

    def banned(self):
        bullying_count = 0
        for conversation in self.user.conversations:
            bullying_count += conversation.messages.where(Message.is_bullying == True).count()
        return bullying_count >= 3