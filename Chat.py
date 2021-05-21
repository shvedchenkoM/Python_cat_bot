from User import User
from Battle.battle import battle


class Chat:

    def __init__(self, id):
        self.id = id
        self.users = dict()
        self.images = dict()
        for i in range(1, 13):
            self.images[i] = True
        self.battle = None


    def set_cat_name(self, id, cat_name, name):
        if self.is_user_log_in(id):
            return False
        else:
            self.users[id] = User(name, self.images)
            self.users[id].cat.name = cat_name
        return True

    def is_user_log_in(self, id):
        return id in self.users.keys()
