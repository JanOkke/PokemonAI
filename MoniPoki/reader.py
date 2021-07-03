import os


class SimplePokemon:
    def __init__(self):
        self.name = ""
        self.internal_name = ""


class SimpleMove:
    def __init__(self):
        self.name = ""


def parse(file: str, is_pokemon=False, is_move=False) -> list:
    f = open(os.getcwd() + file, "r", encoding='utf-8')
    line = 0
    data = []
    if is_move:
        for text in f:
            line += 1
            if line == 1:
                continue
            text = text.strip("\n")
            if text[0] == "#":
                continue
            else:
                new_move = SimpleMove()
                #print(text.split(","))
                dat = text.split(",")
                new_move.move_id = dat[0]
                new_move.internal_name = dat[1]
                new_move.name = dat[2]
                new_move.function_code = dat[3]
                new_move.base_power = dat[4]
                new_move.move_type = dat[5]
                new_move.category = dat[6]
                new_move.accuracy = dat[7]
                new_move.pp = dat[8]
                new_move.effect_chance = dat[9]
                new_move.target = dat[10]
                new_move.priority = dat[11]
                new_move.flags = dat[12]
                if len(dat) == 14:
                    new_move.description = dat[13]
                else:
                    new_move.description = ""
                    for _ in range(len(dat) - 13):
                        new_move.description += dat[13+_]

                data.append(new_move)
    if is_pokemon:
        new_pokemon = SimplePokemon()
        for text in f:
            line += 1
            if line == 1:
                continue
            text = text.strip("\n")
            if text[0] == "#":
                continue
            if text[0] == "[":
                if new_pokemon.name != "":
                    data.append(new_pokemon)
                dex_number = ""
                for char in text.strip("[").strip("]"):
                    dex_number += char
                new_pokemon = SimplePokemon()
                new_pokemon.species = int(dex_number)
                continue
            try:
                attr, val = text.split(" = ")
                # print(attr, val)
                if attr == 'Name':
                    new_pokemon.name = val
                if attr == 'InternalName':
                    new_pokemon.internal_name = val
                if attr == 'Type1':
                    new_pokemon.type_1 = val
                if attr == 'Type2':
                    new_pokemon.type_2 = val
                if attr == 'BaseStats':
                    new_pokemon.base_stats = val.split(",")
                if attr == "GrowthRate":
                    new_pokemon.growth_rate = val
                if attr == "BaseEXP":
                    new_pokemon.base_exp = int(val)
                if attr == "EffortPoints":
                    new_pokemon.effort_gain = val.split(",")
                if attr == "Abilities":
                    new_pokemon.abilities = val.split(",")
                if attr == "HiddenAbility":
                    new_pokemon.hidden_ability = val
                if attr == "Moves":
                    new_pokemon.lv_up_moves = val.split(",")
                if attr == "EggMoves":
                    new_pokemon.egg_moves = val.split(",")
                if attr == "Compatibility":
                    new_pokemon.compatibility = val.split(",")
                if attr == "StepsToHatch":
                    new_pokemon.egg_steps = int(val)
                if attr == "Height":
                    new_pokemon.dex_height = float(val)
                if attr == "Weight":
                    new_pokemon.dex_weight = float(val)
                if attr == "Pokedex":
                    new_pokemon.dex_entry = val
                if attr == "Evolution":
                    new_pokemon.evolution = val.split(",")
            except Exception:
                print(text)
        try:
            hidden = new_pokemon.hidden_ability
        except AttributeError:
            hidden = new_pokemon.abilities[0]
            new_pokemon.hidden_ability = hidden
            #print(new_pokemon.hidden_ability)
        data.append(new_pokemon)
    return data
