import loader, battle

team_1 = loader.load_from_poke_paste(open(r'C:\Users\Jan-Okke\Desktop\PokemonAI\Teams\elderteam.txt', 'r', encoding='utf-8'))
team_2 = loader.load_from_poke_paste(open(r'C:\Users\Jan-Okke\Desktop\PokemonAI\Teams\falkner.txt', 'r', encoding='utf-8'))


def get_points(your_team: [loader.Pokemon], enemy_team: [loader.Pokemon], status_points=20):
    points = 0
    for pkmn in your_team:
        pkmn: loader.Pokemon
        points += pkmn.get_hp_percentage()
        if pkmn.status != battle.status.NO_STATUS:
            #print("HAS STATUS, MINUS PTS")
            points -= status_points
    for pkmn in enemy_team:
        pkmn: loader.Pokemon
        points -= pkmn.get_hp_percentage()
        if pkmn.status != battle.status.NO_STATUS:
            #print("HAS STATUS, PLUS PTS")
            points += status_points
    return points

battler_1 = team_1[0].clone()
battler_2 = team_2[0].clone()
POINT_TABLE = {}

for move in battler_1.moves:
    POINT_TABLE[move.name] = 0
    for _move in battler_2.moves:
        b1_clone = battler_1.clone()
        b2_clone = battler_2.clone()
        print(move.name, _move.name)
        b2_clone.take_damage(battle.calculate_damage(b1_clone, b2_clone, battle.weather.NO_WEATHER, battle.terrain.NO_TERRAIN, move, can_crit=False, rand_num=85, printing=False))
        b1_clone.take_damage(battle.calculate_damage(b2_clone, b1_clone, battle.weather.NO_WEATHER, battle.terrain.NO_TERRAIN, _move, can_crit=False, rand_num=85, printing=False))
        #print(b1_clone.toString())
        #print(b2_clone.toString())
        team_2[0] = b2_clone
        team_1[0] = b1_clone
        print(get_points(team_1, team_2))
        POINT_TABLE[move.name] += get_points(team_1, team_2)
POINT_TABLE = dict(sorted(POINT_TABLE.items(), key=lambda item: item[1], reverse=True))
print(POINT_TABLE)