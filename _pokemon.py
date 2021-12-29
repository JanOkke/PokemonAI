from pokemon import Pokemon
from _types import *
import species

#################
### BULBASAUR ###
#################

BULBASAUR = Pokemon()
BULBASAUR.species = 1
BULBASAUR.types = GRASS
BULBASAUR.types = [BULBASAUR.types, POISON]
BULBASAUR.abilities = species.abilities(1)
BULBASAUR.hidden_ability = species.hidden_ability(1)

###############
### IVYSAUR ###
###############

IVYSAUR = Pokemon()
IVYSAUR.species = 2
IVYSAUR.types = GRASS
IVYSAUR.types = [IVYSAUR.types, POISON]
IVYSAUR.abilities = species.abilities(2)
IVYSAUR.hidden_ability = species.hidden_ability(2)

################
### VENUSAUR ###
################

VENUSAUR = Pokemon()
VENUSAUR.species = 3
VENUSAUR.types = GRASS
VENUSAUR.types = [VENUSAUR.types, POISON]
VENUSAUR.abilities = species.abilities(3)
VENUSAUR.hidden_ability = species.hidden_ability(3)

##################
### CHARMANDER ###
##################

CHARMANDER = Pokemon()
CHARMANDER.species = 4
CHARMANDER.types = FIRE
CHARMANDER.abilities = species.abilities(4)
CHARMANDER.hidden_ability = species.hidden_ability(4)

##################
### CHARMELEON ###
##################

CHARMELEON = Pokemon()
CHARMELEON.species = 5
CHARMELEON.types = FIRE
CHARMELEON.abilities = species.abilities(5)
CHARMELEON.hidden_ability = species.hidden_ability(5)

#################
### CHARIZARD ###
#################

CHARIZARD = Pokemon()
CHARIZARD.species = 6
CHARIZARD.types = FIRE
CHARIZARD.types = [CHARIZARD.types, FLYING]
CHARIZARD.abilities = species.abilities(6)
CHARIZARD.hidden_ability = species.hidden_ability(6)

################
### SQUIRTLE ###
################

SQUIRTLE = Pokemon()
SQUIRTLE.species = 7
SQUIRTLE.types = WATER
SQUIRTLE.abilities = species.abilities(7)
SQUIRTLE.hidden_ability = species.hidden_ability(7)

#################
### WARTORTLE ###
#################

WARTORTLE = Pokemon()
WARTORTLE.species = 8
WARTORTLE.types = WATER
WARTORTLE.abilities = species.abilities(8)
WARTORTLE.hidden_ability = species.hidden_ability(8)

#################
### BLASTOISE ###
#################

BLASTOISE = Pokemon()
BLASTOISE.species = 9
BLASTOISE.types = WATER
BLASTOISE.abilities = species.abilities(9)
BLASTOISE.hidden_ability = species.hidden_ability(9)

################
### CATERPIE ###
################

CATERPIE = Pokemon()
CATERPIE.species = 10
CATERPIE.types = BUG
CATERPIE.abilities = species.abilities(10)
CATERPIE.hidden_ability = species.hidden_ability(10)

###############
### METAPOD ###
###############

METAPOD = Pokemon()
METAPOD.species = 11
METAPOD.types = BUG
METAPOD.abilities = species.abilities(11)
METAPOD.hidden_ability = species.hidden_ability(11)

##################
### BUTTERFREE ###
##################

BUTTERFREE = Pokemon()
BUTTERFREE.species = 12
BUTTERFREE.types = BUG
BUTTERFREE.types = [BUTTERFREE.types, FLYING]
BUTTERFREE.abilities = species.abilities(12)
BUTTERFREE.hidden_ability = species.hidden_ability(12)

##############
### WEEDLE ###
##############

WEEDLE = Pokemon()
WEEDLE.species = 13
WEEDLE.types = BUG
WEEDLE.types = [WEEDLE.types, POISON]
WEEDLE.abilities = species.abilities(13)
WEEDLE.hidden_ability = species.hidden_ability(13)

##############
### KAKUNA ###
##############

KAKUNA = Pokemon()
KAKUNA.species = 14
KAKUNA.types = BUG
KAKUNA.types = [KAKUNA.types, POISON]
KAKUNA.abilities = species.abilities(14)
KAKUNA.hidden_ability = species.hidden_ability(14)

################
### BEEDRILL ###
################

BEEDRILL = Pokemon()
BEEDRILL.species = 15
BEEDRILL.types = BUG
BEEDRILL.types = [BEEDRILL.types, POISON]
BEEDRILL.abilities = species.abilities(15)
BEEDRILL.hidden_ability = species.hidden_ability(15)

##############
### PIDGEY ###
##############

PIDGEY = Pokemon()
PIDGEY.species = 16
PIDGEY.types = NORMAL
PIDGEY.types = [PIDGEY.types, FLYING]
PIDGEY.abilities = species.abilities(16)
PIDGEY.hidden_ability = species.hidden_ability(16)

#################
### PIDGEOTTO ###
#################

PIDGEOTTO = Pokemon()
PIDGEOTTO.species = 17
PIDGEOTTO.types = NORMAL
PIDGEOTTO.types = [PIDGEOTTO.types, FLYING]
PIDGEOTTO.abilities = species.abilities(17)
PIDGEOTTO.hidden_ability = species.hidden_ability(17)

###############
### PIDGEOT ###
###############

PIDGEOT = Pokemon()
PIDGEOT.species = 18
PIDGEOT.types = NORMAL
PIDGEOT.types = [PIDGEOT.types, FLYING]
PIDGEOT.abilities = species.abilities(18)
PIDGEOT.hidden_ability = species.hidden_ability(18)

###############
### RATTATA ###
###############

RATTATA = Pokemon()
RATTATA.species = 19
RATTATA.types = NORMAL
RATTATA.abilities = species.abilities(19)
RATTATA.hidden_ability = species.hidden_ability(19)

################
### RATICATE ###
################

RATICATE = Pokemon()
RATICATE.species = 20
RATICATE.types = NORMAL
RATICATE.abilities = species.abilities(20)
RATICATE.hidden_ability = species.hidden_ability(20)

###############
### SPEAROW ###
###############

SPEAROW = Pokemon()
SPEAROW.species = 21
SPEAROW.types = NORMAL
SPEAROW.types = [SPEAROW.types, FLYING]
SPEAROW.abilities = species.abilities(21)
SPEAROW.hidden_ability = species.hidden_ability(21)

##############
### FEAROW ###
##############

FEAROW = Pokemon()
FEAROW.species = 22
FEAROW.types = NORMAL
FEAROW.types = [FEAROW.types, FLYING]
FEAROW.abilities = species.abilities(22)
FEAROW.hidden_ability = species.hidden_ability(22)

#############
### EKANS ###
#############

EKANS = Pokemon()
EKANS.species = 23
EKANS.types = POISON
EKANS.abilities = species.abilities(23)
EKANS.hidden_ability = species.hidden_ability(23)

#############
### ARBOK ###
#############

ARBOK = Pokemon()
ARBOK.species = 24
ARBOK.types = POISON
ARBOK.abilities = species.abilities(24)
ARBOK.hidden_ability = species.hidden_ability(24)

###############
### PIKACHU ###
###############

PIKACHU = Pokemon()
PIKACHU.species = 25
PIKACHU.types = ELECTRIC
PIKACHU.abilities = species.abilities(25)
PIKACHU.hidden_ability = species.hidden_ability(25)

##############
### RAICHU ###
##############

RAICHU = Pokemon()
RAICHU.species = 26
RAICHU.types = ELECTRIC
RAICHU.abilities = species.abilities(26)
RAICHU.hidden_ability = species.hidden_ability(26)

#################
### SANDSHREW ###
#################

SANDSHREW = Pokemon()
SANDSHREW.species = 27
SANDSHREW.types = GROUND
SANDSHREW.abilities = species.abilities(27)
SANDSHREW.hidden_ability = species.hidden_ability(27)

#################
### SANDSLASH ###
#################

SANDSLASH = Pokemon()
SANDSLASH.species = 28
SANDSLASH.types = GROUND
SANDSLASH.abilities = species.abilities(28)
SANDSLASH.hidden_ability = species.hidden_ability(28)

#################
### NIDORANfE ###
#################

NIDORANfE = Pokemon()
NIDORANfE.types = POISON
################
### NIDORINA ###
################

NIDORINA = Pokemon()
NIDORINA.species = 30
NIDORINA.types = POISON
NIDORINA.abilities = species.abilities(30)
NIDORINA.hidden_ability = species.hidden_ability(30)

#################
### NIDOQUEEN ###
#################

NIDOQUEEN = Pokemon()
NIDOQUEEN.species = 31
NIDOQUEEN.types = POISON
NIDOQUEEN.types = [NIDOQUEEN.types, GROUND]
NIDOQUEEN.abilities = species.abilities(31)
NIDOQUEEN.hidden_ability = species.hidden_ability(31)

#################
### NIDORANmA ###
#################

NIDORANmA = Pokemon()
NIDORANmA.types = POISON
################
### NIDORINO ###
################

NIDORINO = Pokemon()
NIDORINO.species = 33
NIDORINO.types = POISON
NIDORINO.abilities = species.abilities(33)
NIDORINO.hidden_ability = species.hidden_ability(33)

################
### NIDOKING ###
################

NIDOKING = Pokemon()
NIDOKING.species = 34
NIDOKING.types = POISON
NIDOKING.types = [NIDOKING.types, GROUND]
NIDOKING.abilities = species.abilities(34)
NIDOKING.hidden_ability = species.hidden_ability(34)

################
### CLEFAIRY ###
################

CLEFAIRY = Pokemon()
CLEFAIRY.species = 35
CLEFAIRY.types = FAIRY
CLEFAIRY.abilities = species.abilities(35)
CLEFAIRY.hidden_ability = species.hidden_ability(35)

################
### CLEFABLE ###
################

CLEFABLE = Pokemon()
CLEFABLE.species = 36
CLEFABLE.types = FAIRY
CLEFABLE.abilities = species.abilities(36)
CLEFABLE.hidden_ability = species.hidden_ability(36)

##############
### VULPIX ###
##############

VULPIX = Pokemon()
VULPIX.species = 37
VULPIX.types = FIRE
VULPIX.abilities = species.abilities(37)
VULPIX.hidden_ability = species.hidden_ability(37)

#################
### NINETALES ###
#################

NINETALES = Pokemon()
NINETALES.species = 38
NINETALES.types = FIRE
NINETALES.abilities = species.abilities(38)
NINETALES.hidden_ability = species.hidden_ability(38)

##################
### JIGGLYPUFF ###
##################

JIGGLYPUFF = Pokemon()
JIGGLYPUFF.species = 39
JIGGLYPUFF.types = NORMAL
JIGGLYPUFF.types = [JIGGLYPUFF.types, FAIRY]
JIGGLYPUFF.abilities = species.abilities(39)
JIGGLYPUFF.hidden_ability = species.hidden_ability(39)

##################
### WIGGLYTUFF ###
##################

WIGGLYTUFF = Pokemon()
WIGGLYTUFF.species = 40
WIGGLYTUFF.types = NORMAL
WIGGLYTUFF.types = [WIGGLYTUFF.types, FAIRY]
WIGGLYTUFF.abilities = species.abilities(40)
WIGGLYTUFF.hidden_ability = species.hidden_ability(40)

#############
### ZUBAT ###
#############

ZUBAT = Pokemon()
ZUBAT.species = 41
ZUBAT.types = POISON
ZUBAT.types = [ZUBAT.types, FLYING]
ZUBAT.abilities = species.abilities(41)
ZUBAT.hidden_ability = species.hidden_ability(41)

##############
### GOLBAT ###
##############

GOLBAT = Pokemon()
GOLBAT.species = 42
GOLBAT.types = POISON
GOLBAT.types = [GOLBAT.types, FLYING]
GOLBAT.abilities = species.abilities(42)
GOLBAT.hidden_ability = species.hidden_ability(42)

##############
### ODDISH ###
##############

ODDISH = Pokemon()
ODDISH.species = 43
ODDISH.types = GRASS
ODDISH.types = [ODDISH.types, POISON]
ODDISH.abilities = species.abilities(43)
ODDISH.hidden_ability = species.hidden_ability(43)

#############
### GLOOM ###
#############

GLOOM = Pokemon()
GLOOM.species = 44
GLOOM.types = GRASS
GLOOM.types = [GLOOM.types, POISON]
GLOOM.abilities = species.abilities(44)
GLOOM.hidden_ability = species.hidden_ability(44)

#################
### VILEPLUME ###
#################

VILEPLUME = Pokemon()
VILEPLUME.species = 45
VILEPLUME.types = GRASS
VILEPLUME.types = [VILEPLUME.types, POISON]
VILEPLUME.abilities = species.abilities(45)
VILEPLUME.hidden_ability = species.hidden_ability(45)

#############
### PARAS ###
#############

PARAS = Pokemon()
PARAS.species = 46
PARAS.types = BUG
PARAS.types = [PARAS.types, GRASS]
PARAS.abilities = species.abilities(46)
PARAS.hidden_ability = species.hidden_ability(46)

################
### PARASECT ###
################

PARASECT = Pokemon()
PARASECT.species = 47
PARASECT.types = BUG
PARASECT.types = [PARASECT.types, GRASS]
PARASECT.abilities = species.abilities(47)
PARASECT.hidden_ability = species.hidden_ability(47)

###############
### VENONAT ###
###############

VENONAT = Pokemon()
VENONAT.species = 48
VENONAT.types = BUG
VENONAT.types = [VENONAT.types, POISON]
VENONAT.abilities = species.abilities(48)
VENONAT.hidden_ability = species.hidden_ability(48)

################
### VENOMOTH ###
################

VENOMOTH = Pokemon()
VENOMOTH.species = 49
VENOMOTH.types = BUG
VENOMOTH.types = [VENOMOTH.types, POISON]
VENOMOTH.abilities = species.abilities(49)
VENOMOTH.hidden_ability = species.hidden_ability(49)

###############
### DIGLETT ###
###############

DIGLETT = Pokemon()
DIGLETT.species = 50
DIGLETT.types = GROUND
DIGLETT.abilities = species.abilities(50)
DIGLETT.hidden_ability = species.hidden_ability(50)

###############
### DUGTRIO ###
###############

DUGTRIO = Pokemon()
DUGTRIO.species = 51
DUGTRIO.types = GROUND
DUGTRIO.abilities = species.abilities(51)
DUGTRIO.hidden_ability = species.hidden_ability(51)

##############
### MEOWTH ###
##############

MEOWTH = Pokemon()
MEOWTH.species = 52
MEOWTH.types = NORMAL
MEOWTH.abilities = species.abilities(52)
MEOWTH.hidden_ability = species.hidden_ability(52)

###############
### PERSIAN ###
###############

PERSIAN = Pokemon()
PERSIAN.species = 53
PERSIAN.types = NORMAL
PERSIAN.abilities = species.abilities(53)
PERSIAN.hidden_ability = species.hidden_ability(53)

###############
### PSYDUCK ###
###############

PSYDUCK = Pokemon()
PSYDUCK.species = 54
PSYDUCK.types = WATER
PSYDUCK.abilities = species.abilities(54)
PSYDUCK.hidden_ability = species.hidden_ability(54)

###############
### GOLDUCK ###
###############

GOLDUCK = Pokemon()
GOLDUCK.species = 55
GOLDUCK.types = WATER
GOLDUCK.abilities = species.abilities(55)
GOLDUCK.hidden_ability = species.hidden_ability(55)

##############
### MANKEY ###
##############

MANKEY = Pokemon()
MANKEY.species = 56
MANKEY.types = FIGHTING
MANKEY.abilities = species.abilities(56)
MANKEY.hidden_ability = species.hidden_ability(56)

################
### PRIMEAPE ###
################

PRIMEAPE = Pokemon()
PRIMEAPE.species = 57
PRIMEAPE.types = FIGHTING
PRIMEAPE.abilities = species.abilities(57)
PRIMEAPE.hidden_ability = species.hidden_ability(57)

#################
### GROWLITHE ###
#################

GROWLITHE = Pokemon()
GROWLITHE.species = 58
GROWLITHE.types = FIRE
GROWLITHE.abilities = species.abilities(58)
GROWLITHE.hidden_ability = species.hidden_ability(58)

################
### ARCANINE ###
################

ARCANINE = Pokemon()
ARCANINE.species = 59
ARCANINE.types = FIRE
ARCANINE.abilities = species.abilities(59)
ARCANINE.hidden_ability = species.hidden_ability(59)

###############
### POLIWAG ###
###############

POLIWAG = Pokemon()
POLIWAG.species = 60
POLIWAG.types = WATER
POLIWAG.abilities = species.abilities(60)
POLIWAG.hidden_ability = species.hidden_ability(60)

#################
### POLIWHIRL ###
#################

POLIWHIRL = Pokemon()
POLIWHIRL.species = 61
POLIWHIRL.types = WATER
POLIWHIRL.abilities = species.abilities(61)
POLIWHIRL.hidden_ability = species.hidden_ability(61)

#################
### POLIWRATH ###
#################

POLIWRATH = Pokemon()
POLIWRATH.species = 62
POLIWRATH.types = WATER
POLIWRATH.types = [POLIWRATH.types, FIGHTING]
POLIWRATH.abilities = species.abilities(62)
POLIWRATH.hidden_ability = species.hidden_ability(62)

############
### ABRA ###
############

ABRA = Pokemon()
ABRA.species = 63
ABRA.types = PSYCHIC
ABRA.abilities = species.abilities(63)
ABRA.hidden_ability = species.hidden_ability(63)

###############
### KADABRA ###
###############

KADABRA = Pokemon()
KADABRA.species = 64
KADABRA.types = PSYCHIC
KADABRA.abilities = species.abilities(64)
KADABRA.hidden_ability = species.hidden_ability(64)

################
### ALAKAZAM ###
################

ALAKAZAM = Pokemon()
ALAKAZAM.species = 65
ALAKAZAM.types = PSYCHIC
ALAKAZAM.abilities = species.abilities(65)
ALAKAZAM.hidden_ability = species.hidden_ability(65)

##############
### MACHOP ###
##############

MACHOP = Pokemon()
MACHOP.species = 66
MACHOP.types = FIGHTING
MACHOP.abilities = species.abilities(66)
MACHOP.hidden_ability = species.hidden_ability(66)

###############
### MACHOKE ###
###############

MACHOKE = Pokemon()
MACHOKE.species = 67
MACHOKE.types = FIGHTING
MACHOKE.abilities = species.abilities(67)
MACHOKE.hidden_ability = species.hidden_ability(67)

###############
### MACHAMP ###
###############

MACHAMP = Pokemon()
MACHAMP.species = 68
MACHAMP.types = FIGHTING
MACHAMP.abilities = species.abilities(68)
MACHAMP.hidden_ability = species.hidden_ability(68)

##################
### BELLSPROUT ###
##################

BELLSPROUT = Pokemon()
BELLSPROUT.species = 69
BELLSPROUT.types = GRASS
BELLSPROUT.types = [BELLSPROUT.types, POISON]
BELLSPROUT.abilities = species.abilities(69)
BELLSPROUT.hidden_ability = species.hidden_ability(69)

##################
### WEEPINBELL ###
##################

WEEPINBELL = Pokemon()
WEEPINBELL.species = 70
WEEPINBELL.types = GRASS
WEEPINBELL.types = [WEEPINBELL.types, POISON]
WEEPINBELL.abilities = species.abilities(70)
WEEPINBELL.hidden_ability = species.hidden_ability(70)

##################
### VICTREEBEL ###
##################

VICTREEBEL = Pokemon()
VICTREEBEL.species = 71
VICTREEBEL.types = GRASS
VICTREEBEL.types = [VICTREEBEL.types, POISON]
VICTREEBEL.abilities = species.abilities(71)
VICTREEBEL.hidden_ability = species.hidden_ability(71)

#################
### TENTACOOL ###
#################

TENTACOOL = Pokemon()
TENTACOOL.species = 72
TENTACOOL.types = WATER
TENTACOOL.types = [TENTACOOL.types, POISON]
TENTACOOL.abilities = species.abilities(72)
TENTACOOL.hidden_ability = species.hidden_ability(72)

##################
### TENTACRUEL ###
##################

TENTACRUEL = Pokemon()
TENTACRUEL.species = 73
TENTACRUEL.types = WATER
TENTACRUEL.types = [TENTACRUEL.types, POISON]
TENTACRUEL.abilities = species.abilities(73)
TENTACRUEL.hidden_ability = species.hidden_ability(73)

###############
### GEODUDE ###
###############

GEODUDE = Pokemon()
GEODUDE.species = 74
GEODUDE.types = ROCK
GEODUDE.types = [GEODUDE.types, GROUND]
GEODUDE.abilities = species.abilities(74)
GEODUDE.hidden_ability = species.hidden_ability(74)

################
### GRAVELER ###
################

GRAVELER = Pokemon()
GRAVELER.species = 75
GRAVELER.types = ROCK
GRAVELER.types = [GRAVELER.types, GROUND]
GRAVELER.abilities = species.abilities(75)
GRAVELER.hidden_ability = species.hidden_ability(75)

#############
### GOLEM ###
#############

GOLEM = Pokemon()
GOLEM.species = 76
GOLEM.types = ROCK
GOLEM.types = [GOLEM.types, GROUND]
GOLEM.abilities = species.abilities(76)
GOLEM.hidden_ability = species.hidden_ability(76)

##############
### PONYTA ###
##############

PONYTA = Pokemon()
PONYTA.species = 77
PONYTA.types = FIRE
PONYTA.abilities = species.abilities(77)
PONYTA.hidden_ability = species.hidden_ability(77)

################
### RAPIDASH ###
################

RAPIDASH = Pokemon()
RAPIDASH.species = 78
RAPIDASH.types = FIRE
RAPIDASH.abilities = species.abilities(78)
RAPIDASH.hidden_ability = species.hidden_ability(78)

################
### SLOWPOKE ###
################

SLOWPOKE = Pokemon()
SLOWPOKE.species = 79
SLOWPOKE.types = WATER
SLOWPOKE.types = [SLOWPOKE.types, PSYCHIC]
SLOWPOKE.abilities = species.abilities(79)
SLOWPOKE.hidden_ability = species.hidden_ability(79)

###############
### SLOWBRO ###
###############

SLOWBRO = Pokemon()
SLOWBRO.species = 80
SLOWBRO.types = WATER
SLOWBRO.types = [SLOWBRO.types, PSYCHIC]
SLOWBRO.abilities = species.abilities(80)
SLOWBRO.hidden_ability = species.hidden_ability(80)

#################
### MAGNEMITE ###
#################

MAGNEMITE = Pokemon()
MAGNEMITE.species = 81
MAGNEMITE.types = ELECTRIC
MAGNEMITE.types = [MAGNEMITE.types, STEEL]
MAGNEMITE.abilities = species.abilities(81)
MAGNEMITE.hidden_ability = species.hidden_ability(81)

################
### MAGNETON ###
################

MAGNETON = Pokemon()
MAGNETON.species = 82
MAGNETON.types = ELECTRIC
MAGNETON.types = [MAGNETON.types, STEEL]
MAGNETON.abilities = species.abilities(82)
MAGNETON.hidden_ability = species.hidden_ability(82)

#################
### FARFETCHD ###
#################

FARFETCHD = Pokemon()
FARFETCHD.types = NORMAL
FARFETCHD.types = [FARFETCHD.types, FLYING]
#############
### DODUO ###
#############

DODUO = Pokemon()
DODUO.species = 84
DODUO.types = NORMAL
DODUO.types = [DODUO.types, FLYING]
DODUO.abilities = species.abilities(84)
DODUO.hidden_ability = species.hidden_ability(84)

##############
### DODRIO ###
##############

DODRIO = Pokemon()
DODRIO.species = 85
DODRIO.types = NORMAL
DODRIO.types = [DODRIO.types, FLYING]
DODRIO.abilities = species.abilities(85)
DODRIO.hidden_ability = species.hidden_ability(85)

############
### SEEL ###
############

SEEL = Pokemon()
SEEL.species = 86
SEEL.types = WATER
SEEL.abilities = species.abilities(86)
SEEL.hidden_ability = species.hidden_ability(86)

###############
### DEWGONG ###
###############

DEWGONG = Pokemon()
DEWGONG.species = 87
DEWGONG.types = WATER
DEWGONG.types = [DEWGONG.types, ICE]
DEWGONG.abilities = species.abilities(87)
DEWGONG.hidden_ability = species.hidden_ability(87)

##############
### GRIMER ###
##############

GRIMER = Pokemon()
GRIMER.species = 88
GRIMER.types = POISON
GRIMER.abilities = species.abilities(88)
GRIMER.hidden_ability = species.hidden_ability(88)

###########
### MUK ###
###########

MUK = Pokemon()
MUK.species = 89
MUK.types = POISON
MUK.abilities = species.abilities(89)
MUK.hidden_ability = species.hidden_ability(89)

################
### SHELLDER ###
################

SHELLDER = Pokemon()
SHELLDER.species = 90
SHELLDER.types = WATER
SHELLDER.abilities = species.abilities(90)
SHELLDER.hidden_ability = species.hidden_ability(90)

################
### CLOYSTER ###
################

CLOYSTER = Pokemon()
CLOYSTER.species = 91
CLOYSTER.types = WATER
CLOYSTER.types = [CLOYSTER.types, ICE]
CLOYSTER.abilities = species.abilities(91)
CLOYSTER.hidden_ability = species.hidden_ability(91)

##############
### GASTLY ###
##############

GASTLY = Pokemon()
GASTLY.species = 92
GASTLY.types = GHOST
GASTLY.types = [GASTLY.types, POISON]
GASTLY.abilities = species.abilities(92)
GASTLY.hidden_ability = species.hidden_ability(92)

###############
### HAUNTER ###
###############

HAUNTER = Pokemon()
HAUNTER.species = 93
HAUNTER.types = GHOST
HAUNTER.types = [HAUNTER.types, POISON]
HAUNTER.abilities = species.abilities(93)
HAUNTER.hidden_ability = species.hidden_ability(93)

##############
### GENGAR ###
##############

GENGAR = Pokemon()
GENGAR.species = 94
GENGAR.types = GHOST
GENGAR.types = [GENGAR.types, POISON]
GENGAR.abilities = species.abilities(94)
GENGAR.hidden_ability = species.hidden_ability(94)

############
### ONIX ###
############

ONIX = Pokemon()
ONIX.species = 95
ONIX.types = ROCK
ONIX.types = [ONIX.types, GROUND]
ONIX.abilities = species.abilities(95)
ONIX.hidden_ability = species.hidden_ability(95)

###############
### DROWZEE ###
###############

DROWZEE = Pokemon()
DROWZEE.species = 96
DROWZEE.types = PSYCHIC
DROWZEE.abilities = species.abilities(96)
DROWZEE.hidden_ability = species.hidden_ability(96)

#############
### HYPNO ###
#############

HYPNO = Pokemon()
HYPNO.species = 97
HYPNO.types = PSYCHIC
HYPNO.abilities = species.abilities(97)
HYPNO.hidden_ability = species.hidden_ability(97)

##############
### KRABBY ###
##############

KRABBY = Pokemon()
KRABBY.species = 98
KRABBY.types = WATER
KRABBY.abilities = species.abilities(98)
KRABBY.hidden_ability = species.hidden_ability(98)

###############
### KINGLER ###
###############

KINGLER = Pokemon()
KINGLER.species = 99
KINGLER.types = WATER
KINGLER.abilities = species.abilities(99)
KINGLER.hidden_ability = species.hidden_ability(99)

###############
### VOLTORB ###
###############

VOLTORB = Pokemon()
VOLTORB.species = 100
VOLTORB.types = ELECTRIC
VOLTORB.abilities = species.abilities(100)
VOLTORB.hidden_ability = species.hidden_ability(100)

#################
### ELECTRODE ###
#################

ELECTRODE = Pokemon()
ELECTRODE.species = 101
ELECTRODE.types = ELECTRIC
ELECTRODE.abilities = species.abilities(101)
ELECTRODE.hidden_ability = species.hidden_ability(101)

#################
### EXEGGCUTE ###
#################

EXEGGCUTE = Pokemon()
EXEGGCUTE.species = 102
EXEGGCUTE.types = GRASS
EXEGGCUTE.types = [EXEGGCUTE.types, PSYCHIC]
EXEGGCUTE.abilities = species.abilities(102)
EXEGGCUTE.hidden_ability = species.hidden_ability(102)

#################
### EXEGGUTOR ###
#################

EXEGGUTOR = Pokemon()
EXEGGUTOR.species = 103
EXEGGUTOR.types = GRASS
EXEGGUTOR.types = [EXEGGUTOR.types, PSYCHIC]
EXEGGUTOR.abilities = species.abilities(103)
EXEGGUTOR.hidden_ability = species.hidden_ability(103)

##############
### CUBONE ###
##############

CUBONE = Pokemon()
CUBONE.species = 104
CUBONE.types = GROUND
CUBONE.abilities = species.abilities(104)
CUBONE.hidden_ability = species.hidden_ability(104)

###############
### MAROWAK ###
###############

MAROWAK = Pokemon()
MAROWAK.species = 105
MAROWAK.types = GROUND
MAROWAK.abilities = species.abilities(105)
MAROWAK.hidden_ability = species.hidden_ability(105)

#################
### HITMONLEE ###
#################

HITMONLEE = Pokemon()
HITMONLEE.species = 106
HITMONLEE.types = FIGHTING
HITMONLEE.abilities = species.abilities(106)
HITMONLEE.hidden_ability = species.hidden_ability(106)

##################
### HITMONCHAN ###
##################

HITMONCHAN = Pokemon()
HITMONCHAN.species = 107
HITMONCHAN.types = FIGHTING
HITMONCHAN.abilities = species.abilities(107)
HITMONCHAN.hidden_ability = species.hidden_ability(107)

#################
### LICKITUNG ###
#################

LICKITUNG = Pokemon()
LICKITUNG.species = 108
LICKITUNG.types = NORMAL
LICKITUNG.abilities = species.abilities(108)
LICKITUNG.hidden_ability = species.hidden_ability(108)

###############
### KOFFING ###
###############

KOFFING = Pokemon()
KOFFING.species = 109
KOFFING.types = POISON
KOFFING.abilities = species.abilities(109)
KOFFING.hidden_ability = species.hidden_ability(109)

###############
### WEEZING ###
###############

WEEZING = Pokemon()
WEEZING.species = 110
WEEZING.types = POISON
WEEZING.abilities = species.abilities(110)
WEEZING.hidden_ability = species.hidden_ability(110)

###############
### RHYHORN ###
###############

RHYHORN = Pokemon()
RHYHORN.species = 111
RHYHORN.types = GROUND
RHYHORN.types = [RHYHORN.types, ROCK]
RHYHORN.abilities = species.abilities(111)
RHYHORN.hidden_ability = species.hidden_ability(111)

##############
### RHYDON ###
##############

RHYDON = Pokemon()
RHYDON.species = 112
RHYDON.types = GROUND
RHYDON.types = [RHYDON.types, ROCK]
RHYDON.abilities = species.abilities(112)
RHYDON.hidden_ability = species.hidden_ability(112)

###############
### CHANSEY ###
###############

CHANSEY = Pokemon()
CHANSEY.species = 113
CHANSEY.types = NORMAL
CHANSEY.abilities = species.abilities(113)
CHANSEY.hidden_ability = species.hidden_ability(113)

###############
### TANGELA ###
###############

TANGELA = Pokemon()
TANGELA.species = 114
TANGELA.types = GRASS
TANGELA.abilities = species.abilities(114)
TANGELA.hidden_ability = species.hidden_ability(114)

##################
### KANGASKHAN ###
##################

KANGASKHAN = Pokemon()
KANGASKHAN.species = 115
KANGASKHAN.types = NORMAL
KANGASKHAN.abilities = species.abilities(115)
KANGASKHAN.hidden_ability = species.hidden_ability(115)

##############
### HORSEA ###
##############

HORSEA = Pokemon()
HORSEA.species = 116
HORSEA.types = WATER
HORSEA.abilities = species.abilities(116)
HORSEA.hidden_ability = species.hidden_ability(116)

##############
### SEADRA ###
##############

SEADRA = Pokemon()
SEADRA.species = 117
SEADRA.types = WATER
SEADRA.abilities = species.abilities(117)
SEADRA.hidden_ability = species.hidden_ability(117)

###############
### GOLDEEN ###
###############

GOLDEEN = Pokemon()
GOLDEEN.species = 118
GOLDEEN.types = WATER
GOLDEEN.abilities = species.abilities(118)
GOLDEEN.hidden_ability = species.hidden_ability(118)

###############
### SEAKING ###
###############

SEAKING = Pokemon()
SEAKING.species = 119
SEAKING.types = WATER
SEAKING.abilities = species.abilities(119)
SEAKING.hidden_ability = species.hidden_ability(119)

##############
### STARYU ###
##############

STARYU = Pokemon()
STARYU.species = 120
STARYU.types = WATER
STARYU.abilities = species.abilities(120)
STARYU.hidden_ability = species.hidden_ability(120)

###############
### STARMIE ###
###############

