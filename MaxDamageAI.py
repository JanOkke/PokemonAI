from battle import Pokemon, Move, calculate_damage
from FormBuilderUI.main import percentage

class BattleAI:
    def __init__(self, attacker: Pokemon, defender: Pokemon):
        self.attacker = attacker
        self.defender = defender

    def get_highest_damage_action(self):
        damages = []
        for move in self.attacker.moves:
            dmg = percentage(self.defender.hp, calculate_damage(self.attacker, self.defender, move=move, can_crit=False, printing=False, _terrain="", _weather="", rand_num=100))
            print(dmg, move.name)
            damages.append([dmg, move])
        return max(damages)



TestMon1 = Pokemon.create_new_pokemon(100, 56)
TestMon2 = Pokemon.create_new_pokemon(101, 56)
TestMon1.moves.append(Move.create_new_move(None, 15))
TestMon1.moves.append(Move.create_new_move(None, 17))
TestMon1.moves.append(Move.create_new_move(None, 33))

BattleAI(TestMon1, TestMon2).get_highest_damage_action()