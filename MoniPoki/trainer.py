from team import Team, EmptyTeam
from items import ITEMS
from errors import WrongItem

class Trainer:
    def __init__(self, trainer_class: str, name: str, money: int, iq: int):
        self.trainer_class = trainer_class
        self.name = name
        self.money = money
        self.iq = iq
        self.team = EmptyTeam
        self.items = []

    def get_name(self) -> str:
        return self.name

    def get_trainer_class(self) -> str:
        return self.trainer_class

    def get_money(self) -> int:
        return self.money

    def get_iq(self) -> int:
        return self.iq

    def give_team(self, team: Team):
        self.team = team

    def get_team(self) -> Team:
        return self.team

    def add_item(self, item: str):
        if item in ITEMS:
            self.items.append(item)
        else:
            raise WrongItem(item)

    def get_items(self) -> [str]:
        return self.items
