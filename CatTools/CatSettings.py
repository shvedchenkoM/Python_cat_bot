import random
from CatTools.Level import Level


class CatSettings(Level):
    def __init__(self, images):
        Level.__init__(self)
        self.name = ""
        self.murmana = 0
        self.is_boy = False
        self.image_path = self.get_image(images)
        self.level = 1
        self.hunger = 0
        self.mice = 0
        self.mood = 500
        self.win = 0
        self.lose = 0
        self.health = 0

    def get_image(self, images):
        index = random.randint(1, 12)
        while images[index] == False:
            index = random.randint(1, 12)
        print(index)
        images[index] = False
        return "./Images/cat" + str(index) + ".png"

    def mood_desc(self):
        if self.mood >= 400:
            return "Волшебное"
        elif self.mood >= 300 and self.mood < 400:
            return "Нормальное"
        elif self.mood >= 200 and self.mood < 300:
            return "Пойдет, но грусно"
        elif self.mood >= 100 and self.mood < 200:
            return "Ваш котик грустит :("
        elif self.mood < 100:
            return "Ваш котик в депрессии. Срочно отправьте котика на тусу"
