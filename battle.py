from trainer import Trainer
from messages import textbox
import AI
import GUI
from pokemon import Pokemon
import weather, terrain, moves, items, _types, abilities, status, gender
from move import Move
import random
from errors import NoStockpile


def jewel_matches(item: str, typing: str) -> bool:
    return (item == items.BUG_GEM and typing == _types.BUG) or (item == items.DARK_GEM and typing == _types.DARK) or (
            item == items.DRAGON_GEM and typing == _types.DRAGON) or (
                   item == items.ELECTRIC_GEM and typing == _types.ELECTRIC) or (
                   item == items.FAIRY_GEM and typing == _types.FAIRY) or (
                   item == items.FIGHTING_GEM and typing == _types.FIGHTING) or (
                   item == items.FIRE_GEM and typing == _types.FIRE) or (
                   item == items.FLYING_GEM and typing == _types.FLYING) or (
                   item == items.GHOST_GEM and typing == _types.GHOST) or (
                   item == items.GRASS_GEM and typing == _types.GRASS) or (
                   item == items.GROUND_GEM and typing == _types.GROUND) or (
                   item == items.ICE_GEM and typing == _types.ICE) or (
                   item == items.NORMAL_GEM and typing == _types.NORMAL) or (
                   item == items.POISON_GEM and typing == _types.POISON) or (
                   item == items.PSYCHIC_GEM and typing == _types.PSYCHIC) or (
                   item == items.ROCK_GEM and typing == _types.ROCK) or (
                   item == items.STEEL_GEM and typing == _types.STEEL) or (
                   item == items.WATER_GEM and typing == _types.WATER)


def plate_matches(item: str, typing: str) -> bool:
    return False  # TODO


def type_booster_matches(item: str, typing: str) -> bool:
    return False  # TODO


def get_natural_gift_damage(item: str) -> int:
    return 0  # TODO


def berry_matches(typing: str, item: str) -> bool:
    #print('NOU')
    BERRY_TABLE = {_types.FIRE: items.OCCA_BERRY,
                   _types.WATER: items.PASSHO_BERRY,
                   _types.ELECTRIC: items.WACAN_BERRY,
                   _types.GRASS: items.CHOPLE_BERRY,
                   _types.POISON: items.KEBIA_BERRY,
                   _types.ICE: items.YACHE_BERRY,
                   _types.FIGHTING: items.CHOPLE_BERRY,
                   _types.GROUND: items.SHUCA_BERRY,
                   _types.FLYING: items.COBA_BERRY,
                   _types.PSYCHIC: items.PAYAPA_BERRY,
                   _types.BUG: items.TANGA_BERRY,
                   _types.ROCK: items.CHARTI_BERRY,
                   _types.GHOST: items.KASIB_BERRY,
                   _types.DRAGON: items.HABAN_BERRY,
                   _types.DARK: items.COLBUR_BERRY,
                   _types.STEEL: items.BABIRI_BERRY,
                   _types.NORMAL: items.CHILAN_BERRY
                   }
    try:
        berry = BERRY_TABLE[typing]
        if berry == item:
            return True
    except KeyError:
        return False
    return False  # TODO


# ==============================================================================
# Accuracy / Evasion changes
# ==============================================================================

def evasion_items_defender(item: str) -> float:
    # ==============================================================================
    # Bright Powder: reduces accuracy by 10%
    # ==============================================================================

    if item == items.BRIGHT_POWDER:
        return 1.1

    # ==============================================================================
    # Lax incense: reduces accuracy by 10%
    # ==============================================================================

    if item == items.LAX_INCENSE:
        return 1.1
    return 1


def accuracy_items_attacker(item: str) -> float:
    # ==============================================================================
    # Zoom lens: increases accuracy by 20% (if the user moves last) # TODO
    # ==============================================================================

    if item == items.ZOOM_LENS:
        return 1.2

    # ==============================================================================
    # Wide Lens: increases accuracy by 10%
    # ==============================================================================

    if item == items.WIDE_LENS:
        return 1.1
    return 1


# ==============================================================================
# Check if move hits
# ==============================================================================

def move_hits(attacker: Pokemon, defender: Pokemon, _weather: str, _terrain: str, move: Move) -> bool:
    # ==============================================================================
    # Never missing moves (Faint attack, Aerial Ace, Swift)
    # ==============================================================================

    if move.accuracy == -1:
        return True

    # ==============================================================================
    # Blizzard in hail
    # ==============================================================================

    if _weather == weather.HAIL and move.internal_name == moves.BLIZZARD:
        return True

    # ==============================================================================
    # Thunder in rain
    # ==============================================================================

    if _weather == weather.RAIN and move.internal_name == moves.THUNDER:
        return True

    # ==============================================================================
    # Hurricane in rain
    # ==============================================================================

    if _weather == weather.RAIN and move.internal_name == moves.HURRICANE:
        return True

    # ==============================================================================
    # Stomp after minimize  # TODO!
    # ==============================================================================

    # ==============================================================================
    # Toxic when poison type
    # ==============================================================================

    if attacker.has_type(_types.POISON) and move.internal_name == moves.TOXIC:
        return True

    # TODO: flying, digging, diving targets!

    if _weather != weather.FOG:
        return random.randint(1,
                              100) >= move.accuracy * attacker.get_accuracy() / defender.get_evasion() * accuracy_items_attacker(
            attacker.item) / evasion_items_defender(defender.item)
    else:
        return random.randint(1,
                              100) >= move.accuracy * attacker.get_accuracy() / defender.get_evasion() * accuracy_items_attacker(
            attacker.item) / evasion_items_defender(defender.item) * 0.6


