from bots import Detective, Grudger, Cooperator, Cheater, Copycat, Copykitten, Random
from simulator import create_bot, count_bots, run_generation, new_generation

bots = []
bots+= create_bot(Detective,5)
bots+= create_bot(Grudger,5)
bots+= create_bot(Cooperator,5)
bots+= create_bot(Cheater,10)
bots+= create_bot(Copycat,5)
bots+= create_bot(Copykitten,5)
bots+= create_bot(Random,0)

for generation in range(0,10):
    run_generation(bots,rounds=10)
    bots = new_generation(bots,culled=5)
    print ('Bot count:',count_bots(bots))
