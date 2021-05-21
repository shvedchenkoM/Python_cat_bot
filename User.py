from Cat import Cat


class User:

    def __init__(self, name, images):
        self.name = name
        self.cat = Cat(images)


