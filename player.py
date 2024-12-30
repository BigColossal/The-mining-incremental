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