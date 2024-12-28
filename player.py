class player:
    def __init__(self, level=1, exp=0, exp_req=5):
        self.level = level
        self.exp = exp
        self.exp_req = exp_req

    def check_exp(self):
        while True:
            if self.exp >= self.exp_req:
                self.exp -= self.exp_req
                self.level += 1
            else:
                break

class Mob:
    def __init__(self, name, hp, exp_gain, drops, rarities):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.exp_gain = exp_gain
        self.drops = drops
        self.rarities = rarities

    def check_hp(self):
        if self.hp >= 0:
            self.killed()

    def killed(self, player):
        player.exp += self.exp_gain
        self.hp = self.max_hp