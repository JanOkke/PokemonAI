import battle

class MoveAction:
    pass


class SwitchAction:
    pass


class ItemAction:
    pass


class Action:
    def __init__(self, type: classmethod, user: battle.Pokemon, act: battle.Move, _battle: battle.Battle, opponent: battle.Pokemon):
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

    def handle_actions(self):
        if not self.handled:
            PRIOLIST = []
            for action in self.actions:
                if action.type == MoveAction:
                    PRIOLIST.append([action.act.priority, action.user.speed, action])
                elif action.type == SwitchAction:
                    PRIOLIST.append([7, action.user.speed, action])
                elif action.type == ItemAction:
                    PRIOLIST.append([6, action.user.speed, action])
            PRIOLIST.sort(reverse=True)
            print("To handle:\n")
            for priority, speed, action in PRIOLIST:
                print("Priority:", priority, "Pokemon Speed:", speed, "Action:", action.act)
            self.handled = True

