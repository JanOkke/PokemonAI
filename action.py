class MoveAction:
    pass

class SwitchAction:
    pass

class ItemAction:
    pass

class Action:
    def __init__(self, type, user):
        self.type = type
        self.user = user


class ActionOrder:
    def __init__(self):
        self.actions = []
        self.handled = False

    def add_task(self, action: Action):
        self.actions.append(action)

    def handle(self):
        if not self.handled:
            for action in self.actions:
                if action.type == MoveAction:
                    print("It is a move!")
            self.handled = True