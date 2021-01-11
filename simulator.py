from random import random
import itertools

def run_round(bot1,bot2):
    """Takes 2 bots and subjects them to a match"""
    if bot1.decide() == 'cooperate' and bot2.decide() == 'cooperate':
        bot1.coins+=2
        bot2.coins+=2
        bot1.memory = 'cooperate'
        bot2.memory = 'cooperate'
    elif bot1.decide() == 'cheat' and bot2.decide() == 'cooperate':
        bot1.coins+=3
        if bot2.coins > 0:
            bot2.coins-=1
        bot1.memory = 'cooperate'
        bot2.memory = 'cheat'
    elif bot1.decide() == 'cooperate' and bot2.decide() == 'cheat':
        if bot1.coins > 0:
            bot1.coins-=1
        bot2.coins+=3
        bot1.memory = 'cheat'
        bot2.memory = 'cooperate'
    elif bot1.decide() == 'cheat' and bot2.decide() == 'cheat':
        bot1.memory = 'cheat'
        bot2.memory = 'cheat'

def report_game(bot1,bot2):
    """Reports winner of game after rounds"""
    if bot1.coins > bot2.coins:
        return f"In match between {bot1} and {bot2}, {bot1} wins by {bot1.coins-bot2.coins}!"
    elif bot2.coins > bot1.coins:
        return f"In match between {bot1} and {bot2}, {bot2} wins by {bot2.coins-bot1.coins}!"
    else:
        return f"In match between {bot1} and {bot2}, its a tie! (Coins increased by {bot1.coins})"

def run_game(bot1,bot2,rounds):
    """Takes 2 bots and subjects them to n rounds, declare winner after each game"""
    bot1.reset()
    bot2.reset()
    for round in range(1,rounds+1):
        run_round(bot1,bot2)
    bot1.bank+=bot1.coins
    bot2.bank+=bot2.coins
    return report_game(bot1,bot2)

def run_generation(bots, rounds, track = False):
    """Run generation of games with n rounds each"""
    bot_pairs = list(itertools.combinations(bots, 2))

    for bot1, bot2 in bot_pairs:
        result = run_game (bot1, bot2, rounds=rounds)
        if track:
            print (result)
    print (rank_bots(bots))
    return bots

def create_bot(bot,n=1):
    """Create n bots and return as list"""
    return [bot() for i in range(1,n+1)]

def rank_bots(bots):
    """Rank bots based on amount of coins"""
    return sorted(bots, key=lambda x: x.bank, reverse = True)

def count_bots(bots):
    """Count bots in list, return dictionary """
    registry = {}
    for bot in bots:
        if type(bot).__name__ in registry:
            registry[type(bot).__name__]+= 1
        else:
            registry[type(bot).__name__] = 1
    return registry

def new_generation(bots,culled=5):
    """Create new generation of bots by removing bottom ranked and populating top ranked"""
    if culled != 0:
        bots = rank_bots(bots)
        top_bots = bots[:culled]
        middle_bots = bots[culled:-culled]
        bottom_bots = bots[-culled:]
        new_bots = [bot.spawn() for bot in top_bots]
        print ('Bots joing next generation: ',new_bots)
        bots =  top_bots + middle_bots + new_bots
    return bots


