class Bot (object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.round = 0
        self.coins = 0
        self.bank = 0
        self.memory = 'cooperate'
        self.secondary_reset()
        return self

    def secondary_reset(self):
        pass

    @classmethod
    def spawn(cls):
        "Return new copy of self"
        return cls()

    def __repr__(self):
        return f"{type(self).__name__}({self.bank})"
