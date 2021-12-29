NO_STATUS = 0
SLEEP = 1
POISON = 2
BURN = 3
PARALYSIS = 4
FROZEN = 5
BADLY_POISONED = 6


def get_name(_id: int) -> str:
    names = ["healthy", "asleep", "poisoned", "burned", "paralyzed", "frozen", "badly poisoned"]
    return names[_id]