def is_critical(attacker: Pokemon, defender: Pokemon, move: Move) -> bool:
    # TODO ENERGIEFOKUS -> pokemon.critical_level, moves.KONZENTRATOR
    chances = {0: 1, 1: 3, 2: 12, 3: 24}
    critical_level = 0
    if move.has_high_critical_rate():
        critical_level += 1
    if attacker.has_item(items.SCOPE_LENS):
        critical_level += 1
    if attacker.has_item(items.RAZOR_CLAW):
        critical_level += 1
    if attacker.has_ability(abilities.SUPER_LUCK):
        critical_level += 1
    if attacker.get_species_name() == "Chansey" and attacker.has_item(items.LUCKY_PUNCH):
        critical_level += 2
    if attacker.get_species_name() in ("Farfetch'd", "Farfetchd", "Lauchzelot") and attacker.has_item(items.LEEK):
        critical_level += 2

    if defender.has_ability(abilities.BATTLE_ARMOR):
        return False
    if defender.has_ability(abilities.SHELL_ARMOR):
        return False
    if move.always_crits:
        return True

    return random.randint(1, 24) <= chances[critical_level]


# ==============================================================================
# Damage calculation
# ==============================================================================

def calculate_damage(attacker: Pokemon, defender: Pokemon, _weather: str, _terrain: str, move: Move,
                     helping_hand=False, hit_number=1, stockpiles=0, target_underground=False, target_minimized=False,
                     user_defense_curled=False, previous_move_failed=False, opponent_moved_first=False,
                     target_took_damage_during_round=False, party_killed_before=False, round_used_before=False,
                     fusion_bolt_used=False, fusion_flare_used=False, user_took_damage=False, target_diving=False,
                     target_is_switching=False, used_charge=False, mud_sport=False, water_sport=False,
                     partner: Pokemon = None, battle_turns=0, reflect=False, light_screen=False,
                     aurora_veil=False, double_battle=False, fire_fang_active=False, rand_num=None, can_crit=True, printing=True) -> int:
    # ==============================================================================
    # Dragon Rage always does 40 damage
    # ==============================================================================

    if move.internal_name == moves.DRAGONRAGE:
        return 40

    # ==============================================================================
    # Sonic boom always does 20 damage
    # ==============================================================================

    if move.internal_name == moves.SONICBOOM:
        return 20

    # ==============================================================================
    # HP halving moves (Super Fang, Nature's madness)
    # ==============================================================================

    if move.internal_name in (moves.NATURESMADNESS, moves.SUPERFANG):
        return round(defender.hp / 2 - 0.499)

    # ==============================================================================
    # Level depending damaging moves (Night shade, Seismic Toss)
    # ==============================================================================

    if move.internal_name in (moves.SEISMICTOSS, moves.NIGHTSHADE):
        return attacker.level

    # ==============================================================================
    # One hit K.O. moves (Horn Drill, Sheer Cold, Fissure, Guillotine)
    # ==============================================================================

    if move.internal_name in (moves.HORNDRILL, moves.SHEERCOLD, moves.FISSURE, moves.GUILLOTINE):
        if defender.get_ability() == abilities.STURDY or defender.has_item(items.FOCUS_SASH):
            return 0
        else:
            if printing:
                textbox("It's a one hit K-O!")
            return defender.hp

    # ==============================================================================
    # Roll factor (always max roll on Spit up)
    # ==============================================================================

    if rand_num is None:

        if move.internal_name == moves.SPITUP:
            rand_num = 100
        else:
            rand_num = random.randint(85, 100)

    # ==============================================================================
    # Base Damage = "Basisschaden = RH⋅BS⋅IT⋅LV⋅LS⋅NM⋅AF⋅ZF"
    # ==============================================================================

    base_damage = move.base_damage

    # ==============================================================================
    # Acrobatics variable base damage (double if no item held)
    # ==============================================================================

    if move.internal_name == moves.ACROBATICS:
        if not attacker.is_holding_item():
            base_damage *= 2

    # ==============================================================================
    # Deals damage depending on enemy HP percentage (Wring out, Crush grip)
    # ==============================================================================

    if move.internal_name in (moves.WRINGOUT, moves.CRUSHGRIP):
        base_damage = round(120 * defender.get_hp_percentage() / 100 - 0.499)

    # ==============================================================================
    # Natural Gift (80,90,100)
    # ==============================================================================

    if move.internal_name == moves.NATURALGIFT:
        base_damage = get_natural_gift_damage(attacker.item)

    # ==============================================================================
    # Weight depending moves (Heat Crash, Heavy Slam)
    # ==============================================================================

    if move.internal_name in (moves.HEATCRASH, moves.HEAVYSLAM):
        if defender.get_dex_weight() >= attacker.get_dex_weight() / 2:
            base_damage = 40
        elif defender.get_dex_weight() >= attacker.get_dex_weight() / 3:
            base_damage = 60
        elif defender.get_dex_weight() >= attacker.get_dex_weight() / 4:
            base_damage = 80
        elif defender.get_dex_weight() >= attacker.get_dex_weight() / 5:
            base_damage = 100
        else:
            base_damage = 120

    # ==============================================================================
    # Hex does double damage if the defender has a status condition
    # ==============================================================================

    if move.internal_name == moves.HEX:
        if defender.status == status.NO_STATUS:
            base_damage = 70
        else:
            base_damage = 140

    # ==============================================================================
    # Knock Off does 1.5 times damage
    # ==============================================================================

    if move.internal_name == moves.KNOCKOFF:
        if defender.is_holding_item():
            base_damage *= 1.5

    # ==============================================================================
    # Triple Kick does 10,20,30 damage
    # ==============================================================================

    if move.internal_name == moves.TRIPLEKICK:
        base_damage = hit_number * 10

    # ==============================================================================
    # Flail and reversal do damage depending on the users hp
    # ==============================================================================

    if move.internal_name in (moves.FLAIL, moves.REVERSAL):
        if attacker.get_hp_percentage() > 69:
            base_damage = 20
        elif attacker.get_hp_percentage() > 37:
            base_damage = 40
        elif attacker.get_hp_percentage() > 22:
            base_damage = 80
        elif attacker.get_hp_percentage() > 11:
            base_damage = 100
        elif attacker.get_hp_percentage() > 4:
            base_damage = 150
        else:
            base_damage = 200

    # ==============================================================================
    # Electro ball does more damage if the user is faster than the target
    # ==============================================================================

    if move.internal_name == moves.ELECTROBALL:
        if defender.speed >= attacker.speed / 2:
            base_damage = 60
        elif defender.speed >= attacker.speed / 3:
            base_damage = 80
        elif defender.speed >= attacker.speed / 4:
            base_damage = 120
        else:
            base_damage = 150

    # ==============================================================================
    # Spit up depending on stacks
    # ==============================================================================

    if move.internal_name == moves.SPITUP:

        if stockpiles == 0:
            base_damage = 0
            if printing:
                raise NoStockpile()

        base_damage = stockpiles * 100

    # ==============================================================================
    # Earthquake on underground targets
    # ==============================================================================

    if move.internal_name == moves.EARTHQUAKE:
        if target_underground:
            base_damage *= 2

    # ==============================================================================
    # Moves that depend on users hp (Eruption, Water Spout)
    # ==============================================================================

    if move.internal_name in (moves.ERUPTION, moves.WATERSPOUT):
        base_damage = 150 * attacker.get_hp_percentage() / 100

    # ==============================================================================
    # Facade does double damage when suffering a status condition
    # ==============================================================================

    if move.internal_name == moves.FACADE:
        if attacker.status != status.NO_STATUS:
            base_damage *= 2

    # ==============================================================================
    # Flying press double damage on minimized targets, so does Phantom Force & Shadow Force & Stomp
    # ==============================================================================

    if move.internal_name in (moves.FLYINGPRESS, moves.PHANTOMFORCE, moves.SHADOWFORCE, moves.STOMP):
        if target_minimized:
            base_damage *= 2

    # ==============================================================================
    # Ice Ball, Rollout multiplying damage for each hit
    # ==============================================================================

    if move.internal_name in (moves.ICEBALL, moves.ROLLOUT):
        if user_defense_curled:
            base_damage = 60
        else:
            base_damage = 30
        if hit_number > 1:
            for _ in range(hit_number - 1):
                base_damage *= 2

    # ==============================================================================
    # Frustration -> the less happiness, the more power
    # ==============================================================================

    if move.internal_name == moves.FRUSTRATION:
        base_damage = (255 - attacker.happiness) / 2.5

    # ==============================================================================
    # Stomping Tantrum does double damage if the previous move failed
    # ==============================================================================

    if move.internal_name == moves.STOMPINGTANTRUM:
        if previous_move_failed:
            base_damage *= 2

    # ==============================================================================
    # Low Kick, Grass Knot -> the heavier the target, the more damage is dealt
    # ==============================================================================

    if move.internal_name in (moves.LOWKICK, moves.GRASSKNOT):
        if defender.get_dex_weight() < 10:
            base_damage = 20
        elif defender.get_dex_weight() < 25:
            base_damage = 40
        elif defender.get_dex_weight() < 50:
            base_damage = 60
        elif defender.get_dex_weight() < 100:
            base_damage = 80
        elif defender.get_dex_weight() < 200:
            base_damage = 100
        else:
            base_damage = 120

    # ==============================================================================
    # Payback when slower
    # ==============================================================================

    if move.internal_name == moves.PAYBACK:
        if opponent_moved_first:
            base_damage *= 2

    # ==============================================================================
    # Present's gimmicks
    # ==============================================================================

    if move.internal_name == moves.PRESENT:
        ran = random.randint(1, 10)
        if ran <= 4:
            base_damage = 40
        elif ran <= 7:
            base_damage = 80
        elif ran == 8:
            base_damage = 120
        else:
            base_damage = 0  # TODO: HP Recovery!

    # ==============================================================================
    # Assurance double damage when enemy took damage before
    # ==============================================================================

    if move.internal_name == moves.ASSURANCE:
        if target_took_damage_during_round:
            base_damage *= 2

    # ==============================================================================
    # Gyro Ball -> the slower you are in comparison, the more damage. Cap: 150
    # ==============================================================================

    if move.internal_name == moves.GYROBALL:
        base_damage = 25 * defender.speed / attacker.speed
        if base_damage > 150:
            base_damage = 150  # Max DMG cap

    # ==============================================================================
    # Venoshock: Double damage to poisoned targets
    # ==============================================================================

    if move.internal_name == moves.VENOSHOCK:
        if defender.status in (status.POISON, status.BADLY_POISONED):
            base_damage *= 2

    # ==============================================================================
    # Retaliate: Double damage when revenging a fallen party member
    # ==============================================================================

    if move.internal_name == moves.RETALIATE:
        if party_killed_before:
            base_damage *= 2

    # ==============================================================================
    # Magnitude's random damages
    # ==============================================================================

    if move.internal_name == moves.MAGNITUDE:
        ran = random.randint(1, 20)
        if ran == 1:
            base_damage = 10
        elif ran <= 3:
            base_damage = 30
        elif ran <= 7:
            base_damage = 50
        elif ran <= 13:
            base_damage = 70
        elif ran <= 17:
            base_damage = 90
        elif ran <= 19:
            base_damage = 110
        else:
            base_damage = 150
        if _terrain == terrain.GRASS:
            base_damage /= 2
        if target_underground:
            base_damage *= 2

    # ==============================================================================
    # Round -> double damage when used before
    # ==============================================================================

    if move.internal_name == moves.ROUND:
        if round_used_before:
            base_damage *= 2

    # ==============================================================================
    # Stored Power, Power Trip
    # ==============================================================================

    if move.internal_name in (moves.STOREDPOWER, moves.POWERTRIP):
        for stages in attacker.stat_stages:
            base_damage += 20 * stages

    # ==============================================================================
    # Fusion Bolt / Flare doing double damage when the other was used before
    # ==============================================================================

    if move.internal_name == moves.FUSIONBOLT:
        if fusion_flare_used:
            base_damage *= 2

    if move.internal_name == moves.FUSIONFLARE:
        if fusion_bolt_used:
            base_damage *= 2

    # ==============================================================================
    # Brine does double damage when the target is below half hp
    # ==============================================================================

    if move.internal_name == moves.BRINE:
        if defender.get_hp_percentage() < 50:
            base_damage *= 2

    # ==============================================================================
    # Avalanche and Revenge do double damage when the user was hit before
    # ==============================================================================

    if move.internal_name in (moves.AVALANCHE, moves.REVENGE):
        if user_took_damage:
            base_damage *= 2

    # ==============================================================================
    # Weather Ball has double base power when the weather is rain, sun or hail
    # ==============================================================================

    if move.internal_name == moves.WEATHERBALL:
        if _weather not in (weather.FOG, weather.NO_WEATHER, weather.DELTA_STREAM):
            base_damage *= 2

    # ==============================================================================
    # Nature power table
    # ==============================================================================

    if move.internal_name == moves.NATUREPOWER:
        pass  # TODO!

    # ==============================================================================
    # Smelling Salts does double damage when the target is paralyzed but removes the paralysis
    # ==============================================================================

    if move.internal_name == moves.SMELLINGSALTS:
        if defender.status == status.PARALYSIS:
            base_damage *= 2
            defender.status = status.NO_STATUS  # TODO: only if not fails! idk if I want this here tbh

    # ==============================================================================
    # Return -> friendship based Base damage
    # ==============================================================================

    if move.internal_name == moves.RETURN:
        base_damage = attacker.happiness / 2.5

    # ==============================================================================
    # Fling depends on the item flinged
    # ==============================================================================

    if move.internal_name == moves.FLING:
        pass  # TODO!

    # ==============================================================================
    # Punishment does more damage the more stat boost the enemy has
    # ==============================================================================

    if move.internal_name == moves.PUNISHMENT:
        for stages in defender.stat_stages:
            base_damage += 20 * stages
        if base_damage > 200:
            base_damage = 200  # CAP

    # ==============================================================================
    # Double damage on diving targets (Surf)
    # ==============================================================================

    if move.internal_name == moves.SURF:
        if target_diving:
            base_damage *= 2

    # ==============================================================================
    # The less pp, the more power
    # ==============================================================================

    if move.internal_name == moves.TRUMPCARD:
        if move.pp >= 5:
            base_damage = 40
        elif move.pp == 4:
            base_damage = 50
        elif move.pp == 3:
            base_damage = 60
        elif move.pp == 2:
            base_damage = 75
        elif move.pp == 1:
            base_damage = 190

    # ==============================================================================
    # Double damage on switching
    # ==============================================================================

    if move.internal_name == moves.PURSUIT:
        if target_is_switching:
            base_damage *= 2  # TODO: priority = 8

    # ==============================================================================
    # Smelling salt for sleep (double damage but removes status)
    # ==============================================================================

    if move.internal_name == moves.WAKEUPSLAP:
        if defender.status == status.SLEEP:
            base_damage *= 2
            defender.status = status.NO_STATUS  # TODO again, not sure if I want it that way

    # ==============================================================================
    # Echoed Voice stacks
    # ==============================================================================

    if move.internal_name == moves.ECHOEDVOICE:
        base_damage *= hit_number
        if base_damage > 200:
            base_damage = 200

    # ==============================================================================
    # Fury cutter stacks
    # ==============================================================================

    if move.internal_name == moves.FURYCUTTER:
        base_damage *= hit_number
        if base_damage > 160:
            base_damage = 160

