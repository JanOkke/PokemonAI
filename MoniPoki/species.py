import reader

data = reader.parse(r"\PBS\pokemon.txt", is_pokemon=True)
pokemon_dictionary = {}

pokemon_id = 0
for pokemon in data:
    pokemon_id += 1
    pokemon_dictionary[pokemon.name] = pokemon_id

def get_dex_number(species_name: str) -> int:
    return pokemon_dictionary[species_name]

def growth_rate(species: int) -> str:
    return data[species - 1].growth_rate

def learn_set(species: int) -> list:
    _moves = data[species - 1].lv_up_moves
    __moves = []
    for move in _moves:
        if move.isdecimal():
            continue
        __moves.append(move)
    return __moves


def name(species: int) -> str:
    return data[species - 1].name


def dex_height(species: int) -> int:
    return data[species - 1].dex_height


def dex_weight(species: int) -> int:
    return data[species - 1].dex_weight


def ev_yield(species: int) -> list:
    return data[species - 1].effort_gain


def base_stats(species: int) -> list:
    ret = []
    #for stat in data[species - 1].base_stats:
    #    ret.append(int(stat))
    hp, attack, defense, speed, spatk, spdef = data[species - 1].base_stats
    ret.append(int(hp))
    ret.append(int(attack))
    ret.append(int(defense))
    ret.append(int(spatk))
    ret.append(int(spdef))
    ret.append(int(speed))
    return ret


def abilities(species: int) -> list:
    return data[species - 1].abilities


def hidden_ability(species: int) -> str:
    try:
        return data[species - 1].hidden_ability
    except AttributeError:
        return data[species - 1].abilities[0]


def types(species: int) -> list:
    _types = []
    _types.append(data[species - 1].type_1)
    try:
        _types.append(data[species - 1].type_2)
    except Exception:
        pass
    return _types


def moves(species: int, level: int) -> list:
    _moves = data[species - 1].lv_up_moves
    __moves = []
    for move in _moves:
        if move.isdecimal():
            move = int(move)
        __moves.append(move)
    # print(__moves)
    MOVES = []
    for index in range(len(__moves)):
        if index % 2 == 0 and __moves[index] > level:
            break
        if index % 2 == 1:
            MOVES.append(__moves[index])
    # print(MOVES)
    MOVES.reverse()
    print(MOVES)
    if len(MOVES) <= 4:
        return MOVES
    else:
        return [MOVES[0], MOVES[1], MOVES[2], MOVES[3]]


def dex_entry(species: int) -> str:
    return data[species - 1].dex_entry


