from battle import Pokemon, Move, calculate_damage
from FormBuilderUI.main import percentage
from loader import load_from_poke_paste
from os import getcwd

class BattleAI:
    def __init__(self, attacker: Pokemon, defender: Pokemon):
        self.attacker = attacker
        self.defender = defender

    def get_highest_damage_action(self):
        damages = []
        for move in self.attacker.moves:
            dmg = percentage(self.defender.hp, calculate_damage(self.attacker, self.defender, move=move, can_crit=False, printing=False, _terrain="", _weather="", rand_num=100))
            print(dmg, move.name, 'from:', self.attacker.get_species_name(), 'to:', self.defender.get_species_name(), 'Accuracy:', move.accuracy)
            damages.append([dmg, move])
        return max(damages)



mon1,mon2, mon3, mon4 = load_from_poke_paste(open(getcwd() + r'\Teams\falkner.txt'))

print(BattleAI(mon1, mon2).get_highest_damage_action())
print(BattleAI(mon2, mon1).get_highest_damage_action())
print(BattleAI(mon1, mon3).get_highest_damage_action())
print(BattleAI(mon3, mon1).get_highest_damage_action())