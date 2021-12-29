def is_legal(_move, _battle, user) -> bool:
    if user.is_fainted():
        print("Illegal, pokemon {} fainted!".format(user.get_species_name()))
        return False
    return True # TODO

