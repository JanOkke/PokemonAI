"""f = open("moves.txt", "r")
o = open("moves.py", "w")
line = 0
itemnames = []
for lines in f:
    line += 1
    if line == 1:
        continue
    if lines[0] == "#":
        continue
    lines = lines.strip("\n")
    data = lines.split(",")
    try:
        _id = data[0]
        capsname = data[1]
        name = data[2]
    except ValueError:
        print(data[2])
        continue
    capsname = capsname.strip(" ")
    #name = name.replace(" ", "_")
    itemnames.append([capsname, name])

for item in itemnames:
    o.write(item[0].upper() + ' = "' + item[0] + '"\n')

o.write("\n")
o.write("MOVES = [")
for item in itemnames:
    o.write(item[0].upper() + ", ")
o.write("]\n")"""
"""
f = open("moves.txt", "r")
o = open("_moves.py", "w")

o.write("from move import Move\n\n")

nline = 0
for line in f:
    nline += 1
    if nline == 1:
        continue
    if line[0] == "#":
        continue
    line = line.strip("\n")
    data = line.split(",", maxsplit=13)
    #for d in data:
    #    print(d)
    try:
        _id, internalname, name, code, power, type, category, accuracy, pp, effchance, target, prio, flags, description = data
        if description.__contains__("'"):
            description = description.replace("'", "")
        print(description)
        #print(description)
    except Exception as e:
        exit(str(data) + str(e))
    #print(name, power, pp, type)
    #print("NEWLINE\n")

    o.write("########")
    for _ in range(len(str(internalname))):
        o.write("#")
    o.write("\n")
    o.write("### " + internalname + " ###\n")
    o.write("########")
    for _ in range(len(str(internalname))):
        o.write("#")
    o.write("\n\n")
    o.write("MOVE_" + internalname + " = Move()\n")
    o.write("MOVE_" + internalname + ".name = '" + name + "'\n")
    o.write("MOVE_" + internalname + ".type = '" + type + "'\n")
    o.write("MOVE_" + internalname + ".base_damage = '" + power + "'\n")
    o.write("MOVE_" + internalname + ".category = '" + category + "'\n")
    o.write("MOVE_" + internalname + ".pp = '" + pp + "'\n")
    o.write("MOVE_" + internalname + ".accuracy = '" + accuracy + "'\n")
    o.write("MOVE_" + internalname + ".priority = '" + prio + "'\n")
    o.write("MOVE_" + internalname + ".target = '" + target + "'\n")
    o.write("MOVE_" + internalname + ".additional_effect_chance = '" + effchance + "'\n")
    o.write("MOVE_" + internalname + ".description = '" + description + "'\n")
    o.write("\n")
"""

#import moves
#f = open('moves_base.py', 'a')
#for move in moves.MOVES:
#    f.write(move + ' = battle.Move()\n')

f = open('PBS//abilities.txt')
for line in f:
    try:
        data = line.split(",")
        print(data[2].replace(' ', '_').upper(), "= '" + data[1] + "'")
    except Exception:
        pass