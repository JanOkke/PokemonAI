import movedata, move

lvups = open('unbound_levelup.txt', 'r')

SPECIES = {}
current_key = None

for line in lvups:
    #print(line, end='')
    if line.__contains__('LevelUpLearnset'):
        try:
            SPECIES[line.split('LevelUpMove s')[1].split('LevelUpLearnset')[0]] = {}
            current_key = line.split('LevelUpMove s')[1].split('LevelUpLearnset')[0]
        except Exception as e:
            pass
    if line.__contains__('LEVEL_UP_MOVE('):
        #print(line, end='')
        try:
            if int(line.split('(')[1].split(',')[0].replace(' ', '')) not in SPECIES[current_key].keys():
                SPECIES[current_key] [int(line.split('(')[1].split(',')[0].replace(' ', '')) ] = [line.split('MOVE_')[1].split(')')[0]]
            else:
                SPECIES[current_key][int(line.split('(')[1].split(',')[0].replace(' ', ''))].append(line.split('MOVE_')[1].split(')')[0])
        except Exception as e:
            pass

#for key in SPECIES.keys():
#    print(key, SPECIES[key])


def available_level_up_moves(species_name, level):
    available_moves = []
    if species_name not in SPECIES.keys():
        print('Incorrect species', species_name)
        return []
    data = SPECIES[species_name]
    for key in data.keys():
        if key <= level:
            for _move in data[key]:
                if movedata.get_id(_move) is None:
                    continue
                #print(movedata.get_id(_move), _move)
                _move_ = move.Move.create_new_move(None, movedata.get_id(_move))
                available_moves.append(_move_)
    return available_moves
if __name__ == '__main__':
    for m in (available_level_up_moves('Bulbasaur', 19)):
        print(m)