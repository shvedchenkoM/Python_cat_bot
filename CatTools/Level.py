class Level:
    def __init__(self):
        self.level = 1
        self.level_increase = (50 * self.level) // 2
        self.mana_level_increase = self.level
        self.mice_level_increase = self.level_increase // 2
        self.max_mana_value = self.level_increase
        self.max_hunger = 10

    def update_level(self):
        self.level += 1
        self.level_increase = 50 * self.level // 2
        self.mana_level_increase = self.level
        self.max_mana_value += self.level_increase
        self.max_hunger += 1
