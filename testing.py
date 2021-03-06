import battle, movedata, species
"""
MEW = battle.Pokemon.create_new_pokemon(151, 50)
GENGAR = battle.Pokemon.create_new_pokemon(94, 50)
BLISSEY = battle.Pokemon.create_new_pokemon(242, 50)
IRON_HEAD = battle.Move.create_new_move(None, movedata.get_id("Iron Head"))
SHADOW_BALL = battle.Move.create_new_move(None, movedata.get_id("Shadow Ball"))
SUPERFANG = battle.Move()
SUPERFANG.name = battle.moves.SUPERFANG
GENGAR.ivs = [31,31,31,31,31,31]
GENGAR.evs = [0,0,0,252,0,252]
BLISSEY.ivs = [31,31,31,31,31,31]
BLISSEY.evs = [252,0,0,0,252,0]
#GENGAR.give_item(battle.items.CHOICE_SPECS)
#BLISSEY.evs = [252,0,252,252,252,0]
BLISSEY.give_item(battle.items.LIFE_ORB)
GENGAR.calc_stats()
BLISSEY.calc_stats()
#BLISSEY.hp = BLISSEY.total_hp
#BLISSEY.calc_hp()
#GENGAR.give_item(battle.items.METRONOME)
dmg = 0
n = 0
print(BLISSEY.hp, "BLISSEY", GENGAR.hp, "Gengar")
while not (GENGAR.is_fainted() or BLISSEY.is_fainted()):
    n += 1
    dmg = battle.calculate_damage(GENGAR, BLISSEY, battle.terrain.NO_TERRAIN, battle.weather.NO_WEATHER, move=SHADOW_BALL)
    BLISSEY.take_damage(dmg)
    if BLISSEY.is_fainted():
        print(BLISSEY.hp, "BLISSEY", GENGAR.hp, "Gengar")
        break
    dmg = battle.calculate_damage(BLISSEY, GENGAR, battle.terrain.NO_TERRAIN, battle.weather.NO_WEATHER, move=IRON_HEAD)
    GENGAR.take_damage(dmg)
    print(BLISSEY.hp, "BLISSEY", GENGAR.hp, "Gengar")
"""

def percentage(target_hp, damage):
    return round(damage / target_hp * 100 - 0.499)