# ==============================================================================
# Helping hand support
# ==============================================================================

    if helping_hand:
        base_damage *= 1.5

# ==============================================================================
# ITEMS
# ==============================================================================

    # ==============================================================================
    # Adamant Orb
    # ==============================================================================

    if attacker.has_item(items.ADAMANT_ORB) and move.type in (
            _types.DRAGON, _types.STEEL) and attacker.get_species_name() == "Dialga":
        base_damage *= 1.2

    # ==============================================================================
    # Type specific gems
    # ==============================================================================

    if jewel_matches(attacker.item, move.type):
        base_damage *= 1.5

    # ==============================================================================
    # Muscle Band
    # ==============================================================================

    if attacker.has_item(items.MUSCLE_BAND) and move.is_physical():
        base_damage *= 1.1

    # ==============================================================================
    # Griseous Orb
    # ==============================================================================

    if attacker.has_item(items.GRISEOUS_ORB) and move.type in (
            _types.DRAGON, _types.GHOST) and attacker.get_species_name() == "Giratina":
        base_damage *= 1.2

    # ==============================================================================
    # Rose Incense
    # ==============================================================================

    if attacker.has_item(items.ROSE_INCENSE) and move.type == _types.GRASS:
        base_damage *= 1.2

    # ==============================================================================
    # Wise Glasses
    # ==============================================================================

    if attacker.has_item(items.WISE_GLASSES) and move.is_special():
        base_damage *= 1.1

    # ==============================================================================
    # Odd Incense
    # ==============================================================================

    if attacker.has_item(items.ODD_INCENSE) and move.type == _types.PSYCHIC:
        base_damage *= 1.2

    # ==============================================================================
    # Sea Incense
    # ==============================================================================

    if attacker.has_item(items.SEA_INCENSE) and move.type == _types.WATER:
        base_damage *= 1.2

    # ==============================================================================
    # Rock Incense
    # ==============================================================================

    if attacker.has_item(items.ROCK_INCENSE) and move.type == _types.ROCK:
        base_damage *= 1.2

    # ==============================================================================
    # Boosting plates
    # ==============================================================================

    if plate_matches(attacker.item, move.type):
        base_damage *= 1.2

    # ==============================================================================
    # Type boosting items (spell tag, miracle seed etc.)
    # ==============================================================================

    if type_booster_matches(attacker.item, move.type):
        base_damage *= 1.2

    # ==============================================================================
    # Lustrous Orb
    # ==============================================================================

    if attacker.has_item(items.LUSTROUS_ORB) and move.type in (
            _types.DRAGON, _types.WATER) and attacker.get_species_name() == "Palkia":
        base_damage *= 1.2

    # ==============================================================================
    # Wave Incense
    # ==============================================================================

    if attacker.has_item(items.WAVE_INCENSE) and move.type == _types.WATER:
        base_damage *= 1.2

