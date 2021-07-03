import items

ITEMS = []

def add_to_bag(item: str):
    if item in items:
        ITEMS.append(item)