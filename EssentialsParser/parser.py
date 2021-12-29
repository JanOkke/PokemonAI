from loader import load_from_poke_paste


def load(file, trainer_type: str, trainer_name: str, trainer_id: int=None, lose_text: str="I lost."):
    team = load_from_poke_paste(open(file))
    ret = ""
    ret += "#-------------------------------\n"
    ret += "[" + trainer_type.upper() + "," + trainer_name.capitalize()
    if trainer_id is not None:
        ret += "," + str(trainer_id)
    ret += "]\n"
    ret += 'LoseText = "' + lose_text + '"\n'
    for mon in team:
        ret += "Pokemon = " + str(mon.get_species_name()).upper() + "," + str(mon.level) + "\n"
        ret += "\tMoves = "
        for move in mon.moves:
            ret += move.internal_name.upper() + ","
        ret = ret[:-1]
        ret += "\n"
        if mon.is_holding_item():
            ret += "\tItem = " + mon.item.upper().replace('_', '') + "\n"
        ability = mon.get_ability()
        ability_list = mon.get_ability_list()
        _index = 0
        if ability.upper().replace(' ', '') == mon.hidden_ability:
            _index = 2
        else:
            index = 0
            for ab in ability_list:
                if ability.upper().replace(' ', '') == ab:
                    _index = index
                index += 1
        #print(_index)
        ret += "\tAbility = " + str(_index) + "\n"
        ret += "# " + ability + "\n"
        ret += "\tIV = 31\n"
        ret += "\tNature = " + mon.nature.upper() + "\n"
        for move in mon.moves:
            if move.name == "Return":
                ret += "\tHappiness = 255\n"
    return ret

if __name__ == '__main__':
    print(load(r'C:\Users\Jan-Okke\Desktop\PokemonAI\Teams\morty.txt', 'LEADER_Bugsy', 'Bugsy',
               lose_text="Good job! Take this Badge as symbol for your victory."))
