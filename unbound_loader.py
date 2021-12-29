import loader
import unbound_reader
import _pokemon
import battle
import weather
import terrain
import growth
import datetime

def percentage(target_hp, damage):
    return round(damage / target_hp * 100 - 0.499)

LEVEL_CAP = 20
ENEMY_TEAM = 'Teams\\bugsy.txt'
WEATHER = weather.NO_WEATHER
TERRAIN = terrain.NO_TERRAIN

LEGENDARY_POKEMON = ['Articuno','Zapdos','Moltres','Mewtwo','Entei','Suicune','Raikou','Ho-Oh','Lugia','Regice','Registeel','Regirock','Latias','Latios','Kyogre','Groudon','Rayquaza','Deoxys','Uxie',
'Mesprit','Azelf','Palkia','Dialga','Giratina','Cresselia','Darkrai','Heatran','Regigigas','Cobalion','Terrakion','Virizion','Tornadus','Thundurus','Landorus','Zekrom','Reshiram',
'Kyurem','Xerneas','Yveltal','Zygarde','Tapu Koko','Tapu Lele','Tapu Bulu','Tapu Fini','Solgaleo','Lunala','Necrozma','Zacian','Zamazenta','Eternatus','Kubfu','Urshifu','Regieleki',
'Regidrago','Glastrier','Spectrier','Calyrex','Mew','Celebi','Jirachi','Manaphy','Phione','Shaymin','Arceus','Victini','Keldeo','Meloetta','Genesect','Diancie','Hoopa','Volcanion',
'Magearna','Marshadow','Zeraora','Meltan','Melmetal','Zarude']



enemies = (loader.load_from_poke_paste(open(ENEMY_TEAM)))
Calcs = []
print("Started Calculations - ", datetime.datetime.now())
for enemy in enemies:
    enemy.calc_stats()
    #print(enemy.get_species_name(),enemy.hp,enemy.attack,enemy.defense,enemy.sp_atk,enemy.sp_def,enemy.speed, enemy.level)
    for pokemon in _pokemon.ALL_POKEMON:
        if pokemon.get_species_name() in LEGENDARY_POKEMON:
            continue
        pokemon.growth_rate = growth.MEDIUM_SLOW # DEBUG
        pokemon.set_level(LEVEL_CAP)
        pokemon.heal()
        pokemon.calc_stats()
        #print(pokemon.get_species_name(),pokemon.hp,pokemon.attack,pokemon.defense,pokemon.sp_atk,pokemon.sp_def,pokemon.speed, pokemon.level)
        available_moves = unbound_reader.available_level_up_moves(pokemon.get_species_name(), LEVEL_CAP)
        for move in available_moves:
            dmg = battle.calculate_damage(pokemon, enemy, WEATHER, TERRAIN, move, can_crit=False, printing=False)
            if percentage(enemy.total_hp, dmg) < 30:
                continue
            Calcs.append([percentage(enemy.total_hp, dmg), '{1} (Lv {4}) did {0}/{6} ({7}%) damage to {2} (Lv {5}) with move {3}'.format(dmg, pokemon.get_species_name(), enemy.get_species_name(), move.name, LEVEL_CAP, enemy.level, enemy.total_hp, percentage(enemy.total_hp, dmg))])
print("Finished Calculations - ", datetime.datetime.now())
Calcs.sort(reverse=True)
for calc in Calcs:
    print(calc[1])