STARMIE = Pokemon()
STARMIE.species = 121
STARMIE.types = WATER
STARMIE.types = [STARMIE.types, PSYCHIC]
STARMIE.abilities = species.abilities(121)
STARMIE.hidden_ability = species.hidden_ability(121)

##############
### MRMIME ###
##############

MRMIME = Pokemon()
MRMIME.types = PSYCHIC
MRMIME.types = [MRMIME.types, FAIRY]
###############
### SCYTHER ###
###############

SCYTHER = Pokemon()
SCYTHER.species = 123
SCYTHER.types = BUG
SCYTHER.types = [SCYTHER.types, FLYING]
SCYTHER.abilities = species.abilities(123)
SCYTHER.hidden_ability = species.hidden_ability(123)

############
### JYNX ###
############

JYNX = Pokemon()
JYNX.species = 124
JYNX.types = ICE
JYNX.types = [JYNX.types, PSYCHIC]
JYNX.abilities = species.abilities(124)
JYNX.hidden_ability = species.hidden_ability(124)

##################
### ELECTABUZZ ###
##################

ELECTABUZZ = Pokemon()
ELECTABUZZ.species = 125
ELECTABUZZ.types = ELECTRIC
ELECTABUZZ.abilities = species.abilities(125)
ELECTABUZZ.hidden_ability = species.hidden_ability(125)

##############
### MAGMAR ###
##############

MAGMAR = Pokemon()
MAGMAR.species = 126
MAGMAR.types = FIRE
MAGMAR.abilities = species.abilities(126)
MAGMAR.hidden_ability = species.hidden_ability(126)

##############
### PINSIR ###
##############

PINSIR = Pokemon()
PINSIR.species = 127
PINSIR.types = BUG
PINSIR.abilities = species.abilities(127)
PINSIR.hidden_ability = species.hidden_ability(127)

##############
### TAUROS ###
##############

TAUROS = Pokemon()
TAUROS.species = 128
TAUROS.types = NORMAL
TAUROS.abilities = species.abilities(128)
TAUROS.hidden_ability = species.hidden_ability(128)

################
### MAGIKARP ###
################

MAGIKARP = Pokemon()
MAGIKARP.species = 129
MAGIKARP.types = WATER
MAGIKARP.abilities = species.abilities(129)
MAGIKARP.hidden_ability = species.hidden_ability(129)

################
### GYARADOS ###
################

GYARADOS = Pokemon()
GYARADOS.species = 130
GYARADOS.types = WATER
GYARADOS.types = [GYARADOS.types, FLYING]
GYARADOS.abilities = species.abilities(130)
GYARADOS.hidden_ability = species.hidden_ability(130)

##############
### LAPRAS ###
##############

LAPRAS = Pokemon()
LAPRAS.species = 131
LAPRAS.types = WATER
LAPRAS.types = [LAPRAS.types, ICE]
LAPRAS.abilities = species.abilities(131)
LAPRAS.hidden_ability = species.hidden_ability(131)

#############
### DITTO ###
#############

DITTO = Pokemon()
DITTO.species = 132
DITTO.types = NORMAL
DITTO.abilities = species.abilities(132)
DITTO.hidden_ability = species.hidden_ability(132)

#############
### EEVEE ###
#############

EEVEE = Pokemon()
EEVEE.species = 133
EEVEE.types = NORMAL
EEVEE.abilities = species.abilities(133)
EEVEE.hidden_ability = species.hidden_ability(133)

################
### VAPOREON ###
################

VAPOREON = Pokemon()
VAPOREON.species = 134
VAPOREON.types = WATER
VAPOREON.abilities = species.abilities(134)
VAPOREON.hidden_ability = species.hidden_ability(134)

###############
### JOLTEON ###
###############

JOLTEON = Pokemon()
JOLTEON.species = 135
JOLTEON.types = ELECTRIC
JOLTEON.abilities = species.abilities(135)
JOLTEON.hidden_ability = species.hidden_ability(135)

###############
### FLAREON ###
###############

FLAREON = Pokemon()
FLAREON.species = 136
FLAREON.types = FIRE
FLAREON.abilities = species.abilities(136)
FLAREON.hidden_ability = species.hidden_ability(136)

###############
### PORYGON ###
###############

PORYGON = Pokemon()
PORYGON.species = 137
PORYGON.types = NORMAL
PORYGON.abilities = species.abilities(137)
PORYGON.hidden_ability = species.hidden_ability(137)

###############
### OMANYTE ###
###############

OMANYTE = Pokemon()
OMANYTE.species = 138
OMANYTE.types = ROCK
OMANYTE.types = [OMANYTE.types, WATER]
OMANYTE.abilities = species.abilities(138)
OMANYTE.hidden_ability = species.hidden_ability(138)

###############
### OMASTAR ###
###############

OMASTAR = Pokemon()
OMASTAR.species = 139
OMASTAR.types = ROCK
OMASTAR.types = [OMASTAR.types, WATER]
OMASTAR.abilities = species.abilities(139)
OMASTAR.hidden_ability = species.hidden_ability(139)

##############
### KABUTO ###
##############

KABUTO = Pokemon()
KABUTO.species = 140
KABUTO.types = ROCK
KABUTO.types = [KABUTO.types, WATER]
KABUTO.abilities = species.abilities(140)
KABUTO.hidden_ability = species.hidden_ability(140)

################
### KABUTOPS ###
################

KABUTOPS = Pokemon()
KABUTOPS.species = 141
KABUTOPS.types = ROCK
KABUTOPS.types = [KABUTOPS.types, WATER]
KABUTOPS.abilities = species.abilities(141)
KABUTOPS.hidden_ability = species.hidden_ability(141)

##################
### AERODACTYL ###
##################

AERODACTYL = Pokemon()
AERODACTYL.species = 142
AERODACTYL.types = ROCK
AERODACTYL.types = [AERODACTYL.types, FLYING]
AERODACTYL.abilities = species.abilities(142)
AERODACTYL.hidden_ability = species.hidden_ability(142)

###############
### SNORLAX ###
###############

SNORLAX = Pokemon()
SNORLAX.species = 143
SNORLAX.types = NORMAL
SNORLAX.abilities = species.abilities(143)
SNORLAX.hidden_ability = species.hidden_ability(143)

################
### ARTICUNO ###
################

ARTICUNO = Pokemon()
ARTICUNO.species = 144
ARTICUNO.types = ICE
ARTICUNO.types = [ARTICUNO.types, FLYING]
ARTICUNO.abilities = species.abilities(144)
ARTICUNO.hidden_ability = species.hidden_ability(144)

##############
### ZAPDOS ###
##############

ZAPDOS = Pokemon()
ZAPDOS.species = 145
ZAPDOS.types = ELECTRIC
ZAPDOS.types = [ZAPDOS.types, FLYING]
ZAPDOS.abilities = species.abilities(145)
ZAPDOS.hidden_ability = species.hidden_ability(145)

###############
### MOLTRES ###
###############

MOLTRES = Pokemon()
MOLTRES.species = 146
MOLTRES.types = FIRE
MOLTRES.types = [MOLTRES.types, FLYING]
MOLTRES.abilities = species.abilities(146)
MOLTRES.hidden_ability = species.hidden_ability(146)

###############
### DRATINI ###
###############

DRATINI = Pokemon()
DRATINI.species = 147
DRATINI.types = DRAGON
DRATINI.abilities = species.abilities(147)
DRATINI.hidden_ability = species.hidden_ability(147)

#################
### DRAGONAIR ###
#################

DRAGONAIR = Pokemon()
DRAGONAIR.species = 148
DRAGONAIR.types = DRAGON
DRAGONAIR.abilities = species.abilities(148)
DRAGONAIR.hidden_ability = species.hidden_ability(148)

#################
### DRAGONITE ###
#################

DRAGONITE = Pokemon()
DRAGONITE.species = 149
DRAGONITE.types = DRAGON
DRAGONITE.types = [DRAGONITE.types, FLYING]
DRAGONITE.abilities = species.abilities(149)
DRAGONITE.hidden_ability = species.hidden_ability(149)

##############
### MEWTWO ###
##############

MEWTWO = Pokemon()
MEWTWO.species = 150
MEWTWO.types = PSYCHIC
MEWTWO.abilities = species.abilities(150)
MEWTWO.hidden_ability = species.hidden_ability(150)

###########
### MEW ###
###########

MEW = Pokemon()
MEW.species = 151
MEW.types = PSYCHIC
MEW.abilities = species.abilities(151)
MEW.hidden_ability = species.hidden_ability(151)

#################
### CHIKORITA ###
#################

CHIKORITA = Pokemon()
CHIKORITA.species = 152
CHIKORITA.types = GRASS
CHIKORITA.abilities = species.abilities(152)
CHIKORITA.hidden_ability = species.hidden_ability(152)

###############
### BAYLEEF ###
###############

BAYLEEF = Pokemon()
BAYLEEF.species = 153
BAYLEEF.types = GRASS
BAYLEEF.abilities = species.abilities(153)
BAYLEEF.hidden_ability = species.hidden_ability(153)

################
### MEGANIUM ###
################

MEGANIUM = Pokemon()
MEGANIUM.species = 154
MEGANIUM.types = GRASS
MEGANIUM.abilities = species.abilities(154)
MEGANIUM.hidden_ability = species.hidden_ability(154)

#################
### CYNDAQUIL ###
#################

CYNDAQUIL = Pokemon()
CYNDAQUIL.species = 155
CYNDAQUIL.types = FIRE
CYNDAQUIL.abilities = species.abilities(155)
CYNDAQUIL.hidden_ability = species.hidden_ability(155)

###############
### QUILAVA ###
###############

QUILAVA = Pokemon()
QUILAVA.species = 156
QUILAVA.types = FIRE
QUILAVA.abilities = species.abilities(156)
QUILAVA.hidden_ability = species.hidden_ability(156)

##################
### TYPHLOSION ###
##################

TYPHLOSION = Pokemon()
TYPHLOSION.species = 157
TYPHLOSION.types = FIRE
TYPHLOSION.abilities = species.abilities(157)
TYPHLOSION.hidden_ability = species.hidden_ability(157)

################
### TOTODILE ###
################

TOTODILE = Pokemon()
TOTODILE.species = 158
TOTODILE.types = WATER
TOTODILE.abilities = species.abilities(158)
TOTODILE.hidden_ability = species.hidden_ability(158)

################
### CROCONAW ###
################

CROCONAW = Pokemon()
CROCONAW.species = 159
CROCONAW.types = WATER
CROCONAW.abilities = species.abilities(159)
CROCONAW.hidden_ability = species.hidden_ability(159)

##################
### FERALIGATR ###
##################

FERALIGATR = Pokemon()
FERALIGATR.species = 160
FERALIGATR.types = WATER
FERALIGATR.abilities = species.abilities(160)
FERALIGATR.hidden_ability = species.hidden_ability(160)

###############
### SENTRET ###
###############

SENTRET = Pokemon()
SENTRET.species = 161
SENTRET.types = NORMAL
SENTRET.abilities = species.abilities(161)
SENTRET.hidden_ability = species.hidden_ability(161)

##############
### FURRET ###
##############

FURRET = Pokemon()
FURRET.species = 162
FURRET.types = NORMAL
FURRET.abilities = species.abilities(162)
FURRET.hidden_ability = species.hidden_ability(162)

################
### HOOTHOOT ###
################

HOOTHOOT = Pokemon()
HOOTHOOT.species = 163
HOOTHOOT.types = NORMAL
HOOTHOOT.types = [HOOTHOOT.types, FLYING]
HOOTHOOT.abilities = species.abilities(163)
HOOTHOOT.hidden_ability = species.hidden_ability(163)

###############
### NOCTOWL ###
###############

NOCTOWL = Pokemon()
NOCTOWL.species = 164
NOCTOWL.types = NORMAL
NOCTOWL.types = [NOCTOWL.types, FLYING]
NOCTOWL.abilities = species.abilities(164)
NOCTOWL.hidden_ability = species.hidden_ability(164)

##############
### LEDYBA ###
##############

LEDYBA = Pokemon()
LEDYBA.species = 165
LEDYBA.types = BUG
LEDYBA.types = [LEDYBA.types, FLYING]
LEDYBA.abilities = species.abilities(165)
LEDYBA.hidden_ability = species.hidden_ability(165)

##############
### LEDIAN ###
##############

LEDIAN = Pokemon()
LEDIAN.species = 166
LEDIAN.types = BUG
LEDIAN.types = [LEDIAN.types, FLYING]
LEDIAN.abilities = species.abilities(166)
LEDIAN.hidden_ability = species.hidden_ability(166)

################
### SPINARAK ###
################

SPINARAK = Pokemon()
SPINARAK.species = 167
SPINARAK.types = BUG
SPINARAK.types = [SPINARAK.types, POISON]
SPINARAK.abilities = species.abilities(167)
SPINARAK.hidden_ability = species.hidden_ability(167)

###############
### ARIADOS ###
###############

ARIADOS = Pokemon()
ARIADOS.species = 168
ARIADOS.types = BUG
ARIADOS.types = [ARIADOS.types, POISON]
ARIADOS.abilities = species.abilities(168)
ARIADOS.hidden_ability = species.hidden_ability(168)

##############
### CROBAT ###
##############

CROBAT = Pokemon()
CROBAT.species = 169
CROBAT.types = POISON
CROBAT.types = [CROBAT.types, FLYING]
CROBAT.abilities = species.abilities(169)
CROBAT.hidden_ability = species.hidden_ability(169)

################
### CHINCHOU ###
################

CHINCHOU = Pokemon()
CHINCHOU.species = 170
CHINCHOU.types = WATER
CHINCHOU.types = [CHINCHOU.types, ELECTRIC]
CHINCHOU.abilities = species.abilities(170)
CHINCHOU.hidden_ability = species.hidden_ability(170)

###############
### LANTURN ###
###############

LANTURN = Pokemon()
LANTURN.species = 171
LANTURN.types = WATER
LANTURN.types = [LANTURN.types, ELECTRIC]
LANTURN.abilities = species.abilities(171)
LANTURN.hidden_ability = species.hidden_ability(171)

#############
### PICHU ###
#############

PICHU = Pokemon()
PICHU.species = 172
PICHU.types = ELECTRIC
PICHU.abilities = species.abilities(172)
PICHU.hidden_ability = species.hidden_ability(172)

##############
### CLEFFA ###
##############

CLEFFA = Pokemon()
CLEFFA.species = 173
CLEFFA.types = FAIRY
CLEFFA.abilities = species.abilities(173)
CLEFFA.hidden_ability = species.hidden_ability(173)

#################
### IGGLYBUFF ###
#################

IGGLYBUFF = Pokemon()
IGGLYBUFF.species = 174
IGGLYBUFF.types = NORMAL
IGGLYBUFF.types = [IGGLYBUFF.types, FAIRY]
IGGLYBUFF.abilities = species.abilities(174)
IGGLYBUFF.hidden_ability = species.hidden_ability(174)

##############
### TOGEPI ###
##############

TOGEPI = Pokemon()
TOGEPI.species = 175
TOGEPI.types = FAIRY
TOGEPI.abilities = species.abilities(175)
TOGEPI.hidden_ability = species.hidden_ability(175)

###############
### TOGETIC ###
###############

TOGETIC = Pokemon()
TOGETIC.species = 176
TOGETIC.types = FAIRY
TOGETIC.types = [TOGETIC.types, FLYING]
TOGETIC.abilities = species.abilities(176)
TOGETIC.hidden_ability = species.hidden_ability(176)

############
### NATU ###
############

NATU = Pokemon()
NATU.species = 177
NATU.types = PSYCHIC
NATU.types = [NATU.types, FLYING]
NATU.abilities = species.abilities(177)
NATU.hidden_ability = species.hidden_ability(177)

############
### XATU ###
############

XATU = Pokemon()
XATU.species = 178
XATU.types = PSYCHIC
XATU.types = [XATU.types, FLYING]
XATU.abilities = species.abilities(178)
XATU.hidden_ability = species.hidden_ability(178)

##############
### MAREEP ###
##############

MAREEP = Pokemon()
MAREEP.species = 179
MAREEP.types = ELECTRIC
MAREEP.abilities = species.abilities(179)
MAREEP.hidden_ability = species.hidden_ability(179)

###############
### FLAAFFY ###
###############

FLAAFFY = Pokemon()
FLAAFFY.species = 180
FLAAFFY.types = ELECTRIC
FLAAFFY.abilities = species.abilities(180)
FLAAFFY.hidden_ability = species.hidden_ability(180)

################
### AMPHAROS ###
################

AMPHAROS = Pokemon()
AMPHAROS.species = 181
AMPHAROS.types = ELECTRIC
AMPHAROS.abilities = species.abilities(181)
AMPHAROS.hidden_ability = species.hidden_ability(181)

#################
### BELLOSSOM ###
#################

BELLOSSOM = Pokemon()
BELLOSSOM.species = 182
BELLOSSOM.types = GRASS
BELLOSSOM.abilities = species.abilities(182)
BELLOSSOM.hidden_ability = species.hidden_ability(182)

##############
### MARILL ###
##############

MARILL = Pokemon()
MARILL.species = 183
MARILL.types = WATER
MARILL.types = [MARILL.types, FAIRY]
MARILL.abilities = species.abilities(183)
MARILL.hidden_ability = species.hidden_ability(183)

#################
### AZUMARILL ###
#################

AZUMARILL = Pokemon()
AZUMARILL.species = 184
AZUMARILL.types = WATER
AZUMARILL.types = [AZUMARILL.types, FAIRY]
AZUMARILL.abilities = species.abilities(184)
AZUMARILL.hidden_ability = species.hidden_ability(184)

#################
### SUDOWOODO ###
#################

SUDOWOODO = Pokemon()
SUDOWOODO.species = 185
SUDOWOODO.types = ROCK
SUDOWOODO.abilities = species.abilities(185)
SUDOWOODO.hidden_ability = species.hidden_ability(185)

################
### POLITOED ###
################

POLITOED = Pokemon()
POLITOED.species = 186
POLITOED.types = WATER
POLITOED.abilities = species.abilities(186)
POLITOED.hidden_ability = species.hidden_ability(186)

##############
### HOPPIP ###
##############

HOPPIP = Pokemon()
HOPPIP.species = 187
HOPPIP.types = GRASS
HOPPIP.types = [HOPPIP.types, FLYING]
HOPPIP.abilities = species.abilities(187)
HOPPIP.hidden_ability = species.hidden_ability(187)

################
### SKIPLOOM ###
################

SKIPLOOM = Pokemon()
SKIPLOOM.species = 188
SKIPLOOM.types = GRASS
SKIPLOOM.types = [SKIPLOOM.types, FLYING]
SKIPLOOM.abilities = species.abilities(188)
SKIPLOOM.hidden_ability = species.hidden_ability(188)

################
### JUMPLUFF ###
################

JUMPLUFF = Pokemon()
JUMPLUFF.species = 189
JUMPLUFF.types = GRASS
JUMPLUFF.types = [JUMPLUFF.types, FLYING]
JUMPLUFF.abilities = species.abilities(189)
JUMPLUFF.hidden_ability = species.hidden_ability(189)

#############
### AIPOM ###
#############

AIPOM = Pokemon()
AIPOM.species = 190
AIPOM.types = NORMAL
AIPOM.abilities = species.abilities(190)
AIPOM.hidden_ability = species.hidden_ability(190)

###############
### SUNKERN ###
###############

SUNKERN = Pokemon()
SUNKERN.species = 191
SUNKERN.types = GRASS
SUNKERN.abilities = species.abilities(191)
SUNKERN.hidden_ability = species.hidden_ability(191)

################
### SUNFLORA ###
################

SUNFLORA = Pokemon()
SUNFLORA.species = 192
SUNFLORA.types = GRASS
SUNFLORA.abilities = species.abilities(192)
SUNFLORA.hidden_ability = species.hidden_ability(192)

#############
### YANMA ###
#############

YANMA = Pokemon()
YANMA.species = 193
YANMA.types = BUG
YANMA.types = [YANMA.types, FLYING]
YANMA.abilities = species.abilities(193)
YANMA.hidden_ability = species.hidden_ability(193)

##############
### WOOPER ###
##############

WOOPER = Pokemon()
WOOPER.species = 194
WOOPER.types = WATER
WOOPER.types = [WOOPER.types, GROUND]
WOOPER.abilities = species.abilities(194)
WOOPER.hidden_ability = species.hidden_ability(194)

################
### QUAGSIRE ###
################

QUAGSIRE = Pokemon()
QUAGSIRE.species = 195
QUAGSIRE.types = WATER
QUAGSIRE.types = [QUAGSIRE.types, GROUND]
QUAGSIRE.abilities = species.abilities(195)
QUAGSIRE.hidden_ability = species.hidden_ability(195)

##############
### ESPEON ###
##############

ESPEON = Pokemon()
ESPEON.species = 196
ESPEON.types = PSYCHIC
ESPEON.abilities = species.abilities(196)
ESPEON.hidden_ability = species.hidden_ability(196)

###############
### UMBREON ###
###############

UMBREON = Pokemon()
UMBREON.species = 197
UMBREON.types = DARK
UMBREON.abilities = species.abilities(197)
UMBREON.hidden_ability = species.hidden_ability(197)

###############
### MURKROW ###
###############

MURKROW = Pokemon()
MURKROW.species = 198
MURKROW.types = DARK
MURKROW.types = [MURKROW.types, FLYING]
MURKROW.abilities = species.abilities(198)
MURKROW.hidden_ability = species.hidden_ability(198)

################
### SLOWKING ###
################

SLOWKING = Pokemon()
SLOWKING.species = 199
SLOWKING.types = WATER
SLOWKING.types = [SLOWKING.types, PSYCHIC]
SLOWKING.abilities = species.abilities(199)
SLOWKING.hidden_ability = species.hidden_ability(199)

##################
### MISDREAVUS ###
##################

MISDREAVUS = Pokemon()
MISDREAVUS.species = 200
MISDREAVUS.types = GHOST
MISDREAVUS.abilities = species.abilities(200)
MISDREAVUS.hidden_ability = species.hidden_ability(200)

#############
### UNOWN ###
#############

UNOWN = Pokemon()
UNOWN.species = 201
UNOWN.types = PSYCHIC
UNOWN.abilities = species.abilities(201)
UNOWN.hidden_ability = species.hidden_ability(201)

#################
### WOBBUFFET ###
#################

WOBBUFFET = Pokemon()
WOBBUFFET.species = 202
WOBBUFFET.types = PSYCHIC
WOBBUFFET.abilities = species.abilities(202)
WOBBUFFET.hidden_ability = species.hidden_ability(202)

#################
### GIRAFARIG ###
#################

GIRAFARIG = Pokemon()
GIRAFARIG.species = 203
GIRAFARIG.types = NORMAL
GIRAFARIG.types = [GIRAFARIG.types, PSYCHIC]
GIRAFARIG.abilities = species.abilities(203)
GIRAFARIG.hidden_ability = species.hidden_ability(203)

##############
### PINECO ###
##############

PINECO = Pokemon()
PINECO.species = 204
PINECO.types = BUG
PINECO.abilities = species.abilities(204)
PINECO.hidden_ability = species.hidden_ability(204)

##################
### FORRETRESS ###
##################

FORRETRESS = Pokemon()
FORRETRESS.species = 205
FORRETRESS.types = BUG
FORRETRESS.types = [FORRETRESS.types, STEEL]
FORRETRESS.abilities = species.abilities(205)
FORRETRESS.hidden_ability = species.hidden_ability(205)

#################
### DUNSPARCE ###
#################

DUNSPARCE = Pokemon()
DUNSPARCE.species = 206
DUNSPARCE.types = NORMAL
DUNSPARCE.abilities = species.abilities(206)
DUNSPARCE.hidden_ability = species.hidden_ability(206)

##############
### GLIGAR ###
##############

GLIGAR = Pokemon()
GLIGAR.species = 207
GLIGAR.types = GROUND
GLIGAR.types = [GLIGAR.types, FLYING]
GLIGAR.abilities = species.abilities(207)
GLIGAR.hidden_ability = species.hidden_ability(207)

###############
### STEELIX ###
###############

STEELIX = Pokemon()
STEELIX.species = 208
STEELIX.types = STEEL
STEELIX.types = [STEELIX.types, GROUND]
STEELIX.abilities = species.abilities(208)
STEELIX.hidden_ability = species.hidden_ability(208)

################
### SNUBBULL ###
################

SNUBBULL = Pokemon()
SNUBBULL.species = 209
SNUBBULL.types = FAIRY
SNUBBULL.abilities = species.abilities(209)
SNUBBULL.hidden_ability = species.hidden_ability(209)

################
### GRANBULL ###
################

GRANBULL = Pokemon()
GRANBULL.species = 210
GRANBULL.types = FAIRY
GRANBULL.abilities = species.abilities(210)
GRANBULL.hidden_ability = species.hidden_ability(210)

################
### QWILFISH ###
################

QWILFISH = Pokemon()
QWILFISH.species = 211
QWILFISH.types = WATER
QWILFISH.types = [QWILFISH.types, POISON]
QWILFISH.abilities = species.abilities(211)
QWILFISH.hidden_ability = species.hidden_ability(211)

##############
### SCIZOR ###
##############

SCIZOR = Pokemon()
SCIZOR.species = 212
SCIZOR.types = BUG
SCIZOR.types = [SCIZOR.types, STEEL]
SCIZOR.abilities = species.abilities(212)
SCIZOR.hidden_ability = species.hidden_ability(212)

###############
### SHUCKLE ###
###############

SHUCKLE = Pokemon()
SHUCKLE.species = 213
SHUCKLE.types = BUG
SHUCKLE.types = [SHUCKLE.types, ROCK]
SHUCKLE.abilities = species.abilities(213)
SHUCKLE.hidden_ability = species.hidden_ability(213)

#################
### HERACROSS ###
#################

HERACROSS = Pokemon()
HERACROSS.species = 214
HERACROSS.types = BUG
HERACROSS.types = [HERACROSS.types, FIGHTING]
HERACROSS.abilities = species.abilities(214)
HERACROSS.hidden_ability = species.hidden_ability(214)

###############
### SNEASEL ###
###############

SNEASEL = Pokemon()
SNEASEL.species = 215
SNEASEL.types = DARK
SNEASEL.types = [SNEASEL.types, ICE]
SNEASEL.abilities = species.abilities(215)
SNEASEL.hidden_ability = species.hidden_ability(215)

#################
### TEDDIURSA ###
#################

TEDDIURSA = Pokemon()
TEDDIURSA.species = 216
TEDDIURSA.types = NORMAL
TEDDIURSA.abilities = species.abilities(216)
TEDDIURSA.hidden_ability = species.hidden_ability(216)

################
### URSARING ###
################

URSARING = Pokemon()
URSARING.species = 217
URSARING.types = NORMAL
URSARING.abilities = species.abilities(217)
URSARING.hidden_ability = species.hidden_ability(217)

##############
### SLUGMA ###
##############

SLUGMA = Pokemon()
SLUGMA.species = 218
SLUGMA.types = FIRE
SLUGMA.abilities = species.abilities(218)
SLUGMA.hidden_ability = species.hidden_ability(218)

################
### MAGCARGO ###
################

MAGCARGO = Pokemon()
MAGCARGO.species = 219
MAGCARGO.types = FIRE
MAGCARGO.types = [MAGCARGO.types, ROCK]
MAGCARGO.abilities = species.abilities(219)
MAGCARGO.hidden_ability = species.hidden_ability(219)

##############
### SWINUB ###
##############

SWINUB = Pokemon()
SWINUB.species = 220
SWINUB.types = ICE
SWINUB.types = [SWINUB.types, GROUND]
SWINUB.abilities = species.abilities(220)
SWINUB.hidden_ability = species.hidden_ability(220)

#################
### PILOSWINE ###
#################

PILOSWINE = Pokemon()
PILOSWINE.species = 221
PILOSWINE.types = ICE
PILOSWINE.types = [PILOSWINE.types, GROUND]
PILOSWINE.abilities = species.abilities(221)
PILOSWINE.hidden_ability = species.hidden_ability(221)

###############
### CORSOLA ###
###############

CORSOLA = Pokemon()
CORSOLA.species = 222
CORSOLA.types = WATER
CORSOLA.types = [CORSOLA.types, ROCK]
CORSOLA.abilities = species.abilities(222)
CORSOLA.hidden_ability = species.hidden_ability(222)

################
### REMORAID ###
################

REMORAID = Pokemon()
REMORAID.species = 223
REMORAID.types = WATER
REMORAID.abilities = species.abilities(223)
REMORAID.hidden_ability = species.hidden_ability(223)

#################
### OCTILLERY ###
#################

OCTILLERY = Pokemon()
OCTILLERY.species = 224
OCTILLERY.types = WATER
OCTILLERY.abilities = species.abilities(224)
OCTILLERY.hidden_ability = species.hidden_ability(224)

################
### DELIBIRD ###
################

DELIBIRD = Pokemon()
DELIBIRD.species = 225
DELIBIRD.types = ICE
DELIBIRD.types = [DELIBIRD.types, FLYING]
DELIBIRD.abilities = species.abilities(225)
DELIBIRD.hidden_ability = species.hidden_ability(225)

###############
### MANTINE ###
###############

MANTINE = Pokemon()
MANTINE.species = 226
MANTINE.types = WATER
MANTINE.types = [MANTINE.types, FLYING]
MANTINE.abilities = species.abilities(226)
MANTINE.hidden_ability = species.hidden_ability(226)

################
### SKARMORY ###
################

SKARMORY = Pokemon()
SKARMORY.species = 227
SKARMORY.types = STEEL
SKARMORY.types = [SKARMORY.types, FLYING]
SKARMORY.abilities = species.abilities(227)
SKARMORY.hidden_ability = species.hidden_ability(227)

################
### HOUNDOUR ###
################

HOUNDOUR = Pokemon()
HOUNDOUR.species = 228
HOUNDOUR.types = DARK
HOUNDOUR.types = [HOUNDOUR.types, FIRE]
HOUNDOUR.abilities = species.abilities(228)
HOUNDOUR.hidden_ability = species.hidden_ability(228)

################
### HOUNDOOM ###
################

HOUNDOOM = Pokemon()
HOUNDOOM.species = 229
HOUNDOOM.types = DARK
HOUNDOOM.types = [HOUNDOOM.types, FIRE]
HOUNDOOM.abilities = species.abilities(229)
HOUNDOOM.hidden_ability = species.hidden_ability(229)

###############
### KINGDRA ###
###############

KINGDRA = Pokemon()
KINGDRA.species = 230
KINGDRA.types = WATER
KINGDRA.types = [KINGDRA.types, DRAGON]
KINGDRA.abilities = species.abilities(230)
KINGDRA.hidden_ability = species.hidden_ability(230)

##############
### PHANPY ###
##############

PHANPY = Pokemon()
PHANPY.species = 231
PHANPY.types = GROUND
PHANPY.abilities = species.abilities(231)
PHANPY.hidden_ability = species.hidden_ability(231)

###############
### DONPHAN ###
###############

DONPHAN = Pokemon()
DONPHAN.species = 232
DONPHAN.types = GROUND
DONPHAN.abilities = species.abilities(232)
DONPHAN.hidden_ability = species.hidden_ability(232)

################
### PORYGON2 ###
################

PORYGON2 = Pokemon()
PORYGON2.species = 233
PORYGON2.types = NORMAL
PORYGON2.abilities = species.abilities(233)
PORYGON2.hidden_ability = species.hidden_ability(233)

################
### STANTLER ###
################

STANTLER = Pokemon()
STANTLER.species = 234
STANTLER.types = NORMAL
STANTLER.abilities = species.abilities(234)
STANTLER.hidden_ability = species.hidden_ability(234)

################
### SMEARGLE ###
################

SMEARGLE = Pokemon()
SMEARGLE.species = 235
SMEARGLE.types = NORMAL
SMEARGLE.abilities = species.abilities(235)
SMEARGLE.hidden_ability = species.hidden_ability(235)

###############
### TYROGUE ###
###############

TYROGUE = Pokemon()
TYROGUE.species = 236
TYROGUE.types = FIGHTING
TYROGUE.abilities = species.abilities(236)
TYROGUE.hidden_ability = species.hidden_ability(236)

#################
### HITMONTOP ###
#################

HITMONTOP = Pokemon()
HITMONTOP.species = 237
HITMONTOP.types = FIGHTING
HITMONTOP.abilities = species.abilities(237)
HITMONTOP.hidden_ability = species.hidden_ability(237)

################
### SMOOCHUM ###
################

SMOOCHUM = Pokemon()
SMOOCHUM.species = 238
SMOOCHUM.types = ICE
SMOOCHUM.types = [SMOOCHUM.types, PSYCHIC]
SMOOCHUM.abilities = species.abilities(238)
SMOOCHUM.hidden_ability = species.hidden_ability(238)

##############
### ELEKID ###
##############

ELEKID = Pokemon()
ELEKID.species = 239
ELEKID.types = ELECTRIC
ELEKID.abilities = species.abilities(239)
ELEKID.hidden_ability = species.hidden_ability(239)

#############
### MAGBY ###
#############

MAGBY = Pokemon()
MAGBY.species = 240
MAGBY.types = FIRE
MAGBY.abilities = species.abilities(240)
MAGBY.hidden_ability = species.hidden_ability(240)

