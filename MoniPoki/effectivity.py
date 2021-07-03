from _types import *


def is_super_effective(atk_type: str, def_type: str, inverse=False) -> bool:
    #print(atk_type == ELECTRIC, atk_type, def_type == WATER, def_type, "WHAT")
    if inverse:
        return (is_immune(atk_type, def_type)) or (is_ineffective(atk_type, def_type))
    if atk_type == NORMAL:
        pass

    if atk_type == FIGHTING:
        if def_type in (NORMAL, ROCK, STEEL, ICE, DARK):
            return True

    if atk_type == FLYING:
        if def_type in (FIGHTING, BUG, GRASS):
            return True

    if atk_type == POISON:
        if def_type in (GRASS, FAIRY):
            return True

    if atk_type == GROUND:
        if def_type in (POISON, ROCK, STEEL, FIRE, ELECTRIC):
            return True

    if atk_type == ROCK:
        if def_type in (FLYING, BUG, FIRE, ICE):
            return True

    if atk_type == BUG:
        if def_type in (GRASS, PSYCHIC, DARK):
            return True

    if atk_type == GHOST:
        if def_type in (GHOST, PSYCHIC):
            return True

    if atk_type == STEEL:
        if def_type in (ROCK, ICE, FAIRY):
            return True

    if atk_type == FIRE:
        if def_type in (BUG, STEEL, GRASS, ICE):
            return True

    if atk_type == WATER:
        if def_type in (GROUND, ROCK, FIRE):
            return True

    if atk_type == GRASS:
        if def_type in (GROUND, ROCK, WATER):
            return True

    if atk_type == ELECTRIC:
        if def_type in (FLYING, WATER):
            return True

    if atk_type == PSYCHIC:
        if def_type in (FIGHTING, POISON):
            return True

    if atk_type == ICE:
        if def_type in (FLYING, GROUND, GRASS, DRAGON):
            return True

    if atk_type == DRAGON:
        if def_type == DRAGON:
            return True

    if atk_type == DARK:
        if def_type in (GHOST, PSYCHIC):
            return True

    if atk_type == FAIRY:
        if def_type in (FIGHTING, DRAGON, DARK):
            return True
    return False


def is_ineffective(atk_type: str, def_type: str, inverse=False) -> bool:
    #print()
    #print(atk_type == ELECTRIC, atk_type)
    #print(def_type == FIGHTING, def_type)
    #print()
    if inverse:
        return is_super_effective(atk_type, def_type)
    if atk_type == NORMAL:
        if def_type in (ROCK, STEEL):
            return True

    if atk_type == FIGHTING:
        if def_type in (BUG, PSYCHIC, FAIRY):
            return True

    if atk_type == FLYING:
        if def_type in (ROCK, STEEL, ELECTRIC):
            return True

    if atk_type == POISON:
        if def_type in (POISON, GROUND, ROCK, GHOST):
            return True

    if atk_type == GROUND:
        if def_type in (BUG, GRASS):
            return True

    if atk_type == ROCK:
        if def_type in (FIGHTING, GROUND, STEEL):
            return True

    if atk_type == BUG:
        if def_type in (FIGHTING, FLYING, POISON, GHOST, STEEL, FIRE, FAIRY):
            return True

    if atk_type == GHOST:
        if def_type == DARK:
            return True

    if atk_type == STEEL:
        if def_type in (STEEL, FIRE, WATER, ELECTRIC):
            return True

    if atk_type == FIRE:
        if def_type in (ROCK, FIRE, WATER, DRAGON):
            return True

    if atk_type == WATER:
        if def_type in (WATER, GRASS, DRAGON):
            return True

    if atk_type == GRASS:
        if def_type in (FLYING, POISON, BUG, STEEL, FIRE, GRASS, DRAGON):
            return True

    if atk_type == ELECTRIC:
        if def_type in (GRASS, ELECTRIC, DRAGON):
            return True

    if atk_type == PSYCHIC:
        if def_type in (STEEL, PSYCHIC):
            return True

    if atk_type == ICE:
        if def_type in (STEEL, FIRE, WATER, ICE):
            return True

    if atk_type == DRAGON:
        if def_type == STEEL:
            return True

    if atk_type == DARK:
        if def_type in (FIGHTING, DARK, FAIRY):
            return True

    if atk_type == FAIRY:
        if def_type in (POISON, STEEL, FIRE):
            return True
    return False


def is_immune(atk_type: str, def_type: str) -> bool:
    return (atk_type == NORMAL and def_type == GHOST) or (atk_type == FIGHTING and def_type == GHOST) or (
            atk_type == POISON and def_type == STEEL) or (atk_type == GROUND and def_type == STEEL) or (
                   atk_type == GHOST and def_type == NORMAL) or (atk_type == ELECTRIC and def_type == GROUND) or (
                   atk_type == PSYCHIC and def_type == DARK) or (atk_type == DRAGON and def_type == FAIRY)
