from Chat import Chat


class Chats:
    def __init__(self):
        self.chats = dict()

    def get_chat(self, id):

        if id in self.chats.keys():
            return self.chats[id]
        else:
            self.chats[id] = Chat(id)
            return self.chats[id]