###############
### MILTANK ###
###############

MILTANK = Pokemon()
MILTANK.species = 241
MILTANK.types = NORMAL
MILTANK.abilities = species.abilities(241)
MILTANK.hidden_ability = species.hidden_ability(241)

###############
### BLISSEY ###
###############

BLISSEY = Pokemon()
BLISSEY.species = 242
BLISSEY.types = NORMAL
BLISSEY.abilities = species.abilities(242)
BLISSEY.hidden_ability = species.hidden_ability(242)

##############
### RAIKOU ###
##############

RAIKOU = Pokemon()
RAIKOU.species = 243
RAIKOU.types = ELECTRIC
RAIKOU.abilities = species.abilities(243)
RAIKOU.hidden_ability = species.hidden_ability(243)

#############
### ENTEI ###
#############

ENTEI = Pokemon()
ENTEI.species = 244
ENTEI.types = FIRE
ENTEI.abilities = species.abilities(244)
ENTEI.hidden_ability = species.hidden_ability(244)

###############
### SUICUNE ###
###############

SUICUNE = Pokemon()
SUICUNE.species = 245
SUICUNE.types = WATER
SUICUNE.abilities = species.abilities(245)
SUICUNE.hidden_ability = species.hidden_ability(245)

################
### LARVITAR ###
################

LARVITAR = Pokemon()
LARVITAR.species = 246
LARVITAR.types = ROCK
LARVITAR.types = [LARVITAR.types, GROUND]
LARVITAR.abilities = species.abilities(246)
LARVITAR.hidden_ability = species.hidden_ability(246)

###############
### PUPITAR ###
###############

PUPITAR = Pokemon()
PUPITAR.species = 247
PUPITAR.types = ROCK
PUPITAR.types = [PUPITAR.types, GROUND]
PUPITAR.abilities = species.abilities(247)
PUPITAR.hidden_ability = species.hidden_ability(247)

#################
### TYRANITAR ###
#################

TYRANITAR = Pokemon()
TYRANITAR.species = 248
TYRANITAR.types = ROCK
TYRANITAR.types = [TYRANITAR.types, DARK]
TYRANITAR.abilities = species.abilities(248)
TYRANITAR.hidden_ability = species.hidden_ability(248)

#############
### LUGIA ###
#############

LUGIA = Pokemon()
LUGIA.species = 249
LUGIA.types = PSYCHIC
LUGIA.types = [LUGIA.types, FLYING]
LUGIA.abilities = species.abilities(249)
LUGIA.hidden_ability = species.hidden_ability(249)

############
### HOOH ###
############

HOOH = Pokemon()
HOOH.types = FIRE
HOOH.types = [HOOH.types, FLYING]
##############
### CELEBI ###
##############

CELEBI = Pokemon()
CELEBI.species = 251
CELEBI.types = PSYCHIC
CELEBI.types = [CELEBI.types, GRASS]
CELEBI.abilities = species.abilities(251)
CELEBI.hidden_ability = species.hidden_ability(251)

###############
### TREECKO ###
###############

TREECKO = Pokemon()
TREECKO.species = 252
TREECKO.types = GRASS
TREECKO.abilities = species.abilities(252)
TREECKO.hidden_ability = species.hidden_ability(252)

###############
### GROVYLE ###
###############

GROVYLE = Pokemon()
GROVYLE.species = 253
GROVYLE.types = GRASS
GROVYLE.abilities = species.abilities(253)
GROVYLE.hidden_ability = species.hidden_ability(253)

################
### SCEPTILE ###
################

SCEPTILE = Pokemon()
SCEPTILE.species = 254
SCEPTILE.types = GRASS
SCEPTILE.abilities = species.abilities(254)
SCEPTILE.hidden_ability = species.hidden_ability(254)

###############
### TORCHIC ###
###############

TORCHIC = Pokemon()
TORCHIC.species = 255
TORCHIC.types = FIRE
TORCHIC.abilities = species.abilities(255)
TORCHIC.hidden_ability = species.hidden_ability(255)

#################
### COMBUSKEN ###
#################

COMBUSKEN = Pokemon()
COMBUSKEN.species = 256
COMBUSKEN.types = FIRE
COMBUSKEN.types = [COMBUSKEN.types, FIGHTING]
COMBUSKEN.abilities = species.abilities(256)
COMBUSKEN.hidden_ability = species.hidden_ability(256)

################
### BLAZIKEN ###
################

BLAZIKEN = Pokemon()
BLAZIKEN.species = 257
BLAZIKEN.types = FIRE
BLAZIKEN.types = [BLAZIKEN.types, FIGHTING]
BLAZIKEN.abilities = species.abilities(257)
BLAZIKEN.hidden_ability = species.hidden_ability(257)

##############
### MUDKIP ###
##############

MUDKIP = Pokemon()
MUDKIP.species = 258
MUDKIP.types = WATER
MUDKIP.abilities = species.abilities(258)
MUDKIP.hidden_ability = species.hidden_ability(258)

#################
### MARSHTOMP ###
#################

MARSHTOMP = Pokemon()
MARSHTOMP.species = 259
MARSHTOMP.types = WATER
MARSHTOMP.types = [MARSHTOMP.types, GROUND]
MARSHTOMP.abilities = species.abilities(259)
MARSHTOMP.hidden_ability = species.hidden_ability(259)

################
### SWAMPERT ###
################

SWAMPERT = Pokemon()
SWAMPERT.species = 260
SWAMPERT.types = WATER
SWAMPERT.types = [SWAMPERT.types, GROUND]
SWAMPERT.abilities = species.abilities(260)
SWAMPERT.hidden_ability = species.hidden_ability(260)

#################
### POOCHYENA ###
#################

POOCHYENA = Pokemon()
POOCHYENA.species = 261
POOCHYENA.types = DARK
POOCHYENA.abilities = species.abilities(261)
POOCHYENA.hidden_ability = species.hidden_ability(261)

#################
### MIGHTYENA ###
#################

MIGHTYENA = Pokemon()
MIGHTYENA.species = 262
MIGHTYENA.types = DARK
MIGHTYENA.abilities = species.abilities(262)
MIGHTYENA.hidden_ability = species.hidden_ability(262)

#################
### ZIGZAGOON ###
#################

ZIGZAGOON = Pokemon()
ZIGZAGOON.species = 263
ZIGZAGOON.types = NORMAL
ZIGZAGOON.abilities = species.abilities(263)
ZIGZAGOON.hidden_ability = species.hidden_ability(263)

###############
### LINOONE ###
###############

LINOONE = Pokemon()
LINOONE.species = 264
LINOONE.types = NORMAL
LINOONE.abilities = species.abilities(264)
LINOONE.hidden_ability = species.hidden_ability(264)

###############
### WURMPLE ###
###############

WURMPLE = Pokemon()
WURMPLE.species = 265
WURMPLE.types = BUG
WURMPLE.abilities = species.abilities(265)
WURMPLE.hidden_ability = species.hidden_ability(265)

###############
### SILCOON ###
###############

SILCOON = Pokemon()
SILCOON.species = 266
SILCOON.types = BUG
SILCOON.abilities = species.abilities(266)
SILCOON.hidden_ability = species.hidden_ability(266)

#################
### BEAUTIFLY ###
#################

BEAUTIFLY = Pokemon()
BEAUTIFLY.species = 267
BEAUTIFLY.types = BUG
BEAUTIFLY.types = [BEAUTIFLY.types, FLYING]
BEAUTIFLY.abilities = species.abilities(267)
BEAUTIFLY.hidden_ability = species.hidden_ability(267)

###############
### CASCOON ###
###############

CASCOON = Pokemon()
CASCOON.species = 268
CASCOON.types = BUG
CASCOON.abilities = species.abilities(268)
CASCOON.hidden_ability = species.hidden_ability(268)

##############
### DUSTOX ###
##############

DUSTOX = Pokemon()
DUSTOX.species = 269
DUSTOX.types = BUG
DUSTOX.types = [DUSTOX.types, POISON]
DUSTOX.abilities = species.abilities(269)
DUSTOX.hidden_ability = species.hidden_ability(269)

#############
### LOTAD ###
#############

LOTAD = Pokemon()
LOTAD.species = 270
LOTAD.types = WATER
LOTAD.types = [LOTAD.types, GRASS]
LOTAD.abilities = species.abilities(270)
LOTAD.hidden_ability = species.hidden_ability(270)

##############
### LOMBRE ###
##############

LOMBRE = Pokemon()
LOMBRE.species = 271
LOMBRE.types = WATER
LOMBRE.types = [LOMBRE.types, GRASS]
LOMBRE.abilities = species.abilities(271)
LOMBRE.hidden_ability = species.hidden_ability(271)

################
### LUDICOLO ###
################

LUDICOLO = Pokemon()
LUDICOLO.species = 272
LUDICOLO.types = WATER
LUDICOLO.types = [LUDICOLO.types, GRASS]
LUDICOLO.abilities = species.abilities(272)
LUDICOLO.hidden_ability = species.hidden_ability(272)

##############
### SEEDOT ###
##############

SEEDOT = Pokemon()
SEEDOT.species = 273
SEEDOT.types = GRASS
SEEDOT.abilities = species.abilities(273)
SEEDOT.hidden_ability = species.hidden_ability(273)

###############
### NUZLEAF ###
###############

NUZLEAF = Pokemon()
NUZLEAF.species = 274
NUZLEAF.types = GRASS
NUZLEAF.types = [NUZLEAF.types, DARK]
NUZLEAF.abilities = species.abilities(274)
NUZLEAF.hidden_ability = species.hidden_ability(274)

###############
### SHIFTRY ###
###############

SHIFTRY = Pokemon()
SHIFTRY.species = 275
SHIFTRY.types = GRASS
SHIFTRY.types = [SHIFTRY.types, DARK]
SHIFTRY.abilities = species.abilities(275)
SHIFTRY.hidden_ability = species.hidden_ability(275)

###############
### TAILLOW ###
###############

TAILLOW = Pokemon()
TAILLOW.species = 276
TAILLOW.types = NORMAL
TAILLOW.types = [TAILLOW.types, FLYING]
TAILLOW.abilities = species.abilities(276)
TAILLOW.hidden_ability = species.hidden_ability(276)

###############
### SWELLOW ###
###############

SWELLOW = Pokemon()
SWELLOW.species = 277
SWELLOW.types = NORMAL
SWELLOW.types = [SWELLOW.types, FLYING]
SWELLOW.abilities = species.abilities(277)
SWELLOW.hidden_ability = species.hidden_ability(277)

###############
### WINGULL ###
###############

WINGULL = Pokemon()
WINGULL.species = 278
WINGULL.types = WATER
WINGULL.types = [WINGULL.types, FLYING]
WINGULL.abilities = species.abilities(278)
WINGULL.hidden_ability = species.hidden_ability(278)

################
### PELIPPER ###
################

PELIPPER = Pokemon()
PELIPPER.species = 279
PELIPPER.types = WATER
PELIPPER.types = [PELIPPER.types, FLYING]
PELIPPER.abilities = species.abilities(279)
PELIPPER.hidden_ability = species.hidden_ability(279)

#############
### RALTS ###
#############

RALTS = Pokemon()
RALTS.species = 280
RALTS.types = PSYCHIC
RALTS.types = [RALTS.types, FAIRY]
RALTS.abilities = species.abilities(280)
RALTS.hidden_ability = species.hidden_ability(280)

##############
### KIRLIA ###
##############

KIRLIA = Pokemon()
KIRLIA.species = 281
KIRLIA.types = PSYCHIC
KIRLIA.types = [KIRLIA.types, FAIRY]
KIRLIA.abilities = species.abilities(281)
KIRLIA.hidden_ability = species.hidden_ability(281)

#################
### GARDEVOIR ###
#################

GARDEVOIR = Pokemon()
GARDEVOIR.species = 282
GARDEVOIR.types = PSYCHIC
GARDEVOIR.types = [GARDEVOIR.types, FAIRY]
GARDEVOIR.abilities = species.abilities(282)
GARDEVOIR.hidden_ability = species.hidden_ability(282)

###############
### SURSKIT ###
###############

SURSKIT = Pokemon()
SURSKIT.species = 283
SURSKIT.types = BUG
SURSKIT.types = [SURSKIT.types, WATER]
SURSKIT.abilities = species.abilities(283)
SURSKIT.hidden_ability = species.hidden_ability(283)

##################
### MASQUERAIN ###
##################

MASQUERAIN = Pokemon()
MASQUERAIN.species = 284
MASQUERAIN.types = BUG
MASQUERAIN.types = [MASQUERAIN.types, FLYING]
MASQUERAIN.abilities = species.abilities(284)
MASQUERAIN.hidden_ability = species.hidden_ability(284)

#################
### SHROOMISH ###
#################

SHROOMISH = Pokemon()
SHROOMISH.species = 285
SHROOMISH.types = GRASS
SHROOMISH.abilities = species.abilities(285)
SHROOMISH.hidden_ability = species.hidden_ability(285)

###############
### BRELOOM ###
###############

BRELOOM = Pokemon()
BRELOOM.species = 286
BRELOOM.types = GRASS
BRELOOM.types = [BRELOOM.types, FIGHTING]
BRELOOM.abilities = species.abilities(286)
BRELOOM.hidden_ability = species.hidden_ability(286)

###############
### SLAKOTH ###
###############

SLAKOTH = Pokemon()
SLAKOTH.species = 287
SLAKOTH.types = NORMAL
SLAKOTH.abilities = species.abilities(287)
SLAKOTH.hidden_ability = species.hidden_ability(287)

################
### VIGOROTH ###
################

VIGOROTH = Pokemon()
VIGOROTH.species = 288
VIGOROTH.types = NORMAL
VIGOROTH.abilities = species.abilities(288)
VIGOROTH.hidden_ability = species.hidden_ability(288)

###############
### SLAKING ###
###############

SLAKING = Pokemon()
SLAKING.species = 289
SLAKING.types = NORMAL
SLAKING.abilities = species.abilities(289)
SLAKING.hidden_ability = species.hidden_ability(289)

###############
### NINCADA ###
###############

NINCADA = Pokemon()
NINCADA.species = 290
NINCADA.types = BUG
NINCADA.types = [NINCADA.types, GROUND]
NINCADA.abilities = species.abilities(290)
NINCADA.hidden_ability = species.hidden_ability(290)

###############
### NINJASK ###
###############

NINJASK = Pokemon()
NINJASK.species = 291
NINJASK.types = BUG
NINJASK.types = [NINJASK.types, FLYING]
NINJASK.abilities = species.abilities(291)
NINJASK.hidden_ability = species.hidden_ability(291)

################
### SHEDINJA ###
################

SHEDINJA = Pokemon()
SHEDINJA.species = 292
SHEDINJA.types = BUG
SHEDINJA.types = [SHEDINJA.types, GHOST]
SHEDINJA.abilities = species.abilities(292)
SHEDINJA.hidden_ability = species.hidden_ability(292)

###############
### WHISMUR ###
###############

WHISMUR = Pokemon()
WHISMUR.species = 293
WHISMUR.types = NORMAL
WHISMUR.abilities = species.abilities(293)
WHISMUR.hidden_ability = species.hidden_ability(293)

###############
### LOUDRED ###
###############

LOUDRED = Pokemon()
LOUDRED.species = 294
LOUDRED.types = NORMAL
LOUDRED.abilities = species.abilities(294)
LOUDRED.hidden_ability = species.hidden_ability(294)

###############
### EXPLOUD ###
###############

EXPLOUD = Pokemon()
EXPLOUD.species = 295
EXPLOUD.types = NORMAL
EXPLOUD.abilities = species.abilities(295)
EXPLOUD.hidden_ability = species.hidden_ability(295)

################
### MAKUHITA ###
################

MAKUHITA = Pokemon()
MAKUHITA.species = 296
MAKUHITA.types = FIGHTING
MAKUHITA.abilities = species.abilities(296)
MAKUHITA.hidden_ability = species.hidden_ability(296)

################
### HARIYAMA ###
################

HARIYAMA = Pokemon()
HARIYAMA.species = 297
HARIYAMA.types = FIGHTING
HARIYAMA.abilities = species.abilities(297)
HARIYAMA.hidden_ability = species.hidden_ability(297)

###############
### AZURILL ###
###############

AZURILL = Pokemon()
AZURILL.species = 298
AZURILL.types = NORMAL
AZURILL.types = [AZURILL.types, FAIRY]
AZURILL.abilities = species.abilities(298)
AZURILL.hidden_ability = species.hidden_ability(298)

################
### NOSEPASS ###
################

NOSEPASS = Pokemon()
NOSEPASS.species = 299
NOSEPASS.types = ROCK
NOSEPASS.abilities = species.abilities(299)
NOSEPASS.hidden_ability = species.hidden_ability(299)

##############
### SKITTY ###
##############

SKITTY = Pokemon()
SKITTY.species = 300
SKITTY.types = NORMAL
SKITTY.abilities = species.abilities(300)
SKITTY.hidden_ability = species.hidden_ability(300)

################
### DELCATTY ###
################

DELCATTY = Pokemon()
DELCATTY.species = 301
DELCATTY.types = NORMAL
DELCATTY.abilities = species.abilities(301)
DELCATTY.hidden_ability = species.hidden_ability(301)

###############
### SABLEYE ###
###############

SABLEYE = Pokemon()
SABLEYE.species = 302
SABLEYE.types = DARK
SABLEYE.types = [SABLEYE.types, GHOST]
SABLEYE.abilities = species.abilities(302)
SABLEYE.hidden_ability = species.hidden_ability(302)

##############
### MAWILE ###
##############

MAWILE = Pokemon()
MAWILE.species = 303
MAWILE.types = STEEL
MAWILE.types = [MAWILE.types, FAIRY]
MAWILE.abilities = species.abilities(303)
MAWILE.hidden_ability = species.hidden_ability(303)

############
### ARON ###
############

ARON = Pokemon()
ARON.species = 304
ARON.types = STEEL
ARON.types = [ARON.types, ROCK]
ARON.abilities = species.abilities(304)
ARON.hidden_ability = species.hidden_ability(304)

##############
### LAIRON ###
##############

LAIRON = Pokemon()
LAIRON.species = 305
LAIRON.types = STEEL
LAIRON.types = [LAIRON.types, ROCK]
LAIRON.abilities = species.abilities(305)
LAIRON.hidden_ability = species.hidden_ability(305)

##############
### AGGRON ###
##############

AGGRON = Pokemon()
AGGRON.species = 306
AGGRON.types = STEEL
AGGRON.types = [AGGRON.types, ROCK]
AGGRON.abilities = species.abilities(306)
AGGRON.hidden_ability = species.hidden_ability(306)

################
### MEDITITE ###
################

MEDITITE = Pokemon()
MEDITITE.species = 307
MEDITITE.types = FIGHTING
MEDITITE.types = [MEDITITE.types, PSYCHIC]
MEDITITE.abilities = species.abilities(307)
MEDITITE.hidden_ability = species.hidden_ability(307)

################
### MEDICHAM ###
################

MEDICHAM = Pokemon()
MEDICHAM.species = 308
MEDICHAM.types = FIGHTING
MEDICHAM.types = [MEDICHAM.types, PSYCHIC]
MEDICHAM.abilities = species.abilities(308)
MEDICHAM.hidden_ability = species.hidden_ability(308)

#################
### ELECTRIKE ###
#################

ELECTRIKE = Pokemon()
ELECTRIKE.species = 309
ELECTRIKE.types = ELECTRIC
ELECTRIKE.abilities = species.abilities(309)
ELECTRIKE.hidden_ability = species.hidden_ability(309)

#################
### MANECTRIC ###
#################

MANECTRIC = Pokemon()
MANECTRIC.species = 310
MANECTRIC.types = ELECTRIC
MANECTRIC.abilities = species.abilities(310)
MANECTRIC.hidden_ability = species.hidden_ability(310)

##############
### PLUSLE ###
##############

PLUSLE = Pokemon()
PLUSLE.species = 311
PLUSLE.types = ELECTRIC
PLUSLE.abilities = species.abilities(311)
PLUSLE.hidden_ability = species.hidden_ability(311)

#############
### MINUN ###
#############

MINUN = Pokemon()
MINUN.species = 312
MINUN.types = ELECTRIC
MINUN.abilities = species.abilities(312)
MINUN.hidden_ability = species.hidden_ability(312)

###############
### VOLBEAT ###
###############

VOLBEAT = Pokemon()
VOLBEAT.species = 313
VOLBEAT.types = BUG
VOLBEAT.abilities = species.abilities(313)
VOLBEAT.hidden_ability = species.hidden_ability(313)

################
### ILLUMISE ###
################

ILLUMISE = Pokemon()
ILLUMISE.species = 314
ILLUMISE.types = BUG
ILLUMISE.abilities = species.abilities(314)
ILLUMISE.hidden_ability = species.hidden_ability(314)

###############
### ROSELIA ###
###############

ROSELIA = Pokemon()
ROSELIA.species = 315
ROSELIA.types = GRASS
ROSELIA.types = [ROSELIA.types, POISON]
ROSELIA.abilities = species.abilities(315)
ROSELIA.hidden_ability = species.hidden_ability(315)

##############
### GULPIN ###
##############

GULPIN = Pokemon()
GULPIN.species = 316
GULPIN.types = POISON
GULPIN.abilities = species.abilities(316)
GULPIN.hidden_ability = species.hidden_ability(316)

##############
### SWALOT ###
##############

SWALOT = Pokemon()
SWALOT.species = 317
SWALOT.types = POISON
SWALOT.abilities = species.abilities(317)
SWALOT.hidden_ability = species.hidden_ability(317)

################
### CARVANHA ###
################

CARVANHA = Pokemon()
CARVANHA.species = 318
CARVANHA.types = WATER
CARVANHA.types = [CARVANHA.types, DARK]
CARVANHA.abilities = species.abilities(318)
CARVANHA.hidden_ability = species.hidden_ability(318)

################
### SHARPEDO ###
################

SHARPEDO = Pokemon()
SHARPEDO.species = 319
SHARPEDO.types = WATER
SHARPEDO.types = [SHARPEDO.types, DARK]
SHARPEDO.abilities = species.abilities(319)
SHARPEDO.hidden_ability = species.hidden_ability(319)

###############
### WAILMER ###
###############

WAILMER = Pokemon()
WAILMER.species = 320
WAILMER.types = WATER
WAILMER.abilities = species.abilities(320)
WAILMER.hidden_ability = species.hidden_ability(320)

###############
### WAILORD ###
###############

WAILORD = Pokemon()
WAILORD.species = 321
WAILORD.types = WATER
WAILORD.abilities = species.abilities(321)
WAILORD.hidden_ability = species.hidden_ability(321)

#############
### NUMEL ###
#############

NUMEL = Pokemon()
NUMEL.species = 322
NUMEL.types = FIRE
NUMEL.types = [NUMEL.types, GROUND]
NUMEL.abilities = species.abilities(322)
NUMEL.hidden_ability = species.hidden_ability(322)

################
### CAMERUPT ###
################

CAMERUPT = Pokemon()
CAMERUPT.species = 323
CAMERUPT.types = FIRE
CAMERUPT.types = [CAMERUPT.types, GROUND]
CAMERUPT.abilities = species.abilities(323)
CAMERUPT.hidden_ability = species.hidden_ability(323)

###############
### TORKOAL ###
###############

TORKOAL = Pokemon()
TORKOAL.species = 324
TORKOAL.types = FIRE
TORKOAL.abilities = species.abilities(324)
TORKOAL.hidden_ability = species.hidden_ability(324)

##############
### SPOINK ###
##############

SPOINK = Pokemon()
SPOINK.species = 325
SPOINK.types = PSYCHIC
SPOINK.abilities = species.abilities(325)
SPOINK.hidden_ability = species.hidden_ability(325)

###############
### GRUMPIG ###
###############

GRUMPIG = Pokemon()
GRUMPIG.species = 326
GRUMPIG.types = PSYCHIC
GRUMPIG.abilities = species.abilities(326)
GRUMPIG.hidden_ability = species.hidden_ability(326)

##############
### SPINDA ###
##############

SPINDA = Pokemon()
SPINDA.species = 327
SPINDA.types = NORMAL
SPINDA.abilities = species.abilities(327)
SPINDA.hidden_ability = species.hidden_ability(327)

################
### TRAPINCH ###
################

TRAPINCH = Pokemon()
TRAPINCH.species = 328
TRAPINCH.types = GROUND
TRAPINCH.abilities = species.abilities(328)
TRAPINCH.hidden_ability = species.hidden_ability(328)

###############
### VIBRAVA ###
###############

VIBRAVA = Pokemon()
VIBRAVA.species = 329
VIBRAVA.types = GROUND
VIBRAVA.types = [VIBRAVA.types, DRAGON]
VIBRAVA.abilities = species.abilities(329)
VIBRAVA.hidden_ability = species.hidden_ability(329)

##############
### FLYGON ###
##############

FLYGON = Pokemon()
FLYGON.species = 330
FLYGON.types = GROUND
FLYGON.types = [FLYGON.types, DRAGON]
FLYGON.abilities = species.abilities(330)
FLYGON.hidden_ability = species.hidden_ability(330)

##############
### CACNEA ###
##############

CACNEA = Pokemon()
CACNEA.species = 331
CACNEA.types = GRASS
CACNEA.abilities = species.abilities(331)
CACNEA.hidden_ability = species.hidden_ability(331)

################
### CACTURNE ###
################

CACTURNE = Pokemon()
CACTURNE.species = 332
CACTURNE.types = GRASS
CACTURNE.types = [CACTURNE.types, DARK]
CACTURNE.abilities = species.abilities(332)
CACTURNE.hidden_ability = species.hidden_ability(332)

##############
### SWABLU ###
##############

SWABLU = Pokemon()
SWABLU.species = 333
SWABLU.types = NORMAL
SWABLU.types = [SWABLU.types, FLYING]
SWABLU.abilities = species.abilities(333)
SWABLU.hidden_ability = species.hidden_ability(333)

###############
### ALTARIA ###
###############

ALTARIA = Pokemon()
ALTARIA.species = 334
ALTARIA.types = DRAGON
ALTARIA.types = [ALTARIA.types, FLYING]
ALTARIA.abilities = species.abilities(334)
ALTARIA.hidden_ability = species.hidden_ability(334)

################
### ZANGOOSE ###
################

ZANGOOSE = Pokemon()
ZANGOOSE.species = 335
ZANGOOSE.types = NORMAL
ZANGOOSE.abilities = species.abilities(335)
ZANGOOSE.hidden_ability = species.hidden_ability(335)

###############
### SEVIPER ###
###############

SEVIPER = Pokemon()
SEVIPER.species = 336
SEVIPER.types = POISON
SEVIPER.abilities = species.abilities(336)
SEVIPER.hidden_ability = species.hidden_ability(336)

################
### LUNATONE ###
################

LUNATONE = Pokemon()
LUNATONE.species = 337
LUNATONE.types = ROCK
LUNATONE.types = [LUNATONE.types, PSYCHIC]
LUNATONE.abilities = species.abilities(337)
LUNATONE.hidden_ability = species.hidden_ability(337)

###############
### SOLROCK ###
###############

SOLROCK = Pokemon()
SOLROCK.species = 338
SOLROCK.types = ROCK
SOLROCK.types = [SOLROCK.types, PSYCHIC]
SOLROCK.abilities = species.abilities(338)
SOLROCK.hidden_ability = species.hidden_ability(338)

################
### BARBOACH ###
################

BARBOACH = Pokemon()
BARBOACH.species = 339
BARBOACH.types = WATER
BARBOACH.types = [BARBOACH.types, GROUND]
BARBOACH.abilities = species.abilities(339)
BARBOACH.hidden_ability = species.hidden_ability(339)

################
### WHISCASH ###
################

WHISCASH = Pokemon()
WHISCASH.species = 340
WHISCASH.types = WATER
WHISCASH.types = [WHISCASH.types, GROUND]
WHISCASH.abilities = species.abilities(340)
WHISCASH.hidden_ability = species.hidden_ability(340)

################
### CORPHISH ###
################

CORPHISH = Pokemon()
CORPHISH.species = 341
CORPHISH.types = WATER
CORPHISH.abilities = species.abilities(341)
CORPHISH.hidden_ability = species.hidden_ability(341)

#################
### CRAWDAUNT ###
#################

CRAWDAUNT = Pokemon()
CRAWDAUNT.species = 342
CRAWDAUNT.types = WATER
CRAWDAUNT.types = [CRAWDAUNT.types, DARK]
CRAWDAUNT.abilities = species.abilities(342)
CRAWDAUNT.hidden_ability = species.hidden_ability(342)

##############
### BALTOY ###
##############

BALTOY = Pokemon()
BALTOY.species = 343
BALTOY.types = GROUND
BALTOY.types = [BALTOY.types, PSYCHIC]
BALTOY.abilities = species.abilities(343)
BALTOY.hidden_ability = species.hidden_ability(343)

###############
### CLAYDOL ###
###############

CLAYDOL = Pokemon()
CLAYDOL.species = 344
CLAYDOL.types = GROUND
CLAYDOL.types = [CLAYDOL.types, PSYCHIC]
CLAYDOL.abilities = species.abilities(344)
CLAYDOL.hidden_ability = species.hidden_ability(344)

##############
### LILEEP ###
##############

LILEEP = Pokemon()
LILEEP.species = 345
LILEEP.types = ROCK
LILEEP.types = [LILEEP.types, GRASS]
LILEEP.abilities = species.abilities(345)
LILEEP.hidden_ability = species.hidden_ability(345)

###############
### CRADILY ###
###############

CRADILY = Pokemon()
CRADILY.species = 346
CRADILY.types = ROCK
CRADILY.types = [CRADILY.types, GRASS]
CRADILY.abilities = species.abilities(346)
CRADILY.hidden_ability = species.hidden_ability(346)

###############
### ANORITH ###
###############

ANORITH = Pokemon()
ANORITH.species = 347
ANORITH.types = ROCK
ANORITH.types = [ANORITH.types, BUG]
ANORITH.abilities = species.abilities(347)
ANORITH.hidden_ability = species.hidden_ability(347)

###############
### ARMALDO ###
###############

ARMALDO = Pokemon()
ARMALDO.species = 348
ARMALDO.types = ROCK
ARMALDO.types = [ARMALDO.types, BUG]
ARMALDO.abilities = species.abilities(348)
ARMALDO.hidden_ability = species.hidden_ability(348)

##############
### FEEBAS ###
##############

FEEBAS = Pokemon()
FEEBAS.species = 349
FEEBAS.types = WATER
FEEBAS.abilities = species.abilities(349)
FEEBAS.hidden_ability = species.hidden_ability(349)

###############
### MILOTIC ###
###############

MILOTIC = Pokemon()
MILOTIC.species = 350
MILOTIC.types = WATER
MILOTIC.abilities = species.abilities(350)
MILOTIC.hidden_ability = species.hidden_ability(350)

################
### CASTFORM ###
################

CASTFORM = Pokemon()
CASTFORM.species = 351
CASTFORM.types = NORMAL
CASTFORM.abilities = species.abilities(351)
CASTFORM.hidden_ability = species.hidden_ability(351)

###############
### KECLEON ###
###############

KECLEON = Pokemon()
KECLEON.species = 352
KECLEON.types = NORMAL
KECLEON.abilities = species.abilities(352)
KECLEON.hidden_ability = species.hidden_ability(352)

###############
### SHUPPET ###
###############

SHUPPET = Pokemon()
SHUPPET.species = 353
SHUPPET.types = GHOST
SHUPPET.abilities = species.abilities(353)
SHUPPET.hidden_ability = species.hidden_ability(353)

###############
### BANETTE ###
###############

BANETTE = Pokemon()
BANETTE.species = 354
BANETTE.types = GHOST
BANETTE.abilities = species.abilities(354)
BANETTE.hidden_ability = species.hidden_ability(354)

###############
### DUSKULL ###
###############

DUSKULL = Pokemon()
DUSKULL.species = 355
DUSKULL.types = GHOST
DUSKULL.abilities = species.abilities(355)
DUSKULL.hidden_ability = species.hidden_ability(355)

################
### DUSCLOPS ###
################

DUSCLOPS = Pokemon()
DUSCLOPS.species = 356
DUSCLOPS.types = GHOST
DUSCLOPS.abilities = species.abilities(356)
DUSCLOPS.hidden_ability = species.hidden_ability(356)

###############
### TROPIUS ###
###############

TROPIUS = Pokemon()
TROPIUS.species = 357
TROPIUS.types = GRASS
TROPIUS.types = [TROPIUS.types, FLYING]
TROPIUS.abilities = species.abilities(357)
TROPIUS.hidden_ability = species.hidden_ability(357)

################
### CHIMECHO ###
################

CHIMECHO = Pokemon()
CHIMECHO.species = 358
CHIMECHO.types = PSYCHIC
CHIMECHO.abilities = species.abilities(358)
CHIMECHO.hidden_ability = species.hidden_ability(358)

#############
### ABSOL ###
#############

ABSOL = Pokemon()
ABSOL.species = 359
ABSOL.types = DARK
ABSOL.abilities = species.abilities(359)
ABSOL.hidden_ability = species.hidden_ability(359)

##############
### WYNAUT ###
##############

WYNAUT = Pokemon()
WYNAUT.species = 360
WYNAUT.types = PSYCHIC
WYNAUT.abilities = species.abilities(360)
WYNAUT.hidden_ability = species.hidden_ability(360)

###############
### SNORUNT ###
###############

SNORUNT = Pokemon()
SNORUNT.species = 361
SNORUNT.types = ICE
SNORUNT.abilities = species.abilities(361)
SNORUNT.hidden_ability = species.hidden_ability(361)

##############
### GLALIE ###
##############

GLALIE = Pokemon()
GLALIE.species = 362
GLALIE.types = ICE
GLALIE.abilities = species.abilities(362)
GLALIE.hidden_ability = species.hidden_ability(362)

##############
### SPHEAL ###
##############

SPHEAL = Pokemon()
SPHEAL.species = 363
SPHEAL.types = ICE
SPHEAL.types = [SPHEAL.types, WATER]
SPHEAL.abilities = species.abilities(363)
SPHEAL.hidden_ability = species.hidden_ability(363)

##############
### SEALEO ###
##############

SEALEO = Pokemon()
SEALEO.species = 364
SEALEO.types = ICE
SEALEO.types = [SEALEO.types, WATER]
SEALEO.abilities = species.abilities(364)
SEALEO.hidden_ability = species.hidden_ability(364)

###############
### WALREIN ###
###############

WALREIN = Pokemon()
WALREIN.species = 365
WALREIN.types = ICE
WALREIN.types = [WALREIN.types, WATER]
WALREIN.abilities = species.abilities(365)
WALREIN.hidden_ability = species.hidden_ability(365)

################
### CLAMPERL ###
################

CLAMPERL = Pokemon()
CLAMPERL.species = 366
CLAMPERL.types = WATER
CLAMPERL.abilities = species.abilities(366)
CLAMPERL.hidden_ability = species.hidden_ability(366)

###############
### HUNTAIL ###
###############

HUNTAIL = Pokemon()
HUNTAIL.species = 367
HUNTAIL.types = WATER
HUNTAIL.abilities = species.abilities(367)
HUNTAIL.hidden_ability = species.hidden_ability(367)

################
### GOREBYSS ###
################

GOREBYSS = Pokemon()
GOREBYSS.species = 368
GOREBYSS.types = WATER
GOREBYSS.abilities = species.abilities(368)
GOREBYSS.hidden_ability = species.hidden_ability(368)

#################
### RELICANTH ###
#################

RELICANTH = Pokemon()
RELICANTH.species = 369
RELICANTH.types = WATER
RELICANTH.types = [RELICANTH.types, ROCK]
RELICANTH.abilities = species.abilities(369)
RELICANTH.hidden_ability = species.hidden_ability(369)

###############
### LUVDISC ###
###############

LUVDISC = Pokemon()
LUVDISC.species = 370
LUVDISC.types = WATER
LUVDISC.abilities = species.abilities(370)
LUVDISC.hidden_ability = species.hidden_ability(370)

#############
### BAGON ###
#############

BAGON = Pokemon()
BAGON.species = 371
BAGON.types = DRAGON
BAGON.abilities = species.abilities(371)
BAGON.hidden_ability = species.hidden_ability(371)

###############
### SHELGON ###
###############

SHELGON = Pokemon()
SHELGON.species = 372
SHELGON.types = DRAGON
SHELGON.abilities = species.abilities(372)
SHELGON.hidden_ability = species.hidden_ability(372)

#################
### SALAMENCE ###
#################

SALAMENCE = Pokemon()
SALAMENCE.species = 373
SALAMENCE.types = DRAGON
SALAMENCE.types = [SALAMENCE.types, FLYING]
SALAMENCE.abilities = species.abilities(373)
SALAMENCE.hidden_ability = species.hidden_ability(373)

##############
### BELDUM ###
##############

BELDUM = Pokemon()
BELDUM.species = 374
BELDUM.types = STEEL
BELDUM.types = [BELDUM.types, PSYCHIC]
BELDUM.abilities = species.abilities(374)
BELDUM.hidden_ability = species.hidden_ability(374)

##############
### METANG ###
##############

METANG = Pokemon()
METANG.species = 375
METANG.types = STEEL
METANG.types = [METANG.types, PSYCHIC]
METANG.abilities = species.abilities(375)
METANG.hidden_ability = species.hidden_ability(375)

#################
### METAGROSS ###
#################

METAGROSS = Pokemon()
METAGROSS.species = 376
METAGROSS.types = STEEL
METAGROSS.types = [METAGROSS.types, PSYCHIC]
METAGROSS.abilities = species.abilities(376)
METAGROSS.hidden_ability = species.hidden_ability(376)

################
### REGIROCK ###
################

REGIROCK = Pokemon()
REGIROCK.species = 377
REGIROCK.types = ROCK
REGIROCK.abilities = species.abilities(377)
REGIROCK.hidden_ability = species.hidden_ability(377)

##############
### REGICE ###
##############

REGICE = Pokemon()
REGICE.species = 378
REGICE.types = ICE
REGICE.abilities = species.abilities(378)
REGICE.hidden_ability = species.hidden_ability(378)

#################
### REGISTEEL ###
#################

REGISTEEL = Pokemon()
REGISTEEL.species = 379
REGISTEEL.types = STEEL
REGISTEEL.abilities = species.abilities(379)
REGISTEEL.hidden_ability = species.hidden_ability(379)

##############
### LATIAS ###
##############

LATIAS = Pokemon()
LATIAS.species = 380
LATIAS.types = DRAGON
LATIAS.types = [LATIAS.types, PSYCHIC]
LATIAS.abilities = species.abilities(380)
LATIAS.hidden_ability = species.hidden_ability(380)

##############
### LATIOS ###
##############

LATIOS = Pokemon()
LATIOS.species = 381
LATIOS.types = DRAGON
LATIOS.types = [LATIOS.types, PSYCHIC]
LATIOS.abilities = species.abilities(381)
LATIOS.hidden_ability = species.hidden_ability(381)

##############
### KYOGRE ###
##############

KYOGRE = Pokemon()
KYOGRE.species = 382
KYOGRE.types = WATER
KYOGRE.abilities = species.abilities(382)
KYOGRE.hidden_ability = species.hidden_ability(382)

###############
### GROUDON ###
###############

GROUDON = Pokemon()
GROUDON.species = 383
GROUDON.types = GROUND
GROUDON.abilities = species.abilities(383)
GROUDON.hidden_ability = species.hidden_ability(383)

################
### RAYQUAZA ###
################

RAYQUAZA = Pokemon()
RAYQUAZA.species = 384
RAYQUAZA.types = DRAGON
RAYQUAZA.types = [RAYQUAZA.types, FLYING]
RAYQUAZA.abilities = species.abilities(384)
RAYQUAZA.hidden_ability = species.hidden_ability(384)

###############
### JIRACHI ###
###############

JIRACHI = Pokemon()
JIRACHI.species = 385
JIRACHI.types = STEEL
JIRACHI.types = [JIRACHI.types, PSYCHIC]
JIRACHI.abilities = species.abilities(385)
JIRACHI.hidden_ability = species.hidden_ability(385)

##############
### DEOXYS ###
##############

DEOXYS = Pokemon()
DEOXYS.species = 386
DEOXYS.types = PSYCHIC
DEOXYS.abilities = species.abilities(386)
DEOXYS.hidden_ability = species.hidden_ability(386)

###############
### TURTWIG ###
###############

TURTWIG = Pokemon()
TURTWIG.species = 387
TURTWIG.types = GRASS
TURTWIG.abilities = species.abilities(387)
TURTWIG.hidden_ability = species.hidden_ability(387)

##############
### GROTLE ###
##############

GROTLE = Pokemon()
GROTLE.species = 388
GROTLE.types = GRASS
GROTLE.abilities = species.abilities(388)
GROTLE.hidden_ability = species.hidden_ability(388)

################
### TORTERRA ###
################

TORTERRA = Pokemon()
TORTERRA.species = 389
TORTERRA.types = GRASS
TORTERRA.types = [TORTERRA.types, GROUND]
TORTERRA.abilities = species.abilities(389)
TORTERRA.hidden_ability = species.hidden_ability(389)

################
### CHIMCHAR ###
################

CHIMCHAR = Pokemon()
CHIMCHAR.species = 390
CHIMCHAR.types = FIRE
CHIMCHAR.abilities = species.abilities(390)
CHIMCHAR.hidden_ability = species.hidden_ability(390)

################
### MONFERNO ###
################

MONFERNO = Pokemon()
MONFERNO.species = 391
MONFERNO.types = FIRE
MONFERNO.types = [MONFERNO.types, FIGHTING]
MONFERNO.abilities = species.abilities(391)
MONFERNO.hidden_ability = species.hidden_ability(391)

#################
### INFERNAPE ###
#################

INFERNAPE = Pokemon()
INFERNAPE.species = 392
INFERNAPE.types = FIRE
INFERNAPE.types = [INFERNAPE.types, FIGHTING]
INFERNAPE.abilities = species.abilities(392)
INFERNAPE.hidden_ability = species.hidden_ability(392)

##############
### PIPLUP ###
##############

PIPLUP = Pokemon()
PIPLUP.species = 393
PIPLUP.types = WATER
PIPLUP.abilities = species.abilities(393)
PIPLUP.hidden_ability = species.hidden_ability(393)

################
### PRINPLUP ###
################

PRINPLUP = Pokemon()
PRINPLUP.species = 394
PRINPLUP.types = WATER
PRINPLUP.abilities = species.abilities(394)
PRINPLUP.hidden_ability = species.hidden_ability(394)

################
### EMPOLEON ###
################

EMPOLEON = Pokemon()
EMPOLEON.species = 395
EMPOLEON.types = WATER
EMPOLEON.types = [EMPOLEON.types, STEEL]
EMPOLEON.abilities = species.abilities(395)
EMPOLEON.hidden_ability = species.hidden_ability(395)

##############
### STARLY ###
##############

STARLY = Pokemon()
STARLY.species = 396
STARLY.types = NORMAL
STARLY.types = [STARLY.types, FLYING]
STARLY.abilities = species.abilities(396)
STARLY.hidden_ability = species.hidden_ability(396)

################
### STARAVIA ###
################

STARAVIA = Pokemon()
STARAVIA.species = 397
STARAVIA.types = NORMAL
STARAVIA.types = [STARAVIA.types, FLYING]
STARAVIA.abilities = species.abilities(397)
STARAVIA.hidden_ability = species.hidden_ability(397)

#################
### STARAPTOR ###
#################

STARAPTOR = Pokemon()
STARAPTOR.species = 398
STARAPTOR.types = NORMAL
STARAPTOR.types = [STARAPTOR.types, FLYING]
STARAPTOR.abilities = species.abilities(398)
STARAPTOR.hidden_ability = species.hidden_ability(398)

##############
### BIDOOF ###
##############

BIDOOF = Pokemon()
BIDOOF.species = 399
BIDOOF.types = NORMAL
BIDOOF.abilities = species.abilities(399)
BIDOOF.hidden_ability = species.hidden_ability(399)

###############
### BIBAREL ###
###############

BIBAREL = Pokemon()
BIBAREL.species = 400
BIBAREL.types = NORMAL
BIBAREL.types = [BIBAREL.types, WATER]
BIBAREL.abilities = species.abilities(400)
BIBAREL.hidden_ability = species.hidden_ability(400)

#################
### KRICKETOT ###
#################

KRICKETOT = Pokemon()
KRICKETOT.species = 401
KRICKETOT.types = BUG
KRICKETOT.abilities = species.abilities(401)
KRICKETOT.hidden_ability = species.hidden_ability(401)

##################
### KRICKETUNE ###
##################

KRICKETUNE = Pokemon()
KRICKETUNE.species = 402
KRICKETUNE.types = BUG
KRICKETUNE.abilities = species.abilities(402)
KRICKETUNE.hidden_ability = species.hidden_ability(402)

#############
### SHINX ###
#############

SHINX = Pokemon()
SHINX.species = 403
SHINX.types = ELECTRIC
SHINX.abilities = species.abilities(403)
SHINX.hidden_ability = species.hidden_ability(403)

#############
### LUXIO ###
#############

LUXIO = Pokemon()
LUXIO.species = 404
LUXIO.types = ELECTRIC
LUXIO.abilities = species.abilities(404)
LUXIO.hidden_ability = species.hidden_ability(404)

##############
### LUXRAY ###
##############

LUXRAY = Pokemon()
LUXRAY.species = 405
LUXRAY.types = ELECTRIC
LUXRAY.abilities = species.abilities(405)
LUXRAY.hidden_ability = species.hidden_ability(405)

#############
### BUDEW ###
#############

BUDEW = Pokemon()
BUDEW.species = 406
BUDEW.types = GRASS
BUDEW.types = [BUDEW.types, POISON]
BUDEW.abilities = species.abilities(406)
BUDEW.hidden_ability = species.hidden_ability(406)

################
### ROSERADE ###
################

ROSERADE = Pokemon()
ROSERADE.species = 407
ROSERADE.types = GRASS
ROSERADE.types = [ROSERADE.types, POISON]
ROSERADE.abilities = species.abilities(407)
ROSERADE.hidden_ability = species.hidden_ability(407)

################
### CRANIDOS ###
################

CRANIDOS = Pokemon()
CRANIDOS.species = 408
CRANIDOS.types = ROCK
CRANIDOS.abilities = species.abilities(408)
CRANIDOS.hidden_ability = species.hidden_ability(408)

#################
### RAMPARDOS ###
#################

RAMPARDOS = Pokemon()
RAMPARDOS.species = 409
RAMPARDOS.types = ROCK
RAMPARDOS.abilities = species.abilities(409)
RAMPARDOS.hidden_ability = species.hidden_ability(409)

################
### SHIELDON ###
################

SHIELDON = Pokemon()
SHIELDON.species = 410
SHIELDON.types = ROCK
SHIELDON.types = [SHIELDON.types, STEEL]
SHIELDON.abilities = species.abilities(410)
SHIELDON.hidden_ability = species.hidden_ability(410)

#################
### BASTIODON ###
#################

BASTIODON = Pokemon()
BASTIODON.species = 411
BASTIODON.types = ROCK
BASTIODON.types = [BASTIODON.types, STEEL]
BASTIODON.abilities = species.abilities(411)
BASTIODON.hidden_ability = species.hidden_ability(411)

#############
### BURMY ###
#############

BURMY = Pokemon()
BURMY.species = 412
BURMY.types = BUG
BURMY.abilities = species.abilities(412)
BURMY.hidden_ability = species.hidden_ability(412)

################
### WORMADAM ###
################

WORMADAM = Pokemon()
WORMADAM.species = 413
WORMADAM.types = BUG
WORMADAM.types = [WORMADAM.types, GRASS]
WORMADAM.abilities = species.abilities(413)
WORMADAM.hidden_ability = species.hidden_ability(413)

##############
### MOTHIM ###
##############

MOTHIM = Pokemon()
MOTHIM.species = 414
MOTHIM.types = BUG
MOTHIM.types = [MOTHIM.types, FLYING]
MOTHIM.abilities = species.abilities(414)
MOTHIM.hidden_ability = species.hidden_ability(414)

##############
### COMBEE ###
##############

COMBEE = Pokemon()
COMBEE.species = 415
COMBEE.types = BUG
COMBEE.types = [COMBEE.types, FLYING]
COMBEE.abilities = species.abilities(415)
COMBEE.hidden_ability = species.hidden_ability(415)

#################
### VESPIQUEN ###
#################

VESPIQUEN = Pokemon()
VESPIQUEN.species = 416
VESPIQUEN.types = BUG
VESPIQUEN.types = [VESPIQUEN.types, FLYING]
VESPIQUEN.abilities = species.abilities(416)
VESPIQUEN.hidden_ability = species.hidden_ability(416)

#################
### PACHIRISU ###
#################

PACHIRISU = Pokemon()
PACHIRISU.species = 417
PACHIRISU.types = ELECTRIC
PACHIRISU.abilities = species.abilities(417)
PACHIRISU.hidden_ability = species.hidden_ability(417)

##############
### BUIZEL ###
##############

BUIZEL = Pokemon()
BUIZEL.species = 418
BUIZEL.types = WATER
BUIZEL.abilities = species.abilities(418)
BUIZEL.hidden_ability = species.hidden_ability(418)

################
### FLOATZEL ###
################

FLOATZEL = Pokemon()
FLOATZEL.species = 419
FLOATZEL.types = WATER
FLOATZEL.abilities = species.abilities(419)
FLOATZEL.hidden_ability = species.hidden_ability(419)

###############
### CHERUBI ###
###############

CHERUBI = Pokemon()
CHERUBI.species = 420
CHERUBI.types = GRASS
CHERUBI.abilities = species.abilities(420)
CHERUBI.hidden_ability = species.hidden_ability(420)

###############
### CHERRIM ###
###############

CHERRIM = Pokemon()
CHERRIM.species = 421
CHERRIM.types = GRASS
CHERRIM.abilities = species.abilities(421)
CHERRIM.hidden_ability = species.hidden_ability(421)

###############
### SHELLOS ###
###############

SHELLOS = Pokemon()
SHELLOS.species = 422
SHELLOS.types = WATER
SHELLOS.abilities = species.abilities(422)
SHELLOS.hidden_ability = species.hidden_ability(422)

#################
### GASTRODON ###
#################

GASTRODON = Pokemon()
GASTRODON.species = 423
GASTRODON.types = WATER
GASTRODON.types = [GASTRODON.types, GROUND]
GASTRODON.abilities = species.abilities(423)
GASTRODON.hidden_ability = species.hidden_ability(423)

###############
### AMBIPOM ###
###############

AMBIPOM = Pokemon()
AMBIPOM.species = 424
AMBIPOM.types = NORMAL
AMBIPOM.abilities = species.abilities(424)
AMBIPOM.hidden_ability = species.hidden_ability(424)

################
### DRIFLOON ###
################

DRIFLOON = Pokemon()
DRIFLOON.species = 425
DRIFLOON.types = GHOST
DRIFLOON.types = [DRIFLOON.types, FLYING]
DRIFLOON.abilities = species.abilities(425)
DRIFLOON.hidden_ability = species.hidden_ability(425)

################
### DRIFBLIM ###
################

DRIFBLIM = Pokemon()
DRIFBLIM.species = 426
DRIFBLIM.types = GHOST
DRIFBLIM.types = [DRIFBLIM.types, FLYING]
DRIFBLIM.abilities = species.abilities(426)
DRIFBLIM.hidden_ability = species.hidden_ability(426)

###############
### BUNEARY ###
###############

BUNEARY = Pokemon()
BUNEARY.species = 427
BUNEARY.types = NORMAL
BUNEARY.abilities = species.abilities(427)
BUNEARY.hidden_ability = species.hidden_ability(427)

###############
### LOPUNNY ###
###############

LOPUNNY = Pokemon()
LOPUNNY.species = 428
LOPUNNY.types = NORMAL
LOPUNNY.abilities = species.abilities(428)
LOPUNNY.hidden_ability = species.hidden_ability(428)

#################
### MISMAGIUS ###
#################

MISMAGIUS = Pokemon()
MISMAGIUS.species = 429
MISMAGIUS.types = GHOST
MISMAGIUS.abilities = species.abilities(429)
MISMAGIUS.hidden_ability = species.hidden_ability(429)

#################
### HONCHKROW ###
#################

HONCHKROW = Pokemon()
HONCHKROW.species = 430
HONCHKROW.types = DARK
HONCHKROW.types = [HONCHKROW.types, FLYING]
HONCHKROW.abilities = species.abilities(430)
HONCHKROW.hidden_ability = species.hidden_ability(430)

###############
### GLAMEOW ###
###############

GLAMEOW = Pokemon()
GLAMEOW.species = 431
GLAMEOW.types = NORMAL
GLAMEOW.abilities = species.abilities(431)
GLAMEOW.hidden_ability = species.hidden_ability(431)

###############
### PURUGLY ###
###############

PURUGLY = Pokemon()
PURUGLY.species = 432
PURUGLY.types = NORMAL
PURUGLY.abilities = species.abilities(432)
PURUGLY.hidden_ability = species.hidden_ability(432)

#################
### CHINGLING ###
#################

CHINGLING = Pokemon()
CHINGLING.species = 433
CHINGLING.types = PSYCHIC
CHINGLING.abilities = species.abilities(433)
CHINGLING.hidden_ability = species.hidden_ability(433)

##############
### STUNKY ###
##############

STUNKY = Pokemon()
STUNKY.species = 434
STUNKY.types = POISON
STUNKY.types = [STUNKY.types, DARK]
STUNKY.abilities = species.abilities(434)
STUNKY.hidden_ability = species.hidden_ability(434)

################
### SKUNTANK ###
################

SKUNTANK = Pokemon()
SKUNTANK.species = 435
SKUNTANK.types = POISON
SKUNTANK.types = [SKUNTANK.types, DARK]
SKUNTANK.abilities = species.abilities(435)
SKUNTANK.hidden_ability = species.hidden_ability(435)

###############
### BRONZOR ###
###############

BRONZOR = Pokemon()
BRONZOR.species = 436
BRONZOR.types = STEEL
BRONZOR.types = [BRONZOR.types, PSYCHIC]
BRONZOR.abilities = species.abilities(436)
BRONZOR.hidden_ability = species.hidden_ability(436)

################
### BRONZONG ###
################

BRONZONG = Pokemon()
BRONZONG.species = 437
BRONZONG.types = STEEL
BRONZONG.types = [BRONZONG.types, PSYCHIC]
BRONZONG.abilities = species.abilities(437)
BRONZONG.hidden_ability = species.hidden_ability(437)

##############
### BONSLY ###
##############

BONSLY = Pokemon()
BONSLY.species = 438
BONSLY.types = ROCK
BONSLY.abilities = species.abilities(438)
BONSLY.hidden_ability = species.hidden_ability(438)

##############
### MIMEJR ###
##############

MIMEJR = Pokemon()
MIMEJR.types = PSYCHIC
MIMEJR.types = [MIMEJR.types, FAIRY]
###############
### HAPPINY ###
###############

HAPPINY = Pokemon()
HAPPINY.species = 440
HAPPINY.types = NORMAL
HAPPINY.abilities = species.abilities(440)
HAPPINY.hidden_ability = species.hidden_ability(440)

##############
### CHATOT ###
##############

CHATOT = Pokemon()
CHATOT.species = 441
CHATOT.types = NORMAL
CHATOT.types = [CHATOT.types, FLYING]
CHATOT.abilities = species.abilities(441)
CHATOT.hidden_ability = species.hidden_ability(441)

#################
### SPIRITOMB ###
#################

SPIRITOMB = Pokemon()
SPIRITOMB.species = 442
SPIRITOMB.types = GHOST
SPIRITOMB.types = [SPIRITOMB.types, DARK]
SPIRITOMB.abilities = species.abilities(442)
SPIRITOMB.hidden_ability = species.hidden_ability(442)

#############
### GIBLE ###
#############

GIBLE = Pokemon()
GIBLE.species = 443
GIBLE.types = DRAGON
GIBLE.types = [GIBLE.types, GROUND]
GIBLE.abilities = species.abilities(443)
GIBLE.hidden_ability = species.hidden_ability(443)

##############
### GABITE ###
##############

GABITE = Pokemon()
GABITE.species = 444
GABITE.types = DRAGON
GABITE.types = [GABITE.types, GROUND]
GABITE.abilities = species.abilities(444)
GABITE.hidden_ability = species.hidden_ability(444)

################
### GARCHOMP ###
################

GARCHOMP = Pokemon()
GARCHOMP.species = 445
GARCHOMP.types = DRAGON
GARCHOMP.types = [GARCHOMP.types, GROUND]
GARCHOMP.abilities = species.abilities(445)
GARCHOMP.hidden_ability = species.hidden_ability(445)

################
### MUNCHLAX ###
################

MUNCHLAX = Pokemon()
MUNCHLAX.species = 446
MUNCHLAX.types = NORMAL
MUNCHLAX.abilities = species.abilities(446)
MUNCHLAX.hidden_ability = species.hidden_ability(446)

#############
### RIOLU ###
#############

RIOLU = Pokemon()
RIOLU.species = 447
RIOLU.types = FIGHTING
RIOLU.abilities = species.abilities(447)
RIOLU.hidden_ability = species.hidden_ability(447)

###############
### LUCARIO ###
###############

LUCARIO = Pokemon()
LUCARIO.species = 448
LUCARIO.types = FIGHTING
LUCARIO.types = [LUCARIO.types, STEEL]
LUCARIO.abilities = species.abilities(448)
LUCARIO.hidden_ability = species.hidden_ability(448)

##################
### HIPPOPOTAS ###
##################

HIPPOPOTAS = Pokemon()
HIPPOPOTAS.species = 449
HIPPOPOTAS.types = GROUND
HIPPOPOTAS.abilities = species.abilities(449)
HIPPOPOTAS.hidden_ability = species.hidden_ability(449)

#################
### HIPPOWDON ###
#################

HIPPOWDON = Pokemon()
HIPPOWDON.species = 450
HIPPOWDON.types = GROUND
HIPPOWDON.abilities = species.abilities(450)
HIPPOWDON.hidden_ability = species.hidden_ability(450)

###############
### SKORUPI ###
###############

SKORUPI = Pokemon()
SKORUPI.species = 451
SKORUPI.types = POISON
SKORUPI.types = [SKORUPI.types, BUG]
SKORUPI.abilities = species.abilities(451)
SKORUPI.hidden_ability = species.hidden_ability(451)

###############
### DRAPION ###
###############

DRAPION = Pokemon()
DRAPION.species = 452
DRAPION.types = POISON
DRAPION.types = [DRAPION.types, DARK]
DRAPION.abilities = species.abilities(452)
DRAPION.hidden_ability = species.hidden_ability(452)

################
### CROAGUNK ###
################

CROAGUNK = Pokemon()
CROAGUNK.species = 453
CROAGUNK.types = POISON
CROAGUNK.types = [CROAGUNK.types, FIGHTING]
CROAGUNK.abilities = species.abilities(453)
CROAGUNK.hidden_ability = species.hidden_ability(453)

#################
### TOXICROAK ###
#################

TOXICROAK = Pokemon()
TOXICROAK.species = 454
TOXICROAK.types = POISON
TOXICROAK.types = [TOXICROAK.types, FIGHTING]
TOXICROAK.abilities = species.abilities(454)
TOXICROAK.hidden_ability = species.hidden_ability(454)

#################
### CARNIVINE ###
#################

CARNIVINE = Pokemon()
CARNIVINE.species = 455
CARNIVINE.types = GRASS
CARNIVINE.abilities = species.abilities(455)
CARNIVINE.hidden_ability = species.hidden_ability(455)

###############
### FINNEON ###
###############

FINNEON = Pokemon()
FINNEON.species = 456
FINNEON.types = WATER
FINNEON.abilities = species.abilities(456)
FINNEON.hidden_ability = species.hidden_ability(456)

################
### LUMINEON ###
################

LUMINEON = Pokemon()
LUMINEON.species = 457
LUMINEON.types = WATER
LUMINEON.abilities = species.abilities(457)
LUMINEON.hidden_ability = species.hidden_ability(457)

###############
### MANTYKE ###
###############

MANTYKE = Pokemon()
MANTYKE.species = 458
MANTYKE.types = WATER
MANTYKE.types = [MANTYKE.types, FLYING]
MANTYKE.abilities = species.abilities(458)
MANTYKE.hidden_ability = species.hidden_ability(458)

##############
### SNOVER ###
##############

SNOVER = Pokemon()
SNOVER.species = 459
SNOVER.types = GRASS
SNOVER.types = [SNOVER.types, ICE]
SNOVER.abilities = species.abilities(459)
SNOVER.hidden_ability = species.hidden_ability(459)

#################
### ABOMASNOW ###
#################

ABOMASNOW = Pokemon()
ABOMASNOW.species = 460
ABOMASNOW.types = GRASS
ABOMASNOW.types = [ABOMASNOW.types, ICE]
ABOMASNOW.abilities = species.abilities(460)
ABOMASNOW.hidden_ability = species.hidden_ability(460)

###############
### WEAVILE ###
###############

WEAVILE = Pokemon()
WEAVILE.species = 461
WEAVILE.types = DARK
WEAVILE.types = [WEAVILE.types, ICE]
WEAVILE.abilities = species.abilities(461)
WEAVILE.hidden_ability = species.hidden_ability(461)

#################
### MAGNEZONE ###
#################

MAGNEZONE = Pokemon()
MAGNEZONE.species = 462
MAGNEZONE.types = ELECTRIC
MAGNEZONE.types = [MAGNEZONE.types, STEEL]
MAGNEZONE.abilities = species.abilities(462)
MAGNEZONE.hidden_ability = species.hidden_ability(462)

##################
### LICKILICKY ###
##################

LICKILICKY = Pokemon()
LICKILICKY.species = 463
LICKILICKY.types = NORMAL
LICKILICKY.abilities = species.abilities(463)
LICKILICKY.hidden_ability = species.hidden_ability(463)

#################
### RHYPERIOR ###
#################

RHYPERIOR = Pokemon()
RHYPERIOR.species = 464
RHYPERIOR.types = GROUND
RHYPERIOR.types = [RHYPERIOR.types, ROCK]
RHYPERIOR.abilities = species.abilities(464)
RHYPERIOR.hidden_ability = species.hidden_ability(464)

#################
### TANGROWTH ###
#################

TANGROWTH = Pokemon()
TANGROWTH.species = 465
TANGROWTH.types = GRASS
TANGROWTH.abilities = species.abilities(465)
TANGROWTH.hidden_ability = species.hidden_ability(465)

##################
### ELECTIVIRE ###
##################

ELECTIVIRE = Pokemon()
ELECTIVIRE.species = 466
ELECTIVIRE.types = ELECTRIC
ELECTIVIRE.abilities = species.abilities(466)
ELECTIVIRE.hidden_ability = species.hidden_ability(466)

#################
### MAGMORTAR ###
#################

MAGMORTAR = Pokemon()
MAGMORTAR.species = 467
MAGMORTAR.types = FIRE
MAGMORTAR.abilities = species.abilities(467)
MAGMORTAR.hidden_ability = species.hidden_ability(467)

################
### TOGEKISS ###
################

TOGEKISS = Pokemon()
TOGEKISS.species = 468
TOGEKISS.types = FAIRY
TOGEKISS.types = [TOGEKISS.types, FLYING]
TOGEKISS.abilities = species.abilities(468)
TOGEKISS.hidden_ability = species.hidden_ability(468)

###############
### YANMEGA ###
###############

YANMEGA = Pokemon()
YANMEGA.species = 469
YANMEGA.types = BUG
YANMEGA.types = [YANMEGA.types, FLYING]
YANMEGA.abilities = species.abilities(469)
YANMEGA.hidden_ability = species.hidden_ability(469)

###############
### LEAFEON ###
###############

LEAFEON = Pokemon()
LEAFEON.species = 470
LEAFEON.types = GRASS
LEAFEON.abilities = species.abilities(470)
LEAFEON.hidden_ability = species.hidden_ability(470)

###############
### GLACEON ###
###############

GLACEON = Pokemon()
GLACEON.species = 471
GLACEON.types = ICE
GLACEON.abilities = species.abilities(471)
GLACEON.hidden_ability = species.hidden_ability(471)

###############
### GLISCOR ###
###############

GLISCOR = Pokemon()
GLISCOR.species = 472
GLISCOR.types = GROUND
GLISCOR.types = [GLISCOR.types, FLYING]
GLISCOR.abilities = species.abilities(472)
GLISCOR.hidden_ability = species.hidden_ability(472)

#################
### MAMOSWINE ###
#################

MAMOSWINE = Pokemon()
MAMOSWINE.species = 473
MAMOSWINE.types = ICE
MAMOSWINE.types = [MAMOSWINE.types, GROUND]
MAMOSWINE.abilities = species.abilities(473)
MAMOSWINE.hidden_ability = species.hidden_ability(473)

################
### PORYGONZ ###
################

PORYGONZ = Pokemon()
PORYGONZ.types = NORMAL
###############
### GALLADE ###
###############

GALLADE = Pokemon()
GALLADE.species = 475
GALLADE.types = PSYCHIC
GALLADE.types = [GALLADE.types, FIGHTING]
GALLADE.abilities = species.abilities(475)
GALLADE.hidden_ability = species.hidden_ability(475)

#################
### PROBOPASS ###
#################

PROBOPASS = Pokemon()
PROBOPASS.species = 476
PROBOPASS.types = ROCK
PROBOPASS.types = [PROBOPASS.types, STEEL]
PROBOPASS.abilities = species.abilities(476)
PROBOPASS.hidden_ability = species.hidden_ability(476)

################
### DUSKNOIR ###
################

DUSKNOIR = Pokemon()
DUSKNOIR.species = 477
DUSKNOIR.types = GHOST
DUSKNOIR.abilities = species.abilities(477)
DUSKNOIR.hidden_ability = species.hidden_ability(477)

################
### FROSLASS ###
################

FROSLASS = Pokemon()
FROSLASS.species = 478
FROSLASS.types = ICE
FROSLASS.types = [FROSLASS.types, GHOST]
FROSLASS.abilities = species.abilities(478)
FROSLASS.hidden_ability = species.hidden_ability(478)

#############
### ROTOM ###
#############

ROTOM = Pokemon()
ROTOM.species = 479
ROTOM.types = ELECTRIC
ROTOM.types = [ROTOM.types, GHOST]
ROTOM.abilities = species.abilities(479)
ROTOM.hidden_ability = species.hidden_ability(479)

############
### UXIE ###
############

UXIE = Pokemon()
UXIE.species = 480
UXIE.types = PSYCHIC
UXIE.abilities = species.abilities(480)
UXIE.hidden_ability = species.hidden_ability(480)

###############
### MESPRIT ###
###############

MESPRIT = Pokemon()
MESPRIT.species = 481
MESPRIT.types = PSYCHIC
MESPRIT.abilities = species.abilities(481)
MESPRIT.hidden_ability = species.hidden_ability(481)

#############
### AZELF ###
#############

AZELF = Pokemon()
AZELF.species = 482
AZELF.types = PSYCHIC
AZELF.abilities = species.abilities(482)
AZELF.hidden_ability = species.hidden_ability(482)

##############
### DIALGA ###
##############

DIALGA = Pokemon()
DIALGA.species = 483
DIALGA.types = STEEL
DIALGA.types = [DIALGA.types, DRAGON]
DIALGA.abilities = species.abilities(483)
DIALGA.hidden_ability = species.hidden_ability(483)

##############
### PALKIA ###
##############

PALKIA = Pokemon()
PALKIA.species = 484
PALKIA.types = WATER
PALKIA.types = [PALKIA.types, DRAGON]
PALKIA.abilities = species.abilities(484)
PALKIA.hidden_ability = species.hidden_ability(484)

###############
### HEATRAN ###
###############

HEATRAN = Pokemon()
HEATRAN.species = 485
HEATRAN.types = FIRE
HEATRAN.types = [HEATRAN.types, STEEL]
HEATRAN.abilities = species.abilities(485)
HEATRAN.hidden_ability = species.hidden_ability(485)

#################
### REGIGIGAS ###
#################

REGIGIGAS = Pokemon()
REGIGIGAS.species = 486
REGIGIGAS.types = NORMAL
REGIGIGAS.abilities = species.abilities(486)
REGIGIGAS.hidden_ability = species.hidden_ability(486)

################
### GIRATINA ###
################

GIRATINA = Pokemon()
GIRATINA.species = 487
GIRATINA.types = GHOST
GIRATINA.types = [GIRATINA.types, DRAGON]
GIRATINA.abilities = species.abilities(487)
GIRATINA.hidden_ability = species.hidden_ability(487)

#################
### CRESSELIA ###
#################

CRESSELIA = Pokemon()
CRESSELIA.species = 488
CRESSELIA.types = PSYCHIC
CRESSELIA.abilities = species.abilities(488)
CRESSELIA.hidden_ability = species.hidden_ability(488)

##############
### PHIONE ###
##############

PHIONE = Pokemon()
PHIONE.species = 489
PHIONE.types = WATER
PHIONE.abilities = species.abilities(489)
PHIONE.hidden_ability = species.hidden_ability(489)

###############
### MANAPHY ###
###############

MANAPHY = Pokemon()
MANAPHY.species = 490
MANAPHY.types = WATER
MANAPHY.abilities = species.abilities(490)
MANAPHY.hidden_ability = species.hidden_ability(490)

###############
### DARKRAI ###
###############

DARKRAI = Pokemon()
DARKRAI.species = 491
DARKRAI.types = DARK
DARKRAI.abilities = species.abilities(491)
DARKRAI.hidden_ability = species.hidden_ability(491)

###############
### SHAYMIN ###
###############

SHAYMIN = Pokemon()
SHAYMIN.species = 492
SHAYMIN.types = GRASS
SHAYMIN.abilities = species.abilities(492)
SHAYMIN.hidden_ability = species.hidden_ability(492)

##############
### ARCEUS ###
##############

ARCEUS = Pokemon()
ARCEUS.species = 493
ARCEUS.types = NORMAL
ARCEUS.abilities = species.abilities(493)
ARCEUS.hidden_ability = species.hidden_ability(493)

###############
### VICTINI ###
###############

VICTINI = Pokemon()
VICTINI.species = 494
VICTINI.types = PSYCHIC
VICTINI.types = [VICTINI.types, FIRE]
VICTINI.abilities = species.abilities(494)
VICTINI.hidden_ability = species.hidden_ability(494)

#############
### SNIVY ###
#############

SNIVY = Pokemon()
SNIVY.species = 495
SNIVY.types = GRASS
SNIVY.abilities = species.abilities(495)
SNIVY.hidden_ability = species.hidden_ability(495)

###############
### SERVINE ###
###############

SERVINE = Pokemon()
SERVINE.species = 496
SERVINE.types = GRASS
SERVINE.abilities = species.abilities(496)
SERVINE.hidden_ability = species.hidden_ability(496)

#################
### SERPERIOR ###
#################

SERPERIOR = Pokemon()
SERPERIOR.species = 497
SERPERIOR.types = GRASS
SERPERIOR.abilities = species.abilities(497)
SERPERIOR.hidden_ability = species.hidden_ability(497)

#############
### TEPIG ###
#############

TEPIG = Pokemon()
TEPIG.species = 498
TEPIG.types = FIRE
TEPIG.abilities = species.abilities(498)
TEPIG.hidden_ability = species.hidden_ability(498)

###############
### PIGNITE ###
###############

PIGNITE = Pokemon()
PIGNITE.species = 499
PIGNITE.types = FIRE
PIGNITE.types = [PIGNITE.types, FIGHTING]
PIGNITE.abilities = species.abilities(499)
PIGNITE.hidden_ability = species.hidden_ability(499)

##############
### EMBOAR ###
##############

EMBOAR = Pokemon()
EMBOAR.species = 500
EMBOAR.types = FIRE
EMBOAR.types = [EMBOAR.types, FIGHTING]
EMBOAR.abilities = species.abilities(500)
EMBOAR.hidden_ability = species.hidden_ability(500)

################
### OSHAWOTT ###
################

OSHAWOTT = Pokemon()
OSHAWOTT.species = 501
OSHAWOTT.types = WATER
OSHAWOTT.abilities = species.abilities(501)
OSHAWOTT.hidden_ability = species.hidden_ability(501)

##############
### DEWOTT ###
##############

DEWOTT = Pokemon()
DEWOTT.species = 502
DEWOTT.types = WATER
DEWOTT.abilities = species.abilities(502)
DEWOTT.hidden_ability = species.hidden_ability(502)

################
### SAMUROTT ###
################

SAMUROTT = Pokemon()
SAMUROTT.species = 503
SAMUROTT.types = WATER
SAMUROTT.abilities = species.abilities(503)
SAMUROTT.hidden_ability = species.hidden_ability(503)

##############
### PATRAT ###
##############

PATRAT = Pokemon()
PATRAT.species = 504
PATRAT.types = NORMAL
PATRAT.abilities = species.abilities(504)
PATRAT.hidden_ability = species.hidden_ability(504)

###############
### WATCHOG ###
###############

WATCHOG = Pokemon()
WATCHOG.species = 505
WATCHOG.types = NORMAL
WATCHOG.abilities = species.abilities(505)
WATCHOG.hidden_ability = species.hidden_ability(505)

################
### LILLIPUP ###
################

LILLIPUP = Pokemon()
LILLIPUP.species = 506
LILLIPUP.types = NORMAL
LILLIPUP.abilities = species.abilities(506)
LILLIPUP.hidden_ability = species.hidden_ability(506)

###############
### HERDIER ###
###############

HERDIER = Pokemon()
HERDIER.species = 507
HERDIER.types = NORMAL
HERDIER.abilities = species.abilities(507)
HERDIER.hidden_ability = species.hidden_ability(507)

#################
### STOUTLAND ###
#################

STOUTLAND = Pokemon()
STOUTLAND.species = 508
STOUTLAND.types = NORMAL
STOUTLAND.abilities = species.abilities(508)
STOUTLAND.hidden_ability = species.hidden_ability(508)

################
### PURRLOIN ###
################

PURRLOIN = Pokemon()
PURRLOIN.species = 509
PURRLOIN.types = DARK
PURRLOIN.abilities = species.abilities(509)
PURRLOIN.hidden_ability = species.hidden_ability(509)

###############
### LIEPARD ###
###############

LIEPARD = Pokemon()
LIEPARD.species = 510
LIEPARD.types = DARK
LIEPARD.abilities = species.abilities(510)
LIEPARD.hidden_ability = species.hidden_ability(510)

###############
### PANSAGE ###
###############

PANSAGE = Pokemon()
PANSAGE.species = 511
PANSAGE.types = GRASS
PANSAGE.abilities = species.abilities(511)
PANSAGE.hidden_ability = species.hidden_ability(511)

################
### SIMISAGE ###
################

SIMISAGE = Pokemon()
SIMISAGE.species = 512
SIMISAGE.types = GRASS
SIMISAGE.abilities = species.abilities(512)
SIMISAGE.hidden_ability = species.hidden_ability(512)

###############
### PANSEAR ###
###############

PANSEAR = Pokemon()
PANSEAR.species = 513
PANSEAR.types = FIRE
PANSEAR.abilities = species.abilities(513)
PANSEAR.hidden_ability = species.hidden_ability(513)

################
### SIMISEAR ###
################

SIMISEAR = Pokemon()
SIMISEAR.species = 514
SIMISEAR.types = FIRE
SIMISEAR.abilities = species.abilities(514)
SIMISEAR.hidden_ability = species.hidden_ability(514)

###############
### PANPOUR ###
###############

PANPOUR = Pokemon()
PANPOUR.species = 515
PANPOUR.types = WATER
PANPOUR.abilities = species.abilities(515)
PANPOUR.hidden_ability = species.hidden_ability(515)

################
### SIMIPOUR ###
################

SIMIPOUR = Pokemon()
SIMIPOUR.species = 516
SIMIPOUR.types = WATER
SIMIPOUR.abilities = species.abilities(516)
SIMIPOUR.hidden_ability = species.hidden_ability(516)

#############
### MUNNA ###
#############

MUNNA = Pokemon()
MUNNA.species = 517
MUNNA.types = PSYCHIC
MUNNA.abilities = species.abilities(517)
MUNNA.hidden_ability = species.hidden_ability(517)

################
### MUSHARNA ###
################

MUSHARNA = Pokemon()
MUSHARNA.species = 518
MUSHARNA.types = PSYCHIC
MUSHARNA.abilities = species.abilities(518)
MUSHARNA.hidden_ability = species.hidden_ability(518)

##############
### PIDOVE ###
##############

PIDOVE = Pokemon()
PIDOVE.species = 519
PIDOVE.types = NORMAL
PIDOVE.types = [PIDOVE.types, FLYING]
PIDOVE.abilities = species.abilities(519)
PIDOVE.hidden_ability = species.hidden_ability(519)

#################
### TRANQUILL ###
#################

TRANQUILL = Pokemon()
TRANQUILL.species = 520
TRANQUILL.types = NORMAL
TRANQUILL.types = [TRANQUILL.types, FLYING]
TRANQUILL.abilities = species.abilities(520)
TRANQUILL.hidden_ability = species.hidden_ability(520)

################
### UNFEZANT ###
################

UNFEZANT = Pokemon()
UNFEZANT.species = 521
UNFEZANT.types = NORMAL
UNFEZANT.types = [UNFEZANT.types, FLYING]
UNFEZANT.abilities = species.abilities(521)
UNFEZANT.hidden_ability = species.hidden_ability(521)

###############
### BLITZLE ###
###############

BLITZLE = Pokemon()
BLITZLE.species = 522
BLITZLE.types = ELECTRIC
BLITZLE.abilities = species.abilities(522)
BLITZLE.hidden_ability = species.hidden_ability(522)

#################
### ZEBSTRIKA ###
#################

ZEBSTRIKA = Pokemon()
ZEBSTRIKA.species = 523
ZEBSTRIKA.types = ELECTRIC
ZEBSTRIKA.abilities = species.abilities(523)
ZEBSTRIKA.hidden_ability = species.hidden_ability(523)

##################
### ROGGENROLA ###
##################

ROGGENROLA = Pokemon()
ROGGENROLA.species = 524
ROGGENROLA.types = ROCK
ROGGENROLA.abilities = species.abilities(524)
ROGGENROLA.hidden_ability = species.hidden_ability(524)

###############
### BOLDORE ###
###############

BOLDORE = Pokemon()
BOLDORE.species = 525
BOLDORE.types = ROCK
BOLDORE.abilities = species.abilities(525)
BOLDORE.hidden_ability = species.hidden_ability(525)

################
### GIGALITH ###
################

GIGALITH = Pokemon()
GIGALITH.species = 526
GIGALITH.types = ROCK
GIGALITH.abilities = species.abilities(526)
GIGALITH.hidden_ability = species.hidden_ability(526)

##############
### WOOBAT ###
##############

WOOBAT = Pokemon()
WOOBAT.species = 527
WOOBAT.types = PSYCHIC
WOOBAT.types = [WOOBAT.types, FLYING]
WOOBAT.abilities = species.abilities(527)
WOOBAT.hidden_ability = species.hidden_ability(527)

###############
### SWOOBAT ###
###############

SWOOBAT = Pokemon()
SWOOBAT.species = 528
SWOOBAT.types = PSYCHIC
SWOOBAT.types = [SWOOBAT.types, FLYING]
SWOOBAT.abilities = species.abilities(528)
SWOOBAT.hidden_ability = species.hidden_ability(528)

###############
### DRILBUR ###
###############

DRILBUR = Pokemon()
DRILBUR.species = 529
DRILBUR.types = GROUND
DRILBUR.abilities = species.abilities(529)
DRILBUR.hidden_ability = species.hidden_ability(529)

#################
### EXCADRILL ###
#################

EXCADRILL = Pokemon()
EXCADRILL.species = 530
EXCADRILL.types = GROUND
EXCADRILL.types = [EXCADRILL.types, STEEL]
EXCADRILL.abilities = species.abilities(530)
EXCADRILL.hidden_ability = species.hidden_ability(530)

##############
### AUDINO ###
##############

AUDINO = Pokemon()
AUDINO.species = 531
AUDINO.types = NORMAL
AUDINO.abilities = species.abilities(531)
AUDINO.hidden_ability = species.hidden_ability(531)

###############
### TIMBURR ###
###############

TIMBURR = Pokemon()
TIMBURR.species = 532
TIMBURR.types = FIGHTING
TIMBURR.abilities = species.abilities(532)
TIMBURR.hidden_ability = species.hidden_ability(532)

###############
### GURDURR ###
###############

GURDURR = Pokemon()
GURDURR.species = 533
GURDURR.types = FIGHTING
GURDURR.abilities = species.abilities(533)
GURDURR.hidden_ability = species.hidden_ability(533)

##################
### CONKELDURR ###
##################

CONKELDURR = Pokemon()
CONKELDURR.species = 534
CONKELDURR.types = FIGHTING
CONKELDURR.abilities = species.abilities(534)
CONKELDURR.hidden_ability = species.hidden_ability(534)

###############
### TYMPOLE ###
###############

TYMPOLE = Pokemon()
TYMPOLE.species = 535
TYMPOLE.types = WATER
TYMPOLE.abilities = species.abilities(535)
TYMPOLE.hidden_ability = species.hidden_ability(535)

#################
### PALPITOAD ###
#################

PALPITOAD = Pokemon()
PALPITOAD.species = 536
PALPITOAD.types = WATER
PALPITOAD.types = [PALPITOAD.types, GROUND]
PALPITOAD.abilities = species.abilities(536)
PALPITOAD.hidden_ability = species.hidden_ability(536)

##################
### SEISMITOAD ###
##################

SEISMITOAD = Pokemon()
SEISMITOAD.species = 537
SEISMITOAD.types = WATER
SEISMITOAD.types = [SEISMITOAD.types, GROUND]
SEISMITOAD.abilities = species.abilities(537)
SEISMITOAD.hidden_ability = species.hidden_ability(537)

#############
### THROH ###
#############

THROH = Pokemon()
THROH.species = 538
THROH.types = FIGHTING
THROH.abilities = species.abilities(538)
THROH.hidden_ability = species.hidden_ability(538)

############
### SAWK ###
############

SAWK = Pokemon()
SAWK.species = 539
SAWK.types = FIGHTING
SAWK.abilities = species.abilities(539)
SAWK.hidden_ability = species.hidden_ability(539)

################
### SEWADDLE ###
################

SEWADDLE = Pokemon()
SEWADDLE.species = 540
SEWADDLE.types = BUG
SEWADDLE.types = [SEWADDLE.types, GRASS]
SEWADDLE.abilities = species.abilities(540)
SEWADDLE.hidden_ability = species.hidden_ability(540)

################
### SWADLOON ###
################

SWADLOON = Pokemon()
SWADLOON.species = 541
SWADLOON.types = BUG
SWADLOON.types = [SWADLOON.types, GRASS]
SWADLOON.abilities = species.abilities(541)
SWADLOON.hidden_ability = species.hidden_ability(541)

################
### LEAVANNY ###
################

LEAVANNY = Pokemon()
LEAVANNY.species = 542
LEAVANNY.types = BUG
LEAVANNY.types = [LEAVANNY.types, GRASS]
LEAVANNY.abilities = species.abilities(542)
LEAVANNY.hidden_ability = species.hidden_ability(542)

################
### VENIPEDE ###
################

VENIPEDE = Pokemon()
VENIPEDE.species = 543
VENIPEDE.types = BUG
VENIPEDE.types = [VENIPEDE.types, POISON]
VENIPEDE.abilities = species.abilities(543)
VENIPEDE.hidden_ability = species.hidden_ability(543)

##################
### WHIRLIPEDE ###
##################

WHIRLIPEDE = Pokemon()
WHIRLIPEDE.species = 544
WHIRLIPEDE.types = BUG
WHIRLIPEDE.types = [WHIRLIPEDE.types, POISON]
WHIRLIPEDE.abilities = species.abilities(544)
WHIRLIPEDE.hidden_ability = species.hidden_ability(544)

#################
### SCOLIPEDE ###
#################

SCOLIPEDE = Pokemon()
SCOLIPEDE.species = 545
SCOLIPEDE.types = BUG
SCOLIPEDE.types = [SCOLIPEDE.types, POISON]
SCOLIPEDE.abilities = species.abilities(545)
SCOLIPEDE.hidden_ability = species.hidden_ability(545)

################
### COTTONEE ###
################

COTTONEE = Pokemon()
COTTONEE.species = 546
COTTONEE.types = GRASS
COTTONEE.types = [COTTONEE.types, FAIRY]
COTTONEE.abilities = species.abilities(546)
COTTONEE.hidden_ability = species.hidden_ability(546)

##################
### WHIMSICOTT ###
##################

WHIMSICOTT = Pokemon()
WHIMSICOTT.species = 547
WHIMSICOTT.types = GRASS
WHIMSICOTT.types = [WHIMSICOTT.types, FAIRY]
WHIMSICOTT.abilities = species.abilities(547)
WHIMSICOTT.hidden_ability = species.hidden_ability(547)

###############
### PETILIL ###
###############

PETILIL = Pokemon()
PETILIL.species = 548
PETILIL.types = GRASS
PETILIL.abilities = species.abilities(548)
PETILIL.hidden_ability = species.hidden_ability(548)

#################
### LILLIGANT ###
#################

LILLIGANT = Pokemon()
LILLIGANT.species = 549
LILLIGANT.types = GRASS
LILLIGANT.abilities = species.abilities(549)
LILLIGANT.hidden_ability = species.hidden_ability(549)

################
### BASCULIN ###
################

BASCULIN = Pokemon()
BASCULIN.species = 550
BASCULIN.types = WATER
BASCULIN.abilities = species.abilities(550)
BASCULIN.hidden_ability = species.hidden_ability(550)

###############
### SANDILE ###
###############

SANDILE = Pokemon()
SANDILE.species = 551
SANDILE.types = GROUND
SANDILE.types = [SANDILE.types, DARK]
SANDILE.abilities = species.abilities(551)
SANDILE.hidden_ability = species.hidden_ability(551)

################
### KROKOROK ###
################

KROKOROK = Pokemon()
KROKOROK.species = 552
KROKOROK.types = GROUND
KROKOROK.types = [KROKOROK.types, DARK]
KROKOROK.abilities = species.abilities(552)
KROKOROK.hidden_ability = species.hidden_ability(552)

##################
### KROOKODILE ###
##################

KROOKODILE = Pokemon()
KROOKODILE.species = 553
KROOKODILE.types = GROUND
KROOKODILE.types = [KROOKODILE.types, DARK]
KROOKODILE.abilities = species.abilities(553)
KROOKODILE.hidden_ability = species.hidden_ability(553)

################
### DARUMAKA ###
################

DARUMAKA = Pokemon()
DARUMAKA.species = 554
DARUMAKA.types = FIRE
DARUMAKA.abilities = species.abilities(554)
DARUMAKA.hidden_ability = species.hidden_ability(554)

##################
### DARMANITAN ###
##################

DARMANITAN = Pokemon()
DARMANITAN.species = 555
DARMANITAN.types = FIRE
DARMANITAN.abilities = species.abilities(555)
DARMANITAN.hidden_ability = species.hidden_ability(555)

################
### MARACTUS ###
################

MARACTUS = Pokemon()
MARACTUS.species = 556
MARACTUS.types = GRASS
MARACTUS.abilities = species.abilities(556)
MARACTUS.hidden_ability = species.hidden_ability(556)

###############
### DWEBBLE ###
###############

DWEBBLE = Pokemon()
DWEBBLE.species = 557
DWEBBLE.types = BUG
DWEBBLE.types = [DWEBBLE.types, ROCK]
DWEBBLE.abilities = species.abilities(557)
DWEBBLE.hidden_ability = species.hidden_ability(557)

###############
### CRUSTLE ###
###############

CRUSTLE = Pokemon()
CRUSTLE.species = 558
CRUSTLE.types = BUG
CRUSTLE.types = [CRUSTLE.types, ROCK]
CRUSTLE.abilities = species.abilities(558)
CRUSTLE.hidden_ability = species.hidden_ability(558)

###############
### SCRAGGY ###
###############

SCRAGGY = Pokemon()
SCRAGGY.species = 559
SCRAGGY.types = DARK
SCRAGGY.types = [SCRAGGY.types, FIGHTING]
SCRAGGY.abilities = species.abilities(559)
SCRAGGY.hidden_ability = species.hidden_ability(559)

###############
### SCRAFTY ###
###############

SCRAFTY = Pokemon()
SCRAFTY.species = 560
SCRAFTY.types = DARK
SCRAFTY.types = [SCRAFTY.types, FIGHTING]
SCRAFTY.abilities = species.abilities(560)
SCRAFTY.hidden_ability = species.hidden_ability(560)

################
### SIGILYPH ###
################

SIGILYPH = Pokemon()
SIGILYPH.species = 561
SIGILYPH.types = PSYCHIC
SIGILYPH.types = [SIGILYPH.types, FLYING]
SIGILYPH.abilities = species.abilities(561)
SIGILYPH.hidden_ability = species.hidden_ability(561)

##############
### YAMASK ###
##############

YAMASK = Pokemon()
YAMASK.species = 562
YAMASK.types = GHOST
YAMASK.abilities = species.abilities(562)
YAMASK.hidden_ability = species.hidden_ability(562)

##################
### COFAGRIGUS ###
##################

COFAGRIGUS = Pokemon()
COFAGRIGUS.species = 563
COFAGRIGUS.types = GHOST
COFAGRIGUS.abilities = species.abilities(563)
COFAGRIGUS.hidden_ability = species.hidden_ability(563)

################
### TIRTOUGA ###
################

TIRTOUGA = Pokemon()
TIRTOUGA.species = 564
TIRTOUGA.types = WATER
TIRTOUGA.types = [TIRTOUGA.types, ROCK]
TIRTOUGA.abilities = species.abilities(564)
TIRTOUGA.hidden_ability = species.hidden_ability(564)

##################
### CARRACOSTA ###
##################

CARRACOSTA = Pokemon()
CARRACOSTA.species = 565
CARRACOSTA.types = WATER
CARRACOSTA.types = [CARRACOSTA.types, ROCK]
CARRACOSTA.abilities = species.abilities(565)
CARRACOSTA.hidden_ability = species.hidden_ability(565)

##############
### ARCHEN ###
##############

ARCHEN = Pokemon()
ARCHEN.species = 566
ARCHEN.types = ROCK
ARCHEN.types = [ARCHEN.types, FLYING]
ARCHEN.abilities = species.abilities(566)
ARCHEN.hidden_ability = species.hidden_ability(566)

################
### ARCHEOPS ###
################

ARCHEOPS = Pokemon()
ARCHEOPS.species = 567
ARCHEOPS.types = ROCK
ARCHEOPS.types = [ARCHEOPS.types, FLYING]
ARCHEOPS.abilities = species.abilities(567)
ARCHEOPS.hidden_ability = species.hidden_ability(567)

################
### TRUBBISH ###
################

TRUBBISH = Pokemon()
TRUBBISH.species = 568
TRUBBISH.types = POISON
TRUBBISH.abilities = species.abilities(568)
TRUBBISH.hidden_ability = species.hidden_ability(568)

################
### GARBODOR ###
################

GARBODOR = Pokemon()
GARBODOR.species = 569
GARBODOR.types = POISON
GARBODOR.abilities = species.abilities(569)
GARBODOR.hidden_ability = species.hidden_ability(569)

#############
### ZORUA ###
#############

ZORUA = Pokemon()
ZORUA.species = 570
ZORUA.types = DARK
ZORUA.abilities = species.abilities(570)
ZORUA.hidden_ability = species.hidden_ability(570)

###############
### ZOROARK ###
###############

ZOROARK = Pokemon()
ZOROARK.species = 571
ZOROARK.types = DARK
ZOROARK.abilities = species.abilities(571)
ZOROARK.hidden_ability = species.hidden_ability(571)

################
### MINCCINO ###
################

MINCCINO = Pokemon()
MINCCINO.species = 572
MINCCINO.types = NORMAL
MINCCINO.abilities = species.abilities(572)
MINCCINO.hidden_ability = species.hidden_ability(572)

################
### CINCCINO ###
################

CINCCINO = Pokemon()
CINCCINO.species = 573
CINCCINO.types = NORMAL
CINCCINO.abilities = species.abilities(573)
CINCCINO.hidden_ability = species.hidden_ability(573)

###############
### GOTHITA ###
###############

GOTHITA = Pokemon()
GOTHITA.species = 574
GOTHITA.types = PSYCHIC
GOTHITA.abilities = species.abilities(574)
GOTHITA.hidden_ability = species.hidden_ability(574)

#################
### GOTHORITA ###
#################

GOTHORITA = Pokemon()
GOTHORITA.species = 575
GOTHORITA.types = PSYCHIC
GOTHORITA.abilities = species.abilities(575)
GOTHORITA.hidden_ability = species.hidden_ability(575)

##################
### GOTHITELLE ###
##################

GOTHITELLE = Pokemon()
GOTHITELLE.species = 576
GOTHITELLE.types = PSYCHIC
GOTHITELLE.abilities = species.abilities(576)
GOTHITELLE.hidden_ability = species.hidden_ability(576)

###############
### SOLOSIS ###
###############

SOLOSIS = Pokemon()
SOLOSIS.species = 577
SOLOSIS.types = PSYCHIC
SOLOSIS.abilities = species.abilities(577)
SOLOSIS.hidden_ability = species.hidden_ability(577)

###############
### DUOSION ###
###############

DUOSION = Pokemon()
DUOSION.species = 578
DUOSION.types = PSYCHIC
DUOSION.abilities = species.abilities(578)
DUOSION.hidden_ability = species.hidden_ability(578)

#################
### REUNICLUS ###
#################

REUNICLUS = Pokemon()
REUNICLUS.species = 579
REUNICLUS.types = PSYCHIC
REUNICLUS.abilities = species.abilities(579)
REUNICLUS.hidden_ability = species.hidden_ability(579)

################
### DUCKLETT ###
################

DUCKLETT = Pokemon()
DUCKLETT.species = 580
DUCKLETT.types = WATER
DUCKLETT.types = [DUCKLETT.types, FLYING]
DUCKLETT.abilities = species.abilities(580)
DUCKLETT.hidden_ability = species.hidden_ability(580)

##############
### SWANNA ###
##############

SWANNA = Pokemon()
SWANNA.species = 581
SWANNA.types = WATER
SWANNA.types = [SWANNA.types, FLYING]
SWANNA.abilities = species.abilities(581)
SWANNA.hidden_ability = species.hidden_ability(581)

#################
### VANILLITE ###
#################

VANILLITE = Pokemon()
VANILLITE.species = 582
VANILLITE.types = ICE
VANILLITE.abilities = species.abilities(582)
VANILLITE.hidden_ability = species.hidden_ability(582)

#################
### VANILLISH ###
#################

VANILLISH = Pokemon()
VANILLISH.species = 583
VANILLISH.types = ICE
VANILLISH.abilities = species.abilities(583)
VANILLISH.hidden_ability = species.hidden_ability(583)

#################
### VANILLUXE ###
#################

VANILLUXE = Pokemon()
VANILLUXE.species = 584
VANILLUXE.types = ICE
VANILLUXE.abilities = species.abilities(584)
VANILLUXE.hidden_ability = species.hidden_ability(584)

################
### DEERLING ###
################

DEERLING = Pokemon()
DEERLING.species = 585
DEERLING.types = NORMAL
DEERLING.types = [DEERLING.types, GRASS]
DEERLING.abilities = species.abilities(585)
DEERLING.hidden_ability = species.hidden_ability(585)

################
### SAWSBUCK ###
################

SAWSBUCK = Pokemon()
SAWSBUCK.species = 586
SAWSBUCK.types = NORMAL
SAWSBUCK.types = [SAWSBUCK.types, GRASS]
SAWSBUCK.abilities = species.abilities(586)
SAWSBUCK.hidden_ability = species.hidden_ability(586)

##############
### EMOLGA ###
##############

EMOLGA = Pokemon()
EMOLGA.species = 587
EMOLGA.types = ELECTRIC
EMOLGA.types = [EMOLGA.types, FLYING]
EMOLGA.abilities = species.abilities(587)
EMOLGA.hidden_ability = species.hidden_ability(587)

##################
### KARRABLAST ###
##################

KARRABLAST = Pokemon()
KARRABLAST.species = 588
KARRABLAST.types = BUG
KARRABLAST.abilities = species.abilities(588)
KARRABLAST.hidden_ability = species.hidden_ability(588)

##################
### ESCAVALIER ###
##################

ESCAVALIER = Pokemon()
ESCAVALIER.species = 589
ESCAVALIER.types = BUG
ESCAVALIER.types = [ESCAVALIER.types, STEEL]
ESCAVALIER.abilities = species.abilities(589)
ESCAVALIER.hidden_ability = species.hidden_ability(589)

###############
### FOONGUS ###
###############

FOONGUS = Pokemon()
FOONGUS.species = 590
FOONGUS.types = GRASS
FOONGUS.types = [FOONGUS.types, POISON]
FOONGUS.abilities = species.abilities(590)
FOONGUS.hidden_ability = species.hidden_ability(590)

#################
### AMOONGUSS ###
#################

AMOONGUSS = Pokemon()
AMOONGUSS.species = 591
AMOONGUSS.types = GRASS
AMOONGUSS.types = [AMOONGUSS.types, POISON]
AMOONGUSS.abilities = species.abilities(591)
AMOONGUSS.hidden_ability = species.hidden_ability(591)

################
### FRILLISH ###
################

FRILLISH = Pokemon()
FRILLISH.species = 592
FRILLISH.types = WATER
FRILLISH.types = [FRILLISH.types, GHOST]
FRILLISH.abilities = species.abilities(592)
FRILLISH.hidden_ability = species.hidden_ability(592)

#################
### JELLICENT ###
#################

JELLICENT = Pokemon()
JELLICENT.species = 593
JELLICENT.types = WATER
JELLICENT.types = [JELLICENT.types, GHOST]
JELLICENT.abilities = species.abilities(593)
JELLICENT.hidden_ability = species.hidden_ability(593)

#################
### ALOMOMOLA ###
#################

ALOMOMOLA = Pokemon()
ALOMOMOLA.species = 594
ALOMOMOLA.types = WATER
ALOMOMOLA.abilities = species.abilities(594)
ALOMOMOLA.hidden_ability = species.hidden_ability(594)

##############
### JOLTIK ###
##############

JOLTIK = Pokemon()
JOLTIK.species = 595
JOLTIK.types = BUG
JOLTIK.types = [JOLTIK.types, ELECTRIC]
JOLTIK.abilities = species.abilities(595)
JOLTIK.hidden_ability = species.hidden_ability(595)

##################
### GALVANTULA ###
##################

GALVANTULA = Pokemon()
GALVANTULA.species = 596
GALVANTULA.types = BUG
GALVANTULA.types = [GALVANTULA.types, ELECTRIC]
GALVANTULA.abilities = species.abilities(596)
GALVANTULA.hidden_ability = species.hidden_ability(596)

#################
### FERROSEED ###
#################

FERROSEED = Pokemon()
FERROSEED.species = 597
FERROSEED.types = GRASS
FERROSEED.types = [FERROSEED.types, STEEL]
FERROSEED.abilities = species.abilities(597)
FERROSEED.hidden_ability = species.hidden_ability(597)

##################
### FERROTHORN ###
##################

FERROTHORN = Pokemon()
FERROTHORN.species = 598
FERROTHORN.types = GRASS
FERROTHORN.types = [FERROTHORN.types, STEEL]
FERROTHORN.abilities = species.abilities(598)
FERROTHORN.hidden_ability = species.hidden_ability(598)

#############
### KLINK ###
#############

KLINK = Pokemon()
KLINK.species = 599
KLINK.types = STEEL
KLINK.abilities = species.abilities(599)
KLINK.hidden_ability = species.hidden_ability(599)

#############
### KLANG ###
#############

KLANG = Pokemon()
KLANG.species = 600
KLANG.types = STEEL
KLANG.abilities = species.abilities(600)
KLANG.hidden_ability = species.hidden_ability(600)

#################
### KLINKLANG ###
#################

KLINKLANG = Pokemon()
KLINKLANG.species = 601
KLINKLANG.types = STEEL
KLINKLANG.abilities = species.abilities(601)
KLINKLANG.hidden_ability = species.hidden_ability(601)

##############
### TYNAMO ###
##############

TYNAMO = Pokemon()
TYNAMO.species = 602
TYNAMO.types = ELECTRIC
TYNAMO.abilities = species.abilities(602)
TYNAMO.hidden_ability = species.hidden_ability(602)

#################
### EELEKTRIK ###
#################

EELEKTRIK = Pokemon()
EELEKTRIK.species = 603
EELEKTRIK.types = ELECTRIC
EELEKTRIK.abilities = species.abilities(603)
EELEKTRIK.hidden_ability = species.hidden_ability(603)

##################
### EELEKTROSS ###
##################

EELEKTROSS = Pokemon()
EELEKTROSS.species = 604
EELEKTROSS.types = ELECTRIC
EELEKTROSS.abilities = species.abilities(604)
EELEKTROSS.hidden_ability = species.hidden_ability(604)

##############
### ELGYEM ###
##############

ELGYEM = Pokemon()
ELGYEM.species = 605
ELGYEM.types = PSYCHIC
ELGYEM.abilities = species.abilities(605)
ELGYEM.hidden_ability = species.hidden_ability(605)

################
### BEHEEYEM ###
################

BEHEEYEM = Pokemon()
BEHEEYEM.species = 606
BEHEEYEM.types = PSYCHIC
BEHEEYEM.abilities = species.abilities(606)
BEHEEYEM.hidden_ability = species.hidden_ability(606)

###############
### LITWICK ###
###############

LITWICK = Pokemon()
LITWICK.species = 607
LITWICK.types = GHOST
LITWICK.types = [LITWICK.types, FIRE]
LITWICK.abilities = species.abilities(607)
LITWICK.hidden_ability = species.hidden_ability(607)

###############
### LAMPENT ###
###############

LAMPENT = Pokemon()
LAMPENT.species = 608
LAMPENT.types = GHOST
LAMPENT.types = [LAMPENT.types, FIRE]
LAMPENT.abilities = species.abilities(608)
LAMPENT.hidden_ability = species.hidden_ability(608)

##################
### CHANDELURE ###
##################

CHANDELURE = Pokemon()
CHANDELURE.species = 609
CHANDELURE.types = GHOST
CHANDELURE.types = [CHANDELURE.types, FIRE]
CHANDELURE.abilities = species.abilities(609)
CHANDELURE.hidden_ability = species.hidden_ability(609)

############
### AXEW ###
############

AXEW = Pokemon()
AXEW.species = 610
AXEW.types = DRAGON
AXEW.abilities = species.abilities(610)
AXEW.hidden_ability = species.hidden_ability(610)

###############
### FRAXURE ###
###############

FRAXURE = Pokemon()
FRAXURE.species = 611
FRAXURE.types = DRAGON
FRAXURE.abilities = species.abilities(611)
FRAXURE.hidden_ability = species.hidden_ability(611)

###############
### HAXORUS ###
###############

HAXORUS = Pokemon()
HAXORUS.species = 612
HAXORUS.types = DRAGON
HAXORUS.abilities = species.abilities(612)
HAXORUS.hidden_ability = species.hidden_ability(612)

###############
### CUBCHOO ###
###############

CUBCHOO = Pokemon()
CUBCHOO.species = 613
CUBCHOO.types = ICE
CUBCHOO.abilities = species.abilities(613)
CUBCHOO.hidden_ability = species.hidden_ability(613)

###############
### BEARTIC ###
###############

BEARTIC = Pokemon()
BEARTIC.species = 614
BEARTIC.types = ICE
BEARTIC.abilities = species.abilities(614)
BEARTIC.hidden_ability = species.hidden_ability(614)

#################
### CRYOGONAL ###
#################

CRYOGONAL = Pokemon()
CRYOGONAL.species = 615
CRYOGONAL.types = ICE
CRYOGONAL.abilities = species.abilities(615)
CRYOGONAL.hidden_ability = species.hidden_ability(615)

###############
### SHELMET ###
###############

SHELMET = Pokemon()
SHELMET.species = 616
SHELMET.types = BUG
SHELMET.abilities = species.abilities(616)
SHELMET.hidden_ability = species.hidden_ability(616)

################
### ACCELGOR ###
################

ACCELGOR = Pokemon()
ACCELGOR.species = 617
ACCELGOR.types = BUG
ACCELGOR.abilities = species.abilities(617)
ACCELGOR.hidden_ability = species.hidden_ability(617)

################
### STUNFISK ###
################

STUNFISK = Pokemon()
STUNFISK.species = 618
STUNFISK.types = GROUND
STUNFISK.types = [STUNFISK.types, ELECTRIC]
STUNFISK.abilities = species.abilities(618)
STUNFISK.hidden_ability = species.hidden_ability(618)

###############
### MIENFOO ###
###############

MIENFOO = Pokemon()
MIENFOO.species = 619
MIENFOO.types = FIGHTING
MIENFOO.abilities = species.abilities(619)
MIENFOO.hidden_ability = species.hidden_ability(619)

################
### MIENSHAO ###
################

MIENSHAO = Pokemon()
MIENSHAO.species = 620
MIENSHAO.types = FIGHTING
MIENSHAO.abilities = species.abilities(620)
MIENSHAO.hidden_ability = species.hidden_ability(620)

#################
### DRUDDIGON ###
#################

DRUDDIGON = Pokemon()
DRUDDIGON.species = 621
DRUDDIGON.types = DRAGON
DRUDDIGON.abilities = species.abilities(621)
DRUDDIGON.hidden_ability = species.hidden_ability(621)

##############
### GOLETT ###
##############

GOLETT = Pokemon()
GOLETT.species = 622
GOLETT.types = GROUND
GOLETT.types = [GOLETT.types, GHOST]
GOLETT.abilities = species.abilities(622)
GOLETT.hidden_ability = species.hidden_ability(622)

##############
### GOLURK ###
##############

GOLURK = Pokemon()
GOLURK.species = 623
GOLURK.types = GROUND
GOLURK.types = [GOLURK.types, GHOST]
GOLURK.abilities = species.abilities(623)
GOLURK.hidden_ability = species.hidden_ability(623)

################
### PAWNIARD ###
################

PAWNIARD = Pokemon()
PAWNIARD.species = 624
PAWNIARD.types = DARK
PAWNIARD.types = [PAWNIARD.types, STEEL]
PAWNIARD.abilities = species.abilities(624)
PAWNIARD.hidden_ability = species.hidden_ability(624)

###############
### BISHARP ###
###############

BISHARP = Pokemon()
BISHARP.species = 625
BISHARP.types = DARK
BISHARP.types = [BISHARP.types, STEEL]
BISHARP.abilities = species.abilities(625)
BISHARP.hidden_ability = species.hidden_ability(625)

##################
### BOUFFALANT ###
##################

BOUFFALANT = Pokemon()
BOUFFALANT.species = 626
BOUFFALANT.types = NORMAL
BOUFFALANT.abilities = species.abilities(626)
BOUFFALANT.hidden_ability = species.hidden_ability(626)

###############
### RUFFLET ###
###############

RUFFLET = Pokemon()
RUFFLET.species = 627
RUFFLET.types = NORMAL
RUFFLET.types = [RUFFLET.types, FLYING]
RUFFLET.abilities = species.abilities(627)
RUFFLET.hidden_ability = species.hidden_ability(627)

################
### BRAVIARY ###
################

BRAVIARY = Pokemon()
BRAVIARY.species = 628
BRAVIARY.types = NORMAL
BRAVIARY.types = [BRAVIARY.types, FLYING]
BRAVIARY.abilities = species.abilities(628)
BRAVIARY.hidden_ability = species.hidden_ability(628)

###############
### VULLABY ###
###############

VULLABY = Pokemon()
VULLABY.species = 629
VULLABY.types = DARK
VULLABY.types = [VULLABY.types, FLYING]
VULLABY.abilities = species.abilities(629)
VULLABY.hidden_ability = species.hidden_ability(629)

#################
### MANDIBUZZ ###
#################

MANDIBUZZ = Pokemon()
MANDIBUZZ.species = 630
MANDIBUZZ.types = DARK
MANDIBUZZ.types = [MANDIBUZZ.types, FLYING]
MANDIBUZZ.abilities = species.abilities(630)
MANDIBUZZ.hidden_ability = species.hidden_ability(630)

###############
### HEATMOR ###
###############

HEATMOR = Pokemon()
HEATMOR.species = 631
HEATMOR.types = FIRE
HEATMOR.abilities = species.abilities(631)
HEATMOR.hidden_ability = species.hidden_ability(631)

##############
### DURANT ###
##############

DURANT = Pokemon()
DURANT.species = 632
DURANT.types = BUG
DURANT.types = [DURANT.types, STEEL]
DURANT.abilities = species.abilities(632)
DURANT.hidden_ability = species.hidden_ability(632)

#############
### DEINO ###
#############

DEINO = Pokemon()
DEINO.species = 633
DEINO.types = DARK
DEINO.types = [DEINO.types, DRAGON]
DEINO.abilities = species.abilities(633)
DEINO.hidden_ability = species.hidden_ability(633)

################
### ZWEILOUS ###
################

ZWEILOUS = Pokemon()
ZWEILOUS.species = 634
ZWEILOUS.types = DARK
ZWEILOUS.types = [ZWEILOUS.types, DRAGON]
ZWEILOUS.abilities = species.abilities(634)
ZWEILOUS.hidden_ability = species.hidden_ability(634)

#################
### HYDREIGON ###
#################

HYDREIGON = Pokemon()
HYDREIGON.species = 635
HYDREIGON.types = DARK
HYDREIGON.types = [HYDREIGON.types, DRAGON]
HYDREIGON.abilities = species.abilities(635)
HYDREIGON.hidden_ability = species.hidden_ability(635)

################
### LARVESTA ###
################

LARVESTA = Pokemon()
LARVESTA.species = 636
LARVESTA.types = BUG
LARVESTA.types = [LARVESTA.types, FIRE]
LARVESTA.abilities = species.abilities(636)
LARVESTA.hidden_ability = species.hidden_ability(636)

#################
### VOLCARONA ###
#################

VOLCARONA = Pokemon()
VOLCARONA.species = 637
VOLCARONA.types = BUG
VOLCARONA.types = [VOLCARONA.types, FIRE]
VOLCARONA.abilities = species.abilities(637)
VOLCARONA.hidden_ability = species.hidden_ability(637)

################
### COBALION ###
################

COBALION = Pokemon()
COBALION.species = 638
COBALION.types = STEEL
COBALION.types = [COBALION.types, FIGHTING]
COBALION.abilities = species.abilities(638)
COBALION.hidden_ability = species.hidden_ability(638)

#################
### TERRAKION ###
#################

TERRAKION = Pokemon()
TERRAKION.species = 639
TERRAKION.types = ROCK
TERRAKION.types = [TERRAKION.types, FIGHTING]
TERRAKION.abilities = species.abilities(639)
TERRAKION.hidden_ability = species.hidden_ability(639)

################
### VIRIZION ###
################

VIRIZION = Pokemon()
VIRIZION.species = 640
VIRIZION.types = GRASS
VIRIZION.types = [VIRIZION.types, FIGHTING]
VIRIZION.abilities = species.abilities(640)
VIRIZION.hidden_ability = species.hidden_ability(640)

################
### TORNADUS ###
################

TORNADUS = Pokemon()
TORNADUS.species = 641
TORNADUS.types = FLYING
TORNADUS.abilities = species.abilities(641)
TORNADUS.hidden_ability = species.hidden_ability(641)

#################
### THUNDURUS ###
#################

THUNDURUS = Pokemon()
THUNDURUS.species = 642
THUNDURUS.types = ELECTRIC
THUNDURUS.types = [THUNDURUS.types, FLYING]
THUNDURUS.abilities = species.abilities(642)
THUNDURUS.hidden_ability = species.hidden_ability(642)

################
### RESHIRAM ###
################

RESHIRAM = Pokemon()
RESHIRAM.species = 643
RESHIRAM.types = DRAGON
RESHIRAM.types = [RESHIRAM.types, FIRE]
RESHIRAM.abilities = species.abilities(643)
RESHIRAM.hidden_ability = species.hidden_ability(643)

##############
### ZEKROM ###
##############

ZEKROM = Pokemon()
ZEKROM.species = 644
ZEKROM.types = DRAGON
ZEKROM.types = [ZEKROM.types, ELECTRIC]
ZEKROM.abilities = species.abilities(644)
ZEKROM.hidden_ability = species.hidden_ability(644)

################
### LANDORUS ###
################

LANDORUS = Pokemon()
LANDORUS.species = 645
LANDORUS.types = GROUND
LANDORUS.types = [LANDORUS.types, FLYING]
LANDORUS.abilities = species.abilities(645)
LANDORUS.hidden_ability = species.hidden_ability(645)

##############
### KYUREM ###
##############

KYUREM = Pokemon()
KYUREM.species = 646
KYUREM.types = DRAGON
KYUREM.types = [KYUREM.types, ICE]
KYUREM.abilities = species.abilities(646)
KYUREM.hidden_ability = species.hidden_ability(646)

##############
### KELDEO ###
##############

KELDEO = Pokemon()
KELDEO.species = 647
KELDEO.types = WATER
KELDEO.types = [KELDEO.types, FIGHTING]
KELDEO.abilities = species.abilities(647)
KELDEO.hidden_ability = species.hidden_ability(647)

################
### MELOETTA ###
################

MELOETTA = Pokemon()
MELOETTA.species = 648
MELOETTA.types = NORMAL
MELOETTA.types = [MELOETTA.types, PSYCHIC]
MELOETTA.abilities = species.abilities(648)
MELOETTA.hidden_ability = species.hidden_ability(648)

################
### GENESECT ###
################

GENESECT = Pokemon()
GENESECT.species = 649
GENESECT.types = BUG
GENESECT.types = [GENESECT.types, STEEL]
GENESECT.abilities = species.abilities(649)
GENESECT.hidden_ability = species.hidden_ability(649)

###############
### CHESPIN ###
###############

CHESPIN = Pokemon()
CHESPIN.species = 650
CHESPIN.types = GRASS
CHESPIN.abilities = species.abilities(650)
CHESPIN.hidden_ability = species.hidden_ability(650)

#################
### QUILLADIN ###
#################

QUILLADIN = Pokemon()
QUILLADIN.species = 651
QUILLADIN.types = GRASS
QUILLADIN.abilities = species.abilities(651)
QUILLADIN.hidden_ability = species.hidden_ability(651)

##################
### CHESNAUGHT ###
##################

CHESNAUGHT = Pokemon()
CHESNAUGHT.species = 652
CHESNAUGHT.types = GRASS
CHESNAUGHT.types = [CHESNAUGHT.types, FIGHTING]
CHESNAUGHT.abilities = species.abilities(652)
CHESNAUGHT.hidden_ability = species.hidden_ability(652)

################
### FENNEKIN ###
################

FENNEKIN = Pokemon()
FENNEKIN.species = 653
FENNEKIN.types = FIRE
FENNEKIN.abilities = species.abilities(653)
FENNEKIN.hidden_ability = species.hidden_ability(653)

###############
### BRAIXEN ###
###############

BRAIXEN = Pokemon()
BRAIXEN.species = 654
BRAIXEN.types = FIRE
BRAIXEN.abilities = species.abilities(654)
BRAIXEN.hidden_ability = species.hidden_ability(654)

###############
### DELPHOX ###
###############

DELPHOX = Pokemon()
DELPHOX.species = 655
DELPHOX.types = FIRE
DELPHOX.types = [DELPHOX.types, PSYCHIC]
DELPHOX.abilities = species.abilities(655)
DELPHOX.hidden_ability = species.hidden_ability(655)

###############
### FROAKIE ###
###############

FROAKIE = Pokemon()
FROAKIE.species = 656
FROAKIE.types = WATER
FROAKIE.abilities = species.abilities(656)
FROAKIE.hidden_ability = species.hidden_ability(656)

#################
### FROGADIER ###
#################

FROGADIER = Pokemon()
FROGADIER.species = 657
FROGADIER.types = WATER
FROGADIER.abilities = species.abilities(657)
FROGADIER.hidden_ability = species.hidden_ability(657)

################
### GRENINJA ###
################

GRENINJA = Pokemon()
GRENINJA.species = 658
GRENINJA.types = WATER
GRENINJA.types = [GRENINJA.types, DARK]
GRENINJA.abilities = species.abilities(658)
GRENINJA.hidden_ability = species.hidden_ability(658)

################
### BUNNELBY ###
################

BUNNELBY = Pokemon()
BUNNELBY.species = 659
BUNNELBY.types = NORMAL
BUNNELBY.abilities = species.abilities(659)
BUNNELBY.hidden_ability = species.hidden_ability(659)

#################
### DIGGERSBY ###
#################

DIGGERSBY = Pokemon()
DIGGERSBY.species = 660
DIGGERSBY.types = NORMAL
DIGGERSBY.types = [DIGGERSBY.types, GROUND]
DIGGERSBY.abilities = species.abilities(660)
DIGGERSBY.hidden_ability = species.hidden_ability(660)

##################
### FLETCHLING ###
##################

FLETCHLING = Pokemon()
FLETCHLING.species = 661
FLETCHLING.types = NORMAL
FLETCHLING.types = [FLETCHLING.types, FLYING]
FLETCHLING.abilities = species.abilities(661)
FLETCHLING.hidden_ability = species.hidden_ability(661)

###################
### FLETCHINDER ###
###################

FLETCHINDER = Pokemon()
FLETCHINDER.species = 662
FLETCHINDER.types = FIRE
FLETCHINDER.types = [FLETCHINDER.types, FLYING]
FLETCHINDER.abilities = species.abilities(662)
FLETCHINDER.hidden_ability = species.hidden_ability(662)

##################
### TALONFLAME ###
##################

TALONFLAME = Pokemon()
TALONFLAME.species = 663
TALONFLAME.types = FIRE
TALONFLAME.types = [TALONFLAME.types, FLYING]
TALONFLAME.abilities = species.abilities(663)
TALONFLAME.hidden_ability = species.hidden_ability(663)

##################
### SCATTERBUG ###
##################

SCATTERBUG = Pokemon()
SCATTERBUG.species = 664
SCATTERBUG.types = BUG
SCATTERBUG.abilities = species.abilities(664)
SCATTERBUG.hidden_ability = species.hidden_ability(664)

##############
### SPEWPA ###
##############

SPEWPA = Pokemon()
SPEWPA.species = 665
SPEWPA.types = BUG
SPEWPA.abilities = species.abilities(665)
SPEWPA.hidden_ability = species.hidden_ability(665)

################
### VIVILLON ###
################

VIVILLON = Pokemon()
VIVILLON.species = 666
VIVILLON.types = BUG
VIVILLON.types = [VIVILLON.types, FLYING]
VIVILLON.abilities = species.abilities(666)
VIVILLON.hidden_ability = species.hidden_ability(666)

##############
### LITLEO ###
##############

LITLEO = Pokemon()
LITLEO.species = 667
LITLEO.types = FIRE
LITLEO.types = [LITLEO.types, NORMAL]
LITLEO.abilities = species.abilities(667)
LITLEO.hidden_ability = species.hidden_ability(667)

##############
### PYROAR ###
##############

PYROAR = Pokemon()
PYROAR.species = 668
PYROAR.types = FIRE
PYROAR.types = [PYROAR.types, NORMAL]
PYROAR.abilities = species.abilities(668)
PYROAR.hidden_ability = species.hidden_ability(668)

###############
### FLABEBE ###
###############

FLABEBE = Pokemon()
FLABEBE.types = FAIRY
###############
### FLOETTE ###
###############

FLOETTE = Pokemon()
FLOETTE.species = 670
FLOETTE.types = FAIRY
FLOETTE.abilities = species.abilities(670)
FLOETTE.hidden_ability = species.hidden_ability(670)

###############
### FLORGES ###
###############

FLORGES = Pokemon()
FLORGES.species = 671
FLORGES.types = FAIRY
FLORGES.abilities = species.abilities(671)
FLORGES.hidden_ability = species.hidden_ability(671)

##############
### SKIDDO ###
##############

SKIDDO = Pokemon()
SKIDDO.species = 672
SKIDDO.types = GRASS
SKIDDO.abilities = species.abilities(672)
SKIDDO.hidden_ability = species.hidden_ability(672)

##############
### GOGOAT ###
##############

GOGOAT = Pokemon()
GOGOAT.species = 673
GOGOAT.types = GRASS
GOGOAT.abilities = species.abilities(673)
GOGOAT.hidden_ability = species.hidden_ability(673)

###############
### PANCHAM ###
###############

PANCHAM = Pokemon()
PANCHAM.species = 674
PANCHAM.types = FIGHTING
PANCHAM.abilities = species.abilities(674)
PANCHAM.hidden_ability = species.hidden_ability(674)

###############
### PANGORO ###
###############

PANGORO = Pokemon()
PANGORO.species = 675
PANGORO.types = FIGHTING
PANGORO.types = [PANGORO.types, DARK]
PANGORO.abilities = species.abilities(675)
PANGORO.hidden_ability = species.hidden_ability(675)

###############
### FURFROU ###
###############

FURFROU = Pokemon()
FURFROU.species = 676
FURFROU.types = NORMAL
FURFROU.abilities = species.abilities(676)
FURFROU.hidden_ability = species.hidden_ability(676)

##############
### ESPURR ###
##############

ESPURR = Pokemon()
ESPURR.species = 677
ESPURR.types = PSYCHIC
ESPURR.abilities = species.abilities(677)
ESPURR.hidden_ability = species.hidden_ability(677)

################
### MEOWSTIC ###
################

MEOWSTIC = Pokemon()
MEOWSTIC.species = 678
MEOWSTIC.types = PSYCHIC
MEOWSTIC.abilities = species.abilities(678)
MEOWSTIC.hidden_ability = species.hidden_ability(678)

###############
### HONEDGE ###
###############

HONEDGE = Pokemon()
HONEDGE.species = 679
HONEDGE.types = STEEL
HONEDGE.types = [HONEDGE.types, GHOST]
HONEDGE.abilities = species.abilities(679)
HONEDGE.hidden_ability = species.hidden_ability(679)

################
### DOUBLADE ###
################

DOUBLADE = Pokemon()
DOUBLADE.species = 680
DOUBLADE.types = STEEL
DOUBLADE.types = [DOUBLADE.types, GHOST]
DOUBLADE.abilities = species.abilities(680)
DOUBLADE.hidden_ability = species.hidden_ability(680)

#################
### AEGISLASH ###
#################

AEGISLASH = Pokemon()
AEGISLASH.species = 681
AEGISLASH.types = STEEL
AEGISLASH.types = [AEGISLASH.types, GHOST]
AEGISLASH.abilities = species.abilities(681)
AEGISLASH.hidden_ability = species.hidden_ability(681)

################
### SPRITZEE ###
################

SPRITZEE = Pokemon()
SPRITZEE.species = 682
SPRITZEE.types = FAIRY
SPRITZEE.abilities = species.abilities(682)
SPRITZEE.hidden_ability = species.hidden_ability(682)

##################
### AROMATISSE ###
##################

AROMATISSE = Pokemon()
AROMATISSE.species = 683
AROMATISSE.types = FAIRY
AROMATISSE.abilities = species.abilities(683)
AROMATISSE.hidden_ability = species.hidden_ability(683)

###############
### SWIRLIX ###
###############

SWIRLIX = Pokemon()
SWIRLIX.species = 684
SWIRLIX.types = FAIRY
SWIRLIX.abilities = species.abilities(684)
SWIRLIX.hidden_ability = species.hidden_ability(684)

################
### SLURPUFF ###
################

SLURPUFF = Pokemon()
SLURPUFF.species = 685
SLURPUFF.types = FAIRY
SLURPUFF.abilities = species.abilities(685)
SLURPUFF.hidden_ability = species.hidden_ability(685)

#############
### INKAY ###
#############

INKAY = Pokemon()
INKAY.species = 686
INKAY.types = DARK
INKAY.types = [INKAY.types, PSYCHIC]
INKAY.abilities = species.abilities(686)
INKAY.hidden_ability = species.hidden_ability(686)

###############
### MALAMAR ###
###############

MALAMAR = Pokemon()
MALAMAR.species = 687
MALAMAR.types = DARK
MALAMAR.types = [MALAMAR.types, PSYCHIC]
MALAMAR.abilities = species.abilities(687)
MALAMAR.hidden_ability = species.hidden_ability(687)

###############
### BINACLE ###
###############

BINACLE = Pokemon()
BINACLE.species = 688
BINACLE.types = ROCK
BINACLE.types = [BINACLE.types, WATER]
BINACLE.abilities = species.abilities(688)
BINACLE.hidden_ability = species.hidden_ability(688)

##################
### BARBARACLE ###
##################

BARBARACLE = Pokemon()
BARBARACLE.species = 689
BARBARACLE.types = ROCK
BARBARACLE.types = [BARBARACLE.types, WATER]
BARBARACLE.abilities = species.abilities(689)
BARBARACLE.hidden_ability = species.hidden_ability(689)

##############
### SKRELP ###
##############

SKRELP = Pokemon()
SKRELP.species = 690
SKRELP.types = POISON
SKRELP.types = [SKRELP.types, WATER]
SKRELP.abilities = species.abilities(690)
SKRELP.hidden_ability = species.hidden_ability(690)

################
### DRAGALGE ###
################

DRAGALGE = Pokemon()
DRAGALGE.species = 691
DRAGALGE.types = POISON
DRAGALGE.types = [DRAGALGE.types, DRAGON]
DRAGALGE.abilities = species.abilities(691)
DRAGALGE.hidden_ability = species.hidden_ability(691)

#################
### CLAUNCHER ###
#################

CLAUNCHER = Pokemon()
CLAUNCHER.species = 692
CLAUNCHER.types = WATER
CLAUNCHER.abilities = species.abilities(692)
CLAUNCHER.hidden_ability = species.hidden_ability(692)

#################
### CLAWITZER ###
#################

CLAWITZER = Pokemon()
CLAWITZER.species = 693
CLAWITZER.types = WATER
CLAWITZER.abilities = species.abilities(693)
CLAWITZER.hidden_ability = species.hidden_ability(693)

##################
### HELIOPTILE ###
##################

HELIOPTILE = Pokemon()
HELIOPTILE.species = 694
HELIOPTILE.types = ELECTRIC
HELIOPTILE.types = [HELIOPTILE.types, NORMAL]
HELIOPTILE.abilities = species.abilities(694)
HELIOPTILE.hidden_ability = species.hidden_ability(694)

#################
### HELIOLISK ###
#################

HELIOLISK = Pokemon()
HELIOLISK.species = 695
HELIOLISK.types = ELECTRIC
HELIOLISK.types = [HELIOLISK.types, NORMAL]
HELIOLISK.abilities = species.abilities(695)
HELIOLISK.hidden_ability = species.hidden_ability(695)

##############
### TYRUNT ###
##############

TYRUNT = Pokemon()
TYRUNT.species = 696
TYRUNT.types = ROCK
TYRUNT.types = [TYRUNT.types, DRAGON]
TYRUNT.abilities = species.abilities(696)
TYRUNT.hidden_ability = species.hidden_ability(696)

#################
### TYRANTRUM ###
#################

TYRANTRUM = Pokemon()
TYRANTRUM.species = 697
TYRANTRUM.types = ROCK
TYRANTRUM.types = [TYRANTRUM.types, DRAGON]
TYRANTRUM.abilities = species.abilities(697)
TYRANTRUM.hidden_ability = species.hidden_ability(697)

##############
### AMAURA ###
##############

AMAURA = Pokemon()
AMAURA.species = 698
AMAURA.types = ROCK
AMAURA.types = [AMAURA.types, ICE]
AMAURA.abilities = species.abilities(698)
AMAURA.hidden_ability = species.hidden_ability(698)

###############
### AURORUS ###
###############

AURORUS = Pokemon()
AURORUS.species = 699
AURORUS.types = ROCK
AURORUS.types = [AURORUS.types, ICE]
AURORUS.abilities = species.abilities(699)
AURORUS.hidden_ability = species.hidden_ability(699)

###############
### SYLVEON ###
###############

SYLVEON = Pokemon()
SYLVEON.species = 700
SYLVEON.types = FAIRY
SYLVEON.abilities = species.abilities(700)
SYLVEON.hidden_ability = species.hidden_ability(700)

################
### HAWLUCHA ###
################

HAWLUCHA = Pokemon()
HAWLUCHA.species = 701
HAWLUCHA.types = FIGHTING
HAWLUCHA.types = [HAWLUCHA.types, FLYING]
HAWLUCHA.abilities = species.abilities(701)
HAWLUCHA.hidden_ability = species.hidden_ability(701)

###############
### DEDENNE ###
###############

DEDENNE = Pokemon()
DEDENNE.species = 702
DEDENNE.types = ELECTRIC
DEDENNE.types = [DEDENNE.types, FAIRY]
DEDENNE.abilities = species.abilities(702)
DEDENNE.hidden_ability = species.hidden_ability(702)

###############
### CARBINK ###
###############

CARBINK = Pokemon()
CARBINK.species = 703
CARBINK.types = ROCK
CARBINK.types = [CARBINK.types, FAIRY]
CARBINK.abilities = species.abilities(703)
CARBINK.hidden_ability = species.hidden_ability(703)

#############
### GOOMY ###
#############

GOOMY = Pokemon()
GOOMY.species = 704
GOOMY.types = DRAGON
GOOMY.abilities = species.abilities(704)
GOOMY.hidden_ability = species.hidden_ability(704)

###############
### SLIGGOO ###
###############

SLIGGOO = Pokemon()
SLIGGOO.species = 705
SLIGGOO.types = DRAGON
SLIGGOO.abilities = species.abilities(705)
SLIGGOO.hidden_ability = species.hidden_ability(705)

##############
### GOODRA ###
##############

GOODRA = Pokemon()
GOODRA.species = 706
GOODRA.types = DRAGON
GOODRA.abilities = species.abilities(706)
GOODRA.hidden_ability = species.hidden_ability(706)

##############
### KLEFKI ###
##############

KLEFKI = Pokemon()
KLEFKI.species = 707
KLEFKI.types = STEEL
KLEFKI.types = [KLEFKI.types, FAIRY]
KLEFKI.abilities = species.abilities(707)
KLEFKI.hidden_ability = species.hidden_ability(707)

################
### PHANTUMP ###
################

PHANTUMP = Pokemon()
PHANTUMP.species = 708
PHANTUMP.types = GHOST
PHANTUMP.types = [PHANTUMP.types, GRASS]
PHANTUMP.abilities = species.abilities(708)
PHANTUMP.hidden_ability = species.hidden_ability(708)

#################
### TREVENANT ###
#################

TREVENANT = Pokemon()
TREVENANT.species = 709
TREVENANT.types = GHOST
TREVENANT.types = [TREVENANT.types, GRASS]
TREVENANT.abilities = species.abilities(709)
TREVENANT.hidden_ability = species.hidden_ability(709)

#################
### PUMPKABOO ###
#################

PUMPKABOO = Pokemon()
PUMPKABOO.species = 710
PUMPKABOO.types = GHOST
PUMPKABOO.types = [PUMPKABOO.types, GRASS]
PUMPKABOO.abilities = species.abilities(710)
PUMPKABOO.hidden_ability = species.hidden_ability(710)

#################
### GOURGEIST ###
#################

GOURGEIST = Pokemon()
GOURGEIST.species = 711
GOURGEIST.types = GHOST
GOURGEIST.types = [GOURGEIST.types, GRASS]
GOURGEIST.abilities = species.abilities(711)
GOURGEIST.hidden_ability = species.hidden_ability(711)

################
### BERGMITE ###
################

BERGMITE = Pokemon()
BERGMITE.species = 712
BERGMITE.types = ICE
BERGMITE.abilities = species.abilities(712)
BERGMITE.hidden_ability = species.hidden_ability(712)

###############
### AVALUGG ###
###############

AVALUGG = Pokemon()
AVALUGG.species = 713
AVALUGG.types = ICE
AVALUGG.abilities = species.abilities(713)
AVALUGG.hidden_ability = species.hidden_ability(713)

##############
### NOIBAT ###
##############

NOIBAT = Pokemon()
NOIBAT.species = 714
NOIBAT.types = FLYING
NOIBAT.types = [NOIBAT.types, DRAGON]
NOIBAT.abilities = species.abilities(714)
NOIBAT.hidden_ability = species.hidden_ability(714)

###############
### NOIVERN ###
###############

NOIVERN = Pokemon()
NOIVERN.species = 715
NOIVERN.types = FLYING
NOIVERN.types = [NOIVERN.types, DRAGON]
NOIVERN.abilities = species.abilities(715)
NOIVERN.hidden_ability = species.hidden_ability(715)

###############
### XERNEAS ###
###############

XERNEAS = Pokemon()
XERNEAS.species = 716
XERNEAS.types = FAIRY
XERNEAS.abilities = species.abilities(716)
XERNEAS.hidden_ability = species.hidden_ability(716)

###############
### YVELTAL ###
###############

YVELTAL = Pokemon()
YVELTAL.species = 717
YVELTAL.types = DARK
YVELTAL.types = [YVELTAL.types, FLYING]
YVELTAL.abilities = species.abilities(717)
YVELTAL.hidden_ability = species.hidden_ability(717)

###############
### ZYGARDE ###
###############

ZYGARDE = Pokemon()
ZYGARDE.species = 718
ZYGARDE.types = DRAGON
ZYGARDE.types = [ZYGARDE.types, GROUND]
ZYGARDE.abilities = species.abilities(718)
ZYGARDE.hidden_ability = species.hidden_ability(718)

###############
### DIANCIE ###
###############

DIANCIE = Pokemon()
DIANCIE.species = 719
DIANCIE.types = ROCK
DIANCIE.types = [DIANCIE.types, FAIRY]
DIANCIE.abilities = species.abilities(719)
DIANCIE.hidden_ability = species.hidden_ability(719)

#############
### HOOPA ###
#############

HOOPA = Pokemon()
HOOPA.species = 720
HOOPA.types = PSYCHIC
HOOPA.types = [HOOPA.types, GHOST]
HOOPA.abilities = species.abilities(720)
HOOPA.hidden_ability = species.hidden_ability(720)

#################
### VOLCANION ###
#################

VOLCANION = Pokemon()
VOLCANION.species = 721
VOLCANION.types = FIRE
VOLCANION.types = [VOLCANION.types, WATER]
VOLCANION.abilities = species.abilities(721)
VOLCANION.hidden_ability = species.hidden_ability(721)

##############
### ROWLET ###
##############

ROWLET = Pokemon()
ROWLET.species = 722
ROWLET.types = GRASS
ROWLET.types = [ROWLET.types, FLYING]
ROWLET.abilities = species.abilities(722)
ROWLET.hidden_ability = species.hidden_ability(722)

###############
### DARTRIX ###
###############

DARTRIX = Pokemon()
DARTRIX.species = 723
DARTRIX.types = GRASS
DARTRIX.types = [DARTRIX.types, FLYING]
DARTRIX.abilities = species.abilities(723)
DARTRIX.hidden_ability = species.hidden_ability(723)

#################
### DECIDUEYE ###
#################

DECIDUEYE = Pokemon()
DECIDUEYE.species = 724
DECIDUEYE.types = GRASS
DECIDUEYE.types = [DECIDUEYE.types, GHOST]
DECIDUEYE.abilities = species.abilities(724)
DECIDUEYE.hidden_ability = species.hidden_ability(724)

##############
### LITTEN ###
##############

LITTEN = Pokemon()
LITTEN.species = 725
LITTEN.types = FIRE
LITTEN.abilities = species.abilities(725)
LITTEN.hidden_ability = species.hidden_ability(725)

################
### TORRACAT ###
################

TORRACAT = Pokemon()
TORRACAT.species = 726
TORRACAT.types = FIRE
TORRACAT.abilities = species.abilities(726)
TORRACAT.hidden_ability = species.hidden_ability(726)

##################
### INCINEROAR ###
##################

INCINEROAR = Pokemon()
INCINEROAR.species = 727
INCINEROAR.types = FIRE
INCINEROAR.types = [INCINEROAR.types, DARK]
INCINEROAR.abilities = species.abilities(727)
INCINEROAR.hidden_ability = species.hidden_ability(727)

###############
### POPPLIO ###
###############

POPPLIO = Pokemon()
POPPLIO.species = 728
POPPLIO.types = WATER
POPPLIO.abilities = species.abilities(728)
POPPLIO.hidden_ability = species.hidden_ability(728)

###############
### BRIONNE ###
###############

BRIONNE = Pokemon()
BRIONNE.species = 729
BRIONNE.types = WATER
BRIONNE.abilities = species.abilities(729)
BRIONNE.hidden_ability = species.hidden_ability(729)

#################
### PRIMARINA ###
#################

PRIMARINA = Pokemon()
PRIMARINA.species = 730
PRIMARINA.types = WATER
PRIMARINA.types = [PRIMARINA.types, FAIRY]
PRIMARINA.abilities = species.abilities(730)
PRIMARINA.hidden_ability = species.hidden_ability(730)

###############
### PIKIPEK ###
###############

PIKIPEK = Pokemon()
PIKIPEK.species = 731
PIKIPEK.types = NORMAL
PIKIPEK.types = [PIKIPEK.types, FLYING]
PIKIPEK.abilities = species.abilities(731)
PIKIPEK.hidden_ability = species.hidden_ability(731)

################
### TRUMBEAK ###
################

TRUMBEAK = Pokemon()
TRUMBEAK.species = 732
TRUMBEAK.types = NORMAL
TRUMBEAK.types = [TRUMBEAK.types, FLYING]
TRUMBEAK.abilities = species.abilities(732)
TRUMBEAK.hidden_ability = species.hidden_ability(732)

#################
### TOUCANNON ###
#################

TOUCANNON = Pokemon()
TOUCANNON.species = 733
TOUCANNON.types = NORMAL
TOUCANNON.types = [TOUCANNON.types, FLYING]
TOUCANNON.abilities = species.abilities(733)
TOUCANNON.hidden_ability = species.hidden_ability(733)

###############
### YUNGOOS ###
###############

YUNGOOS = Pokemon()
YUNGOOS.species = 734
YUNGOOS.types = NORMAL
YUNGOOS.abilities = species.abilities(734)
YUNGOOS.hidden_ability = species.hidden_ability(734)

################
### GUMSHOOS ###
################

GUMSHOOS = Pokemon()
GUMSHOOS.species = 735
GUMSHOOS.types = NORMAL
GUMSHOOS.abilities = species.abilities(735)
GUMSHOOS.hidden_ability = species.hidden_ability(735)

###############
### GRUBBIN ###
###############

GRUBBIN = Pokemon()
GRUBBIN.species = 736
GRUBBIN.types = BUG
GRUBBIN.abilities = species.abilities(736)
GRUBBIN.hidden_ability = species.hidden_ability(736)

#################
### CHARJABUG ###
#################

CHARJABUG = Pokemon()
CHARJABUG.species = 737
CHARJABUG.types = BUG
CHARJABUG.types = [CHARJABUG.types, ELECTRIC]
CHARJABUG.abilities = species.abilities(737)
CHARJABUG.hidden_ability = species.hidden_ability(737)

################
### VIKAVOLT ###
################

VIKAVOLT = Pokemon()
VIKAVOLT.species = 738
VIKAVOLT.types = BUG
VIKAVOLT.types = [VIKAVOLT.types, ELECTRIC]
VIKAVOLT.abilities = species.abilities(738)
VIKAVOLT.hidden_ability = species.hidden_ability(738)

##################
### CRABRAWLER ###
##################

CRABRAWLER = Pokemon()
CRABRAWLER.species = 739
CRABRAWLER.types = FIGHTING
CRABRAWLER.abilities = species.abilities(739)
CRABRAWLER.hidden_ability = species.hidden_ability(739)

####################
### CRABOMINABLE ###
####################

CRABOMINABLE = Pokemon()
CRABOMINABLE.species = 740
CRABOMINABLE.types = FIGHTING
CRABOMINABLE.types = [CRABOMINABLE.types, ICE]
CRABOMINABLE.abilities = species.abilities(740)
CRABOMINABLE.hidden_ability = species.hidden_ability(740)

################
### ORICORIO ###
################

ORICORIO = Pokemon()
ORICORIO.species = 741
ORICORIO.types = FIRE
ORICORIO.types = [ORICORIO.types, FLYING]
ORICORIO.abilities = species.abilities(741)
ORICORIO.hidden_ability = species.hidden_ability(741)

################
### CUTIEFLY ###
################

CUTIEFLY = Pokemon()
CUTIEFLY.species = 742
CUTIEFLY.types = BUG
CUTIEFLY.types = [CUTIEFLY.types, FAIRY]
CUTIEFLY.abilities = species.abilities(742)
CUTIEFLY.hidden_ability = species.hidden_ability(742)

################
### RIBOMBEE ###
################

RIBOMBEE = Pokemon()
RIBOMBEE.species = 743
RIBOMBEE.types = BUG
RIBOMBEE.types = [RIBOMBEE.types, FAIRY]
RIBOMBEE.abilities = species.abilities(743)
RIBOMBEE.hidden_ability = species.hidden_ability(743)

################
### ROCKRUFF ###
################

ROCKRUFF = Pokemon()
ROCKRUFF.species = 744
ROCKRUFF.types = ROCK
ROCKRUFF.abilities = species.abilities(744)
ROCKRUFF.hidden_ability = species.hidden_ability(744)

################
### LYCANROC ###
################

LYCANROC = Pokemon()
LYCANROC.species = 745
LYCANROC.types = ROCK
LYCANROC.abilities = species.abilities(745)
LYCANROC.hidden_ability = species.hidden_ability(745)

##################
### WISHIWASHI ###
##################

WISHIWASHI = Pokemon()
WISHIWASHI.species = 746
WISHIWASHI.types = WATER
WISHIWASHI.abilities = species.abilities(746)
WISHIWASHI.hidden_ability = species.hidden_ability(746)

################
### MAREANIE ###
################

MAREANIE = Pokemon()
MAREANIE.species = 747
MAREANIE.types = POISON
MAREANIE.types = [MAREANIE.types, WATER]
MAREANIE.abilities = species.abilities(747)
MAREANIE.hidden_ability = species.hidden_ability(747)

###############
### TOXAPEX ###
###############

TOXAPEX = Pokemon()
TOXAPEX.species = 748
TOXAPEX.types = POISON
TOXAPEX.types = [TOXAPEX.types, WATER]
TOXAPEX.abilities = species.abilities(748)
TOXAPEX.hidden_ability = species.hidden_ability(748)

###############
### MUDBRAY ###
###############

MUDBRAY = Pokemon()
MUDBRAY.species = 749
MUDBRAY.types = GROUND
MUDBRAY.abilities = species.abilities(749)
MUDBRAY.hidden_ability = species.hidden_ability(749)

################
### MUDSDALE ###
################

MUDSDALE = Pokemon()
MUDSDALE.species = 750
MUDSDALE.types = GROUND
MUDSDALE.abilities = species.abilities(750)
MUDSDALE.hidden_ability = species.hidden_ability(750)

################
### DEWPIDER ###
################

DEWPIDER = Pokemon()
DEWPIDER.species = 751
DEWPIDER.types = WATER
DEWPIDER.types = [DEWPIDER.types, BUG]
DEWPIDER.abilities = species.abilities(751)
DEWPIDER.hidden_ability = species.hidden_ability(751)

#################
### ARAQUANID ###
#################

ARAQUANID = Pokemon()
ARAQUANID.species = 752
ARAQUANID.types = WATER
ARAQUANID.types = [ARAQUANID.types, BUG]
ARAQUANID.abilities = species.abilities(752)
ARAQUANID.hidden_ability = species.hidden_ability(752)

################
### FOMANTIS ###
################

FOMANTIS = Pokemon()
FOMANTIS.species = 753
FOMANTIS.types = GRASS
FOMANTIS.abilities = species.abilities(753)
FOMANTIS.hidden_ability = species.hidden_ability(753)

################
### LURANTIS ###
################

LURANTIS = Pokemon()
LURANTIS.species = 754
LURANTIS.types = GRASS
LURANTIS.abilities = species.abilities(754)
LURANTIS.hidden_ability = species.hidden_ability(754)

################
### MORELULL ###
################

MORELULL = Pokemon()
MORELULL.species = 755
MORELULL.types = GRASS
MORELULL.types = [MORELULL.types, FAIRY]
MORELULL.abilities = species.abilities(755)
MORELULL.hidden_ability = species.hidden_ability(755)

#################
### SHIINOTIC ###
#################

SHIINOTIC = Pokemon()
SHIINOTIC.species = 756
SHIINOTIC.types = GRASS
SHIINOTIC.types = [SHIINOTIC.types, FAIRY]
SHIINOTIC.abilities = species.abilities(756)
SHIINOTIC.hidden_ability = species.hidden_ability(756)

################
### SALANDIT ###
################

SALANDIT = Pokemon()
SALANDIT.species = 757
SALANDIT.types = POISON
SALANDIT.types = [SALANDIT.types, FIRE]
SALANDIT.abilities = species.abilities(757)
SALANDIT.hidden_ability = species.hidden_ability(757)

################
### SALAZZLE ###
################

SALAZZLE = Pokemon()
SALAZZLE.species = 758
SALAZZLE.types = POISON
SALAZZLE.types = [SALAZZLE.types, FIRE]
SALAZZLE.abilities = species.abilities(758)
SALAZZLE.hidden_ability = species.hidden_ability(758)

###############
### STUFFUL ###
###############

STUFFUL = Pokemon()
STUFFUL.species = 759
STUFFUL.types = NORMAL
STUFFUL.types = [STUFFUL.types, FIGHTING]
STUFFUL.abilities = species.abilities(759)
STUFFUL.hidden_ability = species.hidden_ability(759)

##############
### BEWEAR ###
##############

BEWEAR = Pokemon()
BEWEAR.species = 760
BEWEAR.types = NORMAL
BEWEAR.types = [BEWEAR.types, FIGHTING]
BEWEAR.abilities = species.abilities(760)
BEWEAR.hidden_ability = species.hidden_ability(760)

#################
### BOUNSWEET ###
#################

BOUNSWEET = Pokemon()
BOUNSWEET.species = 761
BOUNSWEET.types = GRASS
BOUNSWEET.abilities = species.abilities(761)
BOUNSWEET.hidden_ability = species.hidden_ability(761)

###############
### STEENEE ###
###############

STEENEE = Pokemon()
STEENEE.species = 762
STEENEE.types = GRASS
STEENEE.abilities = species.abilities(762)
STEENEE.hidden_ability = species.hidden_ability(762)

################
### TSAREENA ###
################

TSAREENA = Pokemon()
TSAREENA.species = 763
TSAREENA.types = GRASS
TSAREENA.abilities = species.abilities(763)
TSAREENA.hidden_ability = species.hidden_ability(763)

##############
### COMFEY ###
##############

COMFEY = Pokemon()
COMFEY.species = 764
COMFEY.types = FAIRY
COMFEY.abilities = species.abilities(764)
COMFEY.hidden_ability = species.hidden_ability(764)

################
### ORANGURU ###
################

ORANGURU = Pokemon()
ORANGURU.species = 765
ORANGURU.types = NORMAL
ORANGURU.types = [ORANGURU.types, PSYCHIC]
ORANGURU.abilities = species.abilities(765)
ORANGURU.hidden_ability = species.hidden_ability(765)

#################
### PASSIMIAN ###
#################

PASSIMIAN = Pokemon()
PASSIMIAN.species = 766
PASSIMIAN.types = FIGHTING
PASSIMIAN.abilities = species.abilities(766)
PASSIMIAN.hidden_ability = species.hidden_ability(766)

##############
### WIMPOD ###
##############

WIMPOD = Pokemon()
WIMPOD.species = 767
WIMPOD.types = BUG
WIMPOD.types = [WIMPOD.types, WATER]
WIMPOD.abilities = species.abilities(767)
WIMPOD.hidden_ability = species.hidden_ability(767)

#################
### GOLISOPOD ###
#################

GOLISOPOD = Pokemon()
GOLISOPOD.species = 768
GOLISOPOD.types = BUG
GOLISOPOD.types = [GOLISOPOD.types, WATER]
GOLISOPOD.abilities = species.abilities(768)
GOLISOPOD.hidden_ability = species.hidden_ability(768)

#################
### SANDYGAST ###
#################

SANDYGAST = Pokemon()
SANDYGAST.species = 769
SANDYGAST.types = GHOST
SANDYGAST.types = [SANDYGAST.types, GROUND]
SANDYGAST.abilities = species.abilities(769)
SANDYGAST.hidden_ability = species.hidden_ability(769)

#################
### PALOSSAND ###
#################

PALOSSAND = Pokemon()
PALOSSAND.species = 770
PALOSSAND.types = GHOST
PALOSSAND.types = [PALOSSAND.types, GROUND]
PALOSSAND.abilities = species.abilities(770)
PALOSSAND.hidden_ability = species.hidden_ability(770)

#################
### PYUKUMUKU ###
#################

PYUKUMUKU = Pokemon()
PYUKUMUKU.species = 771
PYUKUMUKU.types = WATER
PYUKUMUKU.abilities = species.abilities(771)
PYUKUMUKU.hidden_ability = species.hidden_ability(771)

################
### TYPENULL ###
################

TYPENULL = Pokemon()
TYPENULL.types = NORMAL
################
### SILVALLY ###
################

SILVALLY = Pokemon()
SILVALLY.species = 773
SILVALLY.types = NORMAL
SILVALLY.abilities = species.abilities(773)
SILVALLY.hidden_ability = species.hidden_ability(773)

##############
### MINIOR ###
##############

MINIOR = Pokemon()
MINIOR.species = 774
MINIOR.types = ROCK
MINIOR.types = [MINIOR.types, FLYING]
MINIOR.abilities = species.abilities(774)
MINIOR.hidden_ability = species.hidden_ability(774)

##############
### KOMALA ###
##############

KOMALA = Pokemon()
KOMALA.species = 775
KOMALA.types = NORMAL
KOMALA.abilities = species.abilities(775)
KOMALA.hidden_ability = species.hidden_ability(775)

##################
### TURTONATOR ###
##################

TURTONATOR = Pokemon()
TURTONATOR.species = 776
TURTONATOR.types = FIRE
TURTONATOR.types = [TURTONATOR.types, DRAGON]
TURTONATOR.abilities = species.abilities(776)
TURTONATOR.hidden_ability = species.hidden_ability(776)

##################
### TOGEDEMARU ###
##################

TOGEDEMARU = Pokemon()
TOGEDEMARU.species = 777
TOGEDEMARU.types = ELECTRIC
TOGEDEMARU.types = [TOGEDEMARU.types, STEEL]
TOGEDEMARU.abilities = species.abilities(777)
TOGEDEMARU.hidden_ability = species.hidden_ability(777)

###############
### MIMIKYU ###
###############

MIMIKYU = Pokemon()
MIMIKYU.species = 778
MIMIKYU.types = GHOST
MIMIKYU.types = [MIMIKYU.types, FAIRY]
MIMIKYU.abilities = species.abilities(778)
MIMIKYU.hidden_ability = species.hidden_ability(778)

###############
### BRUXISH ###
###############

BRUXISH = Pokemon()
BRUXISH.species = 779
BRUXISH.types = WATER
BRUXISH.types = [BRUXISH.types, PSYCHIC]
BRUXISH.abilities = species.abilities(779)
BRUXISH.hidden_ability = species.hidden_ability(779)

##############
### DRAMPA ###
##############

DRAMPA = Pokemon()
DRAMPA.species = 780
DRAMPA.types = NORMAL
DRAMPA.types = [DRAMPA.types, DRAGON]
DRAMPA.abilities = species.abilities(780)
DRAMPA.hidden_ability = species.hidden_ability(780)

################
### DHELMISE ###
################

DHELMISE = Pokemon()
DHELMISE.species = 781
DHELMISE.types = GHOST
DHELMISE.types = [DHELMISE.types, GRASS]
DHELMISE.abilities = species.abilities(781)
DHELMISE.hidden_ability = species.hidden_ability(781)

###############
### JANGMOO ###
###############

JANGMOO = Pokemon()
JANGMOO.types = DRAGON
###############
### HAKAMOO ###
###############

HAKAMOO = Pokemon()
HAKAMOO.types = DRAGON
HAKAMOO.types = [HAKAMOO.types, FIGHTING]
##############
### KOMMOO ###
##############

KOMMOO = Pokemon()
KOMMOO.types = DRAGON
KOMMOO.types = [KOMMOO.types, FIGHTING]
################
### TAPUKOKO ###
################

TAPUKOKO = Pokemon()
TAPUKOKO.types = ELECTRIC
TAPUKOKO.types = [TAPUKOKO.types, FAIRY]
################
### TAPULELE ###
################

TAPULELE = Pokemon()
TAPULELE.types = PSYCHIC
TAPULELE.types = [TAPULELE.types, FAIRY]
################
### TAPUBULU ###
################

TAPUBULU = Pokemon()
TAPUBULU.types = GRASS
TAPUBULU.types = [TAPUBULU.types, FAIRY]
################
### TAPUFINI ###
################

TAPUFINI = Pokemon()
TAPUFINI.types = WATER
TAPUFINI.types = [TAPUFINI.types, FAIRY]
##############
### COSMOG ###
##############

COSMOG = Pokemon()
COSMOG.species = 789
COSMOG.types = PSYCHIC
COSMOG.abilities = species.abilities(789)
COSMOG.hidden_ability = species.hidden_ability(789)

###############
### COSMOEM ###
###############

COSMOEM = Pokemon()
COSMOEM.species = 790
COSMOEM.types = PSYCHIC
COSMOEM.abilities = species.abilities(790)
COSMOEM.hidden_ability = species.hidden_ability(790)

################
### SOLGALEO ###
################

SOLGALEO = Pokemon()
SOLGALEO.species = 791
SOLGALEO.types = PSYCHIC
SOLGALEO.types = [SOLGALEO.types, STEEL]
SOLGALEO.abilities = species.abilities(791)
SOLGALEO.hidden_ability = species.hidden_ability(791)

##############
### LUNALA ###
##############

LUNALA = Pokemon()
LUNALA.species = 792
LUNALA.types = PSYCHIC
LUNALA.types = [LUNALA.types, GHOST]
LUNALA.abilities = species.abilities(792)
LUNALA.hidden_ability = species.hidden_ability(792)

################
### NIHILEGO ###
################

NIHILEGO = Pokemon()
NIHILEGO.species = 793
NIHILEGO.types = ROCK
NIHILEGO.types = [NIHILEGO.types, POISON]
NIHILEGO.abilities = species.abilities(793)
NIHILEGO.hidden_ability = species.hidden_ability(793)

################
### BUZZWOLE ###
################

BUZZWOLE = Pokemon()
BUZZWOLE.species = 794
BUZZWOLE.types = BUG
BUZZWOLE.types = [BUZZWOLE.types, FIGHTING]
BUZZWOLE.abilities = species.abilities(794)
BUZZWOLE.hidden_ability = species.hidden_ability(794)

#################
### PHEROMOSA ###
#################

PHEROMOSA = Pokemon()
PHEROMOSA.species = 795
PHEROMOSA.types = BUG
PHEROMOSA.types = [PHEROMOSA.types, FIGHTING]
PHEROMOSA.abilities = species.abilities(795)
PHEROMOSA.hidden_ability = species.hidden_ability(795)

#################
### XURKITREE ###
#################

XURKITREE = Pokemon()
XURKITREE.species = 796
XURKITREE.types = ELECTRIC
XURKITREE.abilities = species.abilities(796)
XURKITREE.hidden_ability = species.hidden_ability(796)

##################
### CELESTEELA ###
##################

CELESTEELA = Pokemon()
CELESTEELA.species = 797
CELESTEELA.types = STEEL
CELESTEELA.types = [CELESTEELA.types, FLYING]
CELESTEELA.abilities = species.abilities(797)
CELESTEELA.hidden_ability = species.hidden_ability(797)

###############
### KARTANA ###
###############

KARTANA = Pokemon()
KARTANA.species = 798
KARTANA.types = GRASS
KARTANA.types = [KARTANA.types, STEEL]
KARTANA.abilities = species.abilities(798)
KARTANA.hidden_ability = species.hidden_ability(798)

################
### GUZZLORD ###
################

GUZZLORD = Pokemon()
GUZZLORD.species = 799
GUZZLORD.types = DARK
GUZZLORD.types = [GUZZLORD.types, DRAGON]
GUZZLORD.abilities = species.abilities(799)
GUZZLORD.hidden_ability = species.hidden_ability(799)

################
### NECROZMA ###
################

NECROZMA = Pokemon()
NECROZMA.species = 800
NECROZMA.types = PSYCHIC
NECROZMA.abilities = species.abilities(800)
NECROZMA.hidden_ability = species.hidden_ability(800)

################
### MAGEARNA ###
################

MAGEARNA = Pokemon()
MAGEARNA.species = 801
MAGEARNA.types = STEEL
MAGEARNA.types = [MAGEARNA.types, FAIRY]
MAGEARNA.abilities = species.abilities(801)
MAGEARNA.hidden_ability = species.hidden_ability(801)

#################
### MARSHADOW ###
#################

MARSHADOW = Pokemon()
MARSHADOW.species = 802
MARSHADOW.types = FIGHTING
MARSHADOW.types = [MARSHADOW.types, GHOST]
MARSHADOW.abilities = species.abilities(802)
MARSHADOW.hidden_ability = species.hidden_ability(802)

###############
### POIPOLE ###
###############

POIPOLE = Pokemon()
POIPOLE.species = 803
POIPOLE.types = POISON
POIPOLE.abilities = species.abilities(803)
POIPOLE.hidden_ability = species.hidden_ability(803)

#################
### NAGANADEL ###
#################

NAGANADEL = Pokemon()
NAGANADEL.species = 804
NAGANADEL.types = POISON
NAGANADEL.types = [NAGANADEL.types, DRAGON]
NAGANADEL.abilities = species.abilities(804)
NAGANADEL.hidden_ability = species.hidden_ability(804)

#################
### STAKATAKA ###
#################

STAKATAKA = Pokemon()
STAKATAKA.species = 805
STAKATAKA.types = ROCK
STAKATAKA.types = [STAKATAKA.types, STEEL]
STAKATAKA.abilities = species.abilities(805)
STAKATAKA.hidden_ability = species.hidden_ability(805)

###################
### BLACEPHALON ###
###################

BLACEPHALON = Pokemon()
BLACEPHALON.species = 806
BLACEPHALON.types = FIRE
BLACEPHALON.types = [BLACEPHALON.types, GHOST]
BLACEPHALON.abilities = species.abilities(806)
BLACEPHALON.hidden_ability = species.hidden_ability(806)

###############
### ZERAORA ###
###############

ZERAORA = Pokemon()
ZERAORA.species = 807
ZERAORA.types = ELECTRIC
ZERAORA.abilities = species.abilities(807)
ZERAORA.hidden_ability = species.hidden_ability(807)

##############
### MELTAN ###
##############

MELTAN = Pokemon()
MELTAN.species = 808
MELTAN.types = STEEL
MELTAN.abilities = species.abilities(808)
MELTAN.hidden_ability = species.hidden_ability(808)

################
### MELMETAL ###
################

MELMETAL = Pokemon()
MELMETAL.species = 809
MELMETAL.types = STEEL
MELMETAL.abilities = species.abilities(809)
MELMETAL.hidden_ability = species.hidden_ability(809)

###############
### GROOKEY ###
###############

GROOKEY = Pokemon()
GROOKEY.species = 810
GROOKEY.types = GRASS
GROOKEY.abilities = species.abilities(810)
GROOKEY.hidden_ability = species.hidden_ability(810)

################
### THWACKEY ###
################

THWACKEY = Pokemon()
THWACKEY.species = 811
THWACKEY.types = GRASS
THWACKEY.abilities = species.abilities(811)
THWACKEY.hidden_ability = species.hidden_ability(811)

#################
### RILLABOOM ###
#################

RILLABOOM = Pokemon()
RILLABOOM.species = 812
RILLABOOM.types = GRASS
RILLABOOM.abilities = species.abilities(812)
RILLABOOM.hidden_ability = species.hidden_ability(812)

#################
### SCORBUNNY ###
#################

SCORBUNNY = Pokemon()
SCORBUNNY.species = 813
SCORBUNNY.types = FIRE
SCORBUNNY.abilities = species.abilities(813)
SCORBUNNY.hidden_ability = species.hidden_ability(813)

##############
### RABOOT ###
##############

RABOOT = Pokemon()
RABOOT.species = 814
RABOOT.types = FIRE
RABOOT.abilities = species.abilities(814)
RABOOT.hidden_ability = species.hidden_ability(814)

#################
### CINDERACE ###
#################

CINDERACE = Pokemon()
CINDERACE.species = 815
CINDERACE.types = FIRE
CINDERACE.abilities = species.abilities(815)
CINDERACE.hidden_ability = species.hidden_ability(815)

##############
### SOBBLE ###
##############

SOBBLE = Pokemon()
SOBBLE.species = 816
SOBBLE.types = WATER
SOBBLE.abilities = species.abilities(816)
SOBBLE.hidden_ability = species.hidden_ability(816)

################
### DRIZZILE ###
################

DRIZZILE = Pokemon()
DRIZZILE.species = 817
DRIZZILE.types = WATER
DRIZZILE.abilities = species.abilities(817)
DRIZZILE.hidden_ability = species.hidden_ability(817)

################
### INTELEON ###
################

INTELEON = Pokemon()
INTELEON.species = 818
INTELEON.types = WATER
INTELEON.abilities = species.abilities(818)
INTELEON.hidden_ability = species.hidden_ability(818)

###############
### SKWOVET ###
###############

SKWOVET = Pokemon()
SKWOVET.species = 819
SKWOVET.types = NORMAL
SKWOVET.abilities = species.abilities(819)
SKWOVET.hidden_ability = species.hidden_ability(819)

################
### GREEDENT ###
################

GREEDENT = Pokemon()
GREEDENT.species = 820
GREEDENT.types = NORMAL
GREEDENT.abilities = species.abilities(820)
GREEDENT.hidden_ability = species.hidden_ability(820)

################
### ROOKIDEE ###
################

ROOKIDEE = Pokemon()
ROOKIDEE.species = 821
ROOKIDEE.types = FLYING
ROOKIDEE.abilities = species.abilities(821)
ROOKIDEE.hidden_ability = species.hidden_ability(821)

###################
### CORVISQUIRE ###
###################

CORVISQUIRE = Pokemon()
CORVISQUIRE.species = 822
CORVISQUIRE.types = FLYING
CORVISQUIRE.abilities = species.abilities(822)
CORVISQUIRE.hidden_ability = species.hidden_ability(822)

###################
### CORVIKNIGHT ###
###################

CORVIKNIGHT = Pokemon()
CORVIKNIGHT.species = 823
CORVIKNIGHT.types = FLYING
CORVIKNIGHT.types = [CORVIKNIGHT.types, STEEL]
CORVIKNIGHT.abilities = species.abilities(823)
CORVIKNIGHT.hidden_ability = species.hidden_ability(823)

###############
### BLIPBUG ###
###############

BLIPBUG = Pokemon()
BLIPBUG.species = 824
BLIPBUG.types = BUG
BLIPBUG.abilities = species.abilities(824)
BLIPBUG.hidden_ability = species.hidden_ability(824)

###############
### DOTTLER ###
###############

DOTTLER = Pokemon()
DOTTLER.species = 825
DOTTLER.types = BUG
DOTTLER.types = [DOTTLER.types, PSYCHIC]
DOTTLER.abilities = species.abilities(825)
DOTTLER.hidden_ability = species.hidden_ability(825)

################
### ORBEETLE ###
################

ORBEETLE = Pokemon()
ORBEETLE.species = 826
ORBEETLE.types = BUG
ORBEETLE.types = [ORBEETLE.types, PSYCHIC]
ORBEETLE.abilities = species.abilities(826)
ORBEETLE.hidden_ability = species.hidden_ability(826)

##############
### NICKIT ###
##############

NICKIT = Pokemon()
NICKIT.species = 827
NICKIT.types = DARK
NICKIT.abilities = species.abilities(827)
NICKIT.hidden_ability = species.hidden_ability(827)

###############
### THIEVUL ###
###############

THIEVUL = Pokemon()
THIEVUL.species = 828
THIEVUL.types = DARK
THIEVUL.abilities = species.abilities(828)
THIEVUL.hidden_ability = species.hidden_ability(828)

##################
### GOSSIFLEUR ###
##################

GOSSIFLEUR = Pokemon()
GOSSIFLEUR.species = 829
GOSSIFLEUR.types = GRASS
GOSSIFLEUR.abilities = species.abilities(829)
GOSSIFLEUR.hidden_ability = species.hidden_ability(829)

################
### ELDEGOSS ###
################

ELDEGOSS = Pokemon()
ELDEGOSS.species = 830
ELDEGOSS.types = GRASS
ELDEGOSS.abilities = species.abilities(830)
ELDEGOSS.hidden_ability = species.hidden_ability(830)

##############
### WOOLOO ###
##############

WOOLOO = Pokemon()
WOOLOO.species = 831
WOOLOO.types = NORMAL
WOOLOO.abilities = species.abilities(831)
WOOLOO.hidden_ability = species.hidden_ability(831)

###############
### DUBWOOL ###
###############

DUBWOOL = Pokemon()
DUBWOOL.species = 832
DUBWOOL.types = NORMAL
DUBWOOL.abilities = species.abilities(832)
DUBWOOL.hidden_ability = species.hidden_ability(832)

###############
### CHEWTLE ###
###############

CHEWTLE = Pokemon()
CHEWTLE.species = 833
CHEWTLE.types = WATER
CHEWTLE.abilities = species.abilities(833)
CHEWTLE.hidden_ability = species.hidden_ability(833)

###############
### DREDNAW ###
###############

DREDNAW = Pokemon()
DREDNAW.species = 834
DREDNAW.types = WATER
DREDNAW.types = [DREDNAW.types, ROCK]
DREDNAW.abilities = species.abilities(834)
DREDNAW.hidden_ability = species.hidden_ability(834)

##############
### YAMPER ###
##############

YAMPER = Pokemon()
YAMPER.species = 835
YAMPER.types = ELECTRIC
YAMPER.abilities = species.abilities(835)
YAMPER.hidden_ability = species.hidden_ability(835)

###############
### BOLTUND ###
###############

BOLTUND = Pokemon()
BOLTUND.species = 836
BOLTUND.types = ELECTRIC
BOLTUND.abilities = species.abilities(836)
BOLTUND.hidden_ability = species.hidden_ability(836)

################
### ROLYCOLY ###
################

ROLYCOLY = Pokemon()
ROLYCOLY.species = 837
ROLYCOLY.types = ROCK
ROLYCOLY.abilities = species.abilities(837)
ROLYCOLY.hidden_ability = species.hidden_ability(837)

##############
### CARKOL ###
##############

CARKOL = Pokemon()
CARKOL.species = 838
CARKOL.types = ROCK
CARKOL.types = [CARKOL.types, FIRE]
CARKOL.abilities = species.abilities(838)
CARKOL.hidden_ability = species.hidden_ability(838)

#################
### COALOSSAL ###
#################

COALOSSAL = Pokemon()
COALOSSAL.species = 839
COALOSSAL.types = ROCK
COALOSSAL.types = [COALOSSAL.types, FIRE]
COALOSSAL.abilities = species.abilities(839)
COALOSSAL.hidden_ability = species.hidden_ability(839)

##############
### APPLIN ###
##############

APPLIN = Pokemon()
APPLIN.species = 840
APPLIN.types = GRASS
APPLIN.types = [APPLIN.types, DRAGON]
APPLIN.abilities = species.abilities(840)
APPLIN.hidden_ability = species.hidden_ability(840)

###############
### FLAPPLE ###
###############

FLAPPLE = Pokemon()
FLAPPLE.species = 841
FLAPPLE.types = GRASS
FLAPPLE.types = [FLAPPLE.types, DRAGON]
FLAPPLE.abilities = species.abilities(841)
FLAPPLE.hidden_ability = species.hidden_ability(841)

################
### APPLETUN ###
################

APPLETUN = Pokemon()
APPLETUN.species = 842
APPLETUN.types = GRASS
APPLETUN.types = [APPLETUN.types, DRAGON]
APPLETUN.abilities = species.abilities(842)
APPLETUN.hidden_ability = species.hidden_ability(842)

#################
### SILICOBRA ###
#################

SILICOBRA = Pokemon()
SILICOBRA.species = 843
SILICOBRA.types = GROUND
SILICOBRA.abilities = species.abilities(843)
SILICOBRA.hidden_ability = species.hidden_ability(843)

##################
### SANDACONDA ###
##################

SANDACONDA = Pokemon()
SANDACONDA.species = 844
SANDACONDA.types = GROUND
SANDACONDA.abilities = species.abilities(844)
SANDACONDA.hidden_ability = species.hidden_ability(844)

#################
### CRAMORANT ###
#################

CRAMORANT = Pokemon()
CRAMORANT.species = 845
CRAMORANT.types = FLYING
CRAMORANT.types = [CRAMORANT.types, WATER]
CRAMORANT.abilities = species.abilities(845)
CRAMORANT.hidden_ability = species.hidden_ability(845)

################
### ARROKUDA ###
################

ARROKUDA = Pokemon()
ARROKUDA.species = 846
ARROKUDA.types = WATER
ARROKUDA.abilities = species.abilities(846)
ARROKUDA.hidden_ability = species.hidden_ability(846)

###################
### BARRASKEWDA ###
###################

BARRASKEWDA = Pokemon()
BARRASKEWDA.species = 847
BARRASKEWDA.types = WATER
BARRASKEWDA.abilities = species.abilities(847)
BARRASKEWDA.hidden_ability = species.hidden_ability(847)

#############
### TOXEL ###
#############

TOXEL = Pokemon()
TOXEL.species = 848
TOXEL.types = ELECTRIC
TOXEL.types = [TOXEL.types, POISON]
TOXEL.abilities = species.abilities(848)
TOXEL.hidden_ability = species.hidden_ability(848)

##################
### TOXTRICITY ###
##################

TOXTRICITY = Pokemon()
TOXTRICITY.species = 849
TOXTRICITY.types = ELECTRIC
TOXTRICITY.types = [TOXTRICITY.types, POISON]
TOXTRICITY.abilities = species.abilities(849)
TOXTRICITY.hidden_ability = species.hidden_ability(849)

##################
### SIZZLIPEDE ###
##################

SIZZLIPEDE = Pokemon()
SIZZLIPEDE.species = 850
SIZZLIPEDE.types = FIRE
SIZZLIPEDE.types = [SIZZLIPEDE.types, BUG]
SIZZLIPEDE.abilities = species.abilities(850)
SIZZLIPEDE.hidden_ability = species.hidden_ability(850)

###################
### CENTISKORCH ###
###################

CENTISKORCH = Pokemon()
CENTISKORCH.species = 851
CENTISKORCH.types = FIRE
CENTISKORCH.types = [CENTISKORCH.types, BUG]
CENTISKORCH.abilities = species.abilities(851)
CENTISKORCH.hidden_ability = species.hidden_ability(851)

#################
### CLOBBOPUS ###
#################

CLOBBOPUS = Pokemon()
CLOBBOPUS.species = 852
CLOBBOPUS.types = FIGHTING
CLOBBOPUS.abilities = species.abilities(852)
CLOBBOPUS.hidden_ability = species.hidden_ability(852)

#################
### GRAPPLOCT ###
#################

GRAPPLOCT = Pokemon()
GRAPPLOCT.species = 853
GRAPPLOCT.types = FIGHTING
GRAPPLOCT.abilities = species.abilities(853)
GRAPPLOCT.hidden_ability = species.hidden_ability(853)

################
### SINISTEA ###
################

SINISTEA = Pokemon()
SINISTEA.species = 854
SINISTEA.types = GHOST
SINISTEA.abilities = species.abilities(854)
SINISTEA.hidden_ability = species.hidden_ability(854)

###################
### POLTEAGEIST ###
###################

POLTEAGEIST = Pokemon()
POLTEAGEIST.species = 855
POLTEAGEIST.types = GHOST
POLTEAGEIST.abilities = species.abilities(855)
POLTEAGEIST.hidden_ability = species.hidden_ability(855)

###############
### HATENNA ###
###############

HATENNA = Pokemon()
HATENNA.species = 856
HATENNA.types = PSYCHIC
HATENNA.abilities = species.abilities(856)
HATENNA.hidden_ability = species.hidden_ability(856)

###############
### HATTREM ###
###############

HATTREM = Pokemon()
HATTREM.species = 857
HATTREM.types = PSYCHIC
HATTREM.abilities = species.abilities(857)
HATTREM.hidden_ability = species.hidden_ability(857)

#################
### HATTERENE ###
#################

HATTERENE = Pokemon()
HATTERENE.species = 858
HATTERENE.types = PSYCHIC
HATTERENE.types = [HATTERENE.types, FAIRY]
HATTERENE.abilities = species.abilities(858)
HATTERENE.hidden_ability = species.hidden_ability(858)

################
### IMPIDIMP ###
################

IMPIDIMP = Pokemon()
IMPIDIMP.species = 859
IMPIDIMP.types = DARK
IMPIDIMP.types = [IMPIDIMP.types, FAIRY]
IMPIDIMP.abilities = species.abilities(859)
IMPIDIMP.hidden_ability = species.hidden_ability(859)

###############
### MORGREM ###
###############

MORGREM = Pokemon()
MORGREM.species = 860
MORGREM.types = DARK
MORGREM.types = [MORGREM.types, FAIRY]
MORGREM.abilities = species.abilities(860)
MORGREM.hidden_ability = species.hidden_ability(860)

##################
### GRIMMSNARL ###
##################

GRIMMSNARL = Pokemon()
GRIMMSNARL.species = 861
GRIMMSNARL.types = DARK
GRIMMSNARL.types = [GRIMMSNARL.types, FAIRY]
GRIMMSNARL.abilities = species.abilities(861)
GRIMMSNARL.hidden_ability = species.hidden_ability(861)

#################
### OBSTAGOON ###
#################

OBSTAGOON = Pokemon()
OBSTAGOON.species = 862
OBSTAGOON.types = DARK
OBSTAGOON.types = [OBSTAGOON.types, NORMAL]
OBSTAGOON.abilities = species.abilities(862)
OBSTAGOON.hidden_ability = species.hidden_ability(862)

##################
### PERRSERKER ###
##################

PERRSERKER = Pokemon()
PERRSERKER.species = 863
PERRSERKER.types = STEEL
PERRSERKER.abilities = species.abilities(863)
PERRSERKER.hidden_ability = species.hidden_ability(863)

###############
### CURSOLA ###
###############

CURSOLA = Pokemon()
CURSOLA.species = 864
CURSOLA.types = GHOST
CURSOLA.abilities = species.abilities(864)
CURSOLA.hidden_ability = species.hidden_ability(864)

#################
### SIRFETCHD ###
#################

SIRFETCHD = Pokemon()
SIRFETCHD.types = FIGHTING
##############
### MRRIME ###
##############

MRRIME = Pokemon()
MRRIME.types = ICE
MRRIME.types = [MRRIME.types, PSYCHIC]
#################
### RUNERIGUS ###
#################

RUNERIGUS = Pokemon()
RUNERIGUS.species = 867
RUNERIGUS.types = GROUND
RUNERIGUS.types = [RUNERIGUS.types, GHOST]
RUNERIGUS.abilities = species.abilities(867)
RUNERIGUS.hidden_ability = species.hidden_ability(867)

###############
### MILCERY ###
###############

MILCERY = Pokemon()
MILCERY.species = 868
MILCERY.types = FAIRY
MILCERY.abilities = species.abilities(868)
MILCERY.hidden_ability = species.hidden_ability(868)

################
### ALCREMIE ###
################

ALCREMIE = Pokemon()
ALCREMIE.species = 869
ALCREMIE.types = FAIRY
ALCREMIE.abilities = species.abilities(869)
ALCREMIE.hidden_ability = species.hidden_ability(869)

###############
### FALINKS ###
###############

FALINKS = Pokemon()
FALINKS.species = 870
FALINKS.types = FIGHTING
FALINKS.abilities = species.abilities(870)
FALINKS.hidden_ability = species.hidden_ability(870)

###################
### PINCHURCHIN ###
###################

PINCHURCHIN = Pokemon()
PINCHURCHIN.types = ELECTRIC
############
### SNOM ###
############

SNOM = Pokemon()
SNOM.species = 872
SNOM.types = ICE
SNOM.types = [SNOM.types, BUG]
SNOM.abilities = species.abilities(872)
SNOM.hidden_ability = species.hidden_ability(872)

################
### FROSMOTH ###
################

FROSMOTH = Pokemon()
FROSMOTH.species = 873
FROSMOTH.types = ICE
FROSMOTH.types = [FROSMOTH.types, BUG]
FROSMOTH.abilities = species.abilities(873)
FROSMOTH.hidden_ability = species.hidden_ability(873)

###################
### STONJOURNER ###
###################

STONJOURNER = Pokemon()
STONJOURNER.species = 874
STONJOURNER.types = ROCK
STONJOURNER.abilities = species.abilities(874)
STONJOURNER.hidden_ability = species.hidden_ability(874)

##############
### EISCUE ###
##############

EISCUE = Pokemon()
EISCUE.species = 875
EISCUE.types = ICE
EISCUE.abilities = species.abilities(875)
EISCUE.hidden_ability = species.hidden_ability(875)

################
### INDEEDEE ###
################

INDEEDEE = Pokemon()
INDEEDEE.species = 876
INDEEDEE.types = PSYCHIC
INDEEDEE.types = [INDEEDEE.types, NORMAL]
INDEEDEE.abilities = species.abilities(876)
INDEEDEE.hidden_ability = species.hidden_ability(876)

###############
### MORPEKO ###
###############

MORPEKO = Pokemon()
MORPEKO.species = 877
MORPEKO.types = ELECTRIC
MORPEKO.types = [MORPEKO.types, DARK]
MORPEKO.abilities = species.abilities(877)
MORPEKO.hidden_ability = species.hidden_ability(877)

##############
### CUFANT ###
##############

CUFANT = Pokemon()
CUFANT.species = 878
CUFANT.types = STEEL
CUFANT.abilities = species.abilities(878)
CUFANT.hidden_ability = species.hidden_ability(878)

##################
### COPPERAJAH ###
##################

COPPERAJAH = Pokemon()
COPPERAJAH.species = 879
COPPERAJAH.types = STEEL
COPPERAJAH.abilities = species.abilities(879)
COPPERAJAH.hidden_ability = species.hidden_ability(879)

#################
### DRACOZOLT ###
#################

DRACOZOLT = Pokemon()
DRACOZOLT.species = 880
DRACOZOLT.types = ELECTRIC
DRACOZOLT.types = [DRACOZOLT.types, DRAGON]
DRACOZOLT.abilities = species.abilities(880)
DRACOZOLT.hidden_ability = species.hidden_ability(880)

#################
### ARCTOZOLT ###
#################

ARCTOZOLT = Pokemon()
ARCTOZOLT.species = 881
ARCTOZOLT.types = ELECTRIC
ARCTOZOLT.types = [ARCTOZOLT.types, ICE]
ARCTOZOLT.abilities = species.abilities(881)
ARCTOZOLT.hidden_ability = species.hidden_ability(881)

#################
### DRACOVISH ###
#################

DRACOVISH = Pokemon()
DRACOVISH.species = 882
DRACOVISH.types = WATER
DRACOVISH.types = [DRACOVISH.types, DRAGON]
DRACOVISH.abilities = species.abilities(882)
DRACOVISH.hidden_ability = species.hidden_ability(882)

#################
### ARCTOVISH ###
#################

ARCTOVISH = Pokemon()
ARCTOVISH.species = 883
ARCTOVISH.types = WATER
ARCTOVISH.types = [ARCTOVISH.types, ICE]
ARCTOVISH.abilities = species.abilities(883)
ARCTOVISH.hidden_ability = species.hidden_ability(883)

#################
### DURALUDON ###
#################

DURALUDON = Pokemon()
DURALUDON.species = 884
DURALUDON.types = STEEL
DURALUDON.types = [DURALUDON.types, DRAGON]
DURALUDON.abilities = species.abilities(884)
DURALUDON.hidden_ability = species.hidden_ability(884)

##############
### DREEPY ###
##############

DREEPY = Pokemon()
DREEPY.species = 885
DREEPY.types = DRAGON
DREEPY.types = [DREEPY.types, GHOST]
DREEPY.abilities = species.abilities(885)
DREEPY.hidden_ability = species.hidden_ability(885)

################
### DRAKLOAK ###
################

DRAKLOAK = Pokemon()
DRAKLOAK.species = 886
DRAKLOAK.types = DRAGON
DRAKLOAK.types = [DRAKLOAK.types, GHOST]
DRAKLOAK.abilities = species.abilities(886)
DRAKLOAK.hidden_ability = species.hidden_ability(886)

#################
### DRAGAPULT ###
#################

DRAGAPULT = Pokemon()
DRAGAPULT.species = 887
DRAGAPULT.types = DRAGON
DRAGAPULT.types = [DRAGAPULT.types, GHOST]
DRAGAPULT.abilities = species.abilities(887)
DRAGAPULT.hidden_ability = species.hidden_ability(887)

##############
### ZACIAN ###
##############

ZACIAN = Pokemon()
ZACIAN.species = 888
ZACIAN.types = FAIRY
ZACIAN.abilities = species.abilities(888)
ZACIAN.hidden_ability = species.hidden_ability(888)

#################
### ZAMAZENTA ###
#################

ZAMAZENTA = Pokemon()
ZAMAZENTA.species = 889
ZAMAZENTA.types = FIGHTING
ZAMAZENTA.abilities = species.abilities(889)
ZAMAZENTA.hidden_ability = species.hidden_ability(889)

#################
### ETERNATUS ###
#################

ETERNATUS = Pokemon()
ETERNATUS.species = 890
ETERNATUS.types = POISON
ETERNATUS.types = [ETERNATUS.types, DRAGON]
ETERNATUS.abilities = species.abilities(890)
ETERNATUS.hidden_ability = species.hidden_ability(890)

ALL_POKEMON = [BULBASAUR,IVYSAUR,VENUSAUR,CHARMANDER,CHARMELEON,CHARIZARD,SQUIRTLE,WARTORTLE,BLASTOISE,CATERPIE,METAPOD,BUTTERFREE,WEEDLE,KAKUNA,BEEDRILL,PIDGEY,PIDGEOTTO,PIDGEOT,RATTATA,RATICATE,SPEAROW,FEAROW,EKANS,ARBOK,PIKACHU,RAICHU,SANDSHREW,SANDSLASH,NIDORANfE,NIDORINA,NIDOQUEEN,NIDORANmA,NIDORINO,NIDOKING,CLEFAIRY,CLEFABLE,VULPIX,NINETALES,JIGGLYPUFF,WIGGLYTUFF,ZUBAT,GOLBAT,ODDISH,GLOOM,VILEPLUME,PARAS,PARASECT,VENONAT,VENOMOTH,DIGLETT,DUGTRIO,MEOWTH,PERSIAN,PSYDUCK,GOLDUCK,MANKEY,PRIMEAPE,GROWLITHE,ARCANINE,POLIWAG,POLIWHIRL,POLIWRATH,ABRA,KADABRA,ALAKAZAM,MACHOP,MACHOKE,MACHAMP,BELLSPROUT,WEEPINBELL,VICTREEBEL,TENTACOOL,TENTACRUEL,GEODUDE,GRAVELER,GOLEM,PONYTA,RAPIDASH,SLOWPOKE,SLOWBRO,MAGNEMITE,MAGNETON,FARFETCHD,DODUO,DODRIO,SEEL,DEWGONG,GRIMER,MUK,SHELLDER,CLOYSTER,GASTLY,HAUNTER,GENGAR,ONIX,DROWZEE,HYPNO,KRABBY,KINGLER,VOLTORB,ELECTRODE,EXEGGCUTE,EXEGGUTOR,CUBONE,MAROWAK,HITMONLEE,HITMONCHAN,LICKITUNG,KOFFING,WEEZING,RHYHORN,RHYDON,CHANSEY,TANGELA,KANGASKHAN,HORSEA,SEADRA,GOLDEEN,SEAKING,STARYU,STARMIE,MRMIME,SCYTHER,JYNX,ELECTABUZZ,MAGMAR,PINSIR,TAUROS,MAGIKARP,GYARADOS,LAPRAS,DITTO,EEVEE,VAPOREON,JOLTEON,FLAREON,PORYGON,OMANYTE,OMASTAR,KABUTO,KABUTOPS,AERODACTYL,SNORLAX,ARTICUNO,ZAPDOS,MOLTRES,DRATINI,DRAGONAIR,DRAGONITE,MEWTWO,MEW,CHIKORITA,BAYLEEF,MEGANIUM,CYNDAQUIL,QUILAVA,TYPHLOSION,TOTODILE,CROCONAW,FERALIGATR,SENTRET,FURRET,HOOTHOOT,NOCTOWL,LEDYBA,LEDIAN,SPINARAK,ARIADOS,CROBAT,CHINCHOU,LANTURN,PICHU,CLEFFA,IGGLYBUFF,TOGEPI,TOGETIC,NATU,XATU,MAREEP,FLAAFFY,AMPHAROS,BELLOSSOM,MARILL,AZUMARILL,SUDOWOODO,POLITOED,HOPPIP,SKIPLOOM,JUMPLUFF,AIPOM,SUNKERN,SUNFLORA,YANMA,WOOPER,QUAGSIRE,ESPEON,UMBREON,MURKROW,SLOWKING,MISDREAVUS,UNOWN,WOBBUFFET,GIRAFARIG,PINECO,FORRETRESS,DUNSPARCE,GLIGAR,STEELIX,SNUBBULL,GRANBULL,QWILFISH,SCIZOR,SHUCKLE,HERACROSS,SNEASEL,TEDDIURSA,URSARING,SLUGMA,MAGCARGO,SWINUB,PILOSWINE,CORSOLA,REMORAID,OCTILLERY,DELIBIRD,MANTINE,SKARMORY,HOUNDOUR,HOUNDOOM,KINGDRA,PHANPY,DONPHAN,PORYGON2,STANTLER,SMEARGLE,TYROGUE,HITMONTOP,SMOOCHUM,ELEKID,MAGBY,MILTANK,BLISSEY,RAIKOU,ENTEI,SUICUNE,LARVITAR,PUPITAR,TYRANITAR,LUGIA,HOOH,CELEBI,TREECKO,GROVYLE,SCEPTILE,TORCHIC,COMBUSKEN,BLAZIKEN,MUDKIP,MARSHTOMP,SWAMPERT,POOCHYENA,MIGHTYENA,ZIGZAGOON,LINOONE,WURMPLE,SILCOON,BEAUTIFLY,CASCOON,DUSTOX,LOTAD,LOMBRE,LUDICOLO,SEEDOT,NUZLEAF,SHIFTRY,TAILLOW,SWELLOW,WINGULL,PELIPPER,RALTS,KIRLIA,GARDEVOIR,SURSKIT,MASQUERAIN,SHROOMISH,BRELOOM,SLAKOTH,VIGOROTH,SLAKING,NINCADA,NINJASK,SHEDINJA,WHISMUR,LOUDRED,EXPLOUD,MAKUHITA,HARIYAMA,AZURILL,NOSEPASS,SKITTY,DELCATTY,SABLEYE,MAWILE,ARON,LAIRON,AGGRON,MEDITITE,MEDICHAM,ELECTRIKE,MANECTRIC,PLUSLE,MINUN,VOLBEAT,ILLUMISE,ROSELIA,GULPIN,SWALOT,CARVANHA,SHARPEDO,WAILMER,WAILORD,NUMEL,CAMERUPT,TORKOAL,SPOINK,GRUMPIG,SPINDA,TRAPINCH,VIBRAVA,FLYGON,CACNEA,CACTURNE,SWABLU,ALTARIA,ZANGOOSE,SEVIPER,LUNATONE,SOLROCK,BARBOACH,WHISCASH,CORPHISH,CRAWDAUNT,BALTOY,CLAYDOL,LILEEP,CRADILY,ANORITH,ARMALDO,FEEBAS,MILOTIC,CASTFORM,KECLEON,SHUPPET,BANETTE,DUSKULL,DUSCLOPS,TROPIUS,CHIMECHO,ABSOL,WYNAUT,SNORUNT,GLALIE,SPHEAL,SEALEO,WALREIN,CLAMPERL,HUNTAIL,GOREBYSS,RELICANTH,LUVDISC,BAGON,SHELGON,SALAMENCE,BELDUM,METANG,METAGROSS,REGIROCK,REGICE,REGISTEEL,LATIAS,LATIOS,KYOGRE,GROUDON,RAYQUAZA,JIRACHI,DEOXYS,TURTWIG,GROTLE,TORTERRA,CHIMCHAR,MONFERNO,INFERNAPE,PIPLUP,PRINPLUP,EMPOLEON,STARLY,STARAVIA,STARAPTOR,BIDOOF,BIBAREL,KRICKETOT,KRICKETUNE,SHINX,LUXIO,LUXRAY,BUDEW,ROSERADE,CRANIDOS,RAMPARDOS,SHIELDON,BASTIODON,BURMY,WORMADAM,MOTHIM,COMBEE,VESPIQUEN,PACHIRISU,BUIZEL,FLOATZEL,CHERUBI,CHERRIM,SHELLOS,GASTRODON,AMBIPOM,DRIFLOON,DRIFBLIM,BUNEARY,LOPUNNY,MISMAGIUS,HONCHKROW,GLAMEOW,PURUGLY,CHINGLING,STUNKY,SKUNTANK,BRONZOR,BRONZONG,BONSLY,MIMEJR,HAPPINY,CHATOT,SPIRITOMB,GIBLE,GABITE,GARCHOMP,MUNCHLAX,RIOLU,LUCARIO,HIPPOPOTAS,HIPPOWDON,SKORUPI,DRAPION,CROAGUNK,TOXICROAK,CARNIVINE,FINNEON,LUMINEON,MANTYKE,SNOVER,ABOMASNOW,WEAVILE,MAGNEZONE,LICKILICKY,RHYPERIOR,TANGROWTH,ELECTIVIRE,MAGMORTAR,TOGEKISS,YANMEGA,LEAFEON,GLACEON,GLISCOR,MAMOSWINE,PORYGONZ,GALLADE,PROBOPASS,DUSKNOIR,FROSLASS,ROTOM,UXIE,MESPRIT,AZELF,DIALGA,PALKIA,HEATRAN,REGIGIGAS,GIRATINA,CRESSELIA,PHIONE,MANAPHY,DARKRAI,SHAYMIN,ARCEUS,VICTINI,SNIVY,SERVINE,SERPERIOR,TEPIG,PIGNITE,EMBOAR,OSHAWOTT,DEWOTT,SAMUROTT,PATRAT,WATCHOG,LILLIPUP,HERDIER,STOUTLAND,PURRLOIN,LIEPARD,PANSAGE,SIMISAGE,PANSEAR,SIMISEAR,PANPOUR,SIMIPOUR,MUNNA,MUSHARNA,PIDOVE,TRANQUILL,UNFEZANT,BLITZLE,ZEBSTRIKA,ROGGENROLA,BOLDORE,GIGALITH,WOOBAT,SWOOBAT,DRILBUR,EXCADRILL,AUDINO,TIMBURR,GURDURR,CONKELDURR,TYMPOLE,PALPITOAD,SEISMITOAD,THROH,SAWK,SEWADDLE,SWADLOON,LEAVANNY,VENIPEDE,WHIRLIPEDE,SCOLIPEDE,COTTONEE,WHIMSICOTT,PETILIL,LILLIGANT,BASCULIN,SANDILE,KROKOROK,KROOKODILE,DARUMAKA,DARMANITAN,MARACTUS,DWEBBLE,CRUSTLE,SCRAGGY,SCRAFTY,SIGILYPH,YAMASK,COFAGRIGUS,TIRTOUGA,CARRACOSTA,ARCHEN,ARCHEOPS,TRUBBISH,GARBODOR,ZORUA,ZOROARK,MINCCINO,CINCCINO,GOTHITA,GOTHORITA,GOTHITELLE,SOLOSIS,DUOSION,REUNICLUS,DUCKLETT,SWANNA,VANILLITE,VANILLISH,VANILLUXE,DEERLING,SAWSBUCK,EMOLGA,KARRABLAST,ESCAVALIER,FOONGUS,AMOONGUSS,FRILLISH,JELLICENT,ALOMOMOLA,JOLTIK,GALVANTULA,FERROSEED,FERROTHORN,KLINK,KLANG,KLINKLANG,TYNAMO,EELEKTRIK,EELEKTROSS,ELGYEM,BEHEEYEM,LITWICK,LAMPENT,CHANDELURE,AXEW,FRAXURE,HAXORUS,CUBCHOO,BEARTIC,CRYOGONAL,SHELMET,ACCELGOR,STUNFISK,MIENFOO,MIENSHAO,DRUDDIGON,GOLETT,GOLURK,PAWNIARD,BISHARP,BOUFFALANT,RUFFLET,BRAVIARY,VULLABY,MANDIBUZZ,HEATMOR,DURANT,DEINO,ZWEILOUS,HYDREIGON,LARVESTA,VOLCARONA,COBALION,TERRAKION,VIRIZION,TORNADUS,THUNDURUS,RESHIRAM,ZEKROM,LANDORUS,KYUREM,KELDEO,MELOETTA,GENESECT,CHESPIN,QUILLADIN,CHESNAUGHT,FENNEKIN,BRAIXEN,DELPHOX,FROAKIE,FROGADIER,GRENINJA,BUNNELBY,DIGGERSBY,FLETCHLING,FLETCHINDER,TALONFLAME,SCATTERBUG,SPEWPA,VIVILLON,LITLEO,PYROAR,FLABEBE,FLOETTE,FLORGES,SKIDDO,GOGOAT,PANCHAM,PANGORO,FURFROU,ESPURR,MEOWSTIC,HONEDGE,DOUBLADE,AEGISLASH,SPRITZEE,AROMATISSE,SWIRLIX,SLURPUFF,INKAY,MALAMAR,BINACLE,BARBARACLE,SKRELP,DRAGALGE,CLAUNCHER,CLAWITZER,HELIOPTILE,HELIOLISK,TYRUNT,TYRANTRUM,AMAURA,AURORUS,SYLVEON,HAWLUCHA,DEDENNE,CARBINK,GOOMY,SLIGGOO,GOODRA,KLEFKI,PHANTUMP,TREVENANT,PUMPKABOO,GOURGEIST,BERGMITE,AVALUGG,NOIBAT,NOIVERN,XERNEAS,YVELTAL,ZYGARDE,DIANCIE,HOOPA,VOLCANION,ROWLET,DARTRIX,DECIDUEYE,LITTEN,TORRACAT,INCINEROAR,POPPLIO,BRIONNE,PRIMARINA,PIKIPEK,TRUMBEAK,TOUCANNON,YUNGOOS,GUMSHOOS,GRUBBIN,CHARJABUG,VIKAVOLT,CRABRAWLER,CRABOMINABLE,ORICORIO,CUTIEFLY,RIBOMBEE,ROCKRUFF,LYCANROC,WISHIWASHI,MAREANIE,TOXAPEX,MUDBRAY,MUDSDALE,DEWPIDER,ARAQUANID,FOMANTIS,LURANTIS,MORELULL,SHIINOTIC,SALANDIT,SALAZZLE,STUFFUL,BEWEAR,BOUNSWEET,STEENEE,TSAREENA,COMFEY,ORANGURU,PASSIMIAN,WIMPOD,GOLISOPOD,SANDYGAST,PALOSSAND,PYUKUMUKU,TYPENULL,SILVALLY,MINIOR,KOMALA,TURTONATOR,TOGEDEMARU,MIMIKYU,BRUXISH,DRAMPA,DHELMISE,JANGMOO,HAKAMOO,KOMMOO,TAPUKOKO,TAPULELE,TAPUBULU,TAPUFINI,COSMOG,COSMOEM,SOLGALEO,LUNALA,NIHILEGO,BUZZWOLE,PHEROMOSA,XURKITREE,CELESTEELA,KARTANA,GUZZLORD,NECROZMA,MAGEARNA,MARSHADOW,POIPOLE,NAGANADEL,STAKATAKA,BLACEPHALON,ZERAORA,MELTAN,MELMETAL,GROOKEY,THWACKEY,RILLABOOM,SCORBUNNY,RABOOT,CINDERACE,SOBBLE,DRIZZILE,INTELEON,SKWOVET,GREEDENT,ROOKIDEE,CORVISQUIRE,CORVIKNIGHT,BLIPBUG,DOTTLER,ORBEETLE,NICKIT,THIEVUL,GOSSIFLEUR,ELDEGOSS,WOOLOO,DUBWOOL,CHEWTLE,DREDNAW,YAMPER,BOLTUND,ROLYCOLY,CARKOL,COALOSSAL,APPLIN,FLAPPLE,APPLETUN,SILICOBRA,SANDACONDA,CRAMORANT,ARROKUDA,BARRASKEWDA,TOXEL,TOXTRICITY,SIZZLIPEDE,CENTISKORCH,CLOBBOPUS,GRAPPLOCT,SINISTEA,POLTEAGEIST,HATENNA,HATTREM,HATTERENE,IMPIDIMP,MORGREM,GRIMMSNARL,OBSTAGOON,PERRSERKER,CURSOLA,SIRFETCHD,MRRIME,RUNERIGUS,MILCERY,ALCREMIE,FALINKS,PINCHURCHIN,SNOM,FROSMOTH,STONJOURNER,EISCUE,INDEEDEE,MORPEKO,CUFANT,COPPERAJAH,DRACOZOLT,ARCTOZOLT,DRACOVISH,ARCTOVISH,DURALUDON,DREEPY,DRAKLOAK,DRAGAPULT,ZACIAN,ZAMAZENTA,ETERNATUS]

