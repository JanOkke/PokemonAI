class WrongExperienceGroup(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + " is not a valid experience group. " + "See growth.py for experience groups."


class WrongLevel(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + " is not a valid level. " + "See settings.py for the level caps."


class ExperienceError(BaseException):
    def __init__(self, e, group):
        self.e = e
        self.group = group

    def __str__(self):
        return str(self.e) + " is not a valid experience amount for the " + self.group + " experience group. " + \
               "See settings.py for the level caps."


class EggStepsLessThanZero(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + " is not a valid value for egg steps. " + "The egg steps must be positive."


class GenderError(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + " is not a valid gender. " + "See gender.py for the available genders."


class PokemonHasItem(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + " already holds an item."


class MoveIndexError(BaseException):
    def __init__(self, e, moves):
        self.e = e
        self.moves = moves

    def __str__(self):
        return str(self.e) + " is an invalid move index in " + str(self.moves)


class InvalidMoveArgument(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + "is an invalid move!"


class TeamSlotError(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + "is an invalid team slot number!"


class EmptyPartyError(BaseException):
    def __str__(self):
        return "Party is empty!"


class WrongItem(BaseException):
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return str(self.e) + "is an invalid item!"


class NoStockpile(BaseException):
    def __str__(self):
        return "No stockpiles used!"