"""
from moves_base import *
from items import *

import Debug.debugger as debugger

DEFENDERLIST = []

FILELIST = ['lorelei1', 'lorelei2', 'bruno1', 'bruno2', 'agatha1', 'agatha2', 'lance1', 'lance2', 'champion']

for files in FILELIST:
    mons = debugger.run(open('Debug\\' + files + '.txt'))
    for mon in mons:
        #print(mon.species)
        evs = mon.evs.split("/")
        hpev = 0
        atkev = 0
        defev = 0
        spatkev = 0
        spdefev = 0
        speedev = 0
        for ev in evs:
            if ev.__contains__('HP'):
                hpev = int(ev.strip(" HP"))
            if ev.__contains__('Atk'):
                atkev = int(ev.strip(" Atk"))
            if ev.__contains__('Def'):
                defev = int(ev.strip(" Def"))
            if ev.__contains__('SpA'):
                spatkev = int(ev.strip(" SpA"))
            if ev.__contains__('SpD'):
                spdefev = int(ev.strip(" SpD"))
            if ev.__contains__('Spe'):
                speedev = int(ev.strip(" Spe"))
        EVS = [hpev, atkev, defev, spatkev, spdefev, speedev]
        #print(mon.evs, EVS)
        mon.evs = EVS
        DEFENDERLIST.append(mon)

attacker = 'Barraskewda'
#defender = 'Poliwrath'
level = 86
#vlevel = 84
evs = [6,252,0,0,0,252]
#vevs = [252, 252, 0, 252, 0, 252]
item = CHOICE_BAND
#ditem = DAMP_ROCK

# ===================
# Calculations
# ===================

movesatt = [LIQUIDATION, EARTHQUAKE, THUNDERPUNCH, POISONJAB, BRICKBREAK, CRUNCH]
ATTACKER = battle.Pokemon.create_new_pokemon(species.get_dex_number(attacker), level)
ATTACKER.evs = evs
ATTACKER.ivs = [31,31,31,31,31,31]
ATTACKER.item = item
ATTACKER.moves = []
for m in movesatt:
    ATTACKER.moves.append(m)
ATTACKER.calc_stats()
#ATTACKER.make_ability_hidden()
#print(ATTACKER.get_ability())
print("Stats", ATTACKER.get_species_name(), '@', item, 'Ability:', ATTACKER.get_ability())
print(ATTACKER.hp, ATTACKER.attack, ATTACKER.defense, ATTACKER.sp_atk, ATTACKER.sp_def, ATTACKER.speed)
for d in DEFENDERLIST:
    can = False
    try:
        defender = d.species
        vlevel = int(d.level)
        #ditem = d.item
        vevs = d.evs

    # ===================
    # Settings
    # ===================

        DEFENDER = battle.Pokemon.create_new_pokemon(species.get_dex_number(defender), vlevel)
        can = True
    except KeyError:
        #print("Couldn't calculate species", d.species)
        continue
    if can:
        DEFENDER.evs = vevs
        DEFENDER.ivs = [31,31,31,31,31,31]
        dmoves = []
        for _move in d.moves:
            #print(_move, DEFENDER.get_species_name())
            try:
                dmoves.append(battle.Move.create_new_move(None, movedata.get_id(_move)))
            except Exception as e:
                pass
                #print(e, _move)
        DEFENDER.set_moves(dmoves)
        #DEFENDER.item = ditem
        DEFENDER.calc_stats()
        #print(" Stats", DEFENDER.get_species_name(), "\n", DEFENDER.hp, DEFENDER.attack, DEFENDER.defense, DEFENDER.sp_atk, DEFENDER.sp_def, DEFENDER.speed)
        #print('\n')
        OUTCOMS = []
        OUTCOMSB = []

        if DEFENDER.speed > ATTACKER.speed:
            slower = True

            for ___move in DEFENDER.moves:
                min_roll = battle.calculate_damage(DEFENDER, ATTACKER, battle.weather.RAIN, battle.terrain.NO_TERRAIN,
                                                   move=___move, rand_num=85, can_crit=False, printing=False)
                max_roll = battle.calculate_damage(DEFENDER, ATTACKER, battle.weather.RAIN, battle.terrain.NO_TERRAIN,
                                                   move=___move, rand_num=100, can_crit=False, printing=False)
                #if percentage(DEFENDER.hp, min_roll) > 90 and min_roll != max_roll:
                OUTCOMS.append(
                        [percentage(ATTACKER.hp, min_roll), percentage(ATTACKER.hp, max_roll), ___move.internal_name])
            for ____move in ATTACKER.moves:

                min_roll = battle.calculate_damage(ATTACKER, DEFENDER, battle.weather.RAIN, battle.terrain.NO_TERRAIN, move=____move, rand_num=85, can_crit=False, printing=False)
                max_roll = battle.calculate_damage(ATTACKER, DEFENDER, battle.weather.RAIN, battle.terrain.NO_TERRAIN, move=____move, rand_num=100, can_crit=False, printing=False)
                #if percentage(DEFENDER.hp, min_roll) > 90 and min_roll != max_roll:
                OUTCOMSB.append([percentage(DEFENDER.hp, min_roll), percentage(DEFENDER.hp, max_roll), ____move.internal_name])

            # print(move.name, percentage(DEFENDER.hp, min_roll), percentage(DEFENDER.hp, max_roll))
        else:
            ATTACKER = battle.Pokemon.create_new_pokemon(species.get_dex_number(attacker), level)
            ATTACKER.evs = evs
            ATTACKER.ivs = [31, 31, 31, 31, 31, 31]
            ATTACKER.item = item
            ATTACKER.moves = []
            #ATTACKER.make_ability_hidden()
            for m in movesatt:
                ATTACKER.moves.append(m)
            ATTACKER.calc_stats()
            slower = False

            for ____move in ATTACKER.moves:

                min_roll = battle.calculate_damage(ATTACKER, DEFENDER, battle.weather.RAIN, battle.terrain.NO_TERRAIN, move=____move, rand_num=85, can_crit=False, printing=False)
                max_roll = battle.calculate_damage(ATTACKER, DEFENDER, battle.weather.RAIN, battle.terrain.NO_TERRAIN, move=____move, rand_num=100, can_crit=False, printing=False)
                #if percentage(DEFENDER.hp, min_roll) > 90 and min_roll != max_roll:
                OUTCOMS.append([percentage(DEFENDER.hp, min_roll), percentage(DEFENDER.hp, max_roll), ____move.internal_name])
            #print(move.name, percentage(DEFENDER.hp, min_roll), percentage(DEFENDER.hp, max_roll))
        OUTCOMS.sort(reverse=True)
        OUTCOMSB.sort(reverse=True)
        if slower:
            b1 = False
            for oc in OUTCOMS:
                if oc[1] > 100:
                    b1 = True
            if b1:
                print('Gets oneshot by', DEFENDER.get_species_name(), OUTCOMS)
            else:
                print('Gets outspeed by', DEFENDER.get_species_name(), OUTCOMS)
                #print('Your return damage:', OUTCOMSB)
        else:
            b1 = False
            for oc in OUTCOMS:
                if oc[1] > 100:
                    b1 = True
            if b1:
                print('Can oneshot', DEFENDER.get_species_name(), OUTCOMS)
            else:
                print('Cannot oneshot', DEFENDER.get_species_name(), OUTCOMS)
        #for oc in OUTCOMS:
        #    print(oc, DEFENDER.get_species_name())

        #print("\n")
        
        OUTCOMS = []
        
        for move in MOVES:
        
            min_roll = battle.calculate_damage(attacker=DEFENDER, defender=ATTACKER, _weather=battle.weather.RAIN, _terrain=battle.terrain.NO_TERRAIN, move=move, rand_num=85, can_crit=False, printing=False)
            max_roll = battle.calculate_damage(attacker=DEFENDER, defender=ATTACKER, _weather=battle.weather.RAIN, _terrain=battle.terrain.NO_TERRAIN, move=move, rand_num=100, can_crit=False, printing=False)
            if percentage(ATTACKER.hp, max_roll) > 50 and min_roll != max_roll:
                OUTCOMS.append([percentage(ATTACKER.hp, min_roll), percentage(ATTACKER.hp, max_roll), move.internal_name])
            #print(move.name, percentage(DEFENDER.hp, min_roll), percentage(DEFENDER.hp, max_roll))
        OUTCOMS.sort(reverse=True)
        for oc in OUTCOMS:
            print(oc)
        """
