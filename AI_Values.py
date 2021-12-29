from _moves import *
from battle import Battle, Move, calculate_damage
from status import NO_STATUS
from items import CHOICE_BAND, CHOICE_SPECS, CHOICE_SCARF


def can_0hko(battle: Battle, move: Move):
    if calculate_damage(battle.team1.get_first_pokemon(), battle.team2.get_first_pokemon(), move=move,
                        _terrain=battle.terrain, _weather=battle.weather, can_crit=False, rand_num=100,
                        printing=False) > battle.team2.get_first_pokemon().hp:
        return True

def can_2hko(battle: Battle, move: Move):
    if calculate_damage(battle.team1.get_first_pokemon(), battle.team2.get_first_pokemon(), move=move,
                        _terrain=battle.terrain, _weather=battle.weather, can_crit=False, rand_num=100,
                        printing=False) > battle.team2.get_first_pokemon().hp / 2:
        return True


def get_range(battle: Battle, move: Move):
    return calculate_damage(battle.team1.get_first_pokemon(), battle.team2.get_first_pokemon(), move=move,
                            _terrain=battle.terrain, _weather=battle.weather, can_crit=False, rand_num=100,
                            printing=False) / battle.team2.get_first_pokemon().hp * 100


def get_move(battle: Battle):
    _0HKO_MOVES = []
    _2HKO_MOVES = []
    RANGES = []
    user_mon = battle.team1.get_first_pokemon()
    defender_mon = battle.team2.get_first_pokemon()
    for move in user_mon.moves:
        if can_0hko(battle, move):
            _0HKO_MOVES.append(move)
        elif can_2hko(battle, move):
            _2HKO_MOVES.append(move)


    if _0HKO_MOVES != []:
        PRIORITY_LIST = []
        for move in _0HKO_MOVES:
            PRIORITY_LIST.append([move.priority, move])
        return max(PRIORITY_LIST)

    else:  # pure definition
        for move in user_mon.moves:
            if move == SWORDSDANCE and _2HKO_MOVES != []:
                for _move in _2HKO_MOVES:
                    if _move.category == PHYSICAL:
                        return move  # SWORDS DANCE
            if move in (WHIRLWIND, ROAR):
                count = 0
                for stages in defender_mon.stat_stages:
                    count += stages
                if count > 2:
                    return move  # WHIRLWIND, ROAR
            if move == SING:
                if _2HKO_MOVES == [] and defender_mon.status == NO_STATUS:
                    return move  # SING
            if move == DISABLE:
                if defender_mon.has_item(CHOICE_SPECS) or defender_mon.has_item(CHOICE_SCARF) or defender_mon.has_item(CHOICE_BAND):
                    return move  # DISABLE
            if move == MIST:
                if defender_mon.moves_cause_status_count >= 2:
                    return move


