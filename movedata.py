import reader

data = reader.parse(r"\PBS\Moves.txt", is_move=True)


def total_pp(move_id: int) -> int:
    return int(data[move_id - 1].pp)


def internal_name(move_id: int) -> str:
    return data[move_id - 1].internal_name


def name(move_id: int) -> str:
    return data[move_id - 1].name


def function_code(move_id: int) -> int:
    return data[move_id - 1].function_code


def damage(move_id: int) -> int:
    return int(data[move_id - 1].base_power)


def move_type(move_id: int) -> str:
    return data[move_id - 1].move_type


def category(move_id: int) -> str:
    return data[move_id - 1].category


def accuracy(move_id: int) -> int:
    return int(data[move_id - 1].accuracy)


def effect_chance(move_id: int) -> int:
    return int(data[move_id - 1].effect_chance)


def target(move_id: int) -> int:
    return data[move_id - 1].target


def priority(move_id: int) -> int:
    return int(data[move_id - 1].priority)


def flags(move_id: int) -> list:
    return data[move_id - 1].flags


def get_id(name: str) -> int:
    for move in data:
        if move.name == name:
            return int(move.move_id)

#print(function_code(get_id("Fire Punch")))