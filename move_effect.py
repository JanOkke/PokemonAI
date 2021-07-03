from battle import Move, Pokemon
from moves import *

def execute(attacker: Pokemon, defender: Pokemon, move: Move):
    name = move.name

    if name == MEGAHORN:
        return
    if name == ATTACKORDER:
        return
    if name == BUGBUZZ:
        if chance(10):
            defender.stat_stages[3] -= 1
    

    for movename in MOVES:
        print(movename)


execute(None, None, Move())