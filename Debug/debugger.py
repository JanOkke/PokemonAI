class Pokemon:
    def __init__(self):
        self.species = ""
        self.nature = ""
        self.level = ""
        self.ability = ""
        self.item = ""
        self.evs = ""
        self.moves = []
    def __str__(self):
        s = "Name: " + self.species + "\nNature: " + self.nature + "\nLevel: " + self.level + "\nAbility: " + self.ability + "\nItem: " + self.item + "\nMoves:"
        for move in self.moves:
            s += "\n" + move
        return s


class Battle:
    def __init__(self):
        self.team = []
        self.name = ""


def create_pokepaste(mon: Pokemon, battler: str):
    text = ""
    text += battler + "("
    text += mon.species.capitalize() + ") @ " + mon.item + "\n"
    text += "Ability: " + mon.ability + "\n"
    text += "Level: " + mon.level + "\n"
    #text += "Level: 76\n"
    text += "EVs:" + mon.evs +"\n"
    text += mon.nature.capitalize() + " Nature" + "\n"
    for move in mon.moves:
        text += "- " + move + "\n"
    return text


def run(file, teamname=None):
    #f = open('brendanvictoryroad.txt')
    f = file

    pokemons = []
    levels = []
    items = []
    abilities = []
    natures = []
    evs = []
    moves1 = []
    moves2 = []
    moves3 = []
    moves4 = []

    for line in f:
        line = line.strip("\n")
        data = line.split(",")
        #print()
        for d in data:
            if len(pokemons) < 6:
                pokemons.append(d)
            elif len(levels) < 6:
                levels.append(d)
            elif len(items) < 6:
                items.append(d)
            elif len(abilities) < 6:
                abilities.append(d)
            elif len(natures) < 6:
                natures.append(d)
            elif len(items) < 6:
                items.append(d)
            elif len(evs) < 6:
                evs.append(d)
            elif len(moves1) < 6:
                moves1.append(d)
            elif len(moves2) < 6:
                moves2.append(d)
            elif len(moves3) < 6:
                moves3.append(d)
            elif len(moves4) < 6:
                moves4.append(d)
            #print(d)

    #print(pokemons)
    #print(levels)
    #print(items)
    #print(abilities)
    #print(natures)
    #print(evs)
    #print(moves1)
    #print(moves2)
    #print(moves3)
    #print(moves4)

    team = Battle()
    #team.name = "BrendanVictoryRoad"
    team.name = teamname
    for n in range(6):
        #print(n)
        pokemon = Pokemon()
        pokemon.species = pokemons[n]
        pokemon.level = levels[n]
        pokemon.item = items[n]
        pokemon.ability = abilities[n]
        pokemon.nature = natures[n]
        pokemon.evs = evs[n]
        pokemon.moves.append(moves1[n])
        pokemon.moves.append(moves2[n])
        pokemon.moves.append(moves3[n])
        pokemon.moves.append(moves4[n])
        team.team.append(pokemon)
        #print(pokemon)

    #for mon in team.team:
        #print(create_pokepaste(mon, team.name))
    return team.team