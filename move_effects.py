from pokemon import Pokemon, _types, status, species
from move import Move, moves
import random
from team import Team

FAIL = "Fail"
FLINCH = "Flinch"

def execute(attacker: Pokemon, defender: Pokemon, move: Move, party: Team, gravity=False, battle_turn=-1):
    code = move.function_code
    if code == "000":
        return
    if code == "001":
        if gravity:
            return FAIL
    if code == "002":
        move.type = _types.TYPELESS
        attacker.take_damage(round(attacker.total_hp / 4))
    if code == "003":
        if defender.status == status.NO_STATUS:
            defender.status = status.SLEEP
        if attacker.get_species_name() == "Meloetta" and move.name == moves.RELICSONG:
            attacker.set_form(1) # dance form

    if code == "004":
        if defender.is_drowsy or defender.status == status.SLEEP:
            return FAIL
        defender.is_drowsy = True

    if code == "005":
        if defender.status == status.NO_STATUS and not defender.has_type(_types.POISON) and not defender.has_type(_types.STEEL):
            defender.status = status.POISON

    if code == "006":
        if defender.status == status.NO_STATUS and not defender.has_type(_types.POISON) and not defender.has_type(_types.STEEL):
            defender.status = status.BADLY_POISONED
            defender.statusCount = 0
        elif move.name == moves.TOXIC:
            return FAIL

    if code == "007":
        if defender.status == status.NO_STATUS and not defender.has_type(_types.ELECTRIC):
            defender.status = status.PARALYSIS
        elif move.name == moves.THUNDERWAVE:
            return FAIL

    if code == "008":
        # THUNDER EFFECTS ARE IN BATTLE.PY
        if defender.status == status.NO_STATUS and not defender.has_type(_types.ELECTRIC):
            defender.status = status.PARALYSIS
        elif move.name == moves.THUNDERWAVE:
            return FAIL

    if code == "009":
        if defender.status == status.NO_STATUS and not defender.has_type(_types.ELECTRIC):
            defender.status = status.PARALYSIS
        return FLINCH

    if code == "00A":
        if defender.status == status.NO_STATUS and not defender.has_type(_types.FIRE):
            defender.status = status.BURN
        elif move.name == moves.WILLOWISP:
            return FAIL

    if code == "00B":
        if defender.status == status.NO_STATUS and not defender.has_type(_types.FIRE):
            defender.status = status.BURN
        return FLINCH

    if code in ("00C", "00D"):
        if defender.status == status.NO_STATUS and not defender.has_type(_types.ICE):
            defender.status = status.FROZEN

    if code in ("00F", "010"):
        return FLINCH

    if code == "011":
        if attacker.status == status.SLEEP:
            return FLINCH
        else:
            return FAIL

    if code == "012":
        if battle_turn == 1:
            return FLINCH
        else:
            return FAIL

    if code in ("013", "014"):
        defender.is_confused = True

    if code == "016":
        if not defender.is_genderless() and attacker.gender != defender.gender:
            defender.is_attracted = True

    if code == "017":
        if defender.status == status.NO_STATUS:
            return
        ran = random.randint(0,2)
        if ran == 0:
            defender.status = status.FROZEN
        if ran == 1:
            defender.status = status.BURN
        if ran == 2:
            defender.status = status.PARALYSIS

    if code == "018":
        if attacker.status in (status.BURN, status.PARALYSIS, status.FROZEN):
            attacker.status = status.NO_STATUS
        else:
            return FAIL

    if code == "019":
        mons = party.get_party()
        for mon in mons:
            mon.status = status.NO_STATUS

    if code == "01A":
        if attacker.safeguard:
            return FAIL
        else:
            attacker.safeguard = True

    if code == "01B":
        if defender.status != status.NO_STATUS:
            defender.status = attacker.status
        else:
            return FAIL

    if code == "01C":
        if attacker.stat_stages[0] < 6:
            attacker.stat_stages[0] += 1