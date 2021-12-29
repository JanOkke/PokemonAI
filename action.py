from pokemon import Pokemon
from move import Move
from battle import calculate_damage, Battle

class MoveAction:
    pass


class SwitchAction:
    pass


class ItemAction:
    pass


class Action:
    def __init__(self, type: classmethod, user: Pokemon, act: Move or Pokemon, _battle: Battle,
                 opponent: Pokemon):
        self.type = type
        self.user = user
        self.act = act
        self.battle = _battle
        self.opponent = opponent


class ActionOrder:
    def __init__(self):
        self.actions = []
        self.handled = False

    def add_action(self, action: Action):
        self.actions.append(action)

    def handle_actions(self, ignore_prio=False):
        if ignore_prio:
            OUTCOME = []
            action_1, action_2 =  self.actions
            if action_1.type == MoveAction:
                if action_2.type == SwitchAction:
                    action_1.opponent = action_2.act
                damage = calculate_damage(action_1.user, action_1.opponent, action_1.battle.weather,
                                              action_1.battle.terrain, action_1.act, can_crit=False, rand_num=100, printing=False)
                action_1.opponent.take_damage(damage)
                print(action_1.opponent.get_species_name(), 'took', damage, 'damage from move', action_1.act)
                OUTCOME.append([action_1.type, damage, action_1.user, action_1.opponent, action_1.act, action_2])
            elif action_1.type == SwitchAction:
                action_1.battle.team1.change_lead(action_1.act)
                OUTCOME.append([action_1.type, 0, action_1.user, action_1.opponent, action_1.act, action_2])
            if action_2.type == MoveAction:
                if action_1.type == SwitchAction:
                    action_2.opponent = action_1.act
                damage = calculate_damage(action_2.user, action_2.opponent, action_2.battle.weather,
                                              action_2.battle.terrain, action_2.act, can_crit=False, rand_num=100, printing=False)
                action_2.opponent.take_damage(damage)
                print(action_2.opponent.get_species_name(), 'took', damage, 'damage from move', action_2.act)
                OUTCOME.append([action_2.type, damage, action_2.user, action_2.opponent, action_2.act, action_1])
            elif action_2.type == SwitchAction:
                action_2.battle.team1.change_lead(action_2.act)
                OUTCOME.append([action_2.type, 0, action_2.user, action_2.opponent, action_2.act, action_1])
            return OUTCOME
        if not self.handled:
            OUTCOME = []
            PRIOLIST = []
            for action in self.actions:
                if action.type == MoveAction:
                    PRIOLIST.append([action.act.priority, action.user.speed, action])
                elif action.type == SwitchAction:
                    PRIOLIST.append([7, action.user.speed, action])
                elif action.type == ItemAction:
                    PRIOLIST.append([6, action.user.speed, action])
            PRIOLIST.sort(reverse=True)
            #print("To handle:\n")
            count = 0
            for priority, speed, action in PRIOLIST:
                count += 1
                #if action.type == SwitchAction:
                #    print(priority, action.act.get_species_name(), count, action.opponent.get_species_name(), action.user.get_species_name())
                #else:
                #    print(priority, action.act, count, action.opponent.get_species_name(), action.user.get_species_name())
                #print("Priority:", priority, "Pokemon Speed:", speed, "Action:", action.act)
                if action.type == MoveAction:
                    damage = calculate_damage(action.user, action.opponent, action.battle.weather,
                                                  action.battle.terrain, action.act, can_crit=False, rand_num=100, printing=False)
                    action.opponent.take_damage(damage)
                    OUTCOME.append([action.type, damage, action.user, action.opponent, action.act])
                if action.type == SwitchAction:
                    action.battle.team1.change_lead(action.act)
                    PRIOLIST[1][2].opponent = action.act
                    OUTCOME.append([action.type, 0, action.user, action.opponent, action.act])
            self.handled = True
            return OUTCOME