DATA = [
    "FURRET",
    "MACHOP",
    "HOOTHOOT",
    "RATTATA",
    "HOUNDOUR",
    "SHINX",
    "PIKACHU",
    "BUDEW",
    "HOOTHOOT",
    "RATTATA",
    "HOOTHOOT",
    "BULBASAUR",
    "RATTATA",
    "PIDGEY",
    "STARLY",
    "SCRAGGY",
    "WEEDLE",
    "CATERPIE",
    "BIDOOF",
    "LITLEO",
    "CATERPIE",
    "SHROOMISH",
    "CATERPIE",
    "SQUIRTLE",
    "PIDGEY",
    "RATTATA",
    "ZIGZAGOON",
    "PIKACHU",
    "PIKACHU",
    "FURRET",
    "ODDISH",
    "WEEDLE",
    "PSYDUCK",
    "PIDGEY",
    "PIDGEY",
    "CHARMANDER",
    "ZUBAT",
    "GEODUDE",
    "PARAS",
    "PHANPY",
    "DRILBUR",
    "NUMEL",
    "ZUBAT",
    "GEODUDE",
    "NOSEPASS",
    "CLEFAIRY",
    "NOSEPASS",
    "LARVITAR",
    "AZURILL",
    "NUMEL",
    "PIDOVE",
    "PATRAT",
    "SWABLU",
    "PATRAT",
    "SPEAROW",
    "SPEAROW",
    "PIKACHU",
    "BUDEW",
    "PIKACHU",
    "GASTLY",
    "MAREEP",
    "MAGNEMITE",
    "BELLSPROUT",
    "PIDOVE",
    "PIKACHU",
    "LITLEO",
    "SNOVER",
    "MAREEP",
    "BELLSPROUT",
    "EKANS",
    "MINUN",
    "PLUSLE",
]
"""
import species, movedata
from moves_base import move_name
from battle import Pokemon, Move
from os import getcwd
from loader import load_from_poke_paste

DATA.sort()

#mon1,mon2, mon3, mon4 = load_from_poke_paste(open(getcwd() + r'\Teams\elderteam.txt'))
mon1,mon2, mon3, mon4 = load_from_poke_paste(open(getcwd() + r'\Teams\falkner.txt'))
mon1.calc_stats()
mon2.calc_stats()
mon3.calc_stats()
mon4.calc_stats()

data_clone = []
for da in DATA:
    if da not in data_clone:
        data_clone.append(da)
for mon in [mon1, mon2, mon3, mon4]:

    for da in data_clone:
        new_pokemon = Pokemon.create_new_pokemon(species.get_dex_number(da.capitalize()), 15)
        new_pokemon.evs = [0, 0, 0, 0, 0, 0]
        new_pokemon.ivs = [31,31,31,31,31,31]
        new_pokemon.calc_stats()
        for move in species.moves(species.get_dex_number(da.capitalize()), 15, full_list=True):
            move = move_name(move)
            new_pokemon.moves.append(Move.create_new_move(None, movedata.get_id(move)))
        for move in new_pokemon.moves:
            #print(move.name)
            damage = percentage(mon1.hp, battle.calculate_damage(new_pokemon, mon, move=move, _weather="", _terrain="", printing=False, rand_num=100, can_crit=False))
            if damage > 50:
                if new_pokemon.speed > mon.speed:
                    print('[FASTER]Level 15', new_pokemon.get_species_name(), move.name, 'vs Level 15', mon.get_species_name() + ':', damage, '%')
                else:
                    print('[SLOWER]Level 15', new_pokemon.get_species_name(), move.name, 'vs Level 15', mon.get_species_name() + ':', damage, '%')
"""
"""
from loader import load_from_poke_paste, getcwd
mon1,mon2, mon3, mon4 = load_from_poke_paste(open(getcwd() + r'\Teams\falkner.txt'))
from action import *
from _moves import *

order = ActionOrder()
test_battle = battle.Battle()

new_action = Action(MoveAction, mon4, EXTREMESPEED, _battle=test_battle, opponent=mon2)
order.add_action(new_action)
new_action = Action(MoveAction, mon3, EXTREMESPEED, _battle=test_battle, opponent=mon1)
order.add_action(new_action)
new_action = Action(MoveAction, mon1, FAKEOUT, _battle=test_battle, opponent=mon1)
order.add_action(new_action)
new_action = Action(MoveAction, mon2, THUNDERBOLT, _battle=test_battle, opponent=mon1)
order.add_action(new_action)
new_action = Action(SwitchAction, mon1, mon2, test_battle, mon3)
order.add_action(new_action)

order.handle_actions()
"""
"""
import species, pokemon, nature, abilities, _moves, items

testmon = pokemon.Pokemon.create_new_pokemon(species.get_dex_number('Darmanitan'), 50)
testmon.ivs = [31,31,31,31,31,31]
testmon.evs = [0,252,0,0,0,0]
#testmon.set_nature(nature.ADAMANT)
testmon.calc_stats()

testmon.item = items.LIFE_ORB
testmon.moves = [_moves.FLAREBLITZ, _moves.EARTHQUAKE, _moves.SUPERPOWER, _moves.STONEEDGE]

for species_num in range(len(species.data)):
    new_mon = pokemon.Pokemon.create_new_pokemon(species_num, level=50)
    new_mon.evs = [0,0,0,0,0,0]
    new_mon.ivs = [31,31,31,31,31,31]
    new_mon.calc_stats()
    #print(new_mon.get_species_name())
    #print(new_mon.hp, new_mon.attack, new_mon.defense, new_mon.sp_atk, new_mon.sp_def, new_mon.speed)
    can0hko = False
    maxdmg = []
    for move in testmon.moves:
        pct = percentage(new_mon.hp, battle.calculate_damage(testmon, new_mon, _weather=None, _terrain=None, move=move, printing=False, can_crit=False, rand_num=100))
        #print(move,pct)
        if pct > 100:
            print(testmon.get_species_name(), 'can oneshot', new_mon.get_species_name(), 'with', move, "(" + str(pct) + "%)")
            can0hko = True
        maxdmg.append([pct, move.name])
    if not can0hko:
        maxdmg.sort()
        maxdmg.reverse()
        print(testmon.get_species_name(), 'can not oneshot', new_mon.get_species_name() + ".", 'Highest Damage:', maxdmg[0])
"""

test_battle = battle.Battle()
from loader import load_from_poke_paste, getcwd
import team
import AI

mon1,mon2,mon3,mon4 = load_from_poke_paste(open(getcwd() + r'\Teams\falkner.txt'))

team1 = team.Team()
team1.add_pokemon(mon1)
team1.add_pokemon(mon2)
team1.add_pokemon(mon3)
team1.add_pokemon(mon4)

mon1,mon2,mon3,mon4 = load_from_poke_paste(open(getcwd() + r'\Teams\elderteam.txt'))

team2 = team.Team()
team2.add_pokemon(mon1)
team2.add_pokemon(mon2)
team2.add_pokemon(mon3)
team2.add_pokemon(mon4)

test_battle.team1 = team1
test_battle.team2 = team2


AI.get_roaster(test_battle)
#actions = AI.get_all_enemy_actions(test_battle)
"""
for action in actions:
    print(action.type)
    print(action.act)
    if action.type == AI.action.MoveAction:
        print(action.user.get_species_name(), action.opponent.get_species_name(), percentage(action.opponent.hp, AI.action.calculate_damage(action.user, action.opponent, test_battle.weather, test_battle.terrain, action.act, rand_num=100, printing=False, can_crit=False)))
"""