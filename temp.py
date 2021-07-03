f = open("levelcurve.txt", "r")

erratic = {}
fast = {}
mediumfast = {}
mediumslow = {}
slow = {}
fluctuating = {}
for line in f:
    line = line.strip("\n")
    #print(line)
    data = line.split(",")
    erratic[int(data[0])] = int(data[1])
    fast[int(data[0])] = int(data[2])
    mediumfast[int(data[0])] = int(data[3])
    mediumslow[int(data[0])] = int(data[4])
    slow[int(data[0])] = int(data[5])
    fluctuating[int(data[0])] = int(data[6])



print(fluctuating)