# ==============================================================================
# Charge, Mud Sport, Water Sport
# ==============================================================================

    if used_charge:
        if move.type == _types.ELECTRIC:
            base_damage *= 2

    if mud_sport:
        if move.type == _types.ELECTRIC:
            base_damage /= 2

    if water_sport:
        if move.type == _types.FIRE:
            base_damage /= 2

# ==============================================================================
# Abilities
# ==============================================================================

    # ==============================================================================
    # Reckless
    # ==============================================================================

    if attacker.has_ability(abilities.RECKLESS):
        if move.does_recoil():
            base_damage *= 1.2

    # ==============================================================================
    # Analytic
    # ==============================================================================

    if attacker.has_ability(abilities.ANALYTIC):
        if opponent_moved_first:
            base_damage *= 1.3

    # ==============================================================================
    # Dark Aura
    # ==============================================================================

    if attacker.has_ability(abilities.DARK_AURA):
        if move.type == _types.DARK:
            base_damage *= 1.3

    # ==============================================================================
    # Iron Fist buffed to 1.3! # TODO
    # ==============================================================================

    if attacker.has_ability(abilities.IRON_FIST):
        if move.is_punching_move():
            base_damage *= 1.3

    if attacker.has_ability(abilities.FAIRY_AURA):
        if move.type == _types.FAIRY:
            base_damage *= 1.3

    if attacker.has_ability(abilities.PIXILATE):
        if move.type == _types.NORMAL:
            base_damage *= 1.3
            move.type = _types.FAIRY  # TODO: not sure if I want this here

    if attacker.has_ability(abilities.REFRIGERATE):
        if move.type == _types.NORMAL:
            base_damage *= 1.3
            move.type = _types.ICE  # TODO: not sure if I want this here

    if attacker.has_ability(abilities.BLAZE):
        if move.type == _types.FIRE and attacker.get_hp_percentage() <= 100 / 3:
            base_damage *= 1.5

    if attacker.has_ability(abilities.SWARM):
        if move.type == _types.BUG and attacker.get_hp_percentage() <= 100 / 3:
            base_damage *= 1.5

    if attacker.has_ability(abilities.TOUGH_CLAWS):
        if move.is_contact_move():
            base_damage *= 1.3

    if attacker.has_ability(abilities.MEGA_LAUNCHER):
        if move.is_pulse_move() or move.internal_name == moves.AURASPHERE:
            base_damage *= 1.5

    if attacker.has_ability(abilities.OVERGROW):
        if move.type == _types.GRASS and attacker.get_hp_percentage() <= 100 / 3:
            base_damage *= 1.5

    if attacker.has_ability(abilities.RIVALRY):
        if defender.gender == gender.NO_GENDER:
            base_damage *= 1  # useless
        elif attacker.gender == defender.gender:
            base_damage *= 1.25
        elif attacker.gender != defender.gender:
            base_damage *= 0.75

    if attacker.has_ability(abilities.TORRENT):
        if move.type == _types.WATER and attacker.get_hp_percentage() <= 100 / 3:
            base_damage *= 1.5

    if attacker.has_ability(abilities.TECHNICIAN):
        if move.base_damage <= 60 or base_damage <= 60:
            base_damage *= 1.5

    if attacker.has_ability(abilities.STRONG_JAW):
        if move.is_biting_move():
            base_damage *= 1.5

    if attacker.has_ability(abilities.AERILATE):
        if move.type == _types.NORMAL:
            base_damage *= 1.3
            move.type = _types.FLYING  # TODO: not sure if I want this here

    if defender.has_ability(abilities.AURA_BREAK):
        if attacker.has_ability(abilities.FAIRY_AURA) or attacker.has_ability(abilities.DARK_AURA):
            base_damage /= 1.3  # reverse of the boost
            base_damage *= 0.7

    if defender.has_ability(abilities.FRIEND_GUARD):
        if move.get_target() == 0:  # TODO! if hits all!!
            base_damage *= 0.75  # TODO! reduces friend damage by *.75

    if defender.has_ability(abilities.HEATPROOF):
        if move.type == _types.FIRE:
            base_damage *= 0.5

    if defender.has_ability(abilities.MULTISCALE):
        if defender.hp == defender.total_hp:
            base_damage *= 0.5

    if defender.has_ability(abilities.THICK_FAT):
        if move.type in (_types.FIRE, _types.ICE):
            base_damage *= 0.5

    if defender.has_ability(abilities.DRY_SKIN):
        if move.type == _types.FIRE:
            base_damage *= 1.25

    if defender.has_ability(abilities.LEVITATE):
        if move.type == _types.GROUND:
            return 0

    if can_crit:

        critical_hit = is_critical(attacker, defender, move)
        if critical_hit:
            if attacker.has_ability(abilities.SNIPER):
                critical_multiplier = 2.25
            else:
                critical_multiplier = 1.5
        else:
            critical_multiplier = 1
    else:
        critical_multiplier = 1
        critical_hit = False

    attack = attacker.attack
    defense = defender.defense
    special_attack = attacker.sp_atk
    special_defense = defender.sp_def

    if attacker.stat_stages[0] > 0:
        attack *= 1 + attacker.stat_stages[0] / 2
    if attacker.stat_stages[0] < 0:
        attack *= 2 / ((attacker.stat_stages[0] * -1) + 2)
    if defender.stat_stages[1] > 0 and not critical_hit and move.internal_name != moves.SACREDSWORD:
        defense *= 1 + defender.stat_stages[1] / 2
    if defender.stat_stages[1] < 0:
        defense *= 2 / ((defender.stat_stages[1] * -1) + 2)
    if attacker.stat_stages[2] > 0:
        special_attack *= 1 + attacker.stat_stages[2] / 2
    if attacker.stat_stages[2] < 0:
        special_attack *= 2 / ((attacker.stat_stages[2] * -1) + 2)
    if defender.stat_stages[3] > 0 and not critical_hit:
        special_defense *= 1 + defender.stat_stages[3] / 2
    if defender.stat_stages[3] < 0:
        special_defense *= 2 / ((defender.stat_stages[3] * -1) + 2)

    if attacker.has_ability(abilities.GUTS):
        if attacker.status != status.NO_STATUS:
            attack *= 1.5

    if attacker.has_ability(abilities.TOXIC_BOOST):
        if attacker.status in ( status.POISON, status.BADLY_POISONED):
            attack *= 1.5

    if attacker.has_ability(abilities.FLARE_BOOST):
        if attacker.status == status.BURN:
            special_attack *= 1.5

    if attacker.has_ability(abilities.HUGE_POWER) or attacker.has_ability(abilities.PURE_POWER):
        attack *= 2

    if partner is not None:
        if partner.has_ability(abilities.PLUS) and attacker.has_ability(abilities.MINUS):
            special_attack *= 1.5
        if partner.has_ability(abilities.MINUS) and attacker.has_ability(abilities.PLUS):
            special_attack *= 1.5

    if attacker.has_ability(abilities.FLOWER_GIFT):
        if _weather == weather.SUNNY:
            attack *= 1.5

    if attacker.has_ability(abilities.SLOW_START):
        if battle_turns <= 5:
            attack *= 0.5

    if attacker.has_ability(abilities.DEFEATIST):
        if attacker.get_hp_percentage() < 50:
            attack *= 0.5
            special_attack *= 0.5

    if attacker.has_ability(abilities.SOLAR_POWER):
        if _weather == weather.SUNNY:
            special_attack *= 1.5

    if attacker.has_ability(abilities.HUSTLE):
        attack *= 1.5

    if attacker.has_item(items.DEEP_SEA_TOOTH):
        if attacker.get_species_name() == "Clamperl":
            special_attack *= 2

    if attacker.has_item(items.THICK_CLUB):
        if attacker.get_species_name() in ("Cubone", "Marowak"):
            attack *= 2

    if attacker.has_item(items.LIGHT_BALL):
        if attacker.get_species_name() == "Pikachu":
            attack *= 2
            special_attack *= 2

    if attacker.has_item(items.SOUL_DEW):
        if attacker.get_species_name() in ("Latias", "Latios"):
            special_attack *= 2

    if attacker.has_item(items.CHOICE_BAND):
        attack *= 1.5

    if attacker.has_item(items.CHOICE_SPECS):
        special_attack *= 1.5

    if defender.has_item(items.DEEP_SEA_SCALE):
        if defender.get_species_name() == "Clamperl":
            special_defense *= 2

    if defender.has_item(items.EVIOLITE):
        if defender.can_evolve():
            defense *= 1.5
            special_defense *= 1.5

    if defender.has_item(items.METAL_POWDER):
        if defender.get_species_name() == "Ditto":  # TODO: pre transform only!
            defense *= 1.5
            special_defense *= 1.5

    if defender.has_ability(abilities.MARVEL_SCALE):
        if defender.status != status.NO_STATUS:
            defense *= 1.5

    if defender.has_item(items.ASSAULT_VEST):
        special_defense *= 1.5

    if defender.has_ability(abilities.FLOWER_GIFT):
        special_defense *= 1.5

    if _weather == weather.SAND:
        if defender.has_type(_types.ROCK):
            special_defense *= 1.5

    if defender.has_item(items.SOUL_DEW):
        if defender.get_species_name() in ("Latios", "Latias"):
            special_defense *= 2

    factor_1 = 1  # burn * reflect light screen * 2v2 * sun rain * fire fang boost

    if attacker.status == status.BURN:
        if attacker.has_ability(abilities.GUTS):
            factor_1 *= 1  # no change
        else:
            factor_1 /= 2
    if not critical_hit:
        if aurora_veil and move.internal_name != moves.BRICKBREAK:
            factor_1 *= 0.5
        elif reflect and move.is_physical() and move.internal_name != moves.BRICKBREAK:
            factor_1 *= 0.5
        elif light_screen and move.is_special():
            factor_1 *= 0.5

    if move.get_target() == 0 and double_battle:  # TODO: 2v2!! and get_target = 0?
        factor_1 *= 0.75

    if _weather == weather.SUNNY:
        if move.type == _types.WATER:
            factor_1 *= 0.5

    if _weather == weather.RAIN:
        if move.type == _types.FIRE:
            factor_1 *= 0.5

    if _weather == weather.RAIN:
        if move.type == _types.WATER:
            factor_1 *= 1.5

    if _weather == weather.SUNNY:
        if move.type == _types.FIRE:
            factor_1 *= 1.5

    if fire_fang_active:
        if move.type == _types.FIRE:
            factor_1 *= 1.5

    factor_2 = 1

    if attacker.has_item(items.LIFE_ORB):
        factor_2 *= 1.3

    if attacker.has_item(items.METRONOME):
        mod = (1 + hit_number / 10)
        if mod > 2:
            mod = 2
        factor_2 *= mod

    if move.internal_name == moves.MEFIRST:
        factor_2 *= 1.5

    factor_3 = 1

    effectivity = 1

    #print(move.type, defender.get_type_1(), move.name)
    if move.is_super_effective(defender.get_type_1()):
        effectivity *= 2
    if move.is_ineffective(defender.get_type_1()):
        effectivity /= 2
    if move.is_immune(defender.get_type_1()):
        effectivity *= 0
    if defender.get_type_2() is not None:
        if move.is_immune(defender.get_type_2()):
            effectivity *= 0
        if move.is_ineffective(defender.get_type_2()):
            effectivity /= 2
        if move.is_super_effective(defender.get_type_2()):
            effectivity *= 2
    # print(defender.get_type_2())
    #print(effectivity, move.name)

    if defender.has_ability(abilities.FILTER) or defender.has_ability(abilities.SOLID_ROCK):
        if effectivity > 1:
            factor_3 /= 2

    if attacker.has_item(items.EXPERT_BELT):
        if effectivity > 1:
            factor_3 *= 1.2

    if attacker.has_ability(abilities.TINTED_LENS):
        if effectivity < 1:
            factor_3 *= 2

    #if effectivity > 1:
    if berry_matches(move.type, defender.item):
        factor_3 /= 2

    # ==============================================================================
    # STAB
    # ==============================================================================

    if attacker.has_type(move.type):
        if attacker.has_ability(abilities.ADAPTABILITY):
            stab = 2
        else:
            stab = 1.5
    else:
        stab = 1


    damage = 0  # STATUS MOVE!

    if printing:

        if effectivity > 1:
            textbox("It's super effective!")
        if effectivity == 0:
            textbox("It had no effect on the opposing " + defender.get_species_name() + "...")
        elif effectivity < 1:
            textbox("It's not very effective...")

#    print(special_attack, special_defense)
    factor_1 *= 1

    if move.is_physical() and move.internal_name != moves.FOULPLAY:
        damage = round( (round(int(attacker.level) * 0.4 + 2) * int(base_damage) * (
                attack / (
                50 * defense)) * factor_1 + 2) * critical_multiplier * factor_2 * rand_num / 100 * stab * effectivity * factor_3 - 0.499)
    if move.is_special() and move.internal_name not in (moves.PSYSHOCK, moves.PSYSTRIKE, moves.SECRETSWORD):
        damage = round( (round(int(attacker.level) * 0.4 + 2) * int(base_damage) * (
                special_attack / (
                50 * special_defense)) * factor_1 + 2) * critical_multiplier * factor_2 * rand_num / 100 * stab * effectivity * factor_3 - 0.499)
    return damage  # TODO


def choose_move(moves):
    return GUI.MoveChooser(moves)


def start_single_battle(own: Trainer, enemy: Trainer, _weather: str, _terrain: str):
    textbox(enemy.get_trainer_class() + enemy.get_name() + "would like to battle!")
    textbox(
        enemy.get_trainer_class() + enemy.get_name() + "sent out" + enemy.team.get_first_pokemon().get_species_name() + "!")
    if own.team.get_first_pokemon().has_nickname():
        textbox("Go, " + own.team.get_first_pokemon().nickname + "!")
        textbox("What will" + own.team.get_first_pokemon().nickname + "do?", press_to_remove=False)
    else:
        textbox("Go, " + own.team.get_first_pokemon().get_species_name() + "!")
        textbox("What will" + own.team.get_first_pokemon().get_species_name() + "do?", press_to_remove=False)
    battle_active = True
    while battle_active:
        while not own.get_team().get_first_pokemon().is_fainted():
            player_mon, ai_mon = own.get_team().get_first_pokemon(), enemy.get_team().get_first_pokemon()
            ai_move = AI.choose_move(own, enemy)
            player_move = choose_move(player_mon.moves)
            if player_mon.speed > ai_mon.speed:
                if move_hits(player_mon, ai_mon, _weather, _terrain, player_move):
                    damage = calculate_damage(player_mon, ai_mon, _weather, _terrain, player_move)
                    ai_mon.set_current_hp(ai_mon.hp - damage)
            if ai_mon.speed > player_mon.speed or ai_mon.speed == player_mon.speed:
                if move_hits(ai_mon, player_mon, _weather, _terrain, ai_move):
                    ...


def start_double_battle():
    pass


def start_tag_battle():
    pass


def start_wild_battle():
    pass
