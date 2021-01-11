from bot import Bot
from random import random

class Cheater(Bot):
    def decide(self):
        return 'cheat'

class Cooperator(Bot):
    def decide(self):
        return 'cooperate'
    
class Copycat(Bot):
    def decide(self):
            return self.memory

class Copykitten(Bot):
    def secondary_reset(self):
        self.cheatCount = 0
    def decide(self):
        if self.memory == 'cheat':
            self.cheatCount+=1
        if self.cheatCount == 2:
            self.cheatCount = 0
            return 'cheat'
        elif self.cheatCount == 1:
            return self.memory
        else:
            self.cheatCount == 0
            return self.memory

class Greedy(Bot):
    def decide(self):
        if self.coins > 1:
            return 'cheat'
        else:
            return 'cooperate'

class Grudger(Bot):
    def secondary_reset(self):
        self.grudge = False
    def decide(self):
        if self.memory == 'cheat':
            self.grudge = True
        if self.grudge:
            return 'cheat'
        else: 
            return 'cooperate'

class Detective(Bot):
    def secondary_reset(self):
        self.identity = 'Copycat'
    def decide(self):
        self.round+=1
        if self.round in [1,2,3,4]: 
            if self.memory == 'cheat':
                self.identity = 'Cheater'
            if self.round == 3:
                return 'cheat'
            return 'cooperate'
        else:
            if self.identity == 'Copycat':
                return self.memory
            elif self.identity == 'Cheater':
                return 'cheat'

class Random(Bot):
     def decide(self):
         n = random()
         if n > 0.5:
             return 'cooperate'
         else:
            return 'cheat'
