from battle import Pokemon, Move, Trainer
from species import get_dex_number
from items import get_item
from nature import get_nature
from movedata import get_id
from os import getcwd

def load_from_poke_paste(file):
    pokemons = []
    new_pokemon = Pokemon()
    lines = 0
    MUST_CREATE_NEW = False
    for line in file:
        lines += 1
        line = line.strip("\n")
        if lines == 1 or MUST_CREATE_NEW:
            new_pokemon = Pokemon.create_new_pokemon(get_dex_number(line.split(" @ ")[0]), 100)
            MUST_CREATE_NEW = False
        if line.__contains__('@'):
            new_pokemon.set_item(get_item(line.split("@ ")[1]))
        if line.__contains__('Ability:'):
            new_pokemon.debug_ability_set(line.split('Ability: ')[1])
        if line.__contains__('Level:'):
            new_pokemon.set_level(int(line.split('Level: ')[1]))
        if line.__contains__('Nature'):
            new_pokemon.set_nature(get_nature(line.split(' Nature')[0]))
        new_pokemon.ivs = [31,31,31,31,31,31]
        new_pokemon.evs = [0,0,0,0,0,0]
        if line.__contains__('- '):
            try:
                new_pokemon.moves.append(Move.create_new_move(None, get_id(line.split('- ')[1])))
            except TypeError:
                print("Error", line)
        if line == "":
            new_pokemon.calc_stats()
            pokemons.append(new_pokemon)
            MUST_CREATE_NEW = True
    if not MUST_CREATE_NEW:
        new_pokemon.calc_stats()
        pokemons.append(new_pokemon)
    return pokemons
if __name__ == '__main__':
    mons = (load_from_poke_paste(open(r'C:\Users\Jan-Okke\Desktop\PokemonAI\Teams\elderteam.txt', 'r', encoding='utf-8')))
    for mon in mons:
        print(mon.get_species_name(), mon.get_move_list(), mon.level, mon.nature, mon.get_ability(), mon.item)