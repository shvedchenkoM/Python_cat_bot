from Cat import Cat


class battle:
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2

    # @staticmethod
    def battle(self):
        if self.cat1.murmana < self.cat2.murmana:
            return self.cat2.name
        elif self.cat1.murmana > self.cat2.murmana:
            return self.cat1.name
        else:
            return "DRAFTssssssssssss"
