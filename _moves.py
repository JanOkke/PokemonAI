from move import Move
from _types import *
from category import *

################
### MEGAHORN ###
################

MEGAHORN = Move()
MEGAHORN.name = "Megahorn"
MEGAHORN.type = BUG
MEGAHORN.base_damage = 120
MEGAHORN.category = PHYSICAL
MEGAHORN.pp = 10
MEGAHORN.accuracy = 85
MEGAHORN.priority = 0
MEGAHORN.target = 'NearOther'
MEGAHORN.additional_effect_chance = 0
MEGAHORN.description = "Using its tough and impressive horn, the user rams into the target with no letup."

###################
### ATTACKORDER ###
###################

ATTACKORDER = Move()
ATTACKORDER.name = "Attack Order"
ATTACKORDER.type = BUG
ATTACKORDER.base_damage = 90
ATTACKORDER.category = PHYSICAL
ATTACKORDER.pp = 15
ATTACKORDER.accuracy = 100
ATTACKORDER.priority = 0
ATTACKORDER.target = 'NearOther'
ATTACKORDER.additional_effect_chance = 0
ATTACKORDER.description = "The user calls out its underlings to pummel the target. Critical hits land more easily."

###############
### BUGBUZZ ###
###############

BUGBUZZ = Move()
BUGBUZZ.name = "Bug Buzz"
BUGBUZZ.type = BUG
BUGBUZZ.base_damage = 90
BUGBUZZ.category = SPECIAL
BUGBUZZ.pp = 10
BUGBUZZ.accuracy = 100
BUGBUZZ.priority = 0
BUGBUZZ.target = 'NearOther'
BUGBUZZ.additional_effect_chance = 10
BUGBUZZ.description = "The user vibrates its wings to generate a damaging sound wave. It may also lower the targets Sp. Def stat."

#######################
### FIRSTIMPRESSION ###
#######################

FIRSTIMPRESSION = Move()
FIRSTIMPRESSION.name = "First Impression"
FIRSTIMPRESSION.type = BUG
FIRSTIMPRESSION.base_damage = 90
FIRSTIMPRESSION.category = PHYSICAL
FIRSTIMPRESSION.pp = 10
FIRSTIMPRESSION.accuracy = 100
FIRSTIMPRESSION.priority = 2
FIRSTIMPRESSION.target = 'NearOther'
FIRSTIMPRESSION.additional_effect_chance = 0
FIRSTIMPRESSION.description = "Although this move has great power, it only works the first turn the user is in battle."

##################
### POLLENPUFF ###
##################

POLLENPUFF = Move()
POLLENPUFF.name = "Pollen Puff"
POLLENPUFF.type = BUG
POLLENPUFF.base_damage = 90
POLLENPUFF.category = SPECIAL
POLLENPUFF.pp = 15
POLLENPUFF.accuracy = 100
POLLENPUFF.priority = 0
POLLENPUFF.target = 'NearOther'
POLLENPUFF.additional_effect_chance = 0
POLLENPUFF.description = "Fires an exploding pollen puff at enemies, or a HP-restoring one at allies."

#################
### LEECHLIFE ###
#################

LEECHLIFE = Move()
LEECHLIFE.name = "Leech Life"
LEECHLIFE.type = BUG
LEECHLIFE.base_damage = 80
LEECHLIFE.category = PHYSICAL
LEECHLIFE.pp = 10
LEECHLIFE.accuracy = 100
LEECHLIFE.priority = 0
LEECHLIFE.target = 'NearOther'
LEECHLIFE.additional_effect_chance = 0
LEECHLIFE.description = "The user drains the targets blood. The users HP is restored by half the damage taken by the target."

#############
### LUNGE ###
#############

LUNGE = Move()
LUNGE.name = "Lunge"
LUNGE.type = BUG
LUNGE.base_damage = 80
LUNGE.category = PHYSICAL
LUNGE.pp = 15
LUNGE.accuracy = 100
LUNGE.priority = 0
LUNGE.target = 'NearOther'
LUNGE.additional_effect_chance = 100
LUNGE.description = "The user makes a lunge at the target, attacking with full force. This lowers the targets Attack stat."

################
### XSCISSOR ###
################

XSCISSOR = Move()
XSCISSOR.name = "X-Scissor"
XSCISSOR.type = BUG
XSCISSOR.base_damage = 80
XSCISSOR.category = PHYSICAL
XSCISSOR.pp = 15
XSCISSOR.accuracy = 100
XSCISSOR.priority = 0
XSCISSOR.target = 'NearOther'
XSCISSOR.additional_effect_chance = 0
XSCISSOR.description = "The user slashes at the foe by crossing its scythes or claws as if they were a pair of scissors."

##################
### SIGNALBEAM ###
##################

SIGNALBEAM = Move()
SIGNALBEAM.name = "Signal Beam"
SIGNALBEAM.type = BUG
SIGNALBEAM.base_damage = 75
SIGNALBEAM.category = SPECIAL
SIGNALBEAM.pp = 15
SIGNALBEAM.accuracy = 100
SIGNALBEAM.priority = 0
SIGNALBEAM.target = 'NearOther'
SIGNALBEAM.additional_effect_chance = 10
SIGNALBEAM.description = "The user attacks with a sinister beam of light. It may also confuse the target."

#############
### UTURN ###
#############

UTURN = Move()
UTURN.name = "U-turn"
UTURN.type = BUG
UTURN.base_damage = 70
UTURN.category = PHYSICAL
UTURN.pp = 20
UTURN.accuracy = 100
UTURN.priority = 0
UTURN.target = 'NearOther'
UTURN.additional_effect_chance = 0
UTURN.description = "After making its attack, the user rushes back to switch places with a party Pokémon in waiting."

###################
### STEAMROLLER ###
###################

STEAMROLLER = Move()
STEAMROLLER.name = "Steamroller"
STEAMROLLER.type = BUG
STEAMROLLER.base_damage = 65
STEAMROLLER.category = PHYSICAL
STEAMROLLER.pp = 20
STEAMROLLER.accuracy = 100
STEAMROLLER.priority = 0
STEAMROLLER.target = 'NearOther'
STEAMROLLER.additional_effect_chance = 30
STEAMROLLER.description = "The user crushes its foes by rolling over them. This attack may make the target flinch."

###############
### BUGBITE ###
###############

BUGBITE = Move()
BUGBITE.name = "Bug Bite"
BUGBITE.type = BUG
BUGBITE.base_damage = 60
BUGBITE.category = PHYSICAL
BUGBITE.pp = 20
BUGBITE.accuracy = 100
BUGBITE.priority = 0
BUGBITE.target = 'NearOther'
BUGBITE.additional_effect_chance = 0
BUGBITE.description = "The user bites the target. If the target is holding a Berry, the user eats it and gains its effect."

##################
### SILVERWIND ###
##################

SILVERWIND = Move()
SILVERWIND.name = "Silver Wind"
SILVERWIND.type = BUG
SILVERWIND.base_damage = 60
SILVERWIND.category = SPECIAL
SILVERWIND.pp = 5
SILVERWIND.accuracy = 100
SILVERWIND.priority = 0
SILVERWIND.target = 'NearOther'
SILVERWIND.additional_effect_chance = 10
SILVERWIND.description = "The foe is attacked with powdery scales blown by wind. It may also raise all the users stats."

###################
### FELLSTINGER ###
###################

FELLSTINGER = Move()
FELLSTINGER.name = "Fell Stinger"
FELLSTINGER.type = BUG
FELLSTINGER.base_damage = 50
FELLSTINGER.category = PHYSICAL
FELLSTINGER.pp = 25
FELLSTINGER.accuracy = 100
FELLSTINGER.priority = 0
FELLSTINGER.target = 'NearOther'
FELLSTINGER.additional_effect_chance = 0
FELLSTINGER.description = "When the user knocks out a target with this move, the users Attack stat rises drastically."

###################
### STRUGGLEBUG ###
###################

STRUGGLEBUG = Move()
STRUGGLEBUG.name = "Struggle Bug"
STRUGGLEBUG.type = BUG
STRUGGLEBUG.base_damage = 50
STRUGGLEBUG.category = SPECIAL
STRUGGLEBUG.pp = 20
STRUGGLEBUG.accuracy = 100
STRUGGLEBUG.priority = 0
STRUGGLEBUG.target = 'AllNearFoes'
STRUGGLEBUG.additional_effect_chance = 100
STRUGGLEBUG.description = "While resisting, the user attacks the opposing Pokémon. The targets Sp. Atk stat is reduced."

##################
### FURYCUTTER ###
##################

FURYCUTTER = Move()
FURYCUTTER.name = "Fury Cutter"
FURYCUTTER.type = BUG
FURYCUTTER.base_damage = 40
FURYCUTTER.category = PHYSICAL
FURYCUTTER.pp = 20
FURYCUTTER.accuracy = 95
FURYCUTTER.priority = 0
FURYCUTTER.target = 'NearOther'
FURYCUTTER.additional_effect_chance = 0
FURYCUTTER.description = "The target is slashed with scythes or claws. Its power increases if it hits in succession."

##################
### PINMISSILE ###
##################

PINMISSILE = Move()
PINMISSILE.name = "Pin Missile"
PINMISSILE.type = BUG
PINMISSILE.base_damage = 25
PINMISSILE.category = PHYSICAL
PINMISSILE.pp = 20
PINMISSILE.accuracy = 95
PINMISSILE.priority = 0
PINMISSILE.target = 'NearOther'
PINMISSILE.additional_effect_chance = 0
PINMISSILE.description = "Sharp spikes are shot at the target in rapid succession. They hit two to five times in a row."

#################
### TWINEEDLE ###
#################

TWINEEDLE = Move()
TWINEEDLE.name = "Twineedle"
TWINEEDLE.type = BUG
TWINEEDLE.base_damage = 25
TWINEEDLE.category = PHYSICAL
TWINEEDLE.pp = 20
TWINEEDLE.accuracy = 100
TWINEEDLE.priority = 0
TWINEEDLE.target = 'NearOther'
TWINEEDLE.additional_effect_chance = 20
TWINEEDLE.description = "The foe is stabbed twice by a pair of stingers. It may also poison the target."

###################
### INFESTATION ###
###################

INFESTATION = Move()
INFESTATION.name = "Infestation"
INFESTATION.type = BUG
INFESTATION.base_damage = 20
INFESTATION.category = SPECIAL
INFESTATION.pp = 20
INFESTATION.accuracy = 100
INFESTATION.priority = 0
INFESTATION.target = 'NearOther'
INFESTATION.additional_effect_chance = 0
INFESTATION.description = "The target is infested and unable to flee for four to five turns."

###################
### DEFENDORDER ###
###################

DEFENDORDER = Move()
DEFENDORDER.name = "Defend Order"
DEFENDORDER.type = BUG
DEFENDORDER.base_damage = 0
DEFENDORDER.category = STATUS
DEFENDORDER.pp = 10
DEFENDORDER.accuracy = 0
DEFENDORDER.priority = 0
DEFENDORDER.target = 'User'
DEFENDORDER.additional_effect_chance = 0
DEFENDORDER.description = "The user calls out its underlings to shield its body, raising its Defense and Sp. Def stats."

#################
### HEALORDER ###
#################

HEALORDER = Move()
HEALORDER.name = "Heal Order"
HEALORDER.type = BUG
HEALORDER.base_damage = 0
HEALORDER.category = STATUS
HEALORDER.pp = 10
HEALORDER.accuracy = 0
HEALORDER.priority = 0
HEALORDER.target = 'User'
HEALORDER.additional_effect_chance = 0
HEALORDER.description = "The user calls out its underlings to heal it. The user regains up to half of its max HP."

##############
### POWDER ###
##############

POWDER = Move()
POWDER.name = "Powder"
POWDER.type = BUG
POWDER.base_damage = 0
POWDER.category = STATUS
POWDER.pp = 20
POWDER.accuracy = 100
POWDER.priority = 0
POWDER.target = 'NearOther'
POWDER.additional_effect_chance = 0
POWDER.description = "The target is covered in a powder that explodes and damages it if it uses a Fire-type move."

###################
### QUIVERDANCE ###
###################

QUIVERDANCE = Move()
QUIVERDANCE.name = "Quiver Dance"
QUIVERDANCE.type = BUG
QUIVERDANCE.base_damage = 0
QUIVERDANCE.category = STATUS
QUIVERDANCE.pp = 20
QUIVERDANCE.accuracy = 0
QUIVERDANCE.priority = 0
QUIVERDANCE.target = 'User'
QUIVERDANCE.additional_effect_chance = 0
QUIVERDANCE.description = "The user performs a beautiful dance. It boosts the users Sp. Atk, Sp. Def, and Speed stats."

##################
### RAGEPOWDER ###
##################

RAGEPOWDER = Move()
RAGEPOWDER.name = "Rage Powder"
RAGEPOWDER.type = BUG
RAGEPOWDER.base_damage = 0
RAGEPOWDER.category = STATUS
RAGEPOWDER.pp = 20
RAGEPOWDER.accuracy = 0
RAGEPOWDER.priority = 2
RAGEPOWDER.target = 'User'
RAGEPOWDER.additional_effect_chance = 0
RAGEPOWDER.description = "The user scatters irritating powder to draw attention to itself. Opponents aim only at the user."

#################
### SPIDERWEB ###
#################

SPIDERWEB = Move()
SPIDERWEB.name = "Spider Web"
SPIDERWEB.type = BUG
SPIDERWEB.base_damage = 0
SPIDERWEB.category = STATUS
SPIDERWEB.pp = 10
SPIDERWEB.accuracy = 0
SPIDERWEB.priority = 0
SPIDERWEB.target = 'NearOther'
SPIDERWEB.additional_effect_chance = 0
SPIDERWEB.description = "The user ensnares the target with thin, gooey silk so it cant flee from battle."

#################
### STICKYWEB ###
#################

STICKYWEB = Move()
STICKYWEB.name = "Sticky Web"
STICKYWEB.type = BUG
STICKYWEB.base_damage = 0
STICKYWEB.category = STATUS
STICKYWEB.pp = 20
STICKYWEB.accuracy = 0
STICKYWEB.priority = 0
STICKYWEB.target = 'FoeSide'
STICKYWEB.additional_effect_chance = 0
STICKYWEB.description = "Weaves a sticky net around the opposing team, which lowers their Speed stats upon switching in."

##################
### STRINGSHOT ###
##################

STRINGSHOT = Move()
STRINGSHOT.name = "String Shot"
STRINGSHOT.type = BUG
STRINGSHOT.base_damage = 0
STRINGSHOT.category = STATUS
STRINGSHOT.pp = 40
STRINGSHOT.accuracy = 95
STRINGSHOT.priority = 0
STRINGSHOT.target = 'AllNearFoes'
STRINGSHOT.additional_effect_chance = 0
STRINGSHOT.description = "The foe is bound with silk blown from the users mouth. This silk reduces the targets Speed."

################
### TAILGLOW ###
################

TAILGLOW = Move()
TAILGLOW.name = "Tail Glow"
TAILGLOW.type = BUG
TAILGLOW.base_damage = 0
TAILGLOW.category = STATUS
TAILGLOW.pp = 20
TAILGLOW.accuracy = 0
TAILGLOW.priority = 0
TAILGLOW.target = 'User'
TAILGLOW.additional_effect_chance = 0
TAILGLOW.description = "The user stares at flashing lights to focus its mind, drastically raising its Sp. Atk stat."

######################
### HYPERSPACEFURY ###
######################

HYPERSPACEFURY = Move()
HYPERSPACEFURY.name = "Hyperspace Fury"
HYPERSPACEFURY.type = DARK
HYPERSPACEFURY.base_damage = 100
HYPERSPACEFURY.category = PHYSICAL
HYPERSPACEFURY.pp = 5
HYPERSPACEFURY.accuracy = 0
HYPERSPACEFURY.priority = 0
HYPERSPACEFURY.target = 'NearOther'
HYPERSPACEFURY.additional_effect_chance = 0
HYPERSPACEFURY.description = "Unleashes a barrage of multi-arm attacks, skipping protections. The users Defense stat falls."

################
### FOULPLAY ###
################

FOULPLAY = Move()
FOULPLAY.name = "Foul Play"
FOULPLAY.type = DARK
FOULPLAY.base_damage = 95
FOULPLAY.category = PHYSICAL
FOULPLAY.pp = 15
FOULPLAY.accuracy = 100
FOULPLAY.priority = 0
FOULPLAY.target = 'NearOther'
FOULPLAY.additional_effect_chance = 0
FOULPLAY.description = "The user turns the foes power against it. It does more damage the higher the targets Attack stat."

#####################
### DARKESTLARIAT ###
#####################

DARKESTLARIAT = Move()
DARKESTLARIAT.name = "Darkest Lariat"
DARKESTLARIAT.type = DARK
DARKESTLARIAT.base_damage = 85
DARKESTLARIAT.category = PHYSICAL
DARKESTLARIAT.pp = 10
DARKESTLARIAT.accuracy = 100
DARKESTLARIAT.priority = 0
DARKESTLARIAT.target = 'NearOther'
DARKESTLARIAT.additional_effect_chance = 0
DARKESTLARIAT.description = "The user swings both arms and hits the target. Ignores the targets stat changes."

#################
### NIGHTDAZE ###
#################

NIGHTDAZE = Move()
NIGHTDAZE.name = "Night Daze"
NIGHTDAZE.type = DARK
NIGHTDAZE.base_damage = 85
NIGHTDAZE.category = SPECIAL
NIGHTDAZE.pp = 10
NIGHTDAZE.accuracy = 95
NIGHTDAZE.priority = 0
NIGHTDAZE.target = 'NearOther'
NIGHTDAZE.additional_effect_chance = 40
NIGHTDAZE.description = "The user lets loose a pitch-black shock wave at its target. It may also lower the targets accuracy."

##############
### CRUNCH ###
##############

CRUNCH = Move()
CRUNCH.name = "Crunch"
CRUNCH.type = DARK
CRUNCH.base_damage = 80
CRUNCH.category = PHYSICAL
CRUNCH.pp = 15
CRUNCH.accuracy = 100
CRUNCH.priority = 0
CRUNCH.target = 'NearOther'
CRUNCH.additional_effect_chance = 20
CRUNCH.description = "The user crunches up the target with sharp fangs. It may also lower the targets Defense stat."

#################
### DARKPULSE ###
#################

DARKPULSE = Move()
DARKPULSE.name = "Dark Pulse"
DARKPULSE.type = DARK
DARKPULSE.base_damage = 80
DARKPULSE.category = SPECIAL
DARKPULSE.pp = 15
DARKPULSE.accuracy = 100
DARKPULSE.priority = 0
DARKPULSE.target = 'Other'
DARKPULSE.additional_effect_chance = 20
DARKPULSE.description = "The user releases a horrible aura imbued with dark thoughts. It may also make the target flinch."

##################
### THROATCHOP ###
##################

THROATCHOP = Move()
THROATCHOP.name = "Throat Chop"
THROATCHOP.type = DARK
THROATCHOP.base_damage = 80
THROATCHOP.category = PHYSICAL
THROATCHOP.pp = 15
THROATCHOP.accuracy = 100
THROATCHOP.priority = 0
THROATCHOP.target = 'NearOther'
THROATCHOP.additional_effect_chance = 100
THROATCHOP.description = "The user attacks the targets throat. The target cannot use sound-based moves for two turns."

##################
### NIGHTSLASH ###
##################

NIGHTSLASH = Move()
NIGHTSLASH.name = "Night Slash"
NIGHTSLASH.type = DARK
NIGHTSLASH.base_damage = 70
NIGHTSLASH.category = PHYSICAL
NIGHTSLASH.pp = 15
NIGHTSLASH.accuracy = 100
NIGHTSLASH.priority = 0
NIGHTSLASH.target = 'NearOther'
NIGHTSLASH.additional_effect_chance = 0
NIGHTSLASH.description = "The user slashes the target the instant an opportunity arises. Critical hits land more easily."

###################
### SUCKERPUNCH ###
###################

SUCKERPUNCH = Move()
SUCKERPUNCH.name = "Sucker Punch"
SUCKERPUNCH.type = DARK
SUCKERPUNCH.base_damage = 70
SUCKERPUNCH.category = PHYSICAL
SUCKERPUNCH.pp = 5
SUCKERPUNCH.accuracy = 100
SUCKERPUNCH.priority = 1
SUCKERPUNCH.target = 'NearOther'
SUCKERPUNCH.additional_effect_chance = 0
SUCKERPUNCH.description = "This move enables the user to attack first. It fails if the target is not readying an attack, however."

################
### KNOCKOFF ###
################

KNOCKOFF = Move()
KNOCKOFF.name = "Knock Off"
KNOCKOFF.type = DARK
KNOCKOFF.base_damage = 65
KNOCKOFF.category = PHYSICAL
KNOCKOFF.pp = 20
KNOCKOFF.accuracy = 100
KNOCKOFF.priority = 0
KNOCKOFF.target = 'NearOther'
KNOCKOFF.additional_effect_chance = 0
KNOCKOFF.description = "The user slaps down the targets held item, preventing that item from being used in the battle."

#################
### ASSURANCE ###
#################

ASSURANCE = Move()
ASSURANCE.name = "Assurance"
ASSURANCE.type = DARK
ASSURANCE.base_damage = 60
ASSURANCE.category = PHYSICAL
ASSURANCE.pp = 10
ASSURANCE.accuracy = 100
ASSURANCE.priority = 0
ASSURANCE.target = 'NearOther'
ASSURANCE.additional_effect_chance = 0
ASSURANCE.description = "If the target has already taken some damage in the same turn, this attacks power is doubled."

############
### BITE ###
############

BITE = Move()
BITE.name = "Bite"
BITE.type = DARK
BITE.base_damage = 60
BITE.category = PHYSICAL
BITE.pp = 25
BITE.accuracy = 100
BITE.priority = 0
BITE.target = 'NearOther'
BITE.additional_effect_chance = 30
BITE.description = "The target is bitten with viciously sharp fangs. It may make the target flinch."

###################
### BRUTALSWING ###
###################

BRUTALSWING = Move()
BRUTALSWING.name = "Brutal Swing"
BRUTALSWING.type = DARK
BRUTALSWING.base_damage = 60
BRUTALSWING.category = PHYSICAL
BRUTALSWING.pp = 20
BRUTALSWING.accuracy = 100
BRUTALSWING.priority = 0
BRUTALSWING.target = 'AllNearOthers'
BRUTALSWING.additional_effect_chance = 0
BRUTALSWING.description = "The user swings its body around violently to inflict damage on everything in its vicinity."

###################
### FEINTATTACK ###
###################

FEINTATTACK = Move()
FEINTATTACK.name = "Feint Attack"
FEINTATTACK.type = DARK
FEINTATTACK.base_damage = 60
FEINTATTACK.category = PHYSICAL
FEINTATTACK.pp = 20
FEINTATTACK.accuracy = 0
FEINTATTACK.priority = 0
FEINTATTACK.target = 'NearOther'
FEINTATTACK.additional_effect_chance = 0
FEINTATTACK.description = "The user draws up to the foe disarmingly, then throws a sucker punch. It hits without fail."

#############
### THIEF ###
#############

THIEF = Move()
THIEF.name = "Thief"
THIEF.type = DARK
THIEF.base_damage = 60
THIEF.category = PHYSICAL
THIEF.pp = 25
THIEF.accuracy = 100
THIEF.priority = 0
THIEF.target = 'NearOther'
THIEF.additional_effect_chance = 0
THIEF.description = "The user attacks and steals the foes held item simultaneously. It cant steal if the user holds an item."

#############
### SNARL ###
#############

SNARL = Move()
SNARL.name = "Snarl"
SNARL.type = DARK
SNARL.base_damage = 55
SNARL.category = SPECIAL
SNARL.pp = 15
SNARL.accuracy = 95
SNARL.priority = 0
SNARL.target = 'AllNearFoes'
SNARL.additional_effect_chance = 100
SNARL.description = "The user yells as if it is ranting about something, making the targets Sp. Atk stat decrease."

###############
### PAYBACK ###
###############

PAYBACK = Move()
PAYBACK.name = "Payback"
PAYBACK.type = DARK
PAYBACK.base_damage = 50
PAYBACK.category = PHYSICAL
PAYBACK.pp = 10
PAYBACK.accuracy = 100
PAYBACK.priority = 0
PAYBACK.target = 'NearOther'
PAYBACK.additional_effect_chance = 0
PAYBACK.description = "If the user moves after the target, this attacks power will be doubled."

###############
### PURSUIT ###
###############

PURSUIT = Move()
PURSUIT.name = "Pursuit"
PURSUIT.type = DARK
PURSUIT.base_damage = 40
PURSUIT.category = PHYSICAL
PURSUIT.pp = 20
PURSUIT.accuracy = 100
PURSUIT.priority = 0
PURSUIT.target = 'NearOther'
PURSUIT.additional_effect_chance = 0
PURSUIT.description = "An attack move that inflicts double damage if used on a target that is switching out of battle."

##############
### BEATUP ###
##############

BEATUP = Move()
BEATUP.name = "Beat Up"
BEATUP.type = DARK
BEATUP.base_damage = 1
BEATUP.category = PHYSICAL
BEATUP.pp = 10
BEATUP.accuracy = 100
BEATUP.priority = 0
BEATUP.target = 'NearOther'
BEATUP.additional_effect_chance = 0
BEATUP.description = "The user gets all the party Pokémon to attack the foe. The more party Pokémon, the more damage."

#############
### FLING ###
#############

FLING = Move()
FLING.name = "Fling"
FLING.type = DARK
FLING.base_damage = 1
FLING.category = PHYSICAL
FLING.pp = 10
FLING.accuracy = 100
FLING.priority = 0
FLING.target = 'NearOther'
FLING.additional_effect_chance = 0
FLING.description = "The user flings its held item at the target to attack. Its power and effects depend on the item."

#################
### POWERTRIP ###
#################

POWERTRIP = Move()
POWERTRIP.name = "Power Trip"
POWERTRIP.type = DARK
POWERTRIP.base_damage = 1
POWERTRIP.category = PHYSICAL
POWERTRIP.pp = 10
POWERTRIP.accuracy = 100
POWERTRIP.priority = 0
POWERTRIP.target = 'NearOther'
POWERTRIP.additional_effect_chance = 0
POWERTRIP.description = "The user boasts of its strength. Power increases the more the users stats are raised."

##################
### PUNISHMENT ###
##################

PUNISHMENT = Move()
PUNISHMENT.name = "Punishment"
PUNISHMENT.type = DARK
PUNISHMENT.base_damage = 1
PUNISHMENT.category = PHYSICAL
PUNISHMENT.pp = 5
PUNISHMENT.accuracy = 100
PUNISHMENT.priority = 0
PUNISHMENT.target = 'NearOther'
PUNISHMENT.additional_effect_chance = 0
PUNISHMENT.description = "This attacks power increases the more the target has powered up with stat changes."

################
### DARKVOID ###
################

DARKVOID = Move()
DARKVOID.name = "Dark Void"
DARKVOID.type = DARK
DARKVOID.base_damage = 0
DARKVOID.category = STATUS
DARKVOID.pp = 10
DARKVOID.accuracy = 50
DARKVOID.priority = 0
DARKVOID.target = 'AllNearFoes'
DARKVOID.additional_effect_chance = 0
DARKVOID.description = "Opposing Pokémon are dragged into a world of total darkness that makes them sleep."

###############
### EMBARGO ###
###############

EMBARGO = Move()
EMBARGO.name = "Embargo"
EMBARGO.type = DARK
EMBARGO.base_damage = 0
EMBARGO.category = STATUS
EMBARGO.pp = 15
EMBARGO.accuracy = 100
EMBARGO.priority = 0
EMBARGO.target = 'NearOther'
EMBARGO.additional_effect_chance = 0
EMBARGO.description = "It prevents the target from using its held item. Its Trainer is also prevented from using items on it."

#################
### FAKETEARS ###
#################

FAKETEARS = Move()
FAKETEARS.name = "Fake Tears"
FAKETEARS.type = DARK
FAKETEARS.base_damage = 0
FAKETEARS.category = STATUS
FAKETEARS.pp = 20
FAKETEARS.accuracy = 100
FAKETEARS.priority = 0
FAKETEARS.target = 'NearOther'
FAKETEARS.additional_effect_chance = 0
FAKETEARS.description = "The user feigns crying to fluster the target, harshly lowering its Sp. Def stat."

###############
### FLATTER ###
###############

FLATTER = Move()
FLATTER.name = "Flatter"
FLATTER.type = DARK
FLATTER.base_damage = 0
FLATTER.category = STATUS
FLATTER.pp = 15
FLATTER.accuracy = 100
FLATTER.priority = 0
FLATTER.target = 'NearOther'
FLATTER.additional_effect_chance = 0
FLATTER.description = "Flattery is used to confuse the target. However, it also raises the targets Sp. Atk stat."

#################
### HONECLAWS ###
#################

HONECLAWS = Move()
HONECLAWS.name = "Hone Claws"
HONECLAWS.type = DARK
HONECLAWS.base_damage = 0
HONECLAWS.category = STATUS
HONECLAWS.pp = 15
HONECLAWS.accuracy = 0
HONECLAWS.priority = 0
HONECLAWS.target = 'User'
HONECLAWS.additional_effect_chance = 0
HONECLAWS.description = "The user sharpens its claws to boost its Attack stat and accuracy."

###############
### MEMENTO ###
###############

MEMENTO = Move()
MEMENTO.name = "Memento"
MEMENTO.type = DARK
MEMENTO.base_damage = 0
MEMENTO.category = STATUS
MEMENTO.pp = 10
MEMENTO.accuracy = 100
MEMENTO.priority = 0
MEMENTO.target = 'NearOther'
MEMENTO.additional_effect_chance = 0
MEMENTO.description = "The user faints when using this move. In return, it harshly lowers the targets Attack and Sp. Atk."

#################
### NASTYPLOT ###
#################

NASTYPLOT = Move()
NASTYPLOT.name = "Nasty Plot"
NASTYPLOT.type = DARK
NASTYPLOT.base_damage = 0
NASTYPLOT.category = STATUS
NASTYPLOT.pp = 20
NASTYPLOT.accuracy = 0
NASTYPLOT.priority = 0
NASTYPLOT.target = 'User'
NASTYPLOT.additional_effect_chance = 0
NASTYPLOT.description = "The user stimulates its brain by thinking bad thoughts. It sharply raises the users Sp. Atk."

###################
### PARTINGSHOT ###
###################

PARTINGSHOT = Move()
PARTINGSHOT.name = "Parting Shot"
PARTINGSHOT.type = DARK
PARTINGSHOT.base_damage = 0
PARTINGSHOT.category = STATUS
PARTINGSHOT.pp = 20
PARTINGSHOT.accuracy = 100
PARTINGSHOT.priority = 0
PARTINGSHOT.target = 'NearOther'
PARTINGSHOT.additional_effect_chance = 0
PARTINGSHOT.description = "With a parting threat, the user lowers the targets Attack and Sp. Atk stats. Then it switches out."

#############
### QUASH ###
#############

QUASH = Move()
QUASH.name = "Quash"
QUASH.type = DARK
QUASH.base_damage = 0
QUASH.category = STATUS
QUASH.pp = 15
QUASH.accuracy = 100
QUASH.priority = 0
QUASH.target = 'NearOther'
QUASH.additional_effect_chance = 0
QUASH.description = "The user suppresses the target and makes its move go last."

##############
### SNATCH ###
##############

SNATCH = Move()
SNATCH.name = "Snatch"
SNATCH.type = DARK
SNATCH.base_damage = 0
SNATCH.category = STATUS
SNATCH.pp = 10
SNATCH.accuracy = 0
SNATCH.priority = 4
SNATCH.target = 'User'
SNATCH.additional_effect_chance = 0
SNATCH.description = "The user steals the effects of any healing or stat-changing move the foe attempts to use."

##################
### SWITCHEROO ###
##################

SWITCHEROO = Move()
SWITCHEROO.name = "Switcheroo"
SWITCHEROO.type = DARK
SWITCHEROO.base_damage = 0
SWITCHEROO.category = STATUS
SWITCHEROO.pp = 10
SWITCHEROO.accuracy = 100
SWITCHEROO.priority = 0
SWITCHEROO.target = 'NearOther'
SWITCHEROO.additional_effect_chance = 0
SWITCHEROO.description = "The user trades held items with the target faster than the eye can follow."

#############
### TAUNT ###
#############

TAUNT = Move()
TAUNT.name = "Taunt"
TAUNT.type = DARK
TAUNT.base_damage = 0
TAUNT.category = STATUS
TAUNT.pp = 20
TAUNT.accuracy = 100
TAUNT.priority = 0
TAUNT.target = 'NearOther'
TAUNT.additional_effect_chance = 0
TAUNT.description = "The target is taunted into a rage that allows it to use only attack moves for three turns."

##################
### TOPSYTURVY ###
##################

TOPSYTURVY = Move()
TOPSYTURVY.name = "Topsy-Turvy"
TOPSYTURVY.type = DARK
TOPSYTURVY.base_damage = 0
TOPSYTURVY.category = STATUS
TOPSYTURVY.pp = 20
TOPSYTURVY.accuracy = 0
TOPSYTURVY.priority = 0
TOPSYTURVY.target = 'NearOther'
TOPSYTURVY.additional_effect_chance = 0
TOPSYTURVY.description = "All stat changes affecting the target turn topsy-turvy and become the opposite of what they were."

###############
### TORMENT ###
###############

TORMENT = Move()
TORMENT.name = "Torment"
TORMENT.type = DARK
TORMENT.base_damage = 0
TORMENT.category = STATUS
TORMENT.pp = 15
TORMENT.accuracy = 100
TORMENT.priority = 0
TORMENT.target = 'NearOther'
TORMENT.additional_effect_chance = 0
TORMENT.description = "The user torments and enrages the foe, making it incapable of using the same move twice in a row."

##################
### ROAROFTIME ###
##################

ROAROFTIME = Move()
ROAROFTIME.name = "Roar of Time"
ROAROFTIME.type = DRAGON
ROAROFTIME.base_damage = 150
ROAROFTIME.category = SPECIAL
ROAROFTIME.pp = 5
ROAROFTIME.accuracy = 90
ROAROFTIME.priority = 0
ROAROFTIME.target = 'NearOther'
ROAROFTIME.additional_effect_chance = 0
ROAROFTIME.description = "The user blasts the target with power that distorts even time. The user must rest on the next turn."

###################
### DRACOMETEOR ###
###################

DRACOMETEOR = Move()
DRACOMETEOR.name = "Draco Meteor"
DRACOMETEOR.type = DRAGON
DRACOMETEOR.base_damage = 130
DRACOMETEOR.category = SPECIAL
DRACOMETEOR.pp = 5
DRACOMETEOR.accuracy = 90
DRACOMETEOR.priority = 0
DRACOMETEOR.target = 'NearOther'
DRACOMETEOR.additional_effect_chance = 0
DRACOMETEOR.description = "Comets are summoned down from the sky. The attacks recoil harshly reduces the users Sp. Atk stat."

###############
### OUTRAGE ###
###############

OUTRAGE = Move()
OUTRAGE.name = "Outrage"
OUTRAGE.type = DRAGON
OUTRAGE.base_damage = 120
OUTRAGE.category = PHYSICAL
OUTRAGE.pp = 10
OUTRAGE.accuracy = 100
OUTRAGE.priority = 0
OUTRAGE.target = 'RandomNearFoe'
OUTRAGE.additional_effect_chance = 0
OUTRAGE.description = "The user rampages and attacks for two to three turns. It then becomes confused, however."

######################
### CLANGINGSCALES ###
######################

CLANGINGSCALES = Move()
CLANGINGSCALES.name = "Clanging Scales"
CLANGINGSCALES.type = DRAGON
CLANGINGSCALES.base_damage = 110
CLANGINGSCALES.category = SPECIAL
CLANGINGSCALES.pp = 5
CLANGINGSCALES.accuracy = 100
CLANGINGSCALES.priority = 0
CLANGINGSCALES.target = 'AllNearFoes'
CLANGINGSCALES.additional_effect_chance = 0
CLANGINGSCALES.description = "The user rubs its scales and makes a huge noise. Also lowers the users Defense stat."

####################
### COREENFORCER ###
####################

COREENFORCER = Move()
COREENFORCER.name = "Core Enforcer"
COREENFORCER.type = DRAGON
COREENFORCER.base_damage = 100
COREENFORCER.category = SPECIAL
COREENFORCER.pp = 10
COREENFORCER.accuracy = 100
COREENFORCER.priority = 0
COREENFORCER.target = 'AllNearFoes'
COREENFORCER.additional_effect_chance = 0
COREENFORCER.description = "If the target has already moved this turn, the effect of its Ability is negated."

##################
### DRAGONRUSH ###
##################

DRAGONRUSH = Move()
DRAGONRUSH.name = "Dragon Rush"
DRAGONRUSH.type = DRAGON
DRAGONRUSH.base_damage = 100
DRAGONRUSH.category = PHYSICAL
DRAGONRUSH.pp = 10
DRAGONRUSH.accuracy = 75
DRAGONRUSH.priority = 0
DRAGONRUSH.target = 'NearOther'
DRAGONRUSH.additional_effect_chance = 20
DRAGONRUSH.description = "The user tackles the foe while exhibiting overwhelming menace. It may also make the target flinch."

###################
### SPACIALREND ###
###################

SPACIALREND = Move()
SPACIALREND.name = "Spacial Rend"
SPACIALREND.type = DRAGON
SPACIALREND.base_damage = 100
SPACIALREND.category = SPECIAL
SPACIALREND.pp = 5
SPACIALREND.accuracy = 95
SPACIALREND.priority = 0
SPACIALREND.target = 'NearOther'
SPACIALREND.additional_effect_chance = 0
SPACIALREND.description = "The user tears the target along with the space around it. Critical hits land more easily."

####################
### DRAGONHAMMER ###
####################

DRAGONHAMMER = Move()
DRAGONHAMMER.name = "Dragon Hammer"
DRAGONHAMMER.type = DRAGON
DRAGONHAMMER.base_damage = 90
DRAGONHAMMER.category = PHYSICAL
DRAGONHAMMER.pp = 15
DRAGONHAMMER.accuracy = 100
DRAGONHAMMER.priority = 0
DRAGONHAMMER.target = 'NearOther'
DRAGONHAMMER.additional_effect_chance = 0
DRAGONHAMMER.description = "The user uses its body like a hammer to attack the target and inflict damage."

###################
### DRAGONPULSE ###
###################

DRAGONPULSE = Move()
DRAGONPULSE.name = "Dragon Pulse"
DRAGONPULSE.type = DRAGON
DRAGONPULSE.base_damage = 85
DRAGONPULSE.category = SPECIAL
DRAGONPULSE.pp = 10
DRAGONPULSE.accuracy = 100
DRAGONPULSE.priority = 0
DRAGONPULSE.target = 'Other'
DRAGONPULSE.additional_effect_chance = 0
DRAGONPULSE.description = "The target is attacked with a shock wave generated by the users gaping mouth."

##################
### DRAGONCLAW ###
##################

DRAGONCLAW = Move()
DRAGONCLAW.name = "Dragon Claw"
DRAGONCLAW.type = DRAGON
DRAGONCLAW.base_damage = 80
DRAGONCLAW.category = PHYSICAL
DRAGONCLAW.pp = 15
DRAGONCLAW.accuracy = 100
DRAGONCLAW.priority = 0
DRAGONCLAW.target = 'NearOther'
DRAGONCLAW.additional_effect_chance = 0
DRAGONCLAW.description = "The user slashes the target with huge, sharp claws."

####################
### DRAGONBREATH ###
####################

DRAGONBREATH = Move()
DRAGONBREATH.name = "Dragon Breath"
DRAGONBREATH.type = DRAGON
DRAGONBREATH.base_damage = 60
DRAGONBREATH.category = SPECIAL
DRAGONBREATH.pp = 20
DRAGONBREATH.accuracy = 100
DRAGONBREATH.priority = 0
DRAGONBREATH.target = 'NearOther'
DRAGONBREATH.additional_effect_chance = 30
DRAGONBREATH.description = "The user exhales a mighty gust that inflicts damage. It may also leave the target with paralysis."

##################
### DRAGONTAIL ###
##################

DRAGONTAIL = Move()
DRAGONTAIL.name = "Dragon Tail"
DRAGONTAIL.type = DRAGON
DRAGONTAIL.base_damage = 60
DRAGONTAIL.category = PHYSICAL
DRAGONTAIL.pp = 10
DRAGONTAIL.accuracy = 90
DRAGONTAIL.priority = -6
DRAGONTAIL.target = 'NearOther'
DRAGONTAIL.additional_effect_chance = 0
DRAGONTAIL.description = "The user knocks away the target and drags out another Pokémon in its party. In the wild, the battle ends."

################
### DUALCHOP ###
################

DUALCHOP = Move()
DUALCHOP.name = "Dual Chop"
DUALCHOP.type = DRAGON
DUALCHOP.base_damage = 40
DUALCHOP.category = PHYSICAL
DUALCHOP.pp = 15
DUALCHOP.accuracy = 90
DUALCHOP.priority = 0
DUALCHOP.target = 'NearOther'
DUALCHOP.additional_effect_chance = 0
DUALCHOP.description = "The user attacks its target by hitting it with brutal strikes. The target is hit twice in a row."

###############
### TWISTER ###
###############

TWISTER = Move()
TWISTER.name = "Twister"
TWISTER.type = DRAGON
TWISTER.base_damage = 40
TWISTER.category = SPECIAL
TWISTER.pp = 20
TWISTER.accuracy = 100
TWISTER.priority = 0
TWISTER.target = 'AllNearFoes'
TWISTER.additional_effect_chance = 20
TWISTER.description = "The user whips up a vicious tornado to tear at the opposing team. It may also make targets flinch."

##################
### DRAGONRAGE ###
##################

DRAGONRAGE = Move()
DRAGONRAGE.name = "Dragon Rage"
DRAGONRAGE.type = DRAGON
DRAGONRAGE.base_damage = 1
DRAGONRAGE.category = SPECIAL
DRAGONRAGE.pp = 10
DRAGONRAGE.accuracy = 100
DRAGONRAGE.priority = 0
DRAGONRAGE.target = 'NearOther'
DRAGONRAGE.additional_effect_chance = 0
DRAGONRAGE.description = "This attack hits the target with a shock wave of pure rage. This attack always inflicts 40 HP damage."

###################
### DRAGONDANCE ###
###################

DRAGONDANCE = Move()
DRAGONDANCE.name = "Dragon Dance"
DRAGONDANCE.type = DRAGON
DRAGONDANCE.base_damage = 0
DRAGONDANCE.category = STATUS
DRAGONDANCE.pp = 20
DRAGONDANCE.accuracy = 0
DRAGONDANCE.priority = 0
DRAGONDANCE.target = 'User'
DRAGONDANCE.additional_effect_chance = 0
DRAGONDANCE.description = "The user vigorously performs a mystic, powerful dance that boosts its Attack and Speed stats."

##################
### BOLTSTRIKE ###
##################

BOLTSTRIKE = Move()
BOLTSTRIKE.name = "Bolt Strike"
BOLTSTRIKE.type = ELECTRIC
BOLTSTRIKE.base_damage = 130
BOLTSTRIKE.category = PHYSICAL
BOLTSTRIKE.pp = 5
BOLTSTRIKE.accuracy = 85
BOLTSTRIKE.priority = 0
BOLTSTRIKE.target = 'NearOther'
BOLTSTRIKE.additional_effect_chance = 20
BOLTSTRIKE.description = "The user charges at its foe, surrounding itself with lightning. It may also leave the target paralyzed."

##################
### VOLTTACKLE ###
##################

VOLTTACKLE = Move()
VOLTTACKLE.name = "Volt Tackle"
VOLTTACKLE.type = ELECTRIC
VOLTTACKLE.base_damage = 120
VOLTTACKLE.category = PHYSICAL
VOLTTACKLE.pp = 15
VOLTTACKLE.accuracy = 100
VOLTTACKLE.priority = 0
VOLTTACKLE.target = 'NearOther'
VOLTTACKLE.additional_effect_chance = 10
VOLTTACKLE.description = "The user electrifies itself, then charges at the foe. It causes considerable damage to the user as well."

#################
### ZAPCANNON ###
#################

ZAPCANNON = Move()
ZAPCANNON.name = "Zap Cannon"
ZAPCANNON.type = ELECTRIC
ZAPCANNON.base_damage = 120
ZAPCANNON.category = SPECIAL
ZAPCANNON.pp = 5
ZAPCANNON.accuracy = 50
ZAPCANNON.priority = 0
ZAPCANNON.target = 'NearOther'
ZAPCANNON.additional_effect_chance = 100
ZAPCANNON.description = "The user fires an electric blast like a cannon to inflict damage and cause paralysis."

###############
### THUNDER ###
###############

THUNDER = Move()
THUNDER.name = "Thunder"
THUNDER.type = ELECTRIC
THUNDER.base_damage = 110
THUNDER.category = SPECIAL
THUNDER.pp = 10
THUNDER.accuracy = 70
THUNDER.priority = 0
THUNDER.target = 'NearOther'
THUNDER.additional_effect_chance = 30
THUNDER.description = "A wicked thunderbolt is dropped on the foe to inflict damage. It may also leave the target paralyzed."

##################
### FUSIONBOLT ###
##################

FUSIONBOLT = Move()
FUSIONBOLT.name = "Fusion Bolt"
FUSIONBOLT.type = ELECTRIC
FUSIONBOLT.base_damage = 100
FUSIONBOLT.category = PHYSICAL
FUSIONBOLT.pp = 5
FUSIONBOLT.accuracy = 100
FUSIONBOLT.priority = 0
FUSIONBOLT.target = 'NearOther'
FUSIONBOLT.additional_effect_chance = 0
FUSIONBOLT.description = "The user throws down a giant thunderbolt. It does more damage if influenced by an enormous flame."

###################
### PLASMAFISTS ###
###################

PLASMAFISTS = Move()
PLASMAFISTS.name = "Plasma Fists"
PLASMAFISTS.type = ELECTRIC
PLASMAFISTS.base_damage = 100
PLASMAFISTS.category = PHYSICAL
PLASMAFISTS.pp = 15
PLASMAFISTS.accuracy = 100
PLASMAFISTS.priority = 0
PLASMAFISTS.target = 'NearOther'
PLASMAFISTS.additional_effect_chance = 0
PLASMAFISTS.description = "The user attacks with electrically charged fists. Normal-type moves become Electric-type."

###################
### THUNDERBOLT ###
###################

THUNDERBOLT = Move()
THUNDERBOLT.name = "Thunderbolt"
THUNDERBOLT.type = ELECTRIC
THUNDERBOLT.base_damage = 90
THUNDERBOLT.category = SPECIAL
THUNDERBOLT.pp = 15
THUNDERBOLT.accuracy = 100
THUNDERBOLT.priority = 0
THUNDERBOLT.target = 'NearOther'
THUNDERBOLT.additional_effect_chance = 10
THUNDERBOLT.description = "A strong electric blast is loosed at the target. It may also leave the target with paralysis."

##################
### WILDCHARGE ###
##################

WILDCHARGE = Move()
WILDCHARGE.name = "Wild Charge"
WILDCHARGE.type = ELECTRIC
WILDCHARGE.base_damage = 90
WILDCHARGE.category = PHYSICAL
WILDCHARGE.pp = 15
WILDCHARGE.accuracy = 100
WILDCHARGE.priority = 0
WILDCHARGE.target = 'NearOther'
WILDCHARGE.additional_effect_chance = 0
WILDCHARGE.description = "The user shrouds itself in electricity and smashes into its foe. It also damages the user a little."

#################
### DISCHARGE ###
#################

DISCHARGE = Move()
DISCHARGE.name = "Discharge"
DISCHARGE.type = ELECTRIC
DISCHARGE.base_damage = 80
DISCHARGE.category = SPECIAL
DISCHARGE.pp = 15
DISCHARGE.accuracy = 100
DISCHARGE.priority = 0
DISCHARGE.target = 'AllNearOthers'
DISCHARGE.additional_effect_chance = 30
DISCHARGE.description = "A flare of electricity is loosed to strike the area around the user. It may also cause paralysis."

###############
### ZINGZAP ###
###############

ZINGZAP = Move()
ZINGZAP.name = "Zing Zap"
ZINGZAP.type = ELECTRIC
ZINGZAP.base_damage = 80
ZINGZAP.category = PHYSICAL
ZINGZAP.pp = 10
ZINGZAP.accuracy = 100
ZINGZAP.priority = 0
ZINGZAP.target = 'NearOther'
ZINGZAP.additional_effect_chance = 30
ZINGZAP.description = "A strong electric blast crashes down on the target. This may also make the target flinch."

####################
### THUNDERPUNCH ###
####################

THUNDERPUNCH = Move()
THUNDERPUNCH.name = "Thunder Punch"
THUNDERPUNCH.type = ELECTRIC
THUNDERPUNCH.base_damage = 75
THUNDERPUNCH.category = PHYSICAL
THUNDERPUNCH.pp = 15
THUNDERPUNCH.accuracy = 100
THUNDERPUNCH.priority = 0
THUNDERPUNCH.target = 'NearOther'
THUNDERPUNCH.additional_effect_chance = 10
THUNDERPUNCH.description = "The target is punched with an electrified fist. It may also leave the target with paralysis."

##################
### VOLTSWITCH ###
##################

VOLTSWITCH = Move()
VOLTSWITCH.name = "Volt Switch"
VOLTSWITCH.type = ELECTRIC
VOLTSWITCH.base_damage = 70
VOLTSWITCH.category = SPECIAL
VOLTSWITCH.pp = 20
VOLTSWITCH.accuracy = 100
VOLTSWITCH.priority = 0
VOLTSWITCH.target = 'NearOther'
VOLTSWITCH.additional_effect_chance = 0
VOLTSWITCH.description = "After making its attack, the user rushes back to switch places with a party Pokémon in waiting."

#######################
### PARABOLICCHARGE ###
#######################

PARABOLICCHARGE = Move()
PARABOLICCHARGE.name = "Parabolic Charge"
PARABOLICCHARGE.type = ELECTRIC
PARABOLICCHARGE.base_damage = 65
PARABOLICCHARGE.category = SPECIAL
PARABOLICCHARGE.pp = 20
PARABOLICCHARGE.accuracy = 100
PARABOLICCHARGE.priority = 0
PARABOLICCHARGE.target = 'AllNearOthers'
PARABOLICCHARGE.additional_effect_chance = 0
PARABOLICCHARGE.description = "The user attacks everything around it. The users HP is restored by half the damage dealt."

#############
### SPARK ###
#############

SPARK = Move()
SPARK.name = "Spark"
SPARK.type = ELECTRIC
SPARK.base_damage = 65
SPARK.category = PHYSICAL
SPARK.pp = 20
SPARK.accuracy = 100
SPARK.priority = 0
SPARK.target = 'NearOther'
SPARK.additional_effect_chance = 30
SPARK.description = "The user throws an electrically charged tackle at the target. It may also leave the target with paralysis."

###################
### THUNDERFANG ###
###################

THUNDERFANG = Move()
THUNDERFANG.name = "Thunder Fang"
THUNDERFANG.type = ELECTRIC
THUNDERFANG.base_damage = 65
THUNDERFANG.category = PHYSICAL
THUNDERFANG.pp = 15
THUNDERFANG.accuracy = 95
THUNDERFANG.priority = 0
THUNDERFANG.target = 'NearOther'
THUNDERFANG.additional_effect_chance = 100
THUNDERFANG.description = "The user bites with electrified fangs. It may also make the target flinch or leave it with paralysis."

#################
### SHOCKWAVE ###
#################

SHOCKWAVE = Move()
SHOCKWAVE.name = "Shock Wave"
SHOCKWAVE.type = ELECTRIC
SHOCKWAVE.base_damage = 60
SHOCKWAVE.category = SPECIAL
SHOCKWAVE.pp = 20
SHOCKWAVE.accuracy = 0
SHOCKWAVE.priority = 0
SHOCKWAVE.target = 'NearOther'
SHOCKWAVE.additional_effect_chance = 0
SHOCKWAVE.description = "The user strikes the target with a quick jolt of electricity. This attack cannot be evaded."

##################
### ELECTROWEB ###
##################

ELECTROWEB = Move()
ELECTROWEB.name = "Electroweb"
ELECTROWEB.type = ELECTRIC
ELECTROWEB.base_damage = 55
ELECTROWEB.category = SPECIAL
ELECTROWEB.pp = 15
ELECTROWEB.accuracy = 95
ELECTROWEB.priority = 0
ELECTROWEB.target = 'AllNearFoes'
ELECTROWEB.additional_effect_chance = 100
ELECTROWEB.description = "The user captures and attacks foes by using an electric net, which lowers their Speed stat."

##################
### CHARGEBEAM ###
##################

CHARGEBEAM = Move()
CHARGEBEAM.name = "Charge Beam"
CHARGEBEAM.type = ELECTRIC
CHARGEBEAM.base_damage = 50
CHARGEBEAM.category = SPECIAL
CHARGEBEAM.pp = 10
CHARGEBEAM.accuracy = 90
CHARGEBEAM.priority = 0
CHARGEBEAM.target = 'NearOther'
CHARGEBEAM.additional_effect_chance = 70
CHARGEBEAM.description = "The user fires a concentrated bundle of electricity. It may also raise the users Sp. Atk stat."

####################
### THUNDERSHOCK ###
####################

THUNDERSHOCK = Move()
THUNDERSHOCK.name = "Thunder Shock"
THUNDERSHOCK.type = ELECTRIC
THUNDERSHOCK.base_damage = 40
THUNDERSHOCK.category = SPECIAL
THUNDERSHOCK.pp = 30
THUNDERSHOCK.accuracy = 100
THUNDERSHOCK.priority = 0
THUNDERSHOCK.target = 'NearOther'
THUNDERSHOCK.additional_effect_chance = 10
THUNDERSHOCK.description = "A jolt of electricity is hurled at the foe to inflict damage. It may also leave the target with paralysis."

##############
### NUZZLE ###
##############

NUZZLE = Move()
NUZZLE.name = "Nuzzle"
NUZZLE.type = ELECTRIC
NUZZLE.base_damage = 20
NUZZLE.category = PHYSICAL
NUZZLE.pp = 20
NUZZLE.accuracy = 100
NUZZLE.priority = 0
NUZZLE.target = 'NearOther'
NUZZLE.additional_effect_chance = 100
NUZZLE.description = "The user nuzzles its electrified cheeks against the target. This also leaves the target with paralysis."

###################
### ELECTROBALL ###
###################

ELECTROBALL = Move()
ELECTROBALL.name = "Electro Ball"
ELECTROBALL.type = ELECTRIC
ELECTROBALL.base_damage = 1
ELECTROBALL.category = SPECIAL
ELECTROBALL.pp = 10
ELECTROBALL.accuracy = 100
ELECTROBALL.priority = 0
ELECTROBALL.target = 'NearOther'
ELECTROBALL.additional_effect_chance = 0
ELECTROBALL.description = "The user hurls an electric orb at the foe. It does more damage the faster the user is."

##############
### CHARGE ###
##############

CHARGE = Move()
CHARGE.name = "Charge"
CHARGE.type = ELECTRIC
CHARGE.base_damage = 0
CHARGE.category = STATUS
CHARGE.pp = 20
CHARGE.accuracy = 0
CHARGE.priority = 0
CHARGE.target = 'User'
CHARGE.additional_effect_chance = 0
CHARGE.description = "The user boosts the power of the Electric move it uses next. It also raises the users Sp. Def stat."

####################
### EERIEIMPULSE ###
####################

EERIEIMPULSE = Move()
EERIEIMPULSE.name = "Eerie Impulse"
EERIEIMPULSE.type = ELECTRIC
EERIEIMPULSE.base_damage = 0
EERIEIMPULSE.category = STATUS
EERIEIMPULSE.pp = 15
EERIEIMPULSE.accuracy = 100
EERIEIMPULSE.priority = 0
EERIEIMPULSE.target = 'NearOther'
EERIEIMPULSE.additional_effect_chance = 0
EERIEIMPULSE.description = "The users body generates an eerie impulse. Harshly lowers the targets Sp. Atk stat."

#######################
### ELECTRICTERRAIN ###
#######################

ELECTRICTERRAIN = Move()
ELECTRICTERRAIN.name = "Electric Terrain"
ELECTRICTERRAIN.type = ELECTRIC
ELECTRICTERRAIN.base_damage = 0
ELECTRICTERRAIN.category = STATUS
ELECTRICTERRAIN.pp = 10
ELECTRICTERRAIN.accuracy = 0
ELECTRICTERRAIN.priority = 0
ELECTRICTERRAIN.target = 'BothSides'
ELECTRICTERRAIN.additional_effect_chance = 0
ELECTRICTERRAIN.description = "The user electrifies the ground for five turns. Pokémon on the ground no longer fall asleep."

#################
### ELECTRIFY ###
#################

ELECTRIFY = Move()
ELECTRIFY.name = "Electrify"
ELECTRIFY.type = ELECTRIC
ELECTRIFY.base_damage = 0
ELECTRIFY.category = STATUS
ELECTRIFY.pp = 20
ELECTRIFY.accuracy = 0
ELECTRIFY.priority = 0
ELECTRIFY.target = 'NearOther'
ELECTRIFY.additional_effect_chance = 0
ELECTRIFY.description = "If the target uses a move after being electrified, that move becomes Electric-type."

#################
### IONDELUGE ###
#################

IONDELUGE = Move()
IONDELUGE.name = "Ion Deluge"
IONDELUGE.type = ELECTRIC
IONDELUGE.base_damage = 0
IONDELUGE.category = STATUS
IONDELUGE.pp = 25
IONDELUGE.accuracy = 0
IONDELUGE.priority = 1
IONDELUGE.target = 'BothSides'
IONDELUGE.additional_effect_chance = 0
IONDELUGE.description = "The user disperses electrically charged particles. Normal-type moves become Electric-type."

##################
### MAGNETRISE ###
##################

MAGNETRISE = Move()
MAGNETRISE.name = "Magnet Rise"
MAGNETRISE.type = ELECTRIC
MAGNETRISE.base_damage = 0
MAGNETRISE.category = STATUS
MAGNETRISE.pp = 10
MAGNETRISE.accuracy = 0
MAGNETRISE.priority = 0
MAGNETRISE.target = 'User'
MAGNETRISE.additional_effect_chance = 0
MAGNETRISE.description = "The user levitates using electrically generated magnetism for five turns."

####################
### MAGNETICFLUX ###
####################

MAGNETICFLUX = Move()
MAGNETICFLUX.name = "Magnetic Flux"
MAGNETICFLUX.type = ELECTRIC
MAGNETICFLUX.base_damage = 0
MAGNETICFLUX.category = STATUS
MAGNETICFLUX.pp = 20
MAGNETICFLUX.accuracy = 0
MAGNETICFLUX.priority = 0
MAGNETICFLUX.target = 'UserAndAllies'
MAGNETICFLUX.additional_effect_chance = 0
MAGNETICFLUX.description = "Manipulates magnetic fields to raise the Defense and Sp. Def stats of allies with Plus or Minus Abilities."

###################
### THUNDERWAVE ###
###################

THUNDERWAVE = Move()
THUNDERWAVE.name = "Thunder Wave"
THUNDERWAVE.type = ELECTRIC
THUNDERWAVE.base_damage = 0
THUNDERWAVE.category = STATUS
THUNDERWAVE.pp = 20
THUNDERWAVE.accuracy = 90
THUNDERWAVE.priority = 0
THUNDERWAVE.target = 'NearOther'
THUNDERWAVE.additional_effect_chance = 0
THUNDERWAVE.description = "A weak electric charge is launched at the target. It causes paralysis if it hits."

###################
### LIGHTOFRUIN ###
###################

LIGHTOFRUIN = Move()
LIGHTOFRUIN.name = "Light of Ruin"
LIGHTOFRUIN.type = FAIRY
LIGHTOFRUIN.base_damage = 140
LIGHTOFRUIN.category = SPECIAL
LIGHTOFRUIN.pp = 5
LIGHTOFRUIN.accuracy = 90
LIGHTOFRUIN.priority = 0
LIGHTOFRUIN.target = 'NearOther'
LIGHTOFRUIN.additional_effect_chance = 0
LIGHTOFRUIN.description = "Fires a powerful beam of light drawn from the Eternal Flower. It also damages the user a lot."

###################
### FLEURCANNON ###
###################

FLEURCANNON = Move()
FLEURCANNON.name = "Fleur Cannon"
FLEURCANNON.type = FAIRY
FLEURCANNON.base_damage = 130
FLEURCANNON.category = SPECIAL
FLEURCANNON.pp = 5
FLEURCANNON.accuracy = 90
FLEURCANNON.priority = 0
FLEURCANNON.target = 'NearOther'
FLEURCANNON.additional_effect_chance = 0
FLEURCANNON.description = "The user unleashes a strong beam. The attacks recoil harshly lowers the users Sp. Atk stat."

#################
### MOONBLAST ###
#################

MOONBLAST = Move()
MOONBLAST.name = "Moonblast"
MOONBLAST.type = FAIRY
MOONBLAST.base_damage = 95
MOONBLAST.category = SPECIAL
MOONBLAST.pp = 15
MOONBLAST.accuracy = 100
MOONBLAST.priority = 0
MOONBLAST.target = 'NearOther'
MOONBLAST.additional_effect_chance = 30
MOONBLAST.description = "The user attacks by borrowing the power of the moon. This may also lower the targets Sp. Atk stat."

#################
### PLAYROUGH ###
#################

PLAYROUGH = Move()
PLAYROUGH.name = "Play Rough"
PLAYROUGH.type = FAIRY
PLAYROUGH.base_damage = 90
PLAYROUGH.category = PHYSICAL
PLAYROUGH.pp = 10
PLAYROUGH.accuracy = 90
PLAYROUGH.priority = 0
PLAYROUGH.target = 'NearOther'
PLAYROUGH.additional_effect_chance = 10
PLAYROUGH.description = "The user plays rough with the target and attacks it. This may also lower the targets Attack stat."

#####################
### DAZZLINGGLEAM ###
#####################

DAZZLINGGLEAM = Move()
DAZZLINGGLEAM.name = "Dazzling Gleam"
DAZZLINGGLEAM.type = FAIRY
DAZZLINGGLEAM.base_damage = 80
DAZZLINGGLEAM.category = SPECIAL
DAZZLINGGLEAM.pp = 10
DAZZLINGGLEAM.accuracy = 100
DAZZLINGGLEAM.priority = 0
DAZZLINGGLEAM.target = 'AllNearFoes'
DAZZLINGGLEAM.additional_effect_chance = 0
DAZZLINGGLEAM.description = "The user damages opposing Pokémon by emitting a powerful flash."

####################
### DRAININGKISS ###
####################

DRAININGKISS = Move()
DRAININGKISS.name = "Draining Kiss"
DRAININGKISS.type = FAIRY
DRAININGKISS.base_damage = 50
DRAININGKISS.category = SPECIAL
DRAININGKISS.pp = 10
DRAININGKISS.accuracy = 100
DRAININGKISS.priority = 0
DRAININGKISS.target = 'NearOther'
DRAININGKISS.additional_effect_chance = 0
DRAININGKISS.description = "The user steals the targets HP with a kiss. The users HP is restored by over half of the damage dealt."

######################
### DISARMINGVOICE ###
######################

DISARMINGVOICE = Move()
DISARMINGVOICE.name = "Disarming Voice"
DISARMINGVOICE.type = FAIRY
DISARMINGVOICE.base_damage = 40
DISARMINGVOICE.category = SPECIAL
DISARMINGVOICE.pp = 15
DISARMINGVOICE.accuracy = 0
DISARMINGVOICE.priority = 0
DISARMINGVOICE.target = 'AllNearFoes'
DISARMINGVOICE.additional_effect_chance = 0
DISARMINGVOICE.description = "Letting out a charming cry, the user does emotional damage to foes. This attack never misses."

#################
### FAIRYWIND ###
#################

FAIRYWIND = Move()
FAIRYWIND.name = "Fairy Wind"
FAIRYWIND.type = FAIRY
FAIRYWIND.base_damage = 40
FAIRYWIND.category = SPECIAL
FAIRYWIND.pp = 30
FAIRYWIND.accuracy = 100
FAIRYWIND.priority = 0
FAIRYWIND.target = 'NearOther'
FAIRYWIND.additional_effect_chance = 0
FAIRYWIND.description = "The user stirs up a fairy wind and strikes the target with it."

####################
### AROMATICMIST ###
####################

AROMATICMIST = Move()
AROMATICMIST.name = "Aromatic Mist"
AROMATICMIST.type = FAIRY
AROMATICMIST.base_damage = 0
AROMATICMIST.category = STATUS
AROMATICMIST.pp = 20
AROMATICMIST.accuracy = 0
AROMATICMIST.priority = 0
AROMATICMIST.target = 'NearAlly'
AROMATICMIST.additional_effect_chance = 0
AROMATICMIST.description = "The user raises the Sp. Def stat of an ally Pokémon by using a mysterious aroma."

####################
### BABYDOLLEYES ###
####################

BABYDOLLEYES = Move()
BABYDOLLEYES.name = "Baby-Doll Eyes"
BABYDOLLEYES.type = FAIRY
BABYDOLLEYES.base_damage = 0
BABYDOLLEYES.category = STATUS
BABYDOLLEYES.pp = 30
BABYDOLLEYES.accuracy = 100
BABYDOLLEYES.priority = 1
BABYDOLLEYES.target = 'NearOther'
BABYDOLLEYES.additional_effect_chance = 0
BABYDOLLEYES.description = "The user stares with its baby-doll eyes, which lowers the targets Attack stat. Always goes first."

#############
### CHARM ###
#############

CHARM = Move()
CHARM.name = "Charm"
CHARM.type = FAIRY
CHARM.base_damage = 0
CHARM.category = STATUS
CHARM.pp = 20
CHARM.accuracy = 100
CHARM.priority = 0
CHARM.target = 'NearOther'
CHARM.additional_effect_chance = 0
CHARM.description = "The user charmingly gazes at the foe, making it less wary. The targets Attack is harshly lowered."

####################
### CRAFTYSHIELD ###
####################

CRAFTYSHIELD = Move()
CRAFTYSHIELD.name = "Crafty Shield"
CRAFTYSHIELD.type = FAIRY
CRAFTYSHIELD.base_damage = 0
CRAFTYSHIELD.category = STATUS
CRAFTYSHIELD.pp = 10
CRAFTYSHIELD.accuracy = 0
CRAFTYSHIELD.priority = 3
CRAFTYSHIELD.target = 'UserSide'
CRAFTYSHIELD.additional_effect_chance = 0
CRAFTYSHIELD.description = "The user protects itself and its allies from status moves with a mysterious power."

#################
### FAIRYLOCK ###
#################

FAIRYLOCK = Move()
FAIRYLOCK.name = "Fairy Lock"
FAIRYLOCK.type = FAIRY
FAIRYLOCK.base_damage = 0
FAIRYLOCK.category = STATUS
FAIRYLOCK.pp = 10
FAIRYLOCK.accuracy = 0
FAIRYLOCK.priority = 0
FAIRYLOCK.target = 'BothSides'
FAIRYLOCK.additional_effect_chance = 0
FAIRYLOCK.description = "By locking down the battlefield, the user keeps all Pokémon from fleeing during the next turn."

#####################
### FLORALHEALING ###
#####################

FLORALHEALING = Move()
FLORALHEALING.name = "Floral Healing"
FLORALHEALING.type = FAIRY
FLORALHEALING.base_damage = 0
FLORALHEALING.category = STATUS
FLORALHEALING.pp = 10
FLORALHEALING.accuracy = 0
FLORALHEALING.priority = 0
FLORALHEALING.target = 'NearOther'
FLORALHEALING.additional_effect_chance = 0
FLORALHEALING.description = "The user restores the targets HP by up to half of its max HP. It restores more HP when the terrain is grass."

####################
### FLOWERSHIELD ###
####################

FLOWERSHIELD = Move()
FLOWERSHIELD.name = "Flower Shield"
FLOWERSHIELD.type = FAIRY
FLOWERSHIELD.base_damage = 0
FLOWERSHIELD.category = STATUS
FLOWERSHIELD.pp = 10
FLOWERSHIELD.accuracy = 0
FLOWERSHIELD.priority = 0
FLOWERSHIELD.target = 'AllBattlers'
FLOWERSHIELD.additional_effect_chance = 0
FLOWERSHIELD.description = "The user raises the Defense stats of all Grass-type Pokémon in battle with a mysterious power."

################
### GEOMANCY ###
################

GEOMANCY = Move()
GEOMANCY.name = "Geomancy"
GEOMANCY.type = FAIRY
GEOMANCY.base_damage = 0
GEOMANCY.category = STATUS
GEOMANCY.pp = 10
GEOMANCY.accuracy = 0
GEOMANCY.priority = 0
GEOMANCY.target = 'User'
GEOMANCY.additional_effect_chance = 0
GEOMANCY.description = "The user absorbs energy and sharply raises its Sp. Atk, Sp. Def, and Speed stats on the next turn."

####################
### MISTYTERRAIN ###
####################

MISTYTERRAIN = Move()
MISTYTERRAIN.name = "Misty Terrain"
MISTYTERRAIN.type = FAIRY
MISTYTERRAIN.base_damage = 0
MISTYTERRAIN.category = STATUS
MISTYTERRAIN.pp = 10
MISTYTERRAIN.accuracy = 0
MISTYTERRAIN.priority = 0
MISTYTERRAIN.target = 'BothSides'
MISTYTERRAIN.additional_effect_chance = 0
MISTYTERRAIN.description = "The user covers the ground with mist for five turns. Grounded Pokémon cant gain status conditions."

#################
### MOONLIGHT ###
#################

MOONLIGHT = Move()
MOONLIGHT.name = "Moonlight"
MOONLIGHT.type = FAIRY
MOONLIGHT.base_damage = 0
MOONLIGHT.category = STATUS
MOONLIGHT.pp = 5
MOONLIGHT.accuracy = 0
MOONLIGHT.priority = 0
MOONLIGHT.target = 'User'
MOONLIGHT.additional_effect_chance = 0
MOONLIGHT.description = "The user restores its own HP. The amount of HP regained varies with the weather."

######################
### NATURESMADNESS ###
######################

NATURESMADNESS = Move()
NATURESMADNESS.name = "Nature's Madness"
NATURESMADNESS.type = FAIRY
NATURESMADNESS.base_damage = 0
NATURESMADNESS.category = STATUS
NATURESMADNESS.pp = 10
NATURESMADNESS.accuracy = 90
NATURESMADNESS.priority = 0
NATURESMADNESS.target = 'NearOther'
NATURESMADNESS.additional_effect_chance = 0
NATURESMADNESS.description = "The user hits the target with the force of nature. It halves the targets HP."

#################
### SWEETKISS ###
#################

SWEETKISS = Move()
SWEETKISS.name = "Sweet Kiss"
SWEETKISS.type = FAIRY
SWEETKISS.base_damage = 0
SWEETKISS.category = STATUS
SWEETKISS.pp = 10
SWEETKISS.accuracy = 75
SWEETKISS.priority = 0
SWEETKISS.target = 'NearOther'
SWEETKISS.additional_effect_chance = 0
SWEETKISS.description = "The user kisses the target with a sweet, angelic cuteness that causes confusion."

##################
### FOCUSPUNCH ###
##################

FOCUSPUNCH = Move()
FOCUSPUNCH.name = "Focus Punch"
FOCUSPUNCH.type = FIGHTING
FOCUSPUNCH.base_damage = 150
FOCUSPUNCH.category = PHYSICAL
FOCUSPUNCH.pp = 20
FOCUSPUNCH.accuracy = 100
FOCUSPUNCH.priority = -3
FOCUSPUNCH.target = 'NearOther'
FOCUSPUNCH.additional_effect_chance = 0
FOCUSPUNCH.description = "The user focuses its mind before launching a punch. It will fail if the user is hit before it is used."

####################
### HIGHJUMPKICK ###
####################

HIGHJUMPKICK = Move()
HIGHJUMPKICK.name = "High Jump Kick"
HIGHJUMPKICK.type = FIGHTING
HIGHJUMPKICK.base_damage = 130
HIGHJUMPKICK.category = PHYSICAL
HIGHJUMPKICK.pp = 10
HIGHJUMPKICK.accuracy = 90
HIGHJUMPKICK.priority = 0
HIGHJUMPKICK.target = 'NearOther'
HIGHJUMPKICK.additional_effect_chance = 0
HIGHJUMPKICK.description = "The target is attacked with a knee kick from a jump. If it misses, the user is hurt instead."

###################
### CLOSECOMBAT ###
###################

CLOSECOMBAT = Move()
CLOSECOMBAT.name = "Close Combat"
CLOSECOMBAT.type = FIGHTING
CLOSECOMBAT.base_damage = 120
CLOSECOMBAT.category = PHYSICAL
CLOSECOMBAT.pp = 5
CLOSECOMBAT.accuracy = 100
CLOSECOMBAT.priority = 0
CLOSECOMBAT.target = 'NearOther'
CLOSECOMBAT.additional_effect_chance = 0
CLOSECOMBAT.description = "The user fights the foe up close without guarding itself. It also cuts the users Defense and Sp. Def."

##################
### FOCUSBLAST ###
##################

FOCUSBLAST = Move()
FOCUSBLAST.name = "Focus Blast"
FOCUSBLAST.type = FIGHTING
FOCUSBLAST.base_damage = 120
FOCUSBLAST.category = SPECIAL
FOCUSBLAST.pp = 5
FOCUSBLAST.accuracy = 70
FOCUSBLAST.priority = 0
FOCUSBLAST.target = 'NearOther'
FOCUSBLAST.additional_effect_chance = 10
FOCUSBLAST.description = "The user heightens its mental focus and unleashes its power. It may also lower the targets Sp. Def."

##################
### SUPERPOWER ###
##################

SUPERPOWER = Move()
SUPERPOWER.name = "Superpower"
SUPERPOWER.type = FIGHTING
SUPERPOWER.base_damage = 120
SUPERPOWER.category = PHYSICAL
SUPERPOWER.pp = 5
SUPERPOWER.accuracy = 100
SUPERPOWER.priority = 0
SUPERPOWER.target = 'NearOther'
SUPERPOWER.additional_effect_chance = 0
SUPERPOWER.description = "The user attacks the target with great power. However, it also lowers the users Attack and Defense."

#################
### CROSSCHOP ###
#################

CROSSCHOP = Move()
CROSSCHOP.name = "Cross Chop"
CROSSCHOP.type = FIGHTING
CROSSCHOP.base_damage = 100
CROSSCHOP.category = PHYSICAL
CROSSCHOP.pp = 5
CROSSCHOP.accuracy = 80
CROSSCHOP.priority = 0
CROSSCHOP.target = 'NearOther'
CROSSCHOP.additional_effect_chance = 0
CROSSCHOP.description = "The user delivers a double chop with its forearms crossed. Critical hits land more easily."

####################
### DYNAMICPUNCH ###
####################

DYNAMICPUNCH = Move()
DYNAMICPUNCH.name = "Dynamic Punch"
DYNAMICPUNCH.type = FIGHTING
DYNAMICPUNCH.base_damage = 100
DYNAMICPUNCH.category = PHYSICAL
DYNAMICPUNCH.pp = 5
DYNAMICPUNCH.accuracy = 50
DYNAMICPUNCH.priority = 0
DYNAMICPUNCH.target = 'NearOther'
DYNAMICPUNCH.additional_effect_chance = 100
DYNAMICPUNCH.description = "The user punches the target with full, concentrated power. It confuses the target if it hits."

###################
### FLYINGPRESS ###
###################

FLYINGPRESS = Move()
FLYINGPRESS.name = "Flying Press"
FLYINGPRESS.type = FIGHTING
FLYINGPRESS.base_damage = 100
FLYINGPRESS.category = PHYSICAL
FLYINGPRESS.pp = 10
FLYINGPRESS.accuracy = 95
FLYINGPRESS.priority = 0
FLYINGPRESS.target = 'Other'
FLYINGPRESS.additional_effect_chance = 0
FLYINGPRESS.description = "The user dives down onto the target from the sky. This move is Fighting and Flying type simultaneously."

#################
### HAMMERARM ###
#################

HAMMERARM = Move()
HAMMERARM.name = "Hammer Arm"
HAMMERARM.type = FIGHTING
HAMMERARM.base_damage = 100
HAMMERARM.category = PHYSICAL
HAMMERARM.pp = 10
HAMMERARM.accuracy = 90
HAMMERARM.priority = 0
HAMMERARM.target = 'NearOther'
HAMMERARM.additional_effect_chance = 0
HAMMERARM.description = "The user swings and hits with its strong and heavy fist. It lowers the users Speed, however."

################
### JUMPKICK ###
################

JUMPKICK = Move()
JUMPKICK.name = "Jump Kick"
JUMPKICK.type = FIGHTING
JUMPKICK.base_damage = 100
JUMPKICK.category = PHYSICAL
JUMPKICK.pp = 10
JUMPKICK.accuracy = 95
JUMPKICK.priority = 0
JUMPKICK.target = 'NearOther'
JUMPKICK.additional_effect_chance = 0
JUMPKICK.description = "The user jumps up high, then strikes with a kick. If the kick misses, the user hurts itself."

###################
### SACREDSWORD ###
###################

SACREDSWORD = Move()
SACREDSWORD.name = "Sacred Sword"
SACREDSWORD.type = FIGHTING
SACREDSWORD.base_damage = 90
SACREDSWORD.category = PHYSICAL
SACREDSWORD.pp = 15
SACREDSWORD.accuracy = 100
SACREDSWORD.priority = 0
SACREDSWORD.target = 'NearOther'
SACREDSWORD.additional_effect_chance = 0
SACREDSWORD.description = "The user attacks by slicing with its long horns. The targets stat changes dont affect the damage."

###################
### SECRETSWORD ###
###################

SECRETSWORD = Move()
SECRETSWORD.name = "Secret Sword"
SECRETSWORD.type = FIGHTING
SECRETSWORD.base_damage = 85
SECRETSWORD.category = SPECIAL
SECRETSWORD.pp = 10
SECRETSWORD.accuracy = 100
SECRETSWORD.priority = 0
SECRETSWORD.target = 'NearOther'
SECRETSWORD.additional_effect_chance = 0
SECRETSWORD.description = "The user cuts with its long horn. The odd power contained in it does physical damage to the foe."

###################
### SKYUPPERCUT ###
###################

SKYUPPERCUT = Move()
SKYUPPERCUT.name = "Sky Uppercut"
SKYUPPERCUT.type = FIGHTING
SKYUPPERCUT.base_damage = 85
SKYUPPERCUT.category = PHYSICAL
SKYUPPERCUT.pp = 15
SKYUPPERCUT.accuracy = 90
SKYUPPERCUT.priority = 0
SKYUPPERCUT.target = 'NearOther'
SKYUPPERCUT.additional_effect_chance = 0
SKYUPPERCUT.description = "The user attacks the target with an uppercut thrown skyward with force."

##################
### AURASPHERE ###
##################

AURASPHERE = Move()
AURASPHERE.name = "Aura Sphere"
AURASPHERE.type = FIGHTING
AURASPHERE.base_damage = 80
AURASPHERE.category = SPECIAL
AURASPHERE.pp = 20
AURASPHERE.accuracy = 0
AURASPHERE.priority = 0
AURASPHERE.target = 'Other'
AURASPHERE.additional_effect_chance = 0
AURASPHERE.description = "The user looses a blast of aura power from deep within its body. This move is certain to hit."

##################
### SUBMISSION ###
##################

SUBMISSION = Move()
SUBMISSION.name = "Submission"
SUBMISSION.type = FIGHTING
SUBMISSION.base_damage = 80
SUBMISSION.category = PHYSICAL
SUBMISSION.pp = 20
SUBMISSION.accuracy = 80
SUBMISSION.priority = 0
SUBMISSION.target = 'NearOther'
SUBMISSION.additional_effect_chance = 0
SUBMISSION.description = "The user grabs the target and recklessly dives for the ground. It also hurts the user slightly."

##################
### BRICKBREAK ###
##################

BRICKBREAK = Move()
BRICKBREAK.name = "Brick Break"
BRICKBREAK.type = FIGHTING
BRICKBREAK.base_damage = 75
BRICKBREAK.category = PHYSICAL
BRICKBREAK.pp = 15
BRICKBREAK.accuracy = 100
BRICKBREAK.priority = 0
BRICKBREAK.target = 'NearOther'
BRICKBREAK.additional_effect_chance = 0
BRICKBREAK.description = "The user attacks with a swift chop. It can also break any barrier such as Light Screen and Reflect."

##################
### DRAINPUNCH ###
##################

DRAINPUNCH = Move()
DRAINPUNCH.name = "Drain Punch"
DRAINPUNCH.type = FIGHTING
DRAINPUNCH.base_damage = 75
DRAINPUNCH.category = PHYSICAL
DRAINPUNCH.pp = 10
DRAINPUNCH.accuracy = 100
DRAINPUNCH.priority = 0
DRAINPUNCH.target = 'NearOther'
DRAINPUNCH.additional_effect_chance = 0
DRAINPUNCH.description = "An energy-draining punch. The users HP is restored by half the damage taken by the target."

##################
### VITALTHROW ###
##################

VITALTHROW = Move()
VITALTHROW.name = "Vital Throw"
VITALTHROW.type = FIGHTING
VITALTHROW.base_damage = 70
VITALTHROW.category = PHYSICAL
VITALTHROW.pp = 10
VITALTHROW.accuracy = 0
VITALTHROW.priority = -1
VITALTHROW.target = 'NearOther'
VITALTHROW.additional_effect_chance = 0
VITALTHROW.description = "The user attacks last. In return, this throw move is guaranteed not to miss."

##################
### WAKEUPSLAP ###
##################

WAKEUPSLAP = Move()
WAKEUPSLAP.name = "Wake-Up Slap"
WAKEUPSLAP.type = FIGHTING
WAKEUPSLAP.base_damage = 70
WAKEUPSLAP.category = PHYSICAL
WAKEUPSLAP.pp = 10
WAKEUPSLAP.accuracy = 100
WAKEUPSLAP.priority = 0
WAKEUPSLAP.target = 'NearOther'
WAKEUPSLAP.additional_effect_chance = 0
WAKEUPSLAP.description = "This attack inflicts big damage on a sleeping target. It also wakes the target up, however."

################
### LOWSWEEP ###
################

LOWSWEEP = Move()
LOWSWEEP.name = "Low Sweep"
LOWSWEEP.type = FIGHTING
LOWSWEEP.base_damage = 65
LOWSWEEP.category = PHYSICAL
LOWSWEEP.pp = 20
LOWSWEEP.accuracy = 100
LOWSWEEP.priority = 0
LOWSWEEP.target = 'NearOther'
LOWSWEEP.additional_effect_chance = 100
LOWSWEEP.description = "The user attacks the targets legs swiftly, reducing the targets Speed stat."

###################
### CIRCLETHROW ###
###################

CIRCLETHROW = Move()
CIRCLETHROW.name = "Circle Throw"
CIRCLETHROW.type = FIGHTING
CIRCLETHROW.base_damage = 60
CIRCLETHROW.category = PHYSICAL
CIRCLETHROW.pp = 10
CIRCLETHROW.accuracy = 90
CIRCLETHROW.priority = -6
CIRCLETHROW.target = 'NearOther'
CIRCLETHROW.additional_effect_chance = 0
CIRCLETHROW.description = "The user throws the target and drags out another Pokémon in its party. In the wild, the battle ends."

#################
### FORCEPALM ###
#################

FORCEPALM = Move()
FORCEPALM.name = "Force Palm"
FORCEPALM.type = FIGHTING
FORCEPALM.base_damage = 60
FORCEPALM.category = PHYSICAL
FORCEPALM.pp = 10
FORCEPALM.accuracy = 100
FORCEPALM.priority = 0
FORCEPALM.target = 'NearOther'
FORCEPALM.additional_effect_chance = 30
FORCEPALM.description = "The target is attacked with a shock wave. It may also leave the target with paralysis."

###############
### REVENGE ###
###############

REVENGE = Move()
REVENGE.name = "Revenge"
REVENGE.type = FIGHTING
REVENGE.base_damage = 60
REVENGE.category = PHYSICAL
REVENGE.pp = 10
REVENGE.accuracy = 100
REVENGE.priority = -4
REVENGE.target = 'NearOther'
REVENGE.additional_effect_chance = 0
REVENGE.description = "An attack move that inflicts double the damage if the user has been hurt by the foe in the same turn."

###################
### ROLLINGKICK ###
###################

ROLLINGKICK = Move()
ROLLINGKICK.name = "Rolling Kick"
ROLLINGKICK.type = FIGHTING
ROLLINGKICK.base_damage = 60
ROLLINGKICK.category = PHYSICAL
ROLLINGKICK.pp = 15
ROLLINGKICK.accuracy = 85
ROLLINGKICK.priority = 0
ROLLINGKICK.target = 'NearOther'
ROLLINGKICK.additional_effect_chance = 30
ROLLINGKICK.description = "The user lashes out with a quick, spinning kick. It may also make the target flinch."

##################
### STORMTHROW ###
##################

STORMTHROW = Move()
STORMTHROW.name = "Storm Throw"
STORMTHROW.type = FIGHTING
STORMTHROW.base_damage = 60
STORMTHROW.category = PHYSICAL
STORMTHROW.pp = 10
STORMTHROW.accuracy = 100
STORMTHROW.priority = 0
STORMTHROW.target = 'NearOther'
STORMTHROW.additional_effect_chance = 0
STORMTHROW.description = "The user strikes the target with a fierce blow. This attack always results in a critical hit."

##################
### KARATECHOP ###
##################

KARATECHOP = Move()
KARATECHOP.name = "Karate Chop"
KARATECHOP.type = FIGHTING
KARATECHOP.base_damage = 50
KARATECHOP.category = PHYSICAL
KARATECHOP.pp = 25
KARATECHOP.accuracy = 100
KARATECHOP.priority = 0
KARATECHOP.target = 'NearOther'
KARATECHOP.additional_effect_chance = 0
KARATECHOP.description = "The target is attacked with a sharp chop. Critical hits land more easily."

#################
### MACHPUNCH ###
#################

MACHPUNCH = Move()
MACHPUNCH.name = "Mach Punch"
MACHPUNCH.type = FIGHTING
MACHPUNCH.base_damage = 40
MACHPUNCH.category = PHYSICAL
MACHPUNCH.pp = 30
MACHPUNCH.accuracy = 100
MACHPUNCH.priority = 1
MACHPUNCH.target = 'NearOther'
MACHPUNCH.additional_effect_chance = 0
MACHPUNCH.description = "The user throws a punch at blinding speed. It is certain to strike first."

####################
### POWERUPPUNCH ###
####################

POWERUPPUNCH = Move()
POWERUPPUNCH.name = "Power-Up Punch"
POWERUPPUNCH.type = FIGHTING
POWERUPPUNCH.base_damage = 40
POWERUPPUNCH.category = PHYSICAL
POWERUPPUNCH.pp = 20
POWERUPPUNCH.accuracy = 100
POWERUPPUNCH.priority = 0
POWERUPPUNCH.target = 'NearOther'
POWERUPPUNCH.additional_effect_chance = 0
POWERUPPUNCH.description = "Striking opponents repeatedly makes the users fists harder, raising the users Attack stat."

#################
### ROCKSMASH ###
#################

ROCKSMASH = Move()
ROCKSMASH.name = "Rock Smash"
ROCKSMASH.type = FIGHTING
ROCKSMASH.base_damage = 40
ROCKSMASH.category = PHYSICAL
ROCKSMASH.pp = 15
ROCKSMASH.accuracy = 100
ROCKSMASH.priority = 0
ROCKSMASH.target = 'NearOther'
ROCKSMASH.additional_effect_chance = 50
ROCKSMASH.description = "The user attacks with a punch that can shatter a rock. It may also lower the foes Defense stat."

##################
### VACUUMWAVE ###
##################

VACUUMWAVE = Move()
VACUUMWAVE.name = "Vacuum Wave"
VACUUMWAVE.type = FIGHTING
VACUUMWAVE.base_damage = 40
VACUUMWAVE.category = SPECIAL
VACUUMWAVE.pp = 30
VACUUMWAVE.accuracy = 100
VACUUMWAVE.priority = 1
VACUUMWAVE.target = 'NearOther'
VACUUMWAVE.additional_effect_chance = 0
VACUUMWAVE.description = "The user whirls its fists to send a wave of pure vacuum at the target. This move always goes first."

##################
### DOUBLEKICK ###
##################

DOUBLEKICK = Move()
DOUBLEKICK.name = "Double Kick"
DOUBLEKICK.type = FIGHTING
DOUBLEKICK.base_damage = 30
DOUBLEKICK.category = PHYSICAL
DOUBLEKICK.pp = 30
DOUBLEKICK.accuracy = 100
DOUBLEKICK.priority = 0
DOUBLEKICK.target = 'NearOther'
DOUBLEKICK.additional_effect_chance = 0
DOUBLEKICK.description = "The target is quickly kicked twice in succession using both feet."

#################
### ARMTHRUST ###
#################

ARMTHRUST = Move()
ARMTHRUST.name = "Arm Thrust"
ARMTHRUST.type = FIGHTING
ARMTHRUST.base_damage = 15
ARMTHRUST.category = PHYSICAL
ARMTHRUST.pp = 20
ARMTHRUST.accuracy = 100
ARMTHRUST.priority = 0
ARMTHRUST.target = 'NearOther'
ARMTHRUST.additional_effect_chance = 0
ARMTHRUST.description = "The user looses a flurry of open-palmed arm thrusts that hit two to five times in a row."

##################
### TRIPLEKICK ###
##################

TRIPLEKICK = Move()
TRIPLEKICK.name = "Triple Kick"
TRIPLEKICK.type = FIGHTING
TRIPLEKICK.base_damage = 10
TRIPLEKICK.category = PHYSICAL
TRIPLEKICK.pp = 10
TRIPLEKICK.accuracy = 90
TRIPLEKICK.priority = 0
TRIPLEKICK.target = 'NearOther'
TRIPLEKICK.additional_effect_chance = 0
TRIPLEKICK.description = "A consecutive three-kick attack that becomes more powerful with each successive hit."

###############
### COUNTER ###
###############

COUNTER = Move()
COUNTER.name = "Counter"
COUNTER.type = FIGHTING
COUNTER.base_damage = 1
COUNTER.category = PHYSICAL
COUNTER.pp = 20
COUNTER.accuracy = 100
COUNTER.priority = -5
COUNTER.target = 'None'
COUNTER.additional_effect_chance = 0
COUNTER.description = "A retaliation move that counters any physical attack, inflicting double the damage taken."

###################
### FINALGAMBIT ###
###################

FINALGAMBIT = Move()
FINALGAMBIT.name = "Final Gambit"
FINALGAMBIT.type = FIGHTING
FINALGAMBIT.base_damage = 1
FINALGAMBIT.category = SPECIAL
FINALGAMBIT.pp = 5
FINALGAMBIT.accuracy = 100
FINALGAMBIT.priority = 0
FINALGAMBIT.target = 'NearOther'
FINALGAMBIT.additional_effect_chance = 0
FINALGAMBIT.description = "The user risks all to attack the foe. The user faints but does damage equal to its HP."

###############
### LOWKICK ###
###############

LOWKICK = Move()
LOWKICK.name = "Low Kick"
LOWKICK.type = FIGHTING
LOWKICK.base_damage = 1
LOWKICK.category = PHYSICAL
LOWKICK.pp = 20
LOWKICK.accuracy = 100
LOWKICK.priority = 0
LOWKICK.target = 'NearOther'
LOWKICK.additional_effect_chance = 0
LOWKICK.description = "A powerful low kick that makes the foe fall over. It inflicts greater damage on heavier foes."

################
### REVERSAL ###
################

REVERSAL = Move()
REVERSAL.name = "Reversal"
REVERSAL.type = FIGHTING
REVERSAL.base_damage = 1
REVERSAL.category = PHYSICAL
REVERSAL.pp = 15
REVERSAL.accuracy = 100
REVERSAL.priority = 0
REVERSAL.target = 'NearOther'
REVERSAL.additional_effect_chance = 0
REVERSAL.description = "An all-out attack that becomes more powerful the less HP the user has."

###################
### SEISMICTOSS ###
###################

SEISMICTOSS = Move()
SEISMICTOSS.name = "Seismic Toss"
SEISMICTOSS.type = FIGHTING
SEISMICTOSS.base_damage = 1
SEISMICTOSS.category = PHYSICAL
SEISMICTOSS.pp = 20
SEISMICTOSS.accuracy = 100
SEISMICTOSS.priority = 0
SEISMICTOSS.target = 'NearOther'
SEISMICTOSS.additional_effect_chance = 0
SEISMICTOSS.description = "The target is thrown using the power of gravity. It inflicts damage equal to the users level."

##############
### BULKUP ###
##############

BULKUP = Move()
BULKUP.name = "Bulk Up"
BULKUP.type = FIGHTING
BULKUP.base_damage = 0
BULKUP.category = STATUS
BULKUP.pp = 20
BULKUP.accuracy = 0
BULKUP.priority = 0
BULKUP.target = 'User'
BULKUP.additional_effect_chance = 0
BULKUP.description = "The user tenses its muscles to bulk up its body, boosting both its Attack and Defense stats."

##############
### DETECT ###
##############

DETECT = Move()
DETECT.name = "Detect"
DETECT.type = FIGHTING
DETECT.base_damage = 0
DETECT.category = STATUS
DETECT.pp = 5
DETECT.accuracy = 0
DETECT.priority = 4
DETECT.target = 'User'
DETECT.additional_effect_chance = 0
DETECT.description = "It enables the user to evade all attacks. Its chance of failing rises if it is used in succession."

################
### MATBLOCK ###
################

MATBLOCK = Move()
MATBLOCK.name = "Mat Block"
MATBLOCK.type = FIGHTING
MATBLOCK.base_damage = 0
MATBLOCK.category = STATUS
MATBLOCK.pp = 10
MATBLOCK.accuracy = 0
MATBLOCK.priority = 0
MATBLOCK.target = 'UserSide'
MATBLOCK.additional_effect_chance = 0
MATBLOCK.description = "Using a pulled-up mat as a shield, the user protects itself and its allies from damaging moves."

##################
### QUICKGUARD ###
##################

QUICKGUARD = Move()
QUICKGUARD.name = "Quick Guard"
QUICKGUARD.type = FIGHTING
QUICKGUARD.base_damage = 0
QUICKGUARD.category = STATUS
QUICKGUARD.pp = 15
QUICKGUARD.accuracy = 0
QUICKGUARD.priority = 3
QUICKGUARD.target = 'UserSide'
QUICKGUARD.additional_effect_chance = 0
QUICKGUARD.description = "The user protects itself and its allies from priority moves. If may fail if used in succession."

###############
### VCREATE ###
###############

VCREATE = Move()
VCREATE.name = "V-create"
VCREATE.type = FIRE
VCREATE.base_damage = 180
VCREATE.category = PHYSICAL
VCREATE.pp = 5
VCREATE.accuracy = 95
VCREATE.priority = 0
VCREATE.target = 'NearOther'
VCREATE.additional_effect_chance = 0
VCREATE.description = "With a fiery forehead, the user hurls itself at the foe. It lowers the users Defense, Sp. Def, and Speed."

#################
### BLASTBURN ###
#################

BLASTBURN = Move()
BLASTBURN.name = "Blast Burn"
BLASTBURN.type = FIRE
BLASTBURN.base_damage = 150
BLASTBURN.category = SPECIAL
BLASTBURN.pp = 5
BLASTBURN.accuracy = 90
BLASTBURN.priority = 0
BLASTBURN.target = 'NearOther'
BLASTBURN.additional_effect_chance = 0
BLASTBURN.description = "The target is razed by a fiery explosion. The user must rest on the next turn, however."

################
### ERUPTION ###
################

ERUPTION = Move()
ERUPTION.name = "Eruption"
ERUPTION.type = FIRE
ERUPTION.base_damage = 150
ERUPTION.category = SPECIAL
ERUPTION.pp = 5
ERUPTION.accuracy = 100
ERUPTION.priority = 0
ERUPTION.target = 'AllNearFoes'
ERUPTION.additional_effect_chance = 0
ERUPTION.description = "The user attacks in an explosive fury. The lower the users HP, the less powerful this attack becomes."

#################
### MINDBLOWN ###
#################

MINDBLOWN = Move()
MINDBLOWN.name = "Mind Blown"
MINDBLOWN.type = FIRE
MINDBLOWN.base_damage = 150
MINDBLOWN.category = SPECIAL
MINDBLOWN.pp = 5
MINDBLOWN.accuracy = 100
MINDBLOWN.priority = 0
MINDBLOWN.target = 'AllNearOthers'
MINDBLOWN.additional_effect_chance = 0
MINDBLOWN.description = "The user attacks everything by causing its own head to explode. This also damages the user."

#################
### SHELLTRAP ###
#################

SHELLTRAP = Move()
SHELLTRAP.name = "Shell Trap"
SHELLTRAP.type = FIRE
SHELLTRAP.base_damage = 150
SHELLTRAP.category = SPECIAL
SHELLTRAP.pp = 5
SHELLTRAP.accuracy = 100
SHELLTRAP.priority = -3
SHELLTRAP.target = 'AllNearFoes'
SHELLTRAP.additional_effect_chance = 0
SHELLTRAP.description = "The user sets a shell trap. If it is hit by a physical move, the trap explodes and hurt the attacker."

#################
### BLUEFLARE ###
#################

BLUEFLARE = Move()
BLUEFLARE.name = "Blue Flare"
BLUEFLARE.type = FIRE
BLUEFLARE.base_damage = 130
BLUEFLARE.category = SPECIAL
BLUEFLARE.pp = 5
BLUEFLARE.accuracy = 85
BLUEFLARE.priority = 0
BLUEFLARE.target = 'NearOther'
BLUEFLARE.additional_effect_chance = 20
BLUEFLARE.description = "The user attacks by engulfing the foe in a beautiful, yet intense, blue flame. It may also burn the foe."

##############
### BURNUP ###
##############

BURNUP = Move()
BURNUP.name = "Burn Up"
BURNUP.type = FIRE
BURNUP.base_damage = 130
BURNUP.category = SPECIAL
BURNUP.pp = 5
BURNUP.accuracy = 100
BURNUP.priority = 0
BURNUP.target = 'NearOther'
BURNUP.additional_effect_chance = 0
BURNUP.description = "To inflict massive damage, the user burns itself out. The user will no longer be Fire type."

################
### OVERHEAT ###
################

OVERHEAT = Move()
OVERHEAT.name = "Overheat"
OVERHEAT.type = FIRE
OVERHEAT.base_damage = 130
OVERHEAT.category = SPECIAL
OVERHEAT.pp = 5
OVERHEAT.accuracy = 90
OVERHEAT.priority = 0
OVERHEAT.target = 'NearOther'
OVERHEAT.additional_effect_chance = 0
OVERHEAT.description = "The user attacks the target at full power. The attacks recoil sharply reduces the users Sp. Atk stat."

##################
### FLAREBLITZ ###
##################

FLAREBLITZ = Move()
FLAREBLITZ.name = "Flare Blitz"
FLAREBLITZ.type = FIRE
FLAREBLITZ.base_damage = 120
FLAREBLITZ.category = PHYSICAL
FLAREBLITZ.pp = 15
FLAREBLITZ.accuracy = 100
FLAREBLITZ.priority = 0
FLAREBLITZ.target = 'NearOther'
FLAREBLITZ.additional_effect_chance = 10
FLAREBLITZ.description = "The user cloaks itself in fire and charges at the foe. The user also takes damage and may burn the target."

#################
### FIREBLAST ###
#################

FIREBLAST = Move()
FIREBLAST.name = "Fire Blast"
FIREBLAST.type = FIRE
FIREBLAST.base_damage = 110
FIREBLAST.category = SPECIAL
FIREBLAST.pp = 5
FIREBLAST.accuracy = 85
FIREBLAST.priority = 0
FIREBLAST.target = 'NearOther'
FIREBLAST.additional_effect_chance = 10
FIREBLAST.description = "The foe is attacked with an intense blast of all-consuming fire. It may also leave the target with a burn."

###################
### FUSIONFLARE ###
###################

FUSIONFLARE = Move()
FUSIONFLARE.name = "Fusion Flare"
FUSIONFLARE.type = FIRE
FUSIONFLARE.base_damage = 100
FUSIONFLARE.category = SPECIAL
FUSIONFLARE.pp = 5
FUSIONFLARE.accuracy = 100
FUSIONFLARE.priority = 0
FUSIONFLARE.target = 'NearOther'
FUSIONFLARE.additional_effect_chance = 0
FUSIONFLARE.description = "The user brings down a giant flame. It does more damage if influenced by an enormous thunderbolt."

###############
### INFERNO ###
###############

INFERNO = Move()
INFERNO.name = "Inferno"
INFERNO.type = FIRE
INFERNO.base_damage = 100
INFERNO.category = SPECIAL
INFERNO.pp = 5
INFERNO.accuracy = 50
INFERNO.priority = 0
INFERNO.target = 'NearOther'
INFERNO.additional_effect_chance = 100
INFERNO.description = "The user attacks by engulfing the target in an intense fire. It leaves the target with a burn."

##################
### MAGMASTORM ###
##################

MAGMASTORM = Move()
MAGMASTORM.name = "Magma Storm"
MAGMASTORM.type = FIRE
MAGMASTORM.base_damage = 100
MAGMASTORM.category = SPECIAL
MAGMASTORM.pp = 5
MAGMASTORM.accuracy = 75
MAGMASTORM.priority = 0
MAGMASTORM.target = 'NearOther'
MAGMASTORM.additional_effect_chance = 0
MAGMASTORM.description = "The target becomes trapped within a maelstrom of fire that rages for four to five turns."

##################
### SACREDFIRE ###
##################

SACREDFIRE = Move()
SACREDFIRE.name = "Sacred Fire"
SACREDFIRE.type = FIRE
SACREDFIRE.base_damage = 100
SACREDFIRE.category = PHYSICAL
SACREDFIRE.pp = 5
SACREDFIRE.accuracy = 95
SACREDFIRE.priority = 0
SACREDFIRE.target = 'NearOther'
SACREDFIRE.additional_effect_chance = 50
SACREDFIRE.description = "The target is razed with a mystical fire of great intensity. It may also leave the target with a burn."

###################
### SEARINGSHOT ###
###################

SEARINGSHOT = Move()
SEARINGSHOT.name = "Searing Shot"
SEARINGSHOT.type = FIRE
SEARINGSHOT.base_damage = 100
SEARINGSHOT.category = SPECIAL
SEARINGSHOT.pp = 5
SEARINGSHOT.accuracy = 100
SEARINGSHOT.priority = 0
SEARINGSHOT.target = 'AllNearOthers'
SEARINGSHOT.additional_effect_chance = 30
SEARINGSHOT.description = "An inferno of scarlet flames torches everything around the user. It may leave the foe with a burn."

################
### HEATWAVE ###
################

HEATWAVE = Move()
HEATWAVE.name = "Heat Wave"
HEATWAVE.type = FIRE
HEATWAVE.base_damage = 95
HEATWAVE.category = SPECIAL
HEATWAVE.pp = 10
HEATWAVE.accuracy = 90
HEATWAVE.priority = 0
HEATWAVE.target = 'AllNearFoes'
HEATWAVE.additional_effect_chance = 10
HEATWAVE.description = "The user attacks by exhaling hot breath on the opposing team. It may also leave targets with a burn."

####################
### FLAMETHROWER ###
####################

FLAMETHROWER = Move()
FLAMETHROWER.name = "Flamethrower"
FLAMETHROWER.type = FIRE
FLAMETHROWER.base_damage = 90
FLAMETHROWER.category = SPECIAL
FLAMETHROWER.pp = 15
FLAMETHROWER.accuracy = 100
FLAMETHROWER.priority = 0
FLAMETHROWER.target = 'NearOther'
FLAMETHROWER.additional_effect_chance = 10
FLAMETHROWER.description = "The target is scorched with an intense blast of fire. It may also leave the target with a burn."

#################
### BLAZEKICK ###
#################

BLAZEKICK = Move()
BLAZEKICK.name = "Blaze Kick"
BLAZEKICK.type = FIRE
BLAZEKICK.base_damage = 85
BLAZEKICK.category = PHYSICAL
BLAZEKICK.pp = 10
BLAZEKICK.accuracy = 90
BLAZEKICK.priority = 0
BLAZEKICK.target = 'NearOther'
BLAZEKICK.additional_effect_chance = 10
BLAZEKICK.description = "The user launches a kick with a high critical-hit ratio. It may also leave the target with a burn."

##################
### FIERYDANCE ###
##################

FIERYDANCE = Move()
FIERYDANCE.name = "Fiery Dance"
FIERYDANCE.type = FIRE
FIERYDANCE.base_damage = 80
FIERYDANCE.category = SPECIAL
FIERYDANCE.pp = 10
FIERYDANCE.accuracy = 100
FIERYDANCE.priority = 0
FIERYDANCE.target = 'NearOther'
FIERYDANCE.additional_effect_chance = 50
FIERYDANCE.description = "Cloaked in flames, the user dances and flaps its wings. It may also raise the users Sp. Atk stat."

################
### FIRELASH ###
################

FIRELASH = Move()
FIRELASH.name = "Fire Lash"
FIRELASH.type = FIRE
FIRELASH.base_damage = 80
FIRELASH.category = PHYSICAL
FIRELASH.pp = 15
FIRELASH.accuracy = 100
FIRELASH.priority = 0
FIRELASH.target = 'NearOther'
FIRELASH.additional_effect_chance = 100
FIRELASH.description = "The user strikes the target with a burning lash. This also lowers the targets Defense stat."

##################
### FIREPLEDGE ###
##################

FIREPLEDGE = Move()
FIREPLEDGE.name = "Fire Pledge"
FIREPLEDGE.type = FIRE
FIREPLEDGE.base_damage = 80
FIREPLEDGE.category = SPECIAL
FIREPLEDGE.pp = 10
FIREPLEDGE.accuracy = 100
FIREPLEDGE.priority = 0
FIREPLEDGE.target = 'NearOther'
FIREPLEDGE.additional_effect_chance = 0
FIREPLEDGE.description = "A column of fire hits opposing Pokémon. When used with its Grass equivalent, it makes a sea of fire."

#################
### LAVAPLUME ###
#################

LAVAPLUME = Move()
LAVAPLUME.name = "Lava Plume"
LAVAPLUME.type = FIRE
LAVAPLUME.base_damage = 80
LAVAPLUME.category = SPECIAL
LAVAPLUME.pp = 15
LAVAPLUME.accuracy = 100
LAVAPLUME.priority = 0
LAVAPLUME.target = 'AllNearOthers'
LAVAPLUME.additional_effect_chance = 30
LAVAPLUME.description = "An inferno of scarlet flames torches everything around the user. It may leave targets with a burn."

#################
### FIREPUNCH ###
#################

FIREPUNCH = Move()
FIREPUNCH.name = "Fire Punch"
FIREPUNCH.type = FIRE
FIREPUNCH.base_damage = 75
FIREPUNCH.category = PHYSICAL
FIREPUNCH.pp = 15
FIREPUNCH.accuracy = 100
FIREPUNCH.priority = 0
FIREPUNCH.target = 'NearOther'
FIREPUNCH.additional_effect_chance = 10
FIREPUNCH.description = "The target is punched with a fiery fist. It may leave the target with a burn."

####################
### MYSTICALFIRE ###
####################

MYSTICALFIRE = Move()
MYSTICALFIRE.name = "Mystical Fire"
MYSTICALFIRE.type = FIRE
MYSTICALFIRE.base_damage = 75
MYSTICALFIRE.category = SPECIAL
MYSTICALFIRE.pp = 10
MYSTICALFIRE.accuracy = 100
MYSTICALFIRE.priority = 0
MYSTICALFIRE.target = 'NearOther'
MYSTICALFIRE.additional_effect_chance = 100
MYSTICALFIRE.description = "The user attacks by breathing a special, hot fire. This also lowers the targets Sp. Atk stat."

##################
### FLAMEBURST ###
##################

FLAMEBURST = Move()
FLAMEBURST.name = "Flame Burst"
FLAMEBURST.type = FIRE
FLAMEBURST.base_damage = 70
FLAMEBURST.category = SPECIAL
FLAMEBURST.pp = 15
FLAMEBURST.accuracy = 100
FLAMEBURST.priority = 0
FLAMEBURST.target = 'NearOther'
FLAMEBURST.additional_effect_chance = 0
FLAMEBURST.description = "The user attacks the foe with a bursting flame. It also damages Pokémon next to the target."

################
### FIREFANG ###
################

FIREFANG = Move()
FIREFANG.name = "Fire Fang"
FIREFANG.type = FIRE
FIREFANG.base_damage = 65
FIREFANG.category = PHYSICAL
FIREFANG.pp = 15
FIREFANG.accuracy = 95
FIREFANG.priority = 0
FIREFANG.target = 'NearOther'
FIREFANG.additional_effect_chance = 100
FIREFANG.description = "The user bites with flame-cloaked fangs. It may also make the target flinch or leave it burned."

##################
### FLAMEWHEEL ###
##################

FLAMEWHEEL = Move()
FLAMEWHEEL.name = "Flame Wheel"
FLAMEWHEEL.type = FIRE
FLAMEWHEEL.base_damage = 60
FLAMEWHEEL.category = PHYSICAL
FLAMEWHEEL.pp = 25
FLAMEWHEEL.accuracy = 100
FLAMEWHEEL.priority = 0
FLAMEWHEEL.target = 'NearOther'
FLAMEWHEEL.additional_effect_chance = 10
FLAMEWHEEL.description = "The user cloaks itself in fire and charges at the target. It may also leave the target with a burn."

##################
### INCINERATE ###
##################

INCINERATE = Move()
INCINERATE.name = "Incinerate"
INCINERATE.type = FIRE
INCINERATE.base_damage = 60
INCINERATE.category = SPECIAL
INCINERATE.pp = 15
INCINERATE.accuracy = 100
INCINERATE.priority = 0
INCINERATE.target = 'AllNearFoes'
INCINERATE.additional_effect_chance = 0
INCINERATE.description = "The user attacks the foe with fire. The targets held Berry becomes burnt up and unusable."

###################
### FLAMECHARGE ###
###################

FLAMECHARGE = Move()
FLAMECHARGE.name = "Flame Charge"
FLAMECHARGE.type = FIRE
FLAMECHARGE.base_damage = 50
FLAMECHARGE.category = PHYSICAL
FLAMECHARGE.pp = 20
FLAMECHARGE.accuracy = 100
FLAMECHARGE.priority = 0
FLAMECHARGE.target = 'NearOther'
FLAMECHARGE.additional_effect_chance = 100
FLAMECHARGE.description = "The user cloaks itself in flame and attacks. Building up more power, it raises the users Speed stat."

#############
### EMBER ###
#############

EMBER = Move()
EMBER.name = "Ember"
EMBER.type = FIRE
EMBER.base_damage = 40
EMBER.category = SPECIAL
EMBER.pp = 25
EMBER.accuracy = 100
EMBER.priority = 0
EMBER.target = 'NearOther'
EMBER.additional_effect_chance = 10
EMBER.description = "The target is attacked with small flames. It may also leave the target with a burn."

################
### FIRESPIN ###
################

FIRESPIN = Move()
FIRESPIN.name = "Fire Spin"
FIRESPIN.type = FIRE
FIRESPIN.base_damage = 35
FIRESPIN.category = SPECIAL
FIRESPIN.pp = 15
FIRESPIN.accuracy = 85
FIRESPIN.priority = 0
FIRESPIN.target = 'NearOther'
FIRESPIN.additional_effect_chance = 0
FIRESPIN.description = "The target becomes trapped within a fierce vortex of fire that rages for four to five turns."

#################
### HEATCRASH ###
#################

HEATCRASH = Move()
HEATCRASH.name = "Heat Crash"
HEATCRASH.type = FIRE
HEATCRASH.base_damage = 1
HEATCRASH.category = PHYSICAL
HEATCRASH.pp = 10
HEATCRASH.accuracy = 100
HEATCRASH.priority = 0
HEATCRASH.target = 'NearOther'
HEATCRASH.additional_effect_chance = 0
HEATCRASH.description = "The user slams the foe with its flaming body. The heavier the user is, the greater the damage."

################
### SUNNYDAY ###
################

SUNNYDAY = Move()
SUNNYDAY.name = "Sunny Day"
SUNNYDAY.type = FIRE
SUNNYDAY.base_damage = 0
SUNNYDAY.category = STATUS
SUNNYDAY.pp = 5
SUNNYDAY.accuracy = 0
SUNNYDAY.priority = 0
SUNNYDAY.target = 'BothSides'
SUNNYDAY.additional_effect_chance = 0
SUNNYDAY.description = "The user intensifies the sun for five turns, powering up Fire-type moves."

#################
### WILLOWISP ###
#################

WILLOWISP = Move()
WILLOWISP.name = "Will-O-Wisp"
WILLOWISP.type = FIRE
WILLOWISP.base_damage = 0
WILLOWISP.category = STATUS
WILLOWISP.pp = 15
WILLOWISP.accuracy = 85
WILLOWISP.priority = 0
WILLOWISP.target = 'NearOther'
WILLOWISP.additional_effect_chance = 0
WILLOWISP.description = "The user shoots a sinister, bluish-white flame at the target to inflict a burn."

#################
### SKYATTACK ###
#################

SKYATTACK = Move()
SKYATTACK.name = "Sky Attack"
SKYATTACK.type = FLYING
SKYATTACK.base_damage = 140
SKYATTACK.category = PHYSICAL
SKYATTACK.pp = 5
SKYATTACK.accuracy = 90
SKYATTACK.priority = 0
SKYATTACK.target = 'Other'
SKYATTACK.additional_effect_chance = 30
SKYATTACK.description = "A second-turn attack move where critical hits land more easily. It may also make the target flinch."

#################
### BRAVEBIRD ###
#################

BRAVEBIRD = Move()
BRAVEBIRD.name = "Brave Bird"
BRAVEBIRD.type = FLYING
BRAVEBIRD.base_damage = 120
BRAVEBIRD.category = PHYSICAL
BRAVEBIRD.pp = 15
BRAVEBIRD.accuracy = 100
BRAVEBIRD.priority = 0
BRAVEBIRD.target = 'Other'
BRAVEBIRD.additional_effect_chance = 0
BRAVEBIRD.description = "The user tucks in its wings and charges from a low altitude. The user also takes serious damage."

####################
### DRAGONASCENT ###
####################

DRAGONASCENT = Move()
DRAGONASCENT.name = "Dragon Ascent"
DRAGONASCENT.type = FLYING
DRAGONASCENT.base_damage = 120
DRAGONASCENT.category = PHYSICAL
DRAGONASCENT.pp = 5
DRAGONASCENT.accuracy = 100
DRAGONASCENT.priority = 0
DRAGONASCENT.target = 'NearOther'
DRAGONASCENT.additional_effect_chance = 0
DRAGONASCENT.description = "The user soars upward and drops at high speeds. Its Defense and Sp. Def stats are lowered."

#################
### HURRICANE ###
#################

HURRICANE = Move()
HURRICANE.name = "Hurricane"
HURRICANE.type = FLYING
HURRICANE.base_damage = 110
HURRICANE.category = SPECIAL
HURRICANE.pp = 10
HURRICANE.accuracy = 70
HURRICANE.priority = 0
HURRICANE.target = 'Other'
HURRICANE.additional_effect_chance = 30
HURRICANE.description = "The user wraps its foe in a fierce wind that flies up into the sky. It may also confuse the foe."

#################
### AEROBLAST ###
#################

AEROBLAST = Move()
AEROBLAST.name = "Aeroblast"
AEROBLAST.type = FLYING
AEROBLAST.base_damage = 100
AEROBLAST.category = SPECIAL
AEROBLAST.pp = 5
AEROBLAST.accuracy = 95
AEROBLAST.priority = 0
AEROBLAST.target = 'Other'
AEROBLAST.additional_effect_chance = 0
AEROBLAST.description = "A vortex of air is shot at the target to inflict damage. Critical hits land more easily."

#################
### BEAKBLAST ###
#################

BEAKBLAST = Move()
BEAKBLAST.name = "Beak Blast"
BEAKBLAST.type = FLYING
BEAKBLAST.base_damage = 100
BEAKBLAST.category = PHYSICAL
BEAKBLAST.pp = 15
BEAKBLAST.accuracy = 100
BEAKBLAST.priority = 0
BEAKBLAST.target = 'NearOther'
BEAKBLAST.additional_effect_chance = 0
BEAKBLAST.description = "The user heats up its beak before attacking. Making contact in this time results in a burn."

###########
### FLY ###
###########

FLY = Move()
FLY.name = "Fly"
FLY.type = FLYING
FLY.base_damage = 90
FLY.category = PHYSICAL
FLY.pp = 15
FLY.accuracy = 95
FLY.priority = 0
FLY.target = 'Other'
FLY.additional_effect_chance = 0
FLY.description = "The user soars, then strikes on the second turn. It can also be used for flying to any familiar town."

##############
### BOUNCE ###
##############

BOUNCE = Move()
BOUNCE.name = "Bounce"
BOUNCE.type = FLYING
BOUNCE.base_damage = 85
BOUNCE.category = PHYSICAL
BOUNCE.pp = 5
BOUNCE.accuracy = 85
BOUNCE.priority = 0
BOUNCE.target = 'Other'
BOUNCE.additional_effect_chance = 30
BOUNCE.description = "The user bounces up high, then drops on the foe on the second turn. It may also paralyze the foe."

#################
### DRILLPECK ###
#################

DRILLPECK = Move()
DRILLPECK.name = "Drill Peck"
DRILLPECK.type = FLYING
DRILLPECK.base_damage = 80
DRILLPECK.category = PHYSICAL
DRILLPECK.pp = 20
DRILLPECK.accuracy = 100
DRILLPECK.priority = 0
DRILLPECK.target = 'Other'
DRILLPECK.additional_effect_chance = 0
DRILLPECK.description = "A corkscrewing attack with the sharp beak acting as a drill."

####################
### OBLIVIONWING ###
####################

OBLIVIONWING = Move()
OBLIVIONWING.name = "Oblivion Wing"
OBLIVIONWING.type = FLYING
OBLIVIONWING.base_damage = 80
OBLIVIONWING.category = SPECIAL
OBLIVIONWING.pp = 10
OBLIVIONWING.accuracy = 100
OBLIVIONWING.priority = 0
OBLIVIONWING.target = 'Other'
OBLIVIONWING.additional_effect_chance = 0
OBLIVIONWING.description = "The user absorbs its targets HP. The users HP is restored by over half of the damage dealt."

################
### AIRSLASH ###
################

AIRSLASH = Move()
AIRSLASH.name = "Air Slash"
AIRSLASH.type = FLYING
AIRSLASH.base_damage = 75
AIRSLASH.category = SPECIAL
AIRSLASH.pp = 15
AIRSLASH.accuracy = 95
AIRSLASH.priority = 0
AIRSLASH.target = 'Other'
AIRSLASH.additional_effect_chance = 30
AIRSLASH.description = "The user attacks with a blade of air that slices even the sky. It may also make the target flinch."

###############
### CHATTER ###
###############

CHATTER = Move()
CHATTER.name = "Chatter"
CHATTER.type = FLYING
CHATTER.base_damage = 65
CHATTER.category = SPECIAL
CHATTER.pp = 20
CHATTER.accuracy = 100
CHATTER.priority = 0
CHATTER.target = 'Other'
CHATTER.additional_effect_chance = 100
CHATTER.description = "The user attacks using a sound wave based on words it has learned. It may also confuse the target."

#################
### AERIALACE ###
#################

AERIALACE = Move()
AERIALACE.name = "Aerial Ace"
AERIALACE.type = FLYING
AERIALACE.base_damage = 60
AERIALACE.category = PHYSICAL
AERIALACE.pp = 20
AERIALACE.accuracy = 0
AERIALACE.priority = 0
AERIALACE.target = 'Other'
AERIALACE.additional_effect_chance = 0
AERIALACE.description = "The user confounds the foe with speed, then slashes. The attack lands without fail."

#################
### AIRCUTTER ###
#################

AIRCUTTER = Move()
AIRCUTTER.name = "Air Cutter"
AIRCUTTER.type = FLYING
AIRCUTTER.base_damage = 60
AIRCUTTER.category = SPECIAL
AIRCUTTER.pp = 25
AIRCUTTER.accuracy = 95
AIRCUTTER.priority = 0
AIRCUTTER.target = 'AllNearFoes'
AIRCUTTER.additional_effect_chance = 0
AIRCUTTER.description = "The user launches razor-like wind to slash the opposing team. Critical hits land more easily."

#############
### PLUCK ###
#############

PLUCK = Move()
PLUCK.name = "Pluck"
PLUCK.type = FLYING
PLUCK.base_damage = 60
PLUCK.category = PHYSICAL
PLUCK.pp = 20
PLUCK.accuracy = 100
PLUCK.priority = 0
PLUCK.target = 'Other'
PLUCK.additional_effect_chance = 0
PLUCK.description = "The user pecks the target. If the target is holding a Berry, the user eats it and gains its effect."

###############
### SKYDROP ###
###############

SKYDROP = Move()
SKYDROP.name = "Sky Drop"
SKYDROP.type = FLYING
SKYDROP.base_damage = 60
SKYDROP.category = PHYSICAL
SKYDROP.pp = 10
SKYDROP.accuracy = 100
SKYDROP.priority = 0
SKYDROP.target = 'Other'
SKYDROP.additional_effect_chance = 0
SKYDROP.description = "The user takes the foe into the sky, then drops it on the next turn. The foe cannot attack while airborne."

##################
### WINGATTACK ###
##################

WINGATTACK = Move()
WINGATTACK.name = "Wing Attack"
WINGATTACK.type = FLYING
WINGATTACK.base_damage = 60
WINGATTACK.category = PHYSICAL
WINGATTACK.pp = 35
WINGATTACK.accuracy = 100
WINGATTACK.priority = 0
WINGATTACK.target = 'Other'
WINGATTACK.additional_effect_chance = 0
WINGATTACK.description = "The target is struck with large, imposing wings spread wide to inflict damage."

##################
### ACROBATICS ###
##################

ACROBATICS = Move()
ACROBATICS.name = "Acrobatics"
ACROBATICS.type = FLYING
ACROBATICS.base_damage = 55
ACROBATICS.category = PHYSICAL
ACROBATICS.pp = 15
ACROBATICS.accuracy = 100
ACROBATICS.priority = 0
ACROBATICS.target = 'Other'
ACROBATICS.additional_effect_chance = 0
ACROBATICS.description = "The user nimbly strikes the foe. This attack does more damage if the user is not holding an item."

############
### GUST ###
############

GUST = Move()
GUST.name = "Gust"
GUST.type = FLYING
GUST.base_damage = 40
GUST.category = SPECIAL
GUST.pp = 35
GUST.accuracy = 100
GUST.priority = 0
GUST.target = 'Other'
GUST.additional_effect_chance = 0
GUST.description = "A gust of wind is whipped up by wings and launched at the target to inflict damage."

############
### PECK ###
############

PECK = Move()
PECK.name = "Peck"
PECK.type = FLYING
PECK.base_damage = 35
PECK.category = PHYSICAL
PECK.pp = 35
PECK.accuracy = 100
PECK.priority = 0
PECK.target = 'Other'
PECK.additional_effect_chance = 0
PECK.description = "The target is jabbed with a sharply pointed beak or horn."

#############
### DEFOG ###
#############

DEFOG = Move()
DEFOG.name = "Defog"
DEFOG.type = FLYING
DEFOG.base_damage = 0
DEFOG.category = STATUS
DEFOG.pp = 15
DEFOG.accuracy = 0
DEFOG.priority = 0
DEFOG.target = 'NearOther'
DEFOG.additional_effect_chance = 0
DEFOG.description = "A strong wind blows away the foes obstacles such as Light Screen. It also lowers their evasion."

####################
### FEATHERDANCE ###
####################

FEATHERDANCE = Move()
FEATHERDANCE.name = "Feather Dance"
FEATHERDANCE.type = FLYING
FEATHERDANCE.base_damage = 0
FEATHERDANCE.category = STATUS
FEATHERDANCE.pp = 15
FEATHERDANCE.accuracy = 100
FEATHERDANCE.priority = 0
FEATHERDANCE.target = 'NearOther'
FEATHERDANCE.additional_effect_chance = 0
FEATHERDANCE.description = "The user covers the targets body with a mass of down that harshly lowers its Attack stat."

##################
### MIRRORMOVE ###
##################

MIRRORMOVE = Move()
MIRRORMOVE.name = "Mirror Move"
MIRRORMOVE.type = FLYING
MIRRORMOVE.base_damage = 0
MIRRORMOVE.category = STATUS
MIRRORMOVE.pp = 20
MIRRORMOVE.accuracy = 0
MIRRORMOVE.priority = 0
MIRRORMOVE.target = 'NearOther'
MIRRORMOVE.additional_effect_chance = 0
MIRRORMOVE.description = "The user counters the target by mimicking the targets last move."

#############
### ROOST ###
#############

ROOST = Move()
ROOST.name = "Roost"
ROOST.type = FLYING
ROOST.base_damage = 0
ROOST.category = STATUS
ROOST.pp = 10
ROOST.accuracy = 0
ROOST.priority = 0
ROOST.target = 'User'
ROOST.additional_effect_chance = 0
ROOST.description = "The user lands and rests its body. It restores the users HP by up to half of its max HP."

################
### TAILWIND ###
################

TAILWIND = Move()
TAILWIND.name = "Tailwind"
TAILWIND.type = FLYING
TAILWIND.base_damage = 0
TAILWIND.category = STATUS
TAILWIND.pp = 15
TAILWIND.accuracy = 0
TAILWIND.priority = 0
TAILWIND.target = 'UserSide'
TAILWIND.additional_effect_chance = 0
TAILWIND.description = "The user whips up a turbulent whirlwind that ups the Speed of all party Pokémon for four turns."

###################
### SHADOWFORCE ###
###################

SHADOWFORCE = Move()
SHADOWFORCE.name = "Shadow Force"
SHADOWFORCE.type = GHOST
SHADOWFORCE.base_damage = 120
SHADOWFORCE.category = PHYSICAL
SHADOWFORCE.pp = 5
SHADOWFORCE.accuracy = 100
SHADOWFORCE.priority = 0
SHADOWFORCE.target = 'NearOther'
SHADOWFORCE.additional_effect_chance = 0
SHADOWFORCE.description = "The user disappears, then strikes the foe on the second turn. It hits even if the foe protects itself."

#####################
### MOONGEISTBEAM ###
#####################

MOONGEISTBEAM = Move()
MOONGEISTBEAM.name = "Moongeist Beam"
MOONGEISTBEAM.type = GHOST
MOONGEISTBEAM.base_damage = 100
MOONGEISTBEAM.category = SPECIAL
MOONGEISTBEAM.pp = 5
MOONGEISTBEAM.accuracy = 100
MOONGEISTBEAM.priority = 0
MOONGEISTBEAM.target = 'NearOther'
MOONGEISTBEAM.additional_effect_chance = 0
MOONGEISTBEAM.description = "The user emits a sinister ray. This move can be used on the target regardless of its Abilities."

####################
### PHANTOMFORCE ###
####################

PHANTOMFORCE = Move()
PHANTOMFORCE.name = "Phantom Force"
PHANTOMFORCE.type = GHOST
PHANTOMFORCE.base_damage = 90
PHANTOMFORCE.category = PHYSICAL
PHANTOMFORCE.pp = 10
PHANTOMFORCE.accuracy = 100
PHANTOMFORCE.priority = 0
PHANTOMFORCE.target = 'NearOther'
PHANTOMFORCE.additional_effect_chance = 0
PHANTOMFORCE.description = "The user vanishes somewhere, then strikes on the next turn. Hits through protections."

#####################
### SPECTRALTHIEF ###
#####################

SPECTRALTHIEF = Move()
SPECTRALTHIEF.name = "Spectral Thief"
SPECTRALTHIEF.type = GHOST
SPECTRALTHIEF.base_damage = 90
SPECTRALTHIEF.category = PHYSICAL
SPECTRALTHIEF.pp = 10
SPECTRALTHIEF.accuracy = 100
SPECTRALTHIEF.priority = 0
SPECTRALTHIEF.target = 'NearOther'
SPECTRALTHIEF.additional_effect_chance = 0
SPECTRALTHIEF.description = "The user hides in the targets shadow, steals the targets stat boosts, and then attacks."

##################
### SHADOWBONE ###
##################

SHADOWBONE = Move()
SHADOWBONE.name = "Shadow Bone"
SHADOWBONE.type = GHOST
SHADOWBONE.base_damage = 85
SHADOWBONE.category = PHYSICAL
SHADOWBONE.pp = 10
SHADOWBONE.accuracy = 100
SHADOWBONE.priority = 0
SHADOWBONE.target = 'NearOther'
SHADOWBONE.additional_effect_chance = 20
SHADOWBONE.description = "The user beats the target with a bone containing a spirit. May lower the targets Defense stat."

##################
### SHADOWBALL ###
##################

SHADOWBALL = Move()
SHADOWBALL.name = "Shadow Ball"
SHADOWBALL.type = GHOST
SHADOWBALL.base_damage = 80
SHADOWBALL.category = SPECIAL
SHADOWBALL.pp = 15
SHADOWBALL.accuracy = 100
SHADOWBALL.priority = 0
SHADOWBALL.target = 'NearOther'
SHADOWBALL.additional_effect_chance = 20
SHADOWBALL.description = "The user hurls a shadowy blob at the target. It may also lower the targets Sp. Def stat."

#####################
### SPIRITSHACKLE ###
#####################

SPIRITSHACKLE = Move()
SPIRITSHACKLE.name = "Spirit Shackle"
SPIRITSHACKLE.type = GHOST
SPIRITSHACKLE.base_damage = 80
SPIRITSHACKLE.category = PHYSICAL
SPIRITSHACKLE.pp = 10
SPIRITSHACKLE.accuracy = 100
SPIRITSHACKLE.priority = 0
SPIRITSHACKLE.target = 'NearOther'
SPIRITSHACKLE.additional_effect_chance = 100
SPIRITSHACKLE.description = "The user attacks while also stitching the targets shadow to the ground to prevent it fleeing."

##################
### SHADOWCLAW ###
##################

SHADOWCLAW = Move()
SHADOWCLAW.name = "Shadow Claw"
SHADOWCLAW.type = GHOST
SHADOWCLAW.base_damage = 70
SHADOWCLAW.category = PHYSICAL
SHADOWCLAW.pp = 15
SHADOWCLAW.accuracy = 100
SHADOWCLAW.priority = 0
SHADOWCLAW.target = 'NearOther'
SHADOWCLAW.additional_effect_chance = 0
SHADOWCLAW.description = "The user slashes with a sharp claw made from shadows. Critical hits land more easily."

###########
### HEX ###
###########

HEX = Move()
HEX.name = "Hex"
HEX.type = GHOST
HEX.base_damage = 65
HEX.category = SPECIAL
HEX.pp = 10
HEX.accuracy = 100
HEX.priority = 0
HEX.target = 'NearOther'
HEX.additional_effect_chance = 0
HEX.description = "This relentless attack does massive damage to a target affected by status problems."

###################
### OMINOUSWIND ###
###################

OMINOUSWIND = Move()
OMINOUSWIND.name = "Ominous Wind"
OMINOUSWIND.type = GHOST
OMINOUSWIND.base_damage = 60
OMINOUSWIND.category = SPECIAL
OMINOUSWIND.pp = 5
OMINOUSWIND.accuracy = 100
OMINOUSWIND.priority = 0
OMINOUSWIND.target = 'NearOther'
OMINOUSWIND.additional_effect_chance = 10
OMINOUSWIND.description = "The user blasts the target with a gust of repulsive wind. It may also raise all the users stats at once."

###################
### SHADOWPUNCH ###
###################

SHADOWPUNCH = Move()
SHADOWPUNCH.name = "Shadow Punch"
SHADOWPUNCH.type = GHOST
SHADOWPUNCH.base_damage = 60
SHADOWPUNCH.category = PHYSICAL
SHADOWPUNCH.pp = 20
SHADOWPUNCH.accuracy = 0
SHADOWPUNCH.priority = 0
SHADOWPUNCH.target = 'NearOther'
SHADOWPUNCH.additional_effect_chance = 0
SHADOWPUNCH.description = "The user throws a punch from the shadows. The punch lands without fail."

###################
### SHADOWSNEAK ###
###################

SHADOWSNEAK = Move()
SHADOWSNEAK.name = "Shadow Sneak"
SHADOWSNEAK.type = GHOST
SHADOWSNEAK.base_damage = 40
SHADOWSNEAK.category = PHYSICAL
SHADOWSNEAK.pp = 30
SHADOWSNEAK.accuracy = 100
SHADOWSNEAK.priority = 1
SHADOWSNEAK.target = 'NearOther'
SHADOWSNEAK.additional_effect_chance = 0
SHADOWSNEAK.description = "The user extends its shadow and attacks the target from behind. This move always goes first."

################
### ASTONISH ###
################

ASTONISH = Move()
ASTONISH.name = "Astonish"
ASTONISH.type = GHOST
ASTONISH.base_damage = 30
ASTONISH.category = PHYSICAL
ASTONISH.pp = 15
ASTONISH.accuracy = 100
ASTONISH.priority = 0
ASTONISH.target = 'NearOther'
ASTONISH.additional_effect_chance = 30
ASTONISH.description = "The user attacks the target while shouting in a startling fashion. It may also make the target flinch."

############
### LICK ###
############

LICK = Move()
LICK.name = "Lick"
LICK.type = GHOST
LICK.base_damage = 30
LICK.category = PHYSICAL
LICK.pp = 30
LICK.accuracy = 100
LICK.priority = 0
LICK.target = 'NearOther'
LICK.additional_effect_chance = 30
LICK.description = "The target is licked with a long tongue, causing damage. It may also leave the target with paralysis."

##################
### NIGHTSHADE ###
##################

NIGHTSHADE = Move()
NIGHTSHADE.name = "Night Shade"
NIGHTSHADE.type = GHOST
NIGHTSHADE.base_damage = 1
NIGHTSHADE.category = SPECIAL
NIGHTSHADE.pp = 15
NIGHTSHADE.accuracy = 100
NIGHTSHADE.priority = 0
NIGHTSHADE.target = 'NearOther'
NIGHTSHADE.additional_effect_chance = 0
NIGHTSHADE.description = "The user makes the foe see a frightening mirage. It inflicts damage matching the users level."

##################
### CONFUSERAY ###
##################

CONFUSERAY = Move()
CONFUSERAY.name = "Confuse Ray"
CONFUSERAY.type = GHOST
CONFUSERAY.base_damage = 0
CONFUSERAY.category = STATUS
CONFUSERAY.pp = 10
CONFUSERAY.accuracy = 100
CONFUSERAY.priority = 0
CONFUSERAY.target = 'NearOther'
CONFUSERAY.additional_effect_chance = 0
CONFUSERAY.description = "The target is exposed to a sinister ray that triggers confusion."

#############
### CURSE ###
#############

CURSE = Move()
CURSE.name = "Curse"
CURSE.type = GHOST
CURSE.base_damage = 0
CURSE.category = STATUS
CURSE.pp = 10
CURSE.accuracy = 0
CURSE.priority = 0
CURSE.target = 'User'
CURSE.additional_effect_chance = 0
CURSE.description = "A move that works differently for the Ghost type than for all the other types."

###################
### DESTINYBOND ###
###################

DESTINYBOND = Move()
DESTINYBOND.name = "Destiny Bond"
DESTINYBOND.type = GHOST
DESTINYBOND.base_damage = 0
DESTINYBOND.category = STATUS
DESTINYBOND.pp = 5
DESTINYBOND.accuracy = 0
DESTINYBOND.priority = 0
DESTINYBOND.target = 'User'
DESTINYBOND.additional_effect_chance = 0
DESTINYBOND.description = "When this move is used, if the user faints, the foe that landed the knockout hit also faints."

##############
### GRUDGE ###
##############

GRUDGE = Move()
GRUDGE.name = "Grudge"
GRUDGE.type = GHOST
GRUDGE.base_damage = 0
GRUDGE.category = STATUS
GRUDGE.pp = 5
GRUDGE.accuracy = 0
GRUDGE.priority = 0
GRUDGE.target = 'User'
GRUDGE.additional_effect_chance = 0
GRUDGE.description = "If the user faints, the users grudge fully depletes the PP of the foes move that knocked it out."

#################
### NIGHTMARE ###
#################

NIGHTMARE = Move()
NIGHTMARE.name = "Nightmare"
NIGHTMARE.type = GHOST
NIGHTMARE.base_damage = 0
NIGHTMARE.category = STATUS
NIGHTMARE.pp = 15
NIGHTMARE.accuracy = 100
NIGHTMARE.priority = 0
NIGHTMARE.target = 'NearOther'
NIGHTMARE.additional_effect_chance = 0
NIGHTMARE.description = "A sleeping target sees a nightmare that inflicts some damage every turn."

#############
### SPITE ###
#############

SPITE = Move()
SPITE.name = "Spite"
SPITE.type = GHOST
SPITE.base_damage = 0
SPITE.category = STATUS
SPITE.pp = 10
SPITE.accuracy = 100
SPITE.priority = 0
SPITE.target = 'NearOther'
SPITE.additional_effect_chance = 0
SPITE.description = "The user unleashes its grudge on the move last used by the target by cutting 4 PP from it."

####################
### TRICKORTREAT ###
####################

TRICKORTREAT = Move()
TRICKORTREAT.name = "Trick-or-Treat"
TRICKORTREAT.type = GHOST
TRICKORTREAT.base_damage = 0
TRICKORTREAT.category = STATUS
TRICKORTREAT.pp = 20
TRICKORTREAT.accuracy = 100
TRICKORTREAT.priority = 0
TRICKORTREAT.target = 'NearOther'
TRICKORTREAT.additional_effect_chance = 0
TRICKORTREAT.description = "The user takes the target trick-or-treating. This adds Ghost type to the targets type."

###################
### FRENZYPLANT ###
###################

FRENZYPLANT = Move()
FRENZYPLANT.name = "Frenzy Plant"
FRENZYPLANT.type = GRASS
FRENZYPLANT.base_damage = 150
FRENZYPLANT.category = SPECIAL
FRENZYPLANT.pp = 5
FRENZYPLANT.accuracy = 90
FRENZYPLANT.priority = 0
FRENZYPLANT.target = 'NearOther'
FRENZYPLANT.additional_effect_chance = 0
FRENZYPLANT.description = "The user slams the target with an enormous tree. The user cant move on the next turn."

#################
### LEAFSTORM ###
#################

LEAFSTORM = Move()
LEAFSTORM.name = "Leaf Storm"
LEAFSTORM.type = GRASS
LEAFSTORM.base_damage = 130
LEAFSTORM.category = SPECIAL
LEAFSTORM.pp = 5
LEAFSTORM.accuracy = 90
LEAFSTORM.priority = 0
LEAFSTORM.target = 'NearOther'
LEAFSTORM.additional_effect_chance = 0
LEAFSTORM.description = "A storm of sharp is whipped up. The attacks recoil harshly reduces the users Sp. Atk stat."

##################
### SOLARBLADE ###
##################

SOLARBLADE = Move()
SOLARBLADE.name = "Solar Blade"
SOLARBLADE.type = GRASS
SOLARBLADE.base_damage = 125
SOLARBLADE.category = PHYSICAL
SOLARBLADE.pp = 10
SOLARBLADE.accuracy = 100
SOLARBLADE.priority = 0
SOLARBLADE.target = 'NearOther'
SOLARBLADE.additional_effect_chance = 0
SOLARBLADE.description = "The user gathers light energy into a blade, attacking the target on the next turn."

##################
### PETALDANCE ###
##################

PETALDANCE = Move()
PETALDANCE.name = "Petal Dance"
PETALDANCE.type = GRASS
PETALDANCE.base_damage = 120
PETALDANCE.category = SPECIAL
PETALDANCE.pp = 10
PETALDANCE.accuracy = 100
PETALDANCE.priority = 0
PETALDANCE.target = 'RandomNearFoe'
PETALDANCE.additional_effect_chance = 0
PETALDANCE.description = "The user attacks by scattering petals for two to three turns. The user then becomes confused."

#################
### POWERWHIP ###
#################

POWERWHIP = Move()
POWERWHIP.name = "Power Whip"
POWERWHIP.type = GRASS
POWERWHIP.base_damage = 120
POWERWHIP.category = PHYSICAL
POWERWHIP.pp = 10
POWERWHIP.accuracy = 85
POWERWHIP.priority = 0
POWERWHIP.target = 'NearOther'
POWERWHIP.additional_effect_chance = 0
POWERWHIP.description = "The user violently whirls its vines or tentacles to harshly lash the target."

#################
### SEEDFLARE ###
#################

SEEDFLARE = Move()
SEEDFLARE.name = "Seed Flare"
SEEDFLARE.type = GRASS
SEEDFLARE.base_damage = 120
SEEDFLARE.category = SPECIAL
SEEDFLARE.pp = 5
SEEDFLARE.accuracy = 85
SEEDFLARE.priority = 0
SEEDFLARE.target = 'NearOther'
SEEDFLARE.additional_effect_chance = 40
SEEDFLARE.description = "The user generates a shock wave from within its body. It may harshly lower the targets Sp. Def."

#################
### SOLARBEAM ###
#################

SOLARBEAM = Move()
SOLARBEAM.name = "Solar Beam"
SOLARBEAM.type = GRASS
SOLARBEAM.base_damage = 120
SOLARBEAM.category = SPECIAL
SOLARBEAM.pp = 10
SOLARBEAM.accuracy = 100
SOLARBEAM.priority = 0
SOLARBEAM.target = 'NearOther'
SOLARBEAM.additional_effect_chance = 0
SOLARBEAM.description = "A two-turn attack. The user gathers light, then blasts a bundled beam on the second turn."

##################
### WOODHAMMER ###
##################

WOODHAMMER = Move()
WOODHAMMER.name = "Wood Hammer"
WOODHAMMER.type = GRASS
WOODHAMMER.base_damage = 120
WOODHAMMER.category = PHYSICAL
WOODHAMMER.pp = 15
WOODHAMMER.accuracy = 100
WOODHAMMER.priority = 0
WOODHAMMER.target = 'NearOther'
WOODHAMMER.additional_effect_chance = 0
WOODHAMMER.description = "The user slams its rugged body into the target to attack. The user also sustains serious damage."

##################
### ENERGYBALL ###
##################

ENERGYBALL = Move()
ENERGYBALL.name = "Energy Ball"
ENERGYBALL.type = GRASS
ENERGYBALL.base_damage = 90
ENERGYBALL.category = SPECIAL
ENERGYBALL.pp = 10
ENERGYBALL.accuracy = 100
ENERGYBALL.priority = 0
ENERGYBALL.target = 'NearOther'
ENERGYBALL.additional_effect_chance = 10
ENERGYBALL.description = "The user draws power from nature and fires it at the target. It may also lower the targets Sp. Def."

#################
### LEAFBLADE ###
#################

LEAFBLADE = Move()
LEAFBLADE.name = "Leaf Blade"
LEAFBLADE.type = GRASS
LEAFBLADE.base_damage = 90
LEAFBLADE.category = PHYSICAL
LEAFBLADE.pp = 15
LEAFBLADE.accuracy = 100
LEAFBLADE.priority = 0
LEAFBLADE.target = 'NearOther'
LEAFBLADE.additional_effect_chance = 0
LEAFBLADE.description = "The user handles a sharp leaf like a sword and attacks by slashing. It has a high critical-hit ratio."

#####################
### PETALBLIZZARD ###
#####################

PETALBLIZZARD = Move()
PETALBLIZZARD.name = "Petal Blizzard"
PETALBLIZZARD.type = GRASS
PETALBLIZZARD.base_damage = 90
PETALBLIZZARD.category = PHYSICAL
PETALBLIZZARD.pp = 15
PETALBLIZZARD.accuracy = 100
PETALBLIZZARD.priority = 0
PETALBLIZZARD.target = 'AllNearOthers'
PETALBLIZZARD.additional_effect_chance = 0
PETALBLIZZARD.description = "The user stirs up a violent petal blizzard and attacks everything around it."

###################
### GRASSPLEDGE ###
###################

GRASSPLEDGE = Move()
GRASSPLEDGE.name = "Grass Pledge"
GRASSPLEDGE.type = GRASS
GRASSPLEDGE.base_damage = 80
GRASSPLEDGE.category = SPECIAL
GRASSPLEDGE.pp = 10
GRASSPLEDGE.accuracy = 100
GRASSPLEDGE.priority = 0
GRASSPLEDGE.target = 'NearOther'
GRASSPLEDGE.additional_effect_chance = 0
GRASSPLEDGE.description = "A column of grass hits the foes. When used with its water equivalent, it creates a vast swamp."

################
### SEEDBOMB ###
################

SEEDBOMB = Move()
SEEDBOMB.name = "Seed Bomb"
SEEDBOMB.type = GRASS
SEEDBOMB.base_damage = 80
SEEDBOMB.category = PHYSICAL
SEEDBOMB.pp = 15
SEEDBOMB.accuracy = 100
SEEDBOMB.priority = 0
SEEDBOMB.target = 'NearOther'
SEEDBOMB.additional_effect_chance = 0
SEEDBOMB.description = "The user slams a barrage of hard-shelled seeds down on the target from above."

#################
### GIGADRAIN ###
#################

GIGADRAIN = Move()
GIGADRAIN.name = "Giga Drain"
GIGADRAIN.type = GRASS
GIGADRAIN.base_damage = 75
GIGADRAIN.category = SPECIAL
GIGADRAIN.pp = 10
GIGADRAIN.accuracy = 100
GIGADRAIN.priority = 0
GIGADRAIN.target = 'NearOther'
GIGADRAIN.additional_effect_chance = 0
GIGADRAIN.description = "A nutrient-draining attack. The users HP is restored by half the damage taken by the target."

#################
### HORNLEECH ###
#################

HORNLEECH = Move()
HORNLEECH.name = "Horn Leech"
HORNLEECH.type = GRASS
HORNLEECH.base_damage = 75
HORNLEECH.category = PHYSICAL
HORNLEECH.pp = 10
HORNLEECH.accuracy = 100
HORNLEECH.priority = 0
HORNLEECH.target = 'NearOther'
HORNLEECH.additional_effect_chance = 0
HORNLEECH.description = "The user drains the foes energy with its horns. The users HP is restored by half the damage inflicted."

################
### TROPKICK ###
################

TROPKICK = Move()
TROPKICK.name = "Trop Kick"
TROPKICK.type = GRASS
TROPKICK.base_damage = 70
TROPKICK.category = PHYSICAL
TROPKICK.pp = 15
TROPKICK.accuracy = 100
TROPKICK.priority = 0
TROPKICK.target = 'NearOther'
TROPKICK.additional_effect_chance = 100
TROPKICK.description = "The user lands an intense tropical kick on the target. This also lowers the targets Attack stat."

###################
### LEAFTORNADO ###
###################

LEAFTORNADO = Move()
LEAFTORNADO.name = "Leaf Tornado"
LEAFTORNADO.type = GRASS
LEAFTORNADO.base_damage = 65
LEAFTORNADO.category = SPECIAL
LEAFTORNADO.pp = 10
LEAFTORNADO.accuracy = 90
LEAFTORNADO.priority = 0
LEAFTORNADO.target = 'NearOther'
LEAFTORNADO.additional_effect_chance = 50
LEAFTORNADO.description = "The user attacks its foe by encircling it in sharp leaves. This attack may also lower the foes accuracy."

###################
### MAGICALLEAF ###
###################

MAGICALLEAF = Move()
MAGICALLEAF.name = "Magical Leaf"
MAGICALLEAF.type = GRASS
MAGICALLEAF.base_damage = 60
MAGICALLEAF.category = SPECIAL
MAGICALLEAF.pp = 20
MAGICALLEAF.accuracy = 0
MAGICALLEAF.priority = 0
MAGICALLEAF.target = 'NearOther'
MAGICALLEAF.additional_effect_chance = 0
MAGICALLEAF.description = "The user scatters curious leaves that chase the target. This attack will not miss."

#################
### NEEDLEARM ###
#################

NEEDLEARM = Move()
NEEDLEARM.name = "Needle Arm"
NEEDLEARM.type = GRASS
NEEDLEARM.base_damage = 60
NEEDLEARM.category = PHYSICAL
NEEDLEARM.pp = 15
NEEDLEARM.accuracy = 100
NEEDLEARM.priority = 0
NEEDLEARM.target = 'NearOther'
NEEDLEARM.additional_effect_chance = 30
NEEDLEARM.description = "The user attacks by wildly swinging its thorny arms. It may also make the target flinch."

#################
### RAZORLEAF ###
#################

RAZORLEAF = Move()
RAZORLEAF.name = "Razor Leaf"
RAZORLEAF.type = GRASS
RAZORLEAF.base_damage = 55
RAZORLEAF.category = PHYSICAL
RAZORLEAF.pp = 25
RAZORLEAF.accuracy = 95
RAZORLEAF.priority = 0
RAZORLEAF.target = 'AllNearFoes'
RAZORLEAF.additional_effect_chance = 0
RAZORLEAF.description = "Sharp-edged leaves are launched to slash at the opposing team. Critical hits land more easily."

################
### VINEWHIP ###
################

VINEWHIP = Move()
VINEWHIP.name = "Vine Whip"
VINEWHIP.type = GRASS
VINEWHIP.base_damage = 45
VINEWHIP.category = PHYSICAL
VINEWHIP.pp = 25
VINEWHIP.accuracy = 100
VINEWHIP.priority = 0
VINEWHIP.target = 'NearOther'
VINEWHIP.additional_effect_chance = 0
VINEWHIP.description = "The target is struck with slender, whiplike vines to inflict damage."

###############
### LEAFAGE ###
###############

LEAFAGE = Move()
LEAFAGE.name = "Leafage"
LEAFAGE.type = GRASS
LEAFAGE.base_damage = 40
LEAFAGE.category = PHYSICAL
LEAFAGE.pp = 40
LEAFAGE.accuracy = 100
LEAFAGE.priority = 0
LEAFAGE.target = 'NearOther'
LEAFAGE.additional_effect_chance = 0
LEAFAGE.description = "The user attacks by pelting the target with leaves."

#################
### MEGADRAIN ###
#################

MEGADRAIN = Move()
MEGADRAIN.name = "Mega Drain"
MEGADRAIN.type = GRASS
MEGADRAIN.base_damage = 40
MEGADRAIN.category = SPECIAL
MEGADRAIN.pp = 15
MEGADRAIN.accuracy = 100
MEGADRAIN.priority = 0
MEGADRAIN.target = 'NearOther'
MEGADRAIN.additional_effect_chance = 0
MEGADRAIN.description = "A nutrient-draining attack. The users HP is restored by half the damage taken by the target."

##################
### BULLETSEED ###
##################

BULLETSEED = Move()
BULLETSEED.name = "Bullet Seed"
BULLETSEED.type = GRASS
BULLETSEED.base_damage = 25
BULLETSEED.category = PHYSICAL
BULLETSEED.pp = 30
BULLETSEED.accuracy = 100
BULLETSEED.priority = 0
BULLETSEED.target = 'NearOther'
BULLETSEED.additional_effect_chance = 0
BULLETSEED.description = "The user forcefully shoots seeds at the target. Two to five seeds are shot in rapid succession."

##############
### ABSORB ###
##############

ABSORB = Move()
ABSORB.name = "Absorb"
ABSORB.type = GRASS
ABSORB.base_damage = 20
ABSORB.category = SPECIAL
ABSORB.pp = 25
ABSORB.accuracy = 100
ABSORB.priority = 0
ABSORB.target = 'NearOther'
ABSORB.additional_effect_chance = 0
ABSORB.description = "A nutrient-draining attack. The users HP is restored by half the damage taken by the target."

#################
### GRASSKNOT ###
#################

GRASSKNOT = Move()
GRASSKNOT.name = "Grass Knot"
GRASSKNOT.type = GRASS
GRASSKNOT.base_damage = 1
GRASSKNOT.category = SPECIAL
GRASSKNOT.pp = 20
GRASSKNOT.accuracy = 100
GRASSKNOT.priority = 0
GRASSKNOT.target = 'NearOther'
GRASSKNOT.additional_effect_chance = 0
GRASSKNOT.description = "The user snares the target with grass and trips it. The heavier the target, the greater the damage."

####################
### AROMATHERAPY ###
####################

AROMATHERAPY = Move()
AROMATHERAPY.name = "Aromatherapy"
AROMATHERAPY.type = GRASS
AROMATHERAPY.base_damage = 0
AROMATHERAPY.category = STATUS
AROMATHERAPY.pp = 5
AROMATHERAPY.accuracy = 0
AROMATHERAPY.priority = 0
AROMATHERAPY.target = 'UserAndAllies'
AROMATHERAPY.additional_effect_chance = 0
AROMATHERAPY.description = "The user releases a soothing scent that heals all status problems affecting the users party."

###################
### COTTONGUARD ###
###################

COTTONGUARD = Move()
COTTONGUARD.name = "Cotton Guard"
COTTONGUARD.type = GRASS
COTTONGUARD.base_damage = 0
COTTONGUARD.category = STATUS
COTTONGUARD.pp = 10
COTTONGUARD.accuracy = 0
COTTONGUARD.priority = 0
COTTONGUARD.target = 'User'
COTTONGUARD.additional_effect_chance = 0
COTTONGUARD.description = "The user protects itself by wrapping its body in soft cotton, drastically raising its Defense stat."

###################
### COTTONSPORE ###
###################

COTTONSPORE = Move()
COTTONSPORE.name = "Cotton Spore"
COTTONSPORE.type = GRASS
COTTONSPORE.base_damage = 0
COTTONSPORE.category = STATUS
COTTONSPORE.pp = 40
COTTONSPORE.accuracy = 100
COTTONSPORE.priority = 0
COTTONSPORE.target = 'AllNearFoes'
COTTONSPORE.additional_effect_chance = 0
COTTONSPORE.description = "The user releases cotton-like spores that cling to the foe, harshly reducing its Speed stat."

####################
### FORESTSCURSE ###
####################

FORESTSCURSE = Move()
FORESTSCURSE.name = "Forest's Curse"
FORESTSCURSE.type = GRASS
FORESTSCURSE.base_damage = 0
FORESTSCURSE.category = STATUS
FORESTSCURSE.pp = 20
FORESTSCURSE.accuracy = 100
FORESTSCURSE.priority = 0
FORESTSCURSE.target = 'NearOther'
FORESTSCURSE.additional_effect_chance = 0
FORESTSCURSE.description = "The user puts a forest curse on the target. The target is now Grass type as well."

####################
### GRASSWHISTLE ###
####################

GRASSWHISTLE = Move()
GRASSWHISTLE.name = "Grass Whistle"
GRASSWHISTLE.type = GRASS
GRASSWHISTLE.base_damage = 0
GRASSWHISTLE.category = STATUS
GRASSWHISTLE.pp = 15
GRASSWHISTLE.accuracy = 55
GRASSWHISTLE.priority = 0
GRASSWHISTLE.target = 'NearOther'
GRASSWHISTLE.additional_effect_chance = 0
GRASSWHISTLE.description = "The user plays a pleasant melody that lulls the target into a deep sleep."

#####################
### GRASSYTERRAIN ###
#####################

GRASSYTERRAIN = Move()
GRASSYTERRAIN.name = "Grassy Terrain"
GRASSYTERRAIN.type = GRASS
GRASSYTERRAIN.base_damage = 0
GRASSYTERRAIN.category = STATUS
GRASSYTERRAIN.pp = 10
GRASSYTERRAIN.accuracy = 0
GRASSYTERRAIN.priority = 0
GRASSYTERRAIN.target = 'BothSides'
GRASSYTERRAIN.additional_effect_chance = 0
GRASSYTERRAIN.description = "The user turns the ground to grass for five turns. Grounded Pokémon restore a little HP every turn."

###############
### INGRAIN ###
###############

INGRAIN = Move()
INGRAIN.name = "Ingrain"
INGRAIN.type = GRASS
INGRAIN.base_damage = 0
INGRAIN.category = STATUS
INGRAIN.pp = 20
INGRAIN.accuracy = 0
INGRAIN.priority = 0
INGRAIN.target = 'User'
INGRAIN.additional_effect_chance = 0
INGRAIN.description = "The user lays roots that restore its HP on every turn. Because it is rooted, it cant switch out."

#################
### LEECHSEED ###
#################

LEECHSEED = Move()
LEECHSEED.name = "Leech Seed"
LEECHSEED.type = GRASS
LEECHSEED.base_damage = 0
LEECHSEED.category = STATUS
LEECHSEED.pp = 10
LEECHSEED.accuracy = 90
LEECHSEED.priority = 0
LEECHSEED.target = 'NearOther'
LEECHSEED.additional_effect_chance = 0
LEECHSEED.description = "A seed is planted on the target. It steals some HP from the target every turn."

###################
### SLEEPPOWDER ###
###################

SLEEPPOWDER = Move()
SLEEPPOWDER.name = "Sleep Powder"
SLEEPPOWDER.type = GRASS
SLEEPPOWDER.base_damage = 0
SLEEPPOWDER.category = STATUS
SLEEPPOWDER.pp = 15
SLEEPPOWDER.accuracy = 75
SLEEPPOWDER.priority = 0
SLEEPPOWDER.target = 'NearOther'
SLEEPPOWDER.additional_effect_chance = 0
SLEEPPOWDER.description = "The user scatters a big cloud of sleep-inducing dust around the target."

###################
### SPIKYSHIELD ###
###################

SPIKYSHIELD = Move()
SPIKYSHIELD.name = "Spiky Shield"
SPIKYSHIELD.type = GRASS
SPIKYSHIELD.base_damage = 0
SPIKYSHIELD.category = STATUS
SPIKYSHIELD.pp = 10
SPIKYSHIELD.accuracy = 0
SPIKYSHIELD.priority = 4
SPIKYSHIELD.target = 'User'
SPIKYSHIELD.additional_effect_chance = 0
SPIKYSHIELD.description = "Protects the user from attacks. Also damages attackers that make contact with the user."

#############
### SPORE ###
#############

SPORE = Move()
SPORE.name = "Spore"
SPORE.type = GRASS
SPORE.base_damage = 0
SPORE.category = STATUS
SPORE.pp = 15
SPORE.accuracy = 100
SPORE.priority = 0
SPORE.target = 'NearOther'
SPORE.additional_effect_chance = 0
SPORE.description = "The user scatters bursts of spores that induce sleep."

###################
### STRENGTHSAP ###
###################

STRENGTHSAP = Move()
STRENGTHSAP.name = "Strength Sap"
STRENGTHSAP.type = GRASS
STRENGTHSAP.base_damage = 0
STRENGTHSAP.category = STATUS
STRENGTHSAP.pp = 10
STRENGTHSAP.accuracy = 100
STRENGTHSAP.priority = 0
STRENGTHSAP.target = 'NearOther'
STRENGTHSAP.additional_effect_chance = 0
STRENGTHSAP.description = "The user restores its HP by the targets Attack stat amount. Then lowers the targets Attack stat."

#################
### STUNSPORE ###
#################

STUNSPORE = Move()
STUNSPORE.name = "Stun Spore"
STUNSPORE.type = GRASS
STUNSPORE.base_damage = 0
STUNSPORE.category = STATUS
STUNSPORE.pp = 30
STUNSPORE.accuracy = 75
STUNSPORE.priority = 0
STUNSPORE.target = 'NearOther'
STUNSPORE.additional_effect_chance = 0
STUNSPORE.description = "The user scatters a cloud of paralyzing powder. It may leave the target with paralysis."

#################
### SYNTHESIS ###
#################

SYNTHESIS = Move()
SYNTHESIS.name = "Synthesis"
SYNTHESIS.type = GRASS
SYNTHESIS.base_damage = 0
SYNTHESIS.category = STATUS
SYNTHESIS.pp = 5
SYNTHESIS.accuracy = 0
SYNTHESIS.priority = 0
SYNTHESIS.target = 'User'
SYNTHESIS.additional_effect_chance = 0
SYNTHESIS.description = "The user restores its own HP. The amount of HP regained varies with the weather."

#################
### WORRYSEED ###
#################

WORRYSEED = Move()
WORRYSEED.name = "Worry Seed"
WORRYSEED.type = GRASS
WORRYSEED.base_damage = 0
WORRYSEED.category = STATUS
WORRYSEED.pp = 10
WORRYSEED.accuracy = 100
WORRYSEED.priority = 0
WORRYSEED.target = 'NearOther'
WORRYSEED.additional_effect_chance = 0
WORRYSEED.description = "A seed that causes worry is planted on the foe. It prevents sleep by making its Ability Insomnia."

#######################
### PRECIPICEBLADES ###
#######################

PRECIPICEBLADES = Move()
PRECIPICEBLADES.name = "Precipice Blades"
PRECIPICEBLADES.type = GROUND
PRECIPICEBLADES.base_damage = 120
PRECIPICEBLADES.category = PHYSICAL
PRECIPICEBLADES.pp = 10
PRECIPICEBLADES.accuracy = 85
PRECIPICEBLADES.priority = 0
PRECIPICEBLADES.target = 'AllNearFoes'
PRECIPICEBLADES.additional_effect_chance = 0
PRECIPICEBLADES.description = "The user attacks its foes by manifesting the power of the land in fearsome blades of stone."

##################
### EARTHQUAKE ###
##################

EARTHQUAKE = Move()
EARTHQUAKE.name = "Earthquake"
EARTHQUAKE.type = GROUND
EARTHQUAKE.base_damage = 100
EARTHQUAKE.category = PHYSICAL
EARTHQUAKE.pp = 10
EARTHQUAKE.accuracy = 100
EARTHQUAKE.priority = 0
EARTHQUAKE.target = 'AllNearOthers'
EARTHQUAKE.additional_effect_chance = 0
EARTHQUAKE.description = "The user sets off an earthquake that strikes every Pokémon around it."

######################
### HIGHHORSEPOWER ###
######################

HIGHHORSEPOWER = Move()
HIGHHORSEPOWER.name = "High Horsepower"
HIGHHORSEPOWER.type = GROUND
HIGHHORSEPOWER.base_damage = 95
HIGHHORSEPOWER.category = PHYSICAL
HIGHHORSEPOWER.pp = 10
HIGHHORSEPOWER.accuracy = 95
HIGHHORSEPOWER.priority = 0
HIGHHORSEPOWER.target = 'NearOther'
HIGHHORSEPOWER.additional_effect_chance = 0
HIGHHORSEPOWER.description = "The user fiercely attacks the target using its entire body."

##################
### EARTHPOWER ###
##################

EARTHPOWER = Move()
EARTHPOWER.name = "Earth Power"
EARTHPOWER.type = GROUND
EARTHPOWER.base_damage = 90
EARTHPOWER.category = SPECIAL
EARTHPOWER.pp = 10
EARTHPOWER.accuracy = 100
EARTHPOWER.priority = 0
EARTHPOWER.target = 'NearOther'
EARTHPOWER.additional_effect_chance = 10
EARTHPOWER.description = "The user makes the ground under the foe erupt with power. It may also lower the targets Sp. Def."

##################
### LANDSWRATH ###
##################

LANDSWRATH = Move()
LANDSWRATH.name = "Land's Wrath"
LANDSWRATH.type = GROUND
LANDSWRATH.base_damage = 90
LANDSWRATH.category = PHYSICAL
LANDSWRATH.pp = 10
LANDSWRATH.accuracy = 100
LANDSWRATH.priority = 0
LANDSWRATH.target = 'AllNearFoes'
LANDSWRATH.additional_effect_chance = 0
LANDSWRATH.description = "The user gathers the energy of the land and focuses that power on foes to damage them."

######################
### THOUSANDARROWS ###
######################

THOUSANDARROWS = Move()
THOUSANDARROWS.name = "Thousand Arrows"
THOUSANDARROWS.type = GROUND
THOUSANDARROWS.base_damage = 90
THOUSANDARROWS.category = PHYSICAL
THOUSANDARROWS.pp = 10
THOUSANDARROWS.accuracy = 100
THOUSANDARROWS.priority = 0
THOUSANDARROWS.target = 'AllNearFoes'
THOUSANDARROWS.additional_effect_chance = 0
THOUSANDARROWS.description = "This move also hits Pokémon that are in the air. Those Pokémon are knocked down to the ground."

#####################
### THOUSANDWAVES ###
#####################

THOUSANDWAVES = Move()
THOUSANDWAVES.name = "Thousand Waves"
THOUSANDWAVES.type = GROUND
THOUSANDWAVES.base_damage = 90
THOUSANDWAVES.category = PHYSICAL
THOUSANDWAVES.pp = 10
THOUSANDWAVES.accuracy = 100
THOUSANDWAVES.priority = 0
THOUSANDWAVES.target = 'AllNearFoes'
THOUSANDWAVES.additional_effect_chance = 0
THOUSANDWAVES.description = "The user attacks with a wave that crawls along the ground. Those it hits cant flee from battle."

###########
### DIG ###
###########

DIG = Move()
DIG.name = "Dig"
DIG.type = GROUND
DIG.base_damage = 80
DIG.category = PHYSICAL
DIG.pp = 10
DIG.accuracy = 100
DIG.priority = 0
DIG.target = 'NearOther'
DIG.additional_effect_chance = 0
DIG.description = "The user burrows, then attacks on the second turn. It can also be used to exit dungeons."

################
### DRILLRUN ###
################

DRILLRUN = Move()
DRILLRUN.name = "Drill Run"
DRILLRUN.type = GROUND
DRILLRUN.base_damage = 80
DRILLRUN.category = PHYSICAL
DRILLRUN.pp = 10
DRILLRUN.accuracy = 95
DRILLRUN.priority = 0
DRILLRUN.target = 'NearOther'
DRILLRUN.additional_effect_chance = 0
DRILLRUN.description = "The user crashes into its target while rotating its body like a drill. Critical hits land more easily."

#######################
### STOMPINGTANTRUM ###
#######################

STOMPINGTANTRUM = Move()
STOMPINGTANTRUM.name = "Stomping Tantrum"
STOMPINGTANTRUM.type = GROUND
STOMPINGTANTRUM.base_damage = 75
STOMPINGTANTRUM.category = PHYSICAL
STOMPINGTANTRUM.pp = 10
STOMPINGTANTRUM.accuracy = 100
STOMPINGTANTRUM.priority = 0
STOMPINGTANTRUM.target = 'NearOther'
STOMPINGTANTRUM.additional_effect_chance = 0
STOMPINGTANTRUM.description = "The user attacks driven by frustration. Power increases if the users previous move failed."

################
### BONECLUB ###
################

BONECLUB = Move()
BONECLUB.name = "Bone Club"
BONECLUB.type = GROUND
BONECLUB.base_damage = 65
BONECLUB.category = PHYSICAL
BONECLUB.pp = 20
BONECLUB.accuracy = 85
BONECLUB.priority = 0
BONECLUB.target = 'NearOther'
BONECLUB.additional_effect_chance = 10
BONECLUB.description = "The user clubs the target with a bone. It may also make the target flinch."

###############
### MUDBOMB ###
###############

MUDBOMB = Move()
MUDBOMB.name = "Mud Bomb"
MUDBOMB.type = GROUND
MUDBOMB.base_damage = 65
MUDBOMB.category = SPECIAL
MUDBOMB.pp = 10
MUDBOMB.accuracy = 85
MUDBOMB.priority = 0
MUDBOMB.target = 'NearOther'
MUDBOMB.additional_effect_chance = 30
MUDBOMB.description = "The user launches a hard-packed mud ball to attack. It may also lower the targets accuracy."

################
### BULLDOZE ###
################

BULLDOZE = Move()
BULLDOZE.name = "Bulldoze"
BULLDOZE.type = GROUND
BULLDOZE.base_damage = 60
BULLDOZE.category = PHYSICAL
BULLDOZE.pp = 20
BULLDOZE.accuracy = 100
BULLDOZE.priority = 0
BULLDOZE.target = 'AllNearOthers'
BULLDOZE.additional_effect_chance = 100
BULLDOZE.description = "The user strikes everything around it by stomping on the ground. It reduces hit Pokémons Speed."

###############
### MUDSHOT ###
###############

MUDSHOT = Move()
MUDSHOT.name = "Mud Shot"
MUDSHOT.type = GROUND
MUDSHOT.base_damage = 55
MUDSHOT.category = SPECIAL
MUDSHOT.pp = 15
MUDSHOT.accuracy = 95
MUDSHOT.priority = 0
MUDSHOT.target = 'NearOther'
MUDSHOT.additional_effect_chance = 100
MUDSHOT.description = "The user attacks by hurling a blob of mud at the target. It also reduces the targets Speed."

##################
### BONEMERANG ###
##################

BONEMERANG = Move()
BONEMERANG.name = "Bonemerang"
BONEMERANG.type = GROUND
BONEMERANG.base_damage = 50
BONEMERANG.category = PHYSICAL
BONEMERANG.pp = 10
BONEMERANG.accuracy = 90
BONEMERANG.priority = 0
BONEMERANG.target = 'NearOther'
BONEMERANG.additional_effect_chance = 0
BONEMERANG.description = "The user throws the bone it holds. The bone loops to hit the target twice, coming and going."

################
### SANDTOMB ###
################

SANDTOMB = Move()
SANDTOMB.name = "Sand Tomb"
SANDTOMB.type = GROUND
SANDTOMB.base_damage = 35
SANDTOMB.category = PHYSICAL
SANDTOMB.pp = 15
SANDTOMB.accuracy = 85
SANDTOMB.priority = 0
SANDTOMB.target = 'NearOther'
SANDTOMB.additional_effect_chance = 0
SANDTOMB.description = "The user traps the target inside a harshly raging sandstorm for four to five turns."

################
### BONERUSH ###
################

BONERUSH = Move()
BONERUSH.name = "Bone Rush"
BONERUSH.type = GROUND
BONERUSH.base_damage = 25
BONERUSH.category = PHYSICAL
BONERUSH.pp = 10
BONERUSH.accuracy = 90
BONERUSH.priority = 0
BONERUSH.target = 'NearOther'
BONERUSH.additional_effect_chance = 0
BONERUSH.description = "The user strikes the target with a hard bone two to five times in a row."

###############
### MUDSLAP ###
###############

MUDSLAP = Move()
MUDSLAP.name = "Mud-Slap"
MUDSLAP.type = GROUND
MUDSLAP.base_damage = 20
MUDSLAP.category = SPECIAL
MUDSLAP.pp = 10
MUDSLAP.accuracy = 100
MUDSLAP.priority = 0
MUDSLAP.target = 'NearOther'
MUDSLAP.additional_effect_chance = 100
MUDSLAP.description = "The user hurls mud in the targets face to inflict damage and lower its accuracy."

###############
### FISSURE ###
###############

FISSURE = Move()
FISSURE.name = "Fissure"
FISSURE.type = GROUND
FISSURE.base_damage = 1
FISSURE.category = PHYSICAL
FISSURE.pp = 5
FISSURE.accuracy = 30
FISSURE.priority = 0
FISSURE.target = 'NearOther'
FISSURE.additional_effect_chance = 0
FISSURE.description = "The user opens up a fissure in the ground and drops the foe in. The target instantly faints if it hits."

#################
### MAGNITUDE ###
#################

MAGNITUDE = Move()
MAGNITUDE.name = "Magnitude"
MAGNITUDE.type = GROUND
MAGNITUDE.base_damage = 1
MAGNITUDE.category = PHYSICAL
MAGNITUDE.pp = 30
MAGNITUDE.accuracy = 100
MAGNITUDE.priority = 0
MAGNITUDE.target = 'AllNearOthers'
MAGNITUDE.additional_effect_chance = 0
MAGNITUDE.description = "The user looses a ground-shaking quake affecting everyone around the user. Its power varies."

################
### MUDSPORT ###
################

MUDSPORT = Move()
MUDSPORT.name = "Mud Sport"
MUDSPORT.type = GROUND
MUDSPORT.base_damage = 0
MUDSPORT.category = STATUS
MUDSPORT.pp = 15
MUDSPORT.accuracy = 0
MUDSPORT.priority = 0
MUDSPORT.target = 'BothSides'
MUDSPORT.additional_effect_chance = 0
MUDSPORT.description = "The user covers itself with mud. It weakens Electric-type moves while the user is in the battle."

##################
### ROTOTILLER ###
##################

ROTOTILLER = Move()
ROTOTILLER.name = "Rototiller"
ROTOTILLER.type = GROUND
ROTOTILLER.base_damage = 0
ROTOTILLER.category = STATUS
ROTOTILLER.pp = 10
ROTOTILLER.accuracy = 0
ROTOTILLER.priority = 0
ROTOTILLER.target = 'AllBattlers'
ROTOTILLER.additional_effect_chance = 0
ROTOTILLER.description = "The user tills the soil to encourage plant growth. This raises the Attack and Sp. Atk of Grass types."

##################
### SANDATTACK ###
##################

SANDATTACK = Move()
SANDATTACK.name = "Sand Attack"
SANDATTACK.type = GROUND
SANDATTACK.base_damage = 0
SANDATTACK.category = STATUS
SANDATTACK.pp = 15
SANDATTACK.accuracy = 100
SANDATTACK.priority = 0
SANDATTACK.target = 'NearOther'
SANDATTACK.additional_effect_chance = 0
SANDATTACK.description = "Sand is hurled in the targets face, reducing its accuracy."

###############
### SHOREUP ###
###############

SHOREUP = Move()
SHOREUP.name = "Shore Up"
SHOREUP.type = GROUND
SHOREUP.base_damage = 0
SHOREUP.category = STATUS
SHOREUP.pp = 10
SHOREUP.accuracy = 0
SHOREUP.priority = 0
SHOREUP.target = 'User'
SHOREUP.additional_effect_chance = 0
SHOREUP.description = "The user regains up to half of its max HP. It restores more HP in a sandstorm."

##############
### SPIKES ###
##############

SPIKES = Move()
SPIKES.name = "Spikes"
SPIKES.type = GROUND
SPIKES.base_damage = 0
SPIKES.category = STATUS
SPIKES.pp = 20
SPIKES.accuracy = 0
SPIKES.priority = 0
SPIKES.target = 'FoeSide'
SPIKES.additional_effect_chance = 0
SPIKES.description = "The user lays a trap of spikes at the foes feet. The trap hurts foes that switch into battle."

###################
### FREEZESHOCK ###
###################

FREEZESHOCK = Move()
FREEZESHOCK.name = "Freeze Shock"
FREEZESHOCK.type = ICE
FREEZESHOCK.base_damage = 140
FREEZESHOCK.category = PHYSICAL
FREEZESHOCK.pp = 5
FREEZESHOCK.accuracy = 90
FREEZESHOCK.priority = 0
FREEZESHOCK.target = 'NearOther'
FREEZESHOCK.additional_effect_chance = 30
FREEZESHOCK.description = "On the second turn, the user hits the foe with electrically charged ice. It may also paralyze the foe."

###############
### ICEBURN ###
###############

ICEBURN = Move()
ICEBURN.name = "Ice Burn"
ICEBURN.type = ICE
ICEBURN.base_damage = 140
ICEBURN.category = SPECIAL
ICEBURN.pp = 5
ICEBURN.accuracy = 90
ICEBURN.priority = 0
ICEBURN.target = 'NearOther'
ICEBURN.additional_effect_chance = 30
ICEBURN.description = "On the second turn, an ultracold, freezing wind surrounds the foe. This may leave it with a burn."

################
### BLIZZARD ###
################

BLIZZARD = Move()
BLIZZARD.name = "Blizzard"
BLIZZARD.type = ICE
BLIZZARD.base_damage = 110
BLIZZARD.category = SPECIAL
BLIZZARD.pp = 5
BLIZZARD.accuracy = 70
BLIZZARD.priority = 0
BLIZZARD.target = 'AllNearFoes'
BLIZZARD.additional_effect_chance = 10
BLIZZARD.description = "A howling blizzard is summoned to strike the opposing team. It may also freeze them solid."

#################
### ICEHAMMER ###
#################

ICEHAMMER = Move()
ICEHAMMER.name = "Ice Hammer"
ICEHAMMER.type = ICE
ICEHAMMER.base_damage = 100
ICEHAMMER.category = PHYSICAL
ICEHAMMER.pp = 10
ICEHAMMER.accuracy = 90
ICEHAMMER.priority = 0
ICEHAMMER.target = 'NearOther'
ICEHAMMER.additional_effect_chance = 0
ICEHAMMER.description = "The user swings and hits with its strong, heavy fist. It lowers the users Speed, however."

###############
### ICEBEAM ###
###############

ICEBEAM = Move()
ICEBEAM.name = "Ice Beam"
ICEBEAM.type = ICE
ICEBEAM.base_damage = 90
ICEBEAM.category = SPECIAL
ICEBEAM.pp = 10
ICEBEAM.accuracy = 100
ICEBEAM.priority = 0
ICEBEAM.target = 'NearOther'
ICEBEAM.additional_effect_chance = 10
ICEBEAM.description = "The target is struck with an icy-cold beam of energy. It may also freeze the target solid."

###################
### ICICLECRASH ###
###################

ICICLECRASH = Move()
ICICLECRASH.name = "Icicle Crash"
ICICLECRASH.type = ICE
ICICLECRASH.base_damage = 85
ICICLECRASH.category = PHYSICAL
ICICLECRASH.pp = 10
ICICLECRASH.accuracy = 90
ICICLECRASH.priority = 0
ICICLECRASH.target = 'NearOther'
ICICLECRASH.additional_effect_chance = 30
ICICLECRASH.description = "The user attacks by harshly dropping an icicle onto the foe. It may also make the target flinch."

################
### ICEPUNCH ###
################

ICEPUNCH = Move()
ICEPUNCH.name = "Ice Punch"
ICEPUNCH.type = ICE
ICEPUNCH.base_damage = 75
ICEPUNCH.category = PHYSICAL
ICEPUNCH.pp = 15
ICEPUNCH.accuracy = 100
ICEPUNCH.priority = 0
ICEPUNCH.target = 'NearOther'
ICEPUNCH.additional_effect_chance = 10
ICEPUNCH.description = "The target is punched with an icy fist. It may also leave the target frozen."

#################
### FREEZEDRY ###
#################

FREEZEDRY = Move()
FREEZEDRY.name = "Freeze-Dry"
FREEZEDRY.type = ICE
FREEZEDRY.base_damage = 70
FREEZEDRY.category = SPECIAL
FREEZEDRY.pp = 20
FREEZEDRY.accuracy = 100
FREEZEDRY.priority = 0
FREEZEDRY.target = 'NearOther'
FREEZEDRY.additional_effect_chance = 10
FREEZEDRY.description = "The user rapidly cools the target. This may freeze the target. Is super-effective on Water types."

##################
### AURORABEAM ###
##################

AURORABEAM = Move()
AURORABEAM.name = "Aurora Beam"
AURORABEAM.type = ICE
AURORABEAM.base_damage = 65
AURORABEAM.category = SPECIAL
AURORABEAM.pp = 20
AURORABEAM.accuracy = 100
AURORABEAM.priority = 0
AURORABEAM.target = 'NearOther'
AURORABEAM.additional_effect_chance = 10
AURORABEAM.description = "The target is hit with a rainbow-colored beam. This may also lower the targets Attack stat."

################
### GLACIATE ###
################

GLACIATE = Move()
GLACIATE.name = "Glaciate"
GLACIATE.type = ICE
GLACIATE.base_damage = 65
GLACIATE.category = SPECIAL
GLACIATE.pp = 10
GLACIATE.accuracy = 95
GLACIATE.priority = 0
GLACIATE.target = 'AllNearFoes'
GLACIATE.additional_effect_chance = 100
GLACIATE.description = "The user attacks by blowing freezing cold air at the foe. This attack reduces the targets Speed stat."

###############
### ICEFANG ###
###############

ICEFANG = Move()
ICEFANG.name = "Ice Fang"
ICEFANG.type = ICE
ICEFANG.base_damage = 65
ICEFANG.category = PHYSICAL
ICEFANG.pp = 15
ICEFANG.accuracy = 95
ICEFANG.priority = 0
ICEFANG.target = 'NearOther'
ICEFANG.additional_effect_chance = 100
ICEFANG.description = "The user bites with cold-infused fangs. It may also make the target flinch or leave it frozen."

#################
### AVALANCHE ###
#################

AVALANCHE = Move()
AVALANCHE.name = "Avalanche"
AVALANCHE.type = ICE
AVALANCHE.base_damage = 60
AVALANCHE.category = PHYSICAL
AVALANCHE.pp = 10
AVALANCHE.accuracy = 100
AVALANCHE.priority = -4
AVALANCHE.target = 'NearOther'
AVALANCHE.additional_effect_chance = 0
AVALANCHE.description = "An attack move that inflicts double the damage if the user has been hurt by the foe in the same turn."

###################
### FROSTBREATH ###
###################

FROSTBREATH = Move()
FROSTBREATH.name = "Frost Breath"
FROSTBREATH.type = ICE
FROSTBREATH.base_damage = 60
FROSTBREATH.category = SPECIAL
FROSTBREATH.pp = 10
FROSTBREATH.accuracy = 90
FROSTBREATH.priority = 0
FROSTBREATH.target = 'NearOther'
FROSTBREATH.additional_effect_chance = 0
FROSTBREATH.description = "The user blows a cold breath on the target. This attack always results in a critical hit."

###############
### ICYWIND ###
###############

ICYWIND = Move()
ICYWIND.name = "Icy Wind"
ICYWIND.type = ICE
ICYWIND.base_damage = 55
ICYWIND.category = SPECIAL
ICYWIND.pp = 15
ICYWIND.accuracy = 95
ICYWIND.priority = 0
ICYWIND.target = 'AllNearFoes'
ICYWIND.additional_effect_chance = 100
ICYWIND.description = "The user attacks with a gust of chilled air. It also lowers the targets Speed stat."

################
### ICESHARD ###
################

ICESHARD = Move()
ICESHARD.name = "Ice Shard"
ICESHARD.type = ICE
ICESHARD.base_damage = 40
ICESHARD.category = PHYSICAL
ICESHARD.pp = 30
ICESHARD.accuracy = 100
ICESHARD.priority = 1
ICESHARD.target = 'NearOther'
ICESHARD.additional_effect_chance = 0
ICESHARD.description = "The user flash freezes chunks of ice and hurls them at the target. This move always goes first."

##################
### POWDERSNOW ###
##################

POWDERSNOW = Move()
POWDERSNOW.name = "Powder Snow"
POWDERSNOW.type = ICE
POWDERSNOW.base_damage = 40
POWDERSNOW.category = SPECIAL
POWDERSNOW.pp = 25
POWDERSNOW.accuracy = 100
POWDERSNOW.priority = 0
POWDERSNOW.target = 'AllNearFoes'
POWDERSNOW.additional_effect_chance = 10
POWDERSNOW.description = "The user attacks with a chilling gust of powdery snow. It may also freeze the targets."

###############
### ICEBALL ###
###############

ICEBALL = Move()
ICEBALL.name = "Ice Ball"
ICEBALL.type = ICE
ICEBALL.base_damage = 30
ICEBALL.category = PHYSICAL
ICEBALL.pp = 20
ICEBALL.accuracy = 90
ICEBALL.priority = 0
ICEBALL.target = 'NearOther'
ICEBALL.additional_effect_chance = 0
ICEBALL.description = "The user continually rolls into the target over five turns. It becomes stronger each time it hits."

###################
### ICICLESPEAR ###
###################

ICICLESPEAR = Move()
ICICLESPEAR.name = "Icicle Spear"
ICICLESPEAR.type = ICE
ICICLESPEAR.base_damage = 25
ICICLESPEAR.category = PHYSICAL
ICICLESPEAR.pp = 30
ICICLESPEAR.accuracy = 100
ICICLESPEAR.priority = 0
ICICLESPEAR.target = 'NearOther'
ICICLESPEAR.additional_effect_chance = 0
ICICLESPEAR.description = "The user launches sharp icicles at the target. It strikes two to five times in a row."

#################
### SHEERCOLD ###
#################

SHEERCOLD = Move()
SHEERCOLD.name = "Sheer Cold"
SHEERCOLD.type = ICE
SHEERCOLD.base_damage = 1
SHEERCOLD.category = SPECIAL
SHEERCOLD.pp = 5
SHEERCOLD.accuracy = 30
SHEERCOLD.priority = 0
SHEERCOLD.target = 'NearOther'
SHEERCOLD.additional_effect_chance = 0
SHEERCOLD.description = "The foe is attacked with a blast of absolute-zero cold. The target instantly faints if it hits."

##################
### AURORAVEIL ###
##################

AURORAVEIL = Move()
AURORAVEIL.name = "Aurora Veil"
AURORAVEIL.type = ICE
AURORAVEIL.base_damage = 0
AURORAVEIL.category = STATUS
AURORAVEIL.pp = 20
AURORAVEIL.accuracy = 0
AURORAVEIL.priority = 0
AURORAVEIL.target = 'UserSide'
AURORAVEIL.additional_effect_chance = 0
AURORAVEIL.description = "This move reduces damage from attacks for five turns. This can be used only in a hailstorm."

############
### HAIL ###
############

HAIL = Move()
HAIL.name = "Hail"
HAIL.type = ICE
HAIL.base_damage = 0
HAIL.category = STATUS
HAIL.pp = 10
HAIL.accuracy = 0
HAIL.priority = 0
HAIL.target = 'BothSides'
HAIL.additional_effect_chance = 0
HAIL.description = "The user summons a hail storm lasting five turns. It damages all Pokémon except the Ice type."

############
### HAZE ###
############

HAZE = Move()
HAZE.name = "Haze"
HAZE.type = ICE
HAZE.base_damage = 0
HAZE.category = STATUS
HAZE.pp = 30
HAZE.accuracy = 0
HAZE.priority = 0
HAZE.target = 'BothSides'
HAZE.additional_effect_chance = 0
HAZE.description = "The user creates a haze that eliminates every stat change among all the Pokémon engaged in battle."

############
### MIST ###
############

MIST = Move()
MIST.name = "Mist"
MIST.type = ICE
MIST.base_damage = 0
MIST.category = STATUS
MIST.pp = 30
MIST.accuracy = 0
MIST.priority = 0
MIST.target = 'UserSide'
MIST.additional_effect_chance = 0
MIST.description = "The user cloaks its body with a white mist that prevents any of its stats from being cut for five turns."

#################
### EXPLOSION ###
#################

EXPLOSION = Move()
EXPLOSION.name = "Explosion"
EXPLOSION.type = NORMAL
EXPLOSION.base_damage = 250
EXPLOSION.category = PHYSICAL
EXPLOSION.pp = 5
EXPLOSION.accuracy = 100
EXPLOSION.priority = 0
EXPLOSION.target = 'AllNearOthers'
EXPLOSION.additional_effect_chance = 0
EXPLOSION.description = "The user explodes to inflict damage on those around it. The user faints upon using this move."

####################
### SELFDESTRUCT ###
####################

SELFDESTRUCT = Move()
SELFDESTRUCT.name = "Self-Destruct"
SELFDESTRUCT.type = NORMAL
SELFDESTRUCT.base_damage = 200
SELFDESTRUCT.category = PHYSICAL
SELFDESTRUCT.pp = 5
SELFDESTRUCT.accuracy = 100
SELFDESTRUCT.priority = 0
SELFDESTRUCT.target = 'AllNearOthers'
SELFDESTRUCT.additional_effect_chance = 0
SELFDESTRUCT.description = "The user blows up to inflict damage on all Pokémon in battle. The user faints upon using this move."

##################
### GIGAIMPACT ###
##################

GIGAIMPACT = Move()
GIGAIMPACT.name = "Giga Impact"
GIGAIMPACT.type = NORMAL
GIGAIMPACT.base_damage = 150
GIGAIMPACT.category = PHYSICAL
GIGAIMPACT.pp = 5
GIGAIMPACT.accuracy = 90
GIGAIMPACT.priority = 0
GIGAIMPACT.target = 'NearOther'
GIGAIMPACT.additional_effect_chance = 0
GIGAIMPACT.description = "The user charges at the target using every bit of its power. The user must rest on the next turn."

#################
### HYPERBEAM ###
#################

HYPERBEAM = Move()
HYPERBEAM.name = "Hyper Beam"
HYPERBEAM.type = NORMAL
HYPERBEAM.base_damage = 150
HYPERBEAM.category = SPECIAL
HYPERBEAM.pp = 5
HYPERBEAM.accuracy = 90
HYPERBEAM.priority = 0
HYPERBEAM.target = 'NearOther'
HYPERBEAM.additional_effect_chance = 0
HYPERBEAM.description = "The foe is attacked with a powerful beam. The user must rest on the next turn to regain its energy."

#################
### BOOMBURST ###
#################

BOOMBURST = Move()
BOOMBURST.name = "Boomburst"
BOOMBURST.type = NORMAL
BOOMBURST.base_damage = 140
BOOMBURST.category = SPECIAL
BOOMBURST.pp = 10
BOOMBURST.accuracy = 100
BOOMBURST.priority = 0
BOOMBURST.target = 'AllNearOthers'
BOOMBURST.additional_effect_chance = 0
BOOMBURST.description = "The user attacks everything around it with the destructive power of a terrible, explosive sound."

##################
### LASTRESORT ###
##################

LASTRESORT = Move()
LASTRESORT.name = "Last Resort"
LASTRESORT.type = NORMAL
LASTRESORT.base_damage = 140
LASTRESORT.category = PHYSICAL
LASTRESORT.pp = 5
LASTRESORT.accuracy = 100
LASTRESORT.priority = 0
LASTRESORT.target = 'NearOther'
LASTRESORT.additional_effect_chance = 0
LASTRESORT.description = "This move can be used only after the user has used all the other moves it knows in the battle."

#################
### SKULLBASH ###
#################

SKULLBASH = Move()
SKULLBASH.name = "Skull Bash"
SKULLBASH.type = NORMAL
SKULLBASH.base_damage = 130
SKULLBASH.category = PHYSICAL
SKULLBASH.pp = 10
SKULLBASH.accuracy = 100
SKULLBASH.priority = 0
SKULLBASH.target = 'NearOther'
SKULLBASH.additional_effect_chance = 0
SKULLBASH.description = "The user tucks in its head to raise its Defense in the first turn, then rams the foe on the next turn."

##################
### DOUBLEEDGE ###
##################

DOUBLEEDGE = Move()
DOUBLEEDGE.name = "Double-Edge"
DOUBLEEDGE.type = NORMAL
DOUBLEEDGE.base_damage = 120
DOUBLEEDGE.category = PHYSICAL
DOUBLEEDGE.pp = 15
DOUBLEEDGE.accuracy = 100
DOUBLEEDGE.priority = 0
DOUBLEEDGE.target = 'NearOther'
DOUBLEEDGE.additional_effect_chance = 0
DOUBLEEDGE.description = "A reckless, life-risking tackle. It also damages the user by a fairly large amount, however."

##################
### HEADCHARGE ###
##################

HEADCHARGE = Move()
HEADCHARGE.name = "Head Charge"
HEADCHARGE.type = NORMAL
HEADCHARGE.base_damage = 120
HEADCHARGE.category = PHYSICAL
HEADCHARGE.pp = 15
HEADCHARGE.accuracy = 100
HEADCHARGE.priority = 0
HEADCHARGE.target = 'NearOther'
HEADCHARGE.additional_effect_chance = 0
HEADCHARGE.description = "The user charges its head into the foe, using its powerful guard hair. The user also takes damage."

################
### MEGAKICK ###
################

MEGAKICK = Move()
MEGAKICK.name = "Mega Kick"
MEGAKICK.type = NORMAL
MEGAKICK.base_damage = 120
MEGAKICK.category = PHYSICAL
MEGAKICK.pp = 5
MEGAKICK.accuracy = 75
MEGAKICK.priority = 0
MEGAKICK.target = 'NearOther'
MEGAKICK.additional_effect_chance = 0
MEGAKICK.description = "The target is attacked by a kick launched with muscle-packed power."

###################
### TECHNOBLAST ###
###################

TECHNOBLAST = Move()
TECHNOBLAST.name = "Techno Blast"
TECHNOBLAST.type = NORMAL
TECHNOBLAST.base_damage = 120
TECHNOBLAST.category = SPECIAL
TECHNOBLAST.pp = 5
TECHNOBLAST.accuracy = 100
TECHNOBLAST.priority = 0
TECHNOBLAST.target = 'NearOther'
TECHNOBLAST.additional_effect_chance = 0
TECHNOBLAST.description = "The user fires a beam of light at its target. The type changes depending on the Drive the user holds."

##############
### THRASH ###
##############

THRASH = Move()
THRASH.name = "Thrash"
THRASH.type = NORMAL
THRASH.base_damage = 120
THRASH.category = PHYSICAL
THRASH.pp = 10
THRASH.accuracy = 100
THRASH.priority = 0
THRASH.target = 'RandomNearFoe'
THRASH.additional_effect_chance = 0
THRASH.description = "The user rampages and attacks for two to three turns. It then becomes confused, however."

###############
### EGGBOMB ###
###############

EGGBOMB = Move()
EGGBOMB.name = "Egg Bomb"
EGGBOMB.type = NORMAL
EGGBOMB.base_damage = 100
EGGBOMB.category = PHYSICAL
EGGBOMB.pp = 10
EGGBOMB.accuracy = 75
EGGBOMB.priority = 0
EGGBOMB.target = 'NearOther'
EGGBOMB.additional_effect_chance = 0
EGGBOMB.description = "A large egg is hurled at the target with maximum force to inflict damage."

################
### JUDGMENT ###
################

JUDGMENT = Move()
JUDGMENT.name = "Judgment"
JUDGMENT.type = NORMAL
JUDGMENT.base_damage = 100
JUDGMENT.category = SPECIAL
JUDGMENT.pp = 10
JUDGMENT.accuracy = 100
JUDGMENT.priority = 0
JUDGMENT.target = 'NearOther'
JUDGMENT.additional_effect_chance = 0
JUDGMENT.description = "The user releases countless shots of light. Its type varies with the kind of Plate the user is holding."

##################
### HYPERVOICE ###
##################

HYPERVOICE = Move()
HYPERVOICE.name = "Hyper Voice"
HYPERVOICE.type = NORMAL
HYPERVOICE.base_damage = 90
HYPERVOICE.category = SPECIAL
HYPERVOICE.pp = 10
HYPERVOICE.accuracy = 100
HYPERVOICE.priority = 0
HYPERVOICE.target = 'AllNearFoes'
HYPERVOICE.additional_effect_chance = 0
HYPERVOICE.description = "The user lets loose a horribly echoing shout with the power to inflict damage."

###################
### MULTIATTACK ###
###################

MULTIATTACK = Move()
MULTIATTACK.name = "Multi-Attack"
MULTIATTACK.type = NORMAL
MULTIATTACK.base_damage = 90
MULTIATTACK.category = PHYSICAL
MULTIATTACK.pp = 10
MULTIATTACK.accuracy = 100
MULTIATTACK.priority = 0
MULTIATTACK.target = 'NearOther'
MULTIATTACK.additional_effect_chance = 0
MULTIATTACK.description = "Cloaking itself in high energy, the user slams into the target. This moves type depends on the held memory."

#######################
### REVELATIONDANCE ###
#######################

REVELATIONDANCE = Move()
REVELATIONDANCE.name = "Revelation Dance"
REVELATIONDANCE.type = NORMAL
REVELATIONDANCE.base_damage = 90
REVELATIONDANCE.category = SPECIAL
REVELATIONDANCE.pp = 15
REVELATIONDANCE.accuracy = 100
REVELATIONDANCE.priority = 0
REVELATIONDANCE.target = 'NearOther'
REVELATIONDANCE.additional_effect_chance = 0
REVELATIONDANCE.description = "The user attacks the target by dancing very hard. The users type determines the type of this move."

#################
### ROCKCLIMB ###
#################

ROCKCLIMB = Move()
ROCKCLIMB.name = "Rock Climb"
ROCKCLIMB.type = NORMAL
ROCKCLIMB.base_damage = 90
ROCKCLIMB.category = PHYSICAL
ROCKCLIMB.pp = 20
ROCKCLIMB.accuracy = 85
ROCKCLIMB.priority = 0
ROCKCLIMB.target = 'NearOther'
ROCKCLIMB.additional_effect_chance = 20
ROCKCLIMB.description = "The user attacks the target by smashing into it with incredible force. It may also confuse the target."

################
### TAKEDOWN ###
################

TAKEDOWN = Move()
TAKEDOWN.name = "Take Down"
TAKEDOWN.type = NORMAL
TAKEDOWN.base_damage = 90
TAKEDOWN.category = PHYSICAL
TAKEDOWN.pp = 20
TAKEDOWN.accuracy = 85
TAKEDOWN.priority = 0
TAKEDOWN.target = 'NearOther'
TAKEDOWN.additional_effect_chance = 0
TAKEDOWN.description = "A reckless, full-body charge attack for slamming into the foe. It also damages the user a little."

##############
### UPROAR ###
##############

UPROAR = Move()
UPROAR.name = "Uproar"
UPROAR.type = NORMAL
UPROAR.base_damage = 90
UPROAR.category = SPECIAL
UPROAR.pp = 10
UPROAR.accuracy = 100
UPROAR.priority = 0
UPROAR.target = 'RandomNearFoe'
UPROAR.additional_effect_chance = 0
UPROAR.description = "The user attacks in an uproar for three turns. Over that time, no one can fall asleep."

################
### BODYSLAM ###
################

BODYSLAM = Move()
BODYSLAM.name = "Body Slam"
BODYSLAM.type = NORMAL
BODYSLAM.base_damage = 85
BODYSLAM.category = PHYSICAL
BODYSLAM.pp = 15
BODYSLAM.accuracy = 100
BODYSLAM.priority = 0
BODYSLAM.target = 'NearOther'
BODYSLAM.additional_effect_chance = 30
BODYSLAM.description = "The user drops onto the target with its full body weight. It may leave the target with paralysis."

####################
### EXTREMESPEED ###
####################

EXTREMESPEED = Move()
EXTREMESPEED.name = "Extreme Speed"
EXTREMESPEED.type = NORMAL
EXTREMESPEED.base_damage = 80
EXTREMESPEED.category = PHYSICAL
EXTREMESPEED.pp = 5
EXTREMESPEED.accuracy = 100
EXTREMESPEED.priority = 2
EXTREMESPEED.target = 'NearOther'
EXTREMESPEED.additional_effect_chance = 0
EXTREMESPEED.description = "The user charges the target at blinding speed. This attack always goes before any other move."

#################
### HYPERFANG ###
#################

HYPERFANG = Move()
HYPERFANG.name = "Hyper Fang"
HYPERFANG.type = NORMAL
HYPERFANG.base_damage = 80
HYPERFANG.category = PHYSICAL
HYPERFANG.pp = 15
HYPERFANG.accuracy = 90
HYPERFANG.priority = 0
HYPERFANG.target = 'NearOther'
HYPERFANG.additional_effect_chance = 10
HYPERFANG.description = "The user bites hard on the target with its sharp front fangs. It may also make the target flinch."

#################
### MEGAPUNCH ###
#################

MEGAPUNCH = Move()
MEGAPUNCH.name = "Mega Punch"
MEGAPUNCH.type = NORMAL
MEGAPUNCH.base_damage = 80
MEGAPUNCH.category = PHYSICAL
MEGAPUNCH.pp = 20
MEGAPUNCH.accuracy = 85
MEGAPUNCH.priority = 0
MEGAPUNCH.target = 'NearOther'
MEGAPUNCH.additional_effect_chance = 0
MEGAPUNCH.description = "The target is slugged by a punch thrown with muscle-packed power."

#################
### RAZORWIND ###
#################

RAZORWIND = Move()
RAZORWIND.name = "Razor Wind"
RAZORWIND.type = NORMAL
RAZORWIND.base_damage = 80
RAZORWIND.category = SPECIAL
RAZORWIND.pp = 10
RAZORWIND.accuracy = 100
RAZORWIND.priority = 0
RAZORWIND.target = 'AllNearFoes'
RAZORWIND.additional_effect_chance = 0
RAZORWIND.description = "A two-turn attack. Blades of wind hit the foe on the second turn. Critical hits land more easily."

############
### SLAM ###
############

SLAM = Move()
SLAM.name = "Slam"
SLAM.type = NORMAL
SLAM.base_damage = 80
SLAM.category = PHYSICAL
SLAM.pp = 20
SLAM.accuracy = 75
SLAM.priority = 0
SLAM.target = 'NearOther'
SLAM.additional_effect_chance = 0
SLAM.description = "The target is slammed with a long tail, vines, etc., to inflict damage."

################
### STRENGTH ###
################

STRENGTH = Move()
STRENGTH.name = "Strength"
STRENGTH.type = NORMAL
STRENGTH.base_damage = 80
STRENGTH.category = PHYSICAL
STRENGTH.pp = 15
STRENGTH.accuracy = 100
STRENGTH.priority = 0
STRENGTH.target = 'NearOther'
STRENGTH.additional_effect_chance = 0
STRENGTH.description = "The target is slugged with a punch thrown at maximum power. It can also be used to move heavy boulders."

#################
### TRIATTACK ###
#################

TRIATTACK = Move()
TRIATTACK.name = "Tri Attack"
TRIATTACK.type = NORMAL
TRIATTACK.base_damage = 80
TRIATTACK.category = SPECIAL
TRIATTACK.pp = 10
TRIATTACK.accuracy = 100
TRIATTACK.priority = 0
TRIATTACK.target = 'NearOther'
TRIATTACK.additional_effect_chance = 20
TRIATTACK.description = "The user strikes with a simultaneous three-beam attack. May also paralyze, burn, or freeze the target."

#################
### CRUSHCLAW ###
#################

CRUSHCLAW = Move()
CRUSHCLAW.name = "Crush Claw"
CRUSHCLAW.type = NORMAL
CRUSHCLAW.base_damage = 75
CRUSHCLAW.category = PHYSICAL
CRUSHCLAW.pp = 10
CRUSHCLAW.accuracy = 95
CRUSHCLAW.priority = 0
CRUSHCLAW.target = 'NearOther'
CRUSHCLAW.additional_effect_chance = 50
CRUSHCLAW.description = "The user slashes the target with hard and sharp claws. It may also lower the targets Defense."

#################
### RELICSONG ###
#################

RELICSONG = Move()
RELICSONG.name = "Relic Song"
RELICSONG.type = NORMAL
RELICSONG.base_damage = 75
RELICSONG.category = SPECIAL
RELICSONG.pp = 10
RELICSONG.accuracy = 100
RELICSONG.priority = 0
RELICSONG.target = 'AllNearFoes'
RELICSONG.additional_effect_chance = 10
RELICSONG.description = "An ancient song appeals to the hearts of those listening. It may also induce sleep."

################
### CHIPAWAY ###
################

CHIPAWAY = Move()
CHIPAWAY.name = "Chip Away"
CHIPAWAY.type = NORMAL
CHIPAWAY.base_damage = 70
CHIPAWAY.category = PHYSICAL
CHIPAWAY.pp = 20
CHIPAWAY.accuracy = 100
CHIPAWAY.priority = 0
CHIPAWAY.target = 'NearOther'
CHIPAWAY.additional_effect_chance = 0
CHIPAWAY.description = "Seeking an opening, the user strikes continually. The foes stat changes dont affect the damage."

##################
### DIZZYPUNCH ###
##################

DIZZYPUNCH = Move()
DIZZYPUNCH.name = "Dizzy Punch"
DIZZYPUNCH.type = NORMAL
DIZZYPUNCH.base_damage = 70
DIZZYPUNCH.category = PHYSICAL
DIZZYPUNCH.pp = 10
DIZZYPUNCH.accuracy = 100
DIZZYPUNCH.priority = 0
DIZZYPUNCH.target = 'NearOther'
DIZZYPUNCH.additional_effect_chance = 20
DIZZYPUNCH.description = "The target is hit with rhythmically launched punches that may also leave it confused."

##############
### FACADE ###
##############

FACADE = Move()
FACADE.name = "Facade"
FACADE.type = NORMAL
FACADE.base_damage = 70
FACADE.category = PHYSICAL
FACADE.pp = 20
FACADE.accuracy = 100
FACADE.priority = 0
FACADE.target = 'NearOther'
FACADE.additional_effect_chance = 0
FACADE.description = "An attack move that doubles its power if the user is poisoned, burned, or has paralysis."

################
### HEADBUTT ###
################

HEADBUTT = Move()
HEADBUTT.name = "Headbutt"
HEADBUTT.type = NORMAL
HEADBUTT.base_damage = 70
HEADBUTT.category = PHYSICAL
HEADBUTT.pp = 15
HEADBUTT.accuracy = 100
HEADBUTT.priority = 0
HEADBUTT.target = 'NearOther'
HEADBUTT.additional_effect_chance = 30
HEADBUTT.description = "The user sticks out its head and attacks by charging into the foe. It may also make the target flinch."

#################
### RETALIATE ###
#################

RETALIATE = Move()
RETALIATE.name = "Retaliate"
RETALIATE.type = NORMAL
RETALIATE.base_damage = 70
RETALIATE.category = PHYSICAL
RETALIATE.pp = 5
RETALIATE.accuracy = 100
RETALIATE.priority = 0
RETALIATE.target = 'NearOther'
RETALIATE.additional_effect_chance = 0
RETALIATE.description = "Gets revenge for a fainted ally. If an ally fainted in the last turn, this attacks damage increases."

###################
### SECRETPOWER ###
###################

SECRETPOWER = Move()
SECRETPOWER.name = "Secret Power"
SECRETPOWER.type = NORMAL
SECRETPOWER.base_damage = 70
SECRETPOWER.category = PHYSICAL
SECRETPOWER.pp = 20
SECRETPOWER.accuracy = 100
SECRETPOWER.priority = 0
SECRETPOWER.target = 'NearOther'
SECRETPOWER.additional_effect_chance = 30
SECRETPOWER.description = "The user attacks with a secret power. Its added effects vary depending on the users environment."

#############
### SLASH ###
#############

SLASH = Move()
SLASH.name = "Slash"
SLASH.type = NORMAL
SLASH.base_damage = 70
SLASH.category = PHYSICAL
SLASH.pp = 20
SLASH.accuracy = 100
SLASH.priority = 0
SLASH.target = 'NearOther'
SLASH.additional_effect_chance = 0
SLASH.description = "The target is attacked with a slash of claws or blades. Critical hits land more easily."

#####################
### SMELLINGSALTS ###
#####################

SMELLINGSALTS = Move()
SMELLINGSALTS.name = "Smelling Salts"
SMELLINGSALTS.type = NORMAL
SMELLINGSALTS.base_damage = 70
SMELLINGSALTS.category = PHYSICAL
SMELLINGSALTS.pp = 10
SMELLINGSALTS.accuracy = 100
SMELLINGSALTS.priority = 0
SMELLINGSALTS.target = 'NearOther'
SMELLINGSALTS.additional_effect_chance = 0
SMELLINGSALTS.description = "This attack inflicts double damage on a paralyzed foe. It also cures the targets paralysis, however."

##################
### HORNATTACK ###
##################

HORNATTACK = Move()
HORNATTACK.name = "Horn Attack"
HORNATTACK.type = NORMAL
HORNATTACK.base_damage = 65
HORNATTACK.category = PHYSICAL
HORNATTACK.pp = 25
HORNATTACK.accuracy = 100
HORNATTACK.priority = 0
HORNATTACK.target = 'NearOther'
HORNATTACK.additional_effect_chance = 0
HORNATTACK.description = "The target is jabbed with a sharply pointed horn to inflict damage."

#############
### STOMP ###
#############

STOMP = Move()
STOMP.name = "Stomp"
STOMP.type = NORMAL
STOMP.base_damage = 65
STOMP.category = PHYSICAL
STOMP.pp = 20
STOMP.accuracy = 100
STOMP.priority = 0
STOMP.target = 'NearOther'
STOMP.additional_effect_chance = 30
STOMP.description = "The target is stomped with a big foot. It may also make the target flinch."

#############
### COVET ###
#############

COVET = Move()
COVET.name = "Covet"
COVET.type = NORMAL
COVET.base_damage = 60
COVET.category = PHYSICAL
COVET.pp = 25
COVET.accuracy = 100
COVET.priority = 0
COVET.target = 'NearOther'
COVET.additional_effect_chance = 0
COVET.description = "The user endearingly approaches the target, then steals the targets held item."

###################
### HIDDENPOWER ###
###################

HIDDENPOWER = Move()
HIDDENPOWER.name = "Hidden Power"
HIDDENPOWER.type = NORMAL
HIDDENPOWER.base_damage = 60
HIDDENPOWER.category = SPECIAL
HIDDENPOWER.pp = 15
HIDDENPOWER.accuracy = 100
HIDDENPOWER.priority = 0
HIDDENPOWER.target = 'NearOther'
HIDDENPOWER.additional_effect_chance = 0
HIDDENPOWER.description = "A unique attack that varies in type and intensity depending on the Pokémon using it."

#############
### ROUND ###
#############

ROUND = Move()
ROUND.name = "Round"
ROUND.type = NORMAL
ROUND.base_damage = 60
ROUND.category = SPECIAL
ROUND.pp = 15
ROUND.accuracy = 100
ROUND.priority = 0
ROUND.target = 'NearOther'
ROUND.additional_effect_chance = 0
ROUND.description = "The user attacks with a song. Others can join in the Round and make the attack do greater damage."

#############
### SWIFT ###
#############

SWIFT = Move()
SWIFT.name = "Swift"
SWIFT.type = NORMAL
SWIFT.base_damage = 60
SWIFT.category = SPECIAL
SWIFT.pp = 20
SWIFT.accuracy = 0
SWIFT.priority = 0
SWIFT.target = 'AllNearFoes'
SWIFT.additional_effect_chance = 0
SWIFT.description = "Star-shaped rays are shot at the opposing team. This attack never misses."

################
### VICEGRIP ###
################

VICEGRIP = Move()
VICEGRIP.name = "Vice Grip"
VICEGRIP.type = NORMAL
VICEGRIP.base_damage = 55
VICEGRIP.category = PHYSICAL
VICEGRIP.pp = 30
VICEGRIP.accuracy = 100
VICEGRIP.priority = 0
VICEGRIP.target = 'NearOther'
VICEGRIP.additional_effect_chance = 0
VICEGRIP.description = "The target is gripped and squeezed from both sides to inflict damage."

###########
### CUT ###
###########

CUT = Move()
CUT.name = "Cut"
CUT.type = NORMAL
CUT.base_damage = 50
CUT.category = PHYSICAL
CUT.pp = 30
CUT.accuracy = 95
CUT.priority = 0
CUT.target = 'NearOther'
CUT.additional_effect_chance = 0
CUT.description = "The target is cut with a scythe or a claw. It can also be used to cut down thin trees."

#############
### SNORE ###
#############

SNORE = Move()
SNORE.name = "Snore"
SNORE.type = NORMAL
SNORE.base_damage = 50
SNORE.category = SPECIAL
SNORE.pp = 15
SNORE.accuracy = 100
SNORE.priority = 0
SNORE.target = 'NearOther'
SNORE.additional_effect_chance = 30
SNORE.description = "An attack that can be used only if the user is asleep. The harsh noise may also make the target flinch."

################
### STRUGGLE ###
################

STRUGGLE = Move()
STRUGGLE.name = "Struggle"
STRUGGLE.type = NORMAL
STRUGGLE.base_damage = 50
STRUGGLE.category = PHYSICAL
STRUGGLE.pp = 1
STRUGGLE.accuracy = 0
STRUGGLE.priority = 0
STRUGGLE.target = 'RandomNearFoe'
STRUGGLE.additional_effect_chance = 0
STRUGGLE.description = "An attack that is used in desperation only if the user has no PP. It also hurts the user slightly."

###################
### WEATHERBALL ###
###################

WEATHERBALL = Move()
WEATHERBALL.name = "Weather Ball"
WEATHERBALL.type = NORMAL
WEATHERBALL.base_damage = 50
WEATHERBALL.category = SPECIAL
WEATHERBALL.pp = 10
WEATHERBALL.accuracy = 100
WEATHERBALL.priority = 0
WEATHERBALL.target = 'NearOther'
WEATHERBALL.additional_effect_chance = 0
WEATHERBALL.description = "An attack move that varies in power and type depending on the weather."

###################
### ECHOEDVOICE ###
###################

ECHOEDVOICE = Move()
ECHOEDVOICE.name = "Echoed Voice"
ECHOEDVOICE.type = NORMAL
ECHOEDVOICE.base_damage = 40
ECHOEDVOICE.category = SPECIAL
ECHOEDVOICE.pp = 15
ECHOEDVOICE.accuracy = 100
ECHOEDVOICE.priority = 0
ECHOEDVOICE.target = 'NearOther'
ECHOEDVOICE.additional_effect_chance = 0
ECHOEDVOICE.description = "The user attacks the foe with an echoing voice. If this move is used every turn, it does greater damage."

###############
### FAKEOUT ###
###############

FAKEOUT = Move()
FAKEOUT.name = "Fake Out"
FAKEOUT.type = NORMAL
FAKEOUT.base_damage = 40
FAKEOUT.category = PHYSICAL
FAKEOUT.pp = 10
FAKEOUT.accuracy = 100
FAKEOUT.priority = 3
FAKEOUT.target = 'NearOther'
FAKEOUT.additional_effect_chance = 100
FAKEOUT.description = "An attack that hits first and makes the target flinch. It only works the first turn the user is in battle."

##################
### FALSESWIPE ###
##################

FALSESWIPE = Move()
FALSESWIPE.name = "False Swipe"
FALSESWIPE.type = NORMAL
FALSESWIPE.base_damage = 40
FALSESWIPE.category = PHYSICAL
FALSESWIPE.pp = 40
FALSESWIPE.accuracy = 100
FALSESWIPE.priority = 0
FALSESWIPE.target = 'NearOther'
FALSESWIPE.additional_effect_chance = 0
FALSESWIPE.description = "A restrained attack that prevents the target from fainting. The target is left with at least 1 HP."

################
### HOLDBACK ###
################

HOLDBACK = Move()
HOLDBACK.name = "Hold Back"
HOLDBACK.type = NORMAL
HOLDBACK.base_damage = 40
HOLDBACK.category = PHYSICAL
HOLDBACK.pp = 40
HOLDBACK.accuracy = 100
HOLDBACK.priority = 0
HOLDBACK.target = 'NearOther'
HOLDBACK.additional_effect_chance = 0
HOLDBACK.description = "The user holds back when it attacks, and the target is left with at least 1 HP."

##############
### PAYDAY ###
##############

PAYDAY = Move()
PAYDAY.name = "Pay Day"
PAYDAY.type = NORMAL
PAYDAY.base_damage = 40
PAYDAY.category = PHYSICAL
PAYDAY.pp = 20
PAYDAY.accuracy = 100
PAYDAY.priority = 0
PAYDAY.target = 'NearOther'
PAYDAY.additional_effect_chance = 0
PAYDAY.description = "Numerous coins are hurled at the target to inflict damage. Money is earned after battle."

#############
### POUND ###
#############

POUND = Move()
POUND.name = "Pound"
POUND.type = NORMAL
POUND.base_damage = 40
POUND.category = PHYSICAL
POUND.pp = 35
POUND.accuracy = 100
POUND.priority = 0
POUND.target = 'NearOther'
POUND.additional_effect_chance = 0
POUND.description = "The target is physically pounded with a long tail or a foreleg, etc."

###################
### QUICKATTACK ###
###################

QUICKATTACK = Move()
QUICKATTACK.name = "Quick Attack"
QUICKATTACK.type = NORMAL
QUICKATTACK.base_damage = 40
QUICKATTACK.category = PHYSICAL
QUICKATTACK.pp = 30
QUICKATTACK.accuracy = 100
QUICKATTACK.priority = 1
QUICKATTACK.target = 'NearOther'
QUICKATTACK.additional_effect_chance = 0
QUICKATTACK.description = "The user lunges at the target at a speed that makes it almost invisible. It is sure to strike first."

###############
### SCRATCH ###
###############

SCRATCH = Move()
SCRATCH.name = "Scratch"
SCRATCH.type = NORMAL
SCRATCH.base_damage = 40
SCRATCH.category = PHYSICAL
SCRATCH.pp = 35
SCRATCH.accuracy = 100
SCRATCH.priority = 0
SCRATCH.target = 'NearOther'
SCRATCH.additional_effect_chance = 0
SCRATCH.description = "Hard, pointed, and sharp claws rake the target to inflict damage."

##############
### TACKLE ###
##############

TACKLE = Move()
TACKLE.name = "Tackle"
TACKLE.type = NORMAL
TACKLE.base_damage = 40
TACKLE.category = PHYSICAL
TACKLE.pp = 35
TACKLE.accuracy = 100
TACKLE.priority = 0
TACKLE.target = 'NearOther'
TACKLE.additional_effect_chance = 0
TACKLE.description = "A physical attack in which the user charges and slams into the target with its whole body."

#################
### DOUBLEHIT ###
#################

DOUBLEHIT = Move()
DOUBLEHIT.name = "Double Hit"
DOUBLEHIT.type = NORMAL
DOUBLEHIT.base_damage = 35
DOUBLEHIT.category = PHYSICAL
DOUBLEHIT.pp = 10
DOUBLEHIT.accuracy = 90
DOUBLEHIT.priority = 0
DOUBLEHIT.target = 'NearOther'
DOUBLEHIT.additional_effect_chance = 0
DOUBLEHIT.description = "The user slams the target with a long tail, vines, or tentacle. The target is hit twice in a row."

#############
### FEINT ###
#############

FEINT = Move()
FEINT.name = "Feint"
FEINT.type = NORMAL
FEINT.base_damage = 30
FEINT.category = PHYSICAL
FEINT.pp = 10
FEINT.accuracy = 100
FEINT.priority = 2
FEINT.target = 'NearOther'
FEINT.additional_effect_chance = 0
FEINT.description = "An attack that hits a target using Protect or Detect. It also lifts the effects of those moves."

################
### TAILSLAP ###
################

TAILSLAP = Move()
TAILSLAP.name = "Tail Slap"
TAILSLAP.type = NORMAL
TAILSLAP.base_damage = 25
TAILSLAP.category = PHYSICAL
TAILSLAP.pp = 10
TAILSLAP.accuracy = 85
TAILSLAP.priority = 0
TAILSLAP.target = 'NearOther'
TAILSLAP.additional_effect_chance = 0
TAILSLAP.description = "The user attacks by striking the target with its hard tail. It hits the Pokémon two to five times in a row."

############
### RAGE ###
############

RAGE = Move()
RAGE.name = "Rage"
RAGE.type = NORMAL
RAGE.base_damage = 20
RAGE.category = PHYSICAL
RAGE.pp = 20
RAGE.accuracy = 100
RAGE.priority = 0
RAGE.target = 'NearOther'
RAGE.additional_effect_chance = 0
RAGE.description = "As long as this move is in use, the users Attack rises each time the user is hit in battle."

#################
### RAPIDSPIN ###
#################

RAPIDSPIN = Move()
RAPIDSPIN.name = "Rapid Spin"
RAPIDSPIN.type = NORMAL
RAPIDSPIN.base_damage = 20
RAPIDSPIN.category = PHYSICAL
RAPIDSPIN.pp = 40
RAPIDSPIN.accuracy = 100
RAPIDSPIN.priority = 0
RAPIDSPIN.target = 'NearOther'
RAPIDSPIN.additional_effect_chance = 0
RAPIDSPIN.description = "A spin attack that can also eliminate such moves as Bind, Wrap, Leech Seed, and Spikes."

###################
### SPIKECANNON ###
###################

SPIKECANNON = Move()
SPIKECANNON.name = "Spike Cannon"
SPIKECANNON.type = NORMAL
SPIKECANNON.base_damage = 20
SPIKECANNON.category = PHYSICAL
SPIKECANNON.pp = 15
SPIKECANNON.accuracy = 100
SPIKECANNON.priority = 0
SPIKECANNON.target = 'NearOther'
SPIKECANNON.additional_effect_chance = 0
SPIKECANNON.description = "Sharp spikes are shot at the target in rapid succession. They hit two to five times in a row."

##################
### COMETPUNCH ###
##################

COMETPUNCH = Move()
COMETPUNCH.name = "Comet Punch"
COMETPUNCH.type = NORMAL
COMETPUNCH.base_damage = 18
COMETPUNCH.category = PHYSICAL
COMETPUNCH.pp = 15
COMETPUNCH.accuracy = 85
COMETPUNCH.priority = 0
COMETPUNCH.target = 'NearOther'
COMETPUNCH.additional_effect_chance = 0
COMETPUNCH.description = "The target is hit with a flurry of punches that strike two to five times in a row."

##################
### FURYSWIPES ###
##################

FURYSWIPES = Move()
FURYSWIPES.name = "Fury Swipes"
FURYSWIPES.type = NORMAL
FURYSWIPES.base_damage = 18
FURYSWIPES.category = PHYSICAL
FURYSWIPES.pp = 15
FURYSWIPES.accuracy = 80
FURYSWIPES.priority = 0
FURYSWIPES.target = 'NearOther'
FURYSWIPES.additional_effect_chance = 0
FURYSWIPES.description = "The target is raked with sharp claws or scythes for two to five times in quick succession."

###############
### BARRAGE ###
###############

BARRAGE = Move()
BARRAGE.name = "Barrage"
BARRAGE.type = NORMAL
BARRAGE.base_damage = 15
BARRAGE.category = PHYSICAL
BARRAGE.pp = 20
BARRAGE.accuracy = 85
BARRAGE.priority = 0
BARRAGE.target = 'NearOther'
BARRAGE.additional_effect_chance = 0
BARRAGE.description = "Round objects are hurled at the target to strike two to five times in a row."

############
### BIND ###
############

BIND = Move()
BIND.name = "Bind"
BIND.type = NORMAL
BIND.base_damage = 15
BIND.category = PHYSICAL
BIND.pp = 20
BIND.accuracy = 85
BIND.priority = 0
BIND.target = 'NearOther'
BIND.additional_effect_chance = 0
BIND.description = "Things such as long bodies or tentacles are used to bind and squeeze the foe for four to five turns."

##################
### DOUBLESLAP ###
##################

DOUBLESLAP = Move()
DOUBLESLAP.name = "Double Slap"
DOUBLESLAP.type = NORMAL
DOUBLESLAP.base_damage = 15
DOUBLESLAP.category = PHYSICAL
DOUBLESLAP.pp = 10
DOUBLESLAP.accuracy = 85
DOUBLESLAP.priority = 0
DOUBLESLAP.target = 'NearOther'
DOUBLESLAP.additional_effect_chance = 0
DOUBLESLAP.description = "The target is slapped repeatedly, back and forth, two to five times in a row."

##################
### FURYATTACK ###
##################

FURYATTACK = Move()
FURYATTACK.name = "Fury Attack"
FURYATTACK.type = NORMAL
FURYATTACK.base_damage = 15
FURYATTACK.category = PHYSICAL
FURYATTACK.pp = 20
FURYATTACK.accuracy = 85
FURYATTACK.priority = 0
FURYATTACK.target = 'NearOther'
FURYATTACK.additional_effect_chance = 0
FURYATTACK.description = "The target is jabbed repeatedly with a horn or beak two to five times in a row."

############
### WRAP ###
############

WRAP = Move()
WRAP.name = "Wrap"
WRAP.type = NORMAL
WRAP.base_damage = 15
WRAP.category = PHYSICAL
WRAP.pp = 20
WRAP.accuracy = 90
WRAP.priority = 0
WRAP.target = 'NearOther'
WRAP.additional_effect_chance = 0
WRAP.description = "A long body or vines are used to wrap and squeeze the target for four to five turns."

#################
### CONSTRICT ###
#################

CONSTRICT = Move()
CONSTRICT.name = "Constrict"
CONSTRICT.type = NORMAL
CONSTRICT.base_damage = 10
CONSTRICT.category = PHYSICAL
CONSTRICT.pp = 35
CONSTRICT.accuracy = 100
CONSTRICT.priority = 0
CONSTRICT.target = 'NearOther'
CONSTRICT.additional_effect_chance = 10
CONSTRICT.description = "The foe is attacked with long, creeping tentacles or vines. It may also lower the targets Speed."

############
### BIDE ###
############

BIDE = Move()
BIDE.name = "Bide"
BIDE.type = NORMAL
BIDE.base_damage = 1
BIDE.category = PHYSICAL
BIDE.pp = 10
BIDE.accuracy = 0
BIDE.priority = 1
BIDE.target = 'None'
BIDE.additional_effect_chance = 0
BIDE.description = "The user endures attacks for two turns, then strikes back to cause double the damage taken."

#################
### CRUSHGRIP ###
#################

CRUSHGRIP = Move()
CRUSHGRIP.name = "Crush Grip"
CRUSHGRIP.type = NORMAL
CRUSHGRIP.base_damage = 1
CRUSHGRIP.category = PHYSICAL
CRUSHGRIP.pp = 5
CRUSHGRIP.accuracy = 100
CRUSHGRIP.priority = 0
CRUSHGRIP.target = 'NearOther'
CRUSHGRIP.additional_effect_chance = 0
CRUSHGRIP.description = "The target is crushed with great force. The attack is more powerful the more HP the target has left."

################
### ENDEAVOR ###
################

ENDEAVOR = Move()
ENDEAVOR.name = "Endeavor"
ENDEAVOR.type = NORMAL
ENDEAVOR.base_damage = 1
ENDEAVOR.category = PHYSICAL
ENDEAVOR.pp = 5
ENDEAVOR.accuracy = 100
ENDEAVOR.priority = 0
ENDEAVOR.target = 'NearOther'
ENDEAVOR.additional_effect_chance = 0
ENDEAVOR.description = "An attack move that cuts down the targets HP to equal the users HP."

#############
### FLAIL ###
#############

FLAIL = Move()
FLAIL.name = "Flail"
FLAIL.type = NORMAL
FLAIL.base_damage = 1
FLAIL.category = PHYSICAL
FLAIL.pp = 15
FLAIL.accuracy = 100
FLAIL.priority = 0
FLAIL.target = 'NearOther'
FLAIL.additional_effect_chance = 0
FLAIL.description = "The user flails about aimlessly to attack. It becomes more powerful the less HP the user has."

###################
### FRUSTRATION ###
###################

FRUSTRATION = Move()
FRUSTRATION.name = "Frustration"
FRUSTRATION.type = NORMAL
FRUSTRATION.base_damage = 1
FRUSTRATION.category = PHYSICAL
FRUSTRATION.pp = 20
FRUSTRATION.accuracy = 100
FRUSTRATION.priority = 0
FRUSTRATION.target = 'NearOther'
FRUSTRATION.additional_effect_chance = 0
FRUSTRATION.description = "A full-power attack that grows more powerful the less the user likes its Trainer."

##################
### GUILLOTINE ###
##################

GUILLOTINE = Move()
GUILLOTINE.name = "Guillotine"
GUILLOTINE.type = NORMAL
GUILLOTINE.base_damage = 1
GUILLOTINE.category = PHYSICAL
GUILLOTINE.pp = 5
GUILLOTINE.accuracy = 30
GUILLOTINE.priority = 0
GUILLOTINE.target = 'NearOther'
GUILLOTINE.additional_effect_chance = 0
GUILLOTINE.description = "A vicious, tearing attack with big pincers. The target will faint instantly if this attack hits."

#################
### HORNDRILL ###
#################

HORNDRILL = Move()
HORNDRILL.name = "Horn Drill"
HORNDRILL.type = NORMAL
HORNDRILL.base_damage = 1
HORNDRILL.category = PHYSICAL
HORNDRILL.pp = 5
HORNDRILL.accuracy = 30
HORNDRILL.priority = 0
HORNDRILL.target = 'NearOther'
HORNDRILL.additional_effect_chance = 0
HORNDRILL.description = "The user stabs the foe with a horn that rotates like a drill. If it hits, the target faints instantly."

###################
### NATURALGIFT ###
###################

NATURALGIFT = Move()
NATURALGIFT.name = "Natural Gift"
NATURALGIFT.type = NORMAL
NATURALGIFT.base_damage = 1
NATURALGIFT.category = PHYSICAL
NATURALGIFT.pp = 15
NATURALGIFT.accuracy = 100
NATURALGIFT.priority = 0
NATURALGIFT.target = 'NearOther'
NATURALGIFT.additional_effect_chance = 0
NATURALGIFT.description = "The user draws power to attack by using its held Berry. The Berry determines its type and power."

###############
### PRESENT ###
###############

PRESENT = Move()
PRESENT.name = "Present"
PRESENT.type = NORMAL
PRESENT.base_damage = 1
PRESENT.category = PHYSICAL
PRESENT.pp = 15
PRESENT.accuracy = 90
PRESENT.priority = 0
PRESENT.target = 'NearOther'
PRESENT.additional_effect_chance = 0
PRESENT.description = "The user attacks by giving the target a gift with a hidden trap. It restores HP sometimes, however."

##############
### RETURN ###
##############

RETURN = Move()
RETURN.name = "Return"
RETURN.type = NORMAL
RETURN.base_damage = 1
RETURN.category = PHYSICAL
RETURN.pp = 20
RETURN.accuracy = 100
RETURN.priority = 0
RETURN.target = 'NearOther'
RETURN.additional_effect_chance = 0
RETURN.description = "A full-power attack that grows more powerful the more the user likes its Trainer."

#################
### SONICBOOM ###
#################

SONICBOOM = Move()
SONICBOOM.name = "Sonic Boom"
SONICBOOM.type = NORMAL
SONICBOOM.base_damage = 1
SONICBOOM.category = SPECIAL
SONICBOOM.pp = 20
SONICBOOM.accuracy = 90
SONICBOOM.priority = 0
SONICBOOM.target = 'NearOther'
SONICBOOM.additional_effect_chance = 0
SONICBOOM.description = "The target is hit with a destructive shock wave that always inflicts 20 HP damage."

##############
### SPITUP ###
##############

SPITUP = Move()
SPITUP.name = "Spit Up"
SPITUP.type = NORMAL
SPITUP.base_damage = 1
SPITUP.category = SPECIAL
SPITUP.pp = 10
SPITUP.accuracy = 100
SPITUP.priority = 0
SPITUP.target = 'NearOther'
SPITUP.additional_effect_chance = 0
SPITUP.description = "The power stored using the move Stockpile is released all at once in an attack."

#################
### SUPERFANG ###
#################

SUPERFANG = Move()
SUPERFANG.name = "Super Fang"
SUPERFANG.type = NORMAL
SUPERFANG.base_damage = 1
SUPERFANG.category = PHYSICAL
SUPERFANG.pp = 10
SUPERFANG.accuracy = 90
SUPERFANG.priority = 0
SUPERFANG.target = 'NearOther'
SUPERFANG.additional_effect_chance = 0
SUPERFANG.description = "The user chomps hard on the target with its sharp front fangs. It cuts the targets HP to half."

#################
### TRUMPCARD ###
#################

TRUMPCARD = Move()
TRUMPCARD.name = "Trump Card"
TRUMPCARD.type = NORMAL
TRUMPCARD.base_damage = 1
TRUMPCARD.category = SPECIAL
TRUMPCARD.pp = 5
TRUMPCARD.accuracy = 0
TRUMPCARD.priority = 0
TRUMPCARD.target = 'NearOther'
TRUMPCARD.additional_effect_chance = 0
TRUMPCARD.description = "The fewer PP this move has, the greater its attack power."

################
### WRINGOUT ###
################

WRINGOUT = Move()
WRINGOUT.name = "Wring Out"
WRINGOUT.type = NORMAL
WRINGOUT.base_damage = 1
WRINGOUT.category = SPECIAL
WRINGOUT.pp = 5
WRINGOUT.accuracy = 100
WRINGOUT.priority = 0
WRINGOUT.target = 'NearOther'
WRINGOUT.additional_effect_chance = 0
WRINGOUT.description = "The user powerfully wrings the foe. The more HP the foe has, the greater this attacks power."

###################
### ACUPRESSURE ###
###################

ACUPRESSURE = Move()
ACUPRESSURE.name = "Acupressure"
ACUPRESSURE.type = NORMAL
ACUPRESSURE.base_damage = 0
ACUPRESSURE.category = STATUS
ACUPRESSURE.pp = 30
ACUPRESSURE.accuracy = 0
ACUPRESSURE.priority = 0
ACUPRESSURE.target = 'UserOrNearAlly'
ACUPRESSURE.additional_effect_chance = 0
ACUPRESSURE.description = "The user applies pressure to stress points, sharply boosting one of its stats."

################
### AFTERYOU ###
################

AFTERYOU = Move()
AFTERYOU.name = "After You"
AFTERYOU.type = NORMAL
AFTERYOU.base_damage = 0
AFTERYOU.category = STATUS
AFTERYOU.pp = 15
AFTERYOU.accuracy = 0
AFTERYOU.priority = 0
AFTERYOU.target = 'NearOther'
AFTERYOU.additional_effect_chance = 0
AFTERYOU.description = "The user helps the target and makes it use its move right after the user."

##############
### ASSIST ###
##############

ASSIST = Move()
ASSIST.name = "Assist"
ASSIST.type = NORMAL
ASSIST.base_damage = 0
ASSIST.category = STATUS
ASSIST.pp = 20
ASSIST.accuracy = 0
ASSIST.priority = 0
ASSIST.target = 'User'
ASSIST.additional_effect_chance = 0
ASSIST.description = "The user hurriedly and randomly uses a move among those known by other Pokémon in the party."

###############
### ATTRACT ###
###############

ATTRACT = Move()
ATTRACT.name = "Attract"
ATTRACT.type = NORMAL
ATTRACT.base_damage = 0
ATTRACT.category = STATUS
ATTRACT.pp = 15
ATTRACT.accuracy = 100
ATTRACT.priority = 0
ATTRACT.target = 'NearOther'
ATTRACT.additional_effect_chance = 0
ATTRACT.description = "If it is the opposite gender of the user, the target becomes infatuated and less likely to attack."

#################
### BATONPASS ###
#################

BATONPASS = Move()
BATONPASS.name = "Baton Pass"
BATONPASS.type = NORMAL
BATONPASS.base_damage = 0
BATONPASS.category = STATUS
BATONPASS.pp = 40
BATONPASS.accuracy = 0
BATONPASS.priority = 0
BATONPASS.target = 'User'
BATONPASS.additional_effect_chance = 0
BATONPASS.description = "The user switches places with a party Pokémon in waiting, passing along any stat changes."

#################
### BELLYDRUM ###
#################

BELLYDRUM = Move()
BELLYDRUM.name = "Belly Drum"
BELLYDRUM.type = NORMAL
BELLYDRUM.base_damage = 0
BELLYDRUM.category = STATUS
BELLYDRUM.pp = 10
BELLYDRUM.accuracy = 0
BELLYDRUM.priority = 0
BELLYDRUM.target = 'User'
BELLYDRUM.additional_effect_chance = 0
BELLYDRUM.description = "The user maximizes its Attack stat in exchange for HP equal to half its max HP."

##############
### BESTOW ###
##############

BESTOW = Move()
BESTOW.name = "Bestow"
BESTOW.type = NORMAL
BESTOW.base_damage = 0
BESTOW.category = STATUS
BESTOW.pp = 15
BESTOW.accuracy = 0
BESTOW.priority = 0
BESTOW.target = 'NearOther'
BESTOW.additional_effect_chance = 0
BESTOW.description = "The user passes its held item to the target when the target isnt holding an item."

#############
### BLOCK ###
#############

BLOCK = Move()
BLOCK.name = "Block"
BLOCK.type = NORMAL
BLOCK.base_damage = 0
BLOCK.category = STATUS
BLOCK.pp = 5
BLOCK.accuracy = 0
BLOCK.priority = 0
BLOCK.target = 'NearOther'
BLOCK.additional_effect_chance = 0
BLOCK.description = "The user blocks the targets way with arms spread wide to prevent escape."

##################
### CAMOUFLAGE ###
##################

CAMOUFLAGE = Move()
CAMOUFLAGE.name = "Camouflage"
CAMOUFLAGE.type = NORMAL
CAMOUFLAGE.base_damage = 0
CAMOUFLAGE.category = STATUS
CAMOUFLAGE.pp = 20
CAMOUFLAGE.accuracy = 0
CAMOUFLAGE.priority = 0
CAMOUFLAGE.target = 'User'
CAMOUFLAGE.additional_effect_chance = 0
CAMOUFLAGE.description = "The users type is changed depending on its environment, such as at waters edge, in grass, or in a cave."

#################
### CAPTIVATE ###
#################

CAPTIVATE = Move()
CAPTIVATE.name = "Captivate"
CAPTIVATE.type = NORMAL
CAPTIVATE.base_damage = 0
CAPTIVATE.category = STATUS
CAPTIVATE.pp = 20
CAPTIVATE.accuracy = 100
CAPTIVATE.priority = 0
CAPTIVATE.target = 'AllNearFoes'
CAPTIVATE.additional_effect_chance = 0
CAPTIVATE.description = "If it is the opposite gender of the user, the target is charmed into harshly lowering its Sp. Atk stat."

#################
### CELEBRATE ###
#################

CELEBRATE = Move()
CELEBRATE.name = "Celebrate"
CELEBRATE.type = NORMAL
CELEBRATE.base_damage = 0
CELEBRATE.category = STATUS
CELEBRATE.pp = 40
CELEBRATE.accuracy = 0
CELEBRATE.priority = 0
CELEBRATE.target = 'User'
CELEBRATE.additional_effect_chance = 0
CELEBRATE.description = "The Pokémon congratulates you on your special day!"

###############
### CONFIDE ###
###############

CONFIDE = Move()
CONFIDE.name = "Confide"
CONFIDE.type = NORMAL
CONFIDE.base_damage = 0
CONFIDE.category = STATUS
CONFIDE.pp = 20
CONFIDE.accuracy = 0
CONFIDE.priority = 0
CONFIDE.target = 'NearOther'
CONFIDE.additional_effect_chance = 0
CONFIDE.description = "The user tells the target a secret. The target loses focus and its Sp. Atk stat is lowered."

##################
### CONVERSION ###
##################

CONVERSION = Move()
CONVERSION.name = "Conversion"
CONVERSION.type = NORMAL
CONVERSION.base_damage = 0
CONVERSION.category = STATUS
CONVERSION.pp = 30
CONVERSION.accuracy = 0
CONVERSION.priority = 0
CONVERSION.target = 'User'
CONVERSION.additional_effect_chance = 0
CONVERSION.description = "The user changes its type to become the same type as one of its moves."

###################
### CONVERSION2 ###
###################

CONVERSION2 = Move()
CONVERSION2.name = "Conversion 2"
CONVERSION2.type = NORMAL
CONVERSION2.base_damage = 0
CONVERSION2.category = STATUS
CONVERSION2.pp = 30
CONVERSION2.accuracy = 0
CONVERSION2.priority = 0
CONVERSION2.target = 'NearOther'
CONVERSION2.additional_effect_chance = 0
CONVERSION2.description = "The user changes its type to make itself resistant to the type of the attack the opponent used last."

###############
### COPYCAT ###
###############

COPYCAT = Move()
COPYCAT.name = "Copycat"
COPYCAT.type = NORMAL
COPYCAT.base_damage = 0
COPYCAT.category = STATUS
COPYCAT.pp = 20
COPYCAT.accuracy = 0
COPYCAT.priority = 0
COPYCAT.target = 'User'
COPYCAT.additional_effect_chance = 0
COPYCAT.description = "The user mimics the move used immediately before it. The move fails if no other move has been used yet."

###################
### DEFENSECURL ###
###################

DEFENSECURL = Move()
DEFENSECURL.name = "Defense Curl"
DEFENSECURL.type = NORMAL
DEFENSECURL.base_damage = 0
DEFENSECURL.category = STATUS
DEFENSECURL.pp = 40
DEFENSECURL.accuracy = 0
DEFENSECURL.priority = 0
DEFENSECURL.target = 'User'
DEFENSECURL.additional_effect_chance = 0
DEFENSECURL.description = "The user curls up to conceal weak spots and raise its Defense stat."

###############
### DISABLE ###
###############

DISABLE = Move()
DISABLE.name = "Disable"
DISABLE.type = NORMAL
DISABLE.base_damage = 0
DISABLE.category = STATUS
DISABLE.pp = 20
DISABLE.accuracy = 100
DISABLE.priority = 0
DISABLE.target = 'NearOther'
DISABLE.additional_effect_chance = 0
DISABLE.description = "For four turns, this move prevents the target from using the move it last used."

##################
### DOUBLETEAM ###
##################

DOUBLETEAM = Move()
DOUBLETEAM.name = "Double Team"
DOUBLETEAM.type = NORMAL
DOUBLETEAM.base_damage = 0
DOUBLETEAM.category = STATUS
DOUBLETEAM.pp = 15
DOUBLETEAM.accuracy = 0
DOUBLETEAM.priority = 0
DOUBLETEAM.target = 'User'
DOUBLETEAM.additional_effect_chance = 0
DOUBLETEAM.description = "By moving rapidly, the user makes illusory copies of itself to raise its evasiveness."

##############
### ENCORE ###
##############

ENCORE = Move()
ENCORE.name = "Encore"
ENCORE.type = NORMAL
ENCORE.base_damage = 0
ENCORE.category = STATUS
ENCORE.pp = 5
ENCORE.accuracy = 100
ENCORE.priority = 0
ENCORE.target = 'NearOther'
ENCORE.additional_effect_chance = 0
ENCORE.description = "The user compels the target to keep using only the move it last used for three turns."

##############
### ENDURE ###
##############

ENDURE = Move()
ENDURE.name = "Endure"
ENDURE.type = NORMAL
ENDURE.base_damage = 0
ENDURE.category = STATUS
ENDURE.pp = 10
ENDURE.accuracy = 0
ENDURE.priority = 4
ENDURE.target = 'User'
ENDURE.additional_effect_chance = 0
ENDURE.description = "The user endures any attack with at least 1 HP. Its chance of failing rises if it is used in succession."

###################
### ENTRAINMENT ###
###################

ENTRAINMENT = Move()
ENTRAINMENT.name = "Entrainment"
ENTRAINMENT.type = NORMAL
ENTRAINMENT.base_damage = 0
ENTRAINMENT.category = STATUS
ENTRAINMENT.pp = 15
ENTRAINMENT.accuracy = 100
ENTRAINMENT.priority = 0
ENTRAINMENT.target = 'NearOther'
ENTRAINMENT.additional_effect_chance = 0
ENTRAINMENT.description = "The user dances to compel the target to mimic it, making the targets Ability the same as the users."

#############
### FLASH ###
#############

FLASH = Move()
FLASH.name = "Flash"
FLASH.type = NORMAL
FLASH.base_damage = 0
FLASH.category = STATUS
FLASH.pp = 20
FLASH.accuracy = 100
FLASH.priority = 0
FLASH.target = 'NearOther'
FLASH.additional_effect_chance = 0
FLASH.description = "The user flashes a light that cuts the targets accuracy. It can also be used to illuminate caves."

###################
### FOCUSENERGY ###
###################

FOCUSENERGY = Move()
FOCUSENERGY.name = "Focus Energy"
FOCUSENERGY.type = NORMAL
FOCUSENERGY.base_damage = 0
FOCUSENERGY.category = STATUS
FOCUSENERGY.pp = 30
FOCUSENERGY.accuracy = 0
FOCUSENERGY.priority = 0
FOCUSENERGY.target = 'User'
FOCUSENERGY.additional_effect_chance = 0
FOCUSENERGY.description = "The user takes a deep breath and focuses so that critical hits land more easily."

################
### FOLLOWME ###
################

FOLLOWME = Move()
FOLLOWME.name = "Follow Me"
FOLLOWME.type = NORMAL
FOLLOWME.base_damage = 0
FOLLOWME.category = STATUS
FOLLOWME.pp = 20
FOLLOWME.accuracy = 0
FOLLOWME.priority = 2
FOLLOWME.target = 'User'
FOLLOWME.additional_effect_chance = 0
FOLLOWME.description = "The user draws attention to itself, making all targets take aim only at the user."

#################
### FORESIGHT ###
#################

FORESIGHT = Move()
FORESIGHT.name = "Foresight"
FORESIGHT.type = NORMAL
FORESIGHT.base_damage = 0
FORESIGHT.category = STATUS
FORESIGHT.pp = 40
FORESIGHT.accuracy = 0
FORESIGHT.priority = 0
FORESIGHT.target = 'NearOther'
FORESIGHT.additional_effect_chance = 0
FORESIGHT.description = "Enables the user to hit a Ghost type with any kind of move. It also enables the user to hit an evasive foe."

#############
### GLARE ###
#############

GLARE = Move()
GLARE.name = "Glare"
GLARE.type = NORMAL
GLARE.base_damage = 0
GLARE.category = STATUS
GLARE.pp = 30
GLARE.accuracy = 100
GLARE.priority = 0
GLARE.target = 'NearOther'
GLARE.additional_effect_chance = 0
GLARE.description = "The user intimidates the target with the pattern on its belly to cause paralysis."

#############
### GROWL ###
#############

GROWL = Move()
GROWL.name = "Growl"
GROWL.type = NORMAL
GROWL.base_damage = 0
GROWL.category = STATUS
GROWL.pp = 40
GROWL.accuracy = 100
GROWL.priority = 0
GROWL.target = 'AllNearFoes'
GROWL.additional_effect_chance = 0
GROWL.description = "The user growls in an endearing way, making the foe less wary. The foes Attack stat is lowered."

##############
### GROWTH ###
##############

GROWTH = Move()
GROWTH.name = "Growth"
GROWTH.type = NORMAL
GROWTH.base_damage = 0
GROWTH.category = STATUS
GROWTH.pp = 20
GROWTH.accuracy = 0
GROWTH.priority = 0
GROWTH.target = 'User'
GROWTH.additional_effect_chance = 0
GROWTH.description = "The users body grows all at once, raising the Atk and Sp. Atk stats."

#################
### HAPPYHOUR ###
#################

HAPPYHOUR = Move()
HAPPYHOUR.name = "Happy Hour"
HAPPYHOUR.type = NORMAL
HAPPYHOUR.base_damage = 0
HAPPYHOUR.category = STATUS
HAPPYHOUR.pp = 30
HAPPYHOUR.accuracy = 0
HAPPYHOUR.priority = 0
HAPPYHOUR.target = 'UserSide'
HAPPYHOUR.additional_effect_chance = 0
HAPPYHOUR.description = "Using Happy Hour doubles the amount of prize money received after battle."

##############
### HARDEN ###
##############

HARDEN = Move()
HARDEN.name = "Harden"
HARDEN.type = NORMAL
HARDEN.base_damage = 0
HARDEN.category = STATUS
HARDEN.pp = 30
HARDEN.accuracy = 0
HARDEN.priority = 0
HARDEN.target = 'User'
HARDEN.additional_effect_chance = 0
HARDEN.description = "The user stiffens all the muscles in its body to raise its Defense stat."

################
### HEALBELL ###
################

HEALBELL = Move()
HEALBELL.name = "Heal Bell"
HEALBELL.type = NORMAL
HEALBELL.base_damage = 0
HEALBELL.category = STATUS
HEALBELL.pp = 5
HEALBELL.accuracy = 0
HEALBELL.priority = 0
HEALBELL.target = 'UserAndAllies'
HEALBELL.additional_effect_chance = 0
HEALBELL.description = "The user makes a soothing bell chime to heal the status problems of all the party Pokémon."

###################
### HELPINGHAND ###
###################

HELPINGHAND = Move()
HELPINGHAND.name = "Helping Hand"
HELPINGHAND.type = NORMAL
HELPINGHAND.base_damage = 0
HELPINGHAND.category = STATUS
HELPINGHAND.pp = 20
HELPINGHAND.accuracy = 0
HELPINGHAND.priority = 5
HELPINGHAND.target = 'NearAlly'
HELPINGHAND.additional_effect_chance = 0
HELPINGHAND.description = "The user assists an ally by boosting the power of its attack."

#################
### HOLDHANDS ###
#################

HOLDHANDS = Move()
HOLDHANDS.name = "Hold Hands"
HOLDHANDS.type = NORMAL
HOLDHANDS.base_damage = 0
HOLDHANDS.category = STATUS
HOLDHANDS.pp = 40
HOLDHANDS.accuracy = 0
HOLDHANDS.priority = 0
HOLDHANDS.target = 'NearAlly'
HOLDHANDS.additional_effect_chance = 0
HOLDHANDS.description = "The user and an ally hold hands. This makes them very happy."

############
### HOWL ###
############

HOWL = Move()
HOWL.name = "Howl"
HOWL.type = NORMAL
HOWL.base_damage = 0
HOWL.category = STATUS
HOWL.pp = 40
HOWL.accuracy = 0
HOWL.priority = 0
HOWL.target = 'User'
HOWL.additional_effect_chance = 0
HOWL.description = "The user howls loudly to raise its spirit, boosting its Attack stat."

##################
### LASERFOCUS ###
##################

LASERFOCUS = Move()
LASERFOCUS.name = "Laser Focus"
LASERFOCUS.type = NORMAL
LASERFOCUS.base_damage = 0
LASERFOCUS.category = STATUS
LASERFOCUS.pp = 30
LASERFOCUS.accuracy = 0
LASERFOCUS.priority = 0
LASERFOCUS.target = 'User'
LASERFOCUS.additional_effect_chance = 0
LASERFOCUS.description = "The user focuses intensely. The attack on the next turn always results in a critical hit."

############
### LEER ###
############

LEER = Move()
LEER.name = "Leer"
LEER.type = NORMAL
LEER.base_damage = 0
LEER.category = STATUS
LEER.pp = 30
LEER.accuracy = 100
LEER.priority = 0
LEER.target = 'AllNearFoes'
LEER.additional_effect_chance = 0
LEER.description = "The user gains an intimidating leer with sharp eyes. The targets Defense stat is reduced."

##############
### LOCKON ###
##############

LOCKON = Move()
LOCKON.name = "Lock-On"
LOCKON.type = NORMAL
LOCKON.base_damage = 0
LOCKON.category = STATUS
LOCKON.pp = 5
LOCKON.accuracy = 0
LOCKON.priority = 0
LOCKON.target = 'NearOther'
LOCKON.additional_effect_chance = 0
LOCKON.description = "The user takes sure aim at the target. It ensures the next attack does not fail to hit the target."

##################
### LOVELYKISS ###
##################

LOVELYKISS = Move()
LOVELYKISS.name = "Lovely Kiss"
LOVELYKISS.type = NORMAL
LOVELYKISS.base_damage = 0
LOVELYKISS.category = STATUS
LOVELYKISS.pp = 10
LOVELYKISS.accuracy = 75
LOVELYKISS.priority = 0
LOVELYKISS.target = 'NearOther'
LOVELYKISS.additional_effect_chance = 0
LOVELYKISS.description = "With a scary face, the user tries to force a kiss on the target. If it suceeds, the target falls asleep."

##################
### LUCKYCHANT ###
##################

LUCKYCHANT = Move()
LUCKYCHANT.name = "Lucky Chant"
LUCKYCHANT.type = NORMAL
LUCKYCHANT.base_damage = 0
LUCKYCHANT.category = STATUS
LUCKYCHANT.pp = 30
LUCKYCHANT.accuracy = 0
LUCKYCHANT.priority = 0
LUCKYCHANT.target = 'UserSide'
LUCKYCHANT.additional_effect_chance = 0
LUCKYCHANT.description = "The user chants an incantation toward the sky, preventing the foe from landing critical hits."

###############
### MEFIRST ###
###############

MEFIRST = Move()
MEFIRST.name = "Me First"
MEFIRST.type = NORMAL
MEFIRST.base_damage = 0
MEFIRST.category = STATUS
MEFIRST.pp = 20
MEFIRST.accuracy = 0
MEFIRST.priority = 0
MEFIRST.target = 'NearFoe'
MEFIRST.additional_effect_chance = 0
MEFIRST.description = "The user tries to cut ahead of the foe to steal and use the foes intended move with greater power."

################
### MEANLOOK ###
################

MEANLOOK = Move()
MEANLOOK.name = "Mean Look"
MEANLOOK.type = NORMAL
MEANLOOK.base_damage = 0
MEANLOOK.category = STATUS
MEANLOOK.pp = 5
MEANLOOK.accuracy = 0
MEANLOOK.priority = 0
MEANLOOK.target = 'NearOther'
MEANLOOK.additional_effect_chance = 0
MEANLOOK.description = "The user pins the target with a dark, arresting look. The target becomes unable to flee."

#################
### METRONOME ###
#################

METRONOME = Move()
METRONOME.name = "Metronome"
METRONOME.type = NORMAL
METRONOME.base_damage = 0
METRONOME.category = STATUS
METRONOME.pp = 10
METRONOME.accuracy = 0
METRONOME.priority = 0
METRONOME.target = 'User'
METRONOME.additional_effect_chance = 0
METRONOME.description = "The user waggles a finger and stimulates its brain into randomly using nearly any move."

#################
### MILKDRINK ###
#################

MILKDRINK = Move()
MILKDRINK.name = "Milk Drink"
MILKDRINK.type = NORMAL
MILKDRINK.base_damage = 0
MILKDRINK.category = STATUS
MILKDRINK.pp = 10
MILKDRINK.accuracy = 0
MILKDRINK.priority = 0
MILKDRINK.target = 'User'
MILKDRINK.additional_effect_chance = 0
MILKDRINK.description = "The user restores its own HP by up to half of its maximum HP. May also be used in the field to heal HP."

#############
### MIMIC ###
#############

MIMIC = Move()
MIMIC.name = "Mimic"
MIMIC.type = NORMAL
MIMIC.base_damage = 0
MIMIC.category = STATUS
MIMIC.pp = 10
MIMIC.accuracy = 0
MIMIC.priority = 0
MIMIC.target = 'NearOther'
MIMIC.additional_effect_chance = 0
MIMIC.description = "The user copies the move last used by the foe. The move can be used until the user is switched out."

##################
### MINDREADER ###
##################

MINDREADER = Move()
MINDREADER.name = "Mind Reader"
MINDREADER.type = NORMAL
MINDREADER.base_damage = 0
MINDREADER.category = STATUS
MINDREADER.pp = 5
MINDREADER.accuracy = 0
MINDREADER.priority = 0
MINDREADER.target = 'NearOther'
MINDREADER.additional_effect_chance = 0
MINDREADER.description = "The user senses the foes movements with its mind to ensure its next attack does not miss the foe."

################
### MINIMIZE ###
################

MINIMIZE = Move()
MINIMIZE.name = "Minimize"
MINIMIZE.type = NORMAL
MINIMIZE.base_damage = 0
MINIMIZE.category = STATUS
MINIMIZE.pp = 10
MINIMIZE.accuracy = 0
MINIMIZE.priority = 0
MINIMIZE.target = 'User'
MINIMIZE.additional_effect_chance = 0
MINIMIZE.description = "The user compresses its body to make itself look smaller, which sharply raises its evasiveness."

##################
### MORNINGSUN ###
##################

MORNINGSUN = Move()
MORNINGSUN.name = "Morning Sun"
MORNINGSUN.type = NORMAL
MORNINGSUN.base_damage = 0
MORNINGSUN.category = STATUS
MORNINGSUN.pp = 5
MORNINGSUN.accuracy = 0
MORNINGSUN.priority = 0
MORNINGSUN.target = 'User'
MORNINGSUN.additional_effect_chance = 0
MORNINGSUN.description = "The user restores its own HP. The amount of HP regained varies with the weather."

###################
### NATUREPOWER ###
###################

NATUREPOWER = Move()
NATUREPOWER.name = "Nature Power"
NATUREPOWER.type = NORMAL
NATUREPOWER.base_damage = 0
NATUREPOWER.category = STATUS
NATUREPOWER.pp = 20
NATUREPOWER.accuracy = 0
NATUREPOWER.priority = 0
NATUREPOWER.target = 'NearOther'
NATUREPOWER.additional_effect_chance = 0
NATUREPOWER.description = "An attack that makes use of natures power. Its effects vary depending on the users environment."

#################
### NOBLEROAR ###
#################

NOBLEROAR = Move()
NOBLEROAR.name = "Noble Roar"
NOBLEROAR.type = NORMAL
NOBLEROAR.base_damage = 0
NOBLEROAR.category = STATUS
NOBLEROAR.pp = 30
NOBLEROAR.accuracy = 0
NOBLEROAR.priority = 0
NOBLEROAR.target = 'NearOther'
NOBLEROAR.additional_effect_chance = 0
NOBLEROAR.description = "Letting out a noble roar, the user intimidates the target and lowers its Attack and Sp. Atk."

##################
### ODORSLEUTH ###
##################

ODORSLEUTH = Move()
ODORSLEUTH.name = "Odor Sleuth"
ODORSLEUTH.type = NORMAL
ODORSLEUTH.base_damage = 0
ODORSLEUTH.category = STATUS
ODORSLEUTH.pp = 40
ODORSLEUTH.accuracy = 0
ODORSLEUTH.priority = 0
ODORSLEUTH.target = 'NearOther'
ODORSLEUTH.additional_effect_chance = 0
ODORSLEUTH.description = "Enables the user to hit a Ghost type with any type of move. It also enables the user to hit an evasive foe."

#################
### PAINSPLIT ###
#################

PAINSPLIT = Move()
PAINSPLIT.name = "Pain Split"
PAINSPLIT.type = NORMAL
PAINSPLIT.base_damage = 0
PAINSPLIT.category = STATUS
PAINSPLIT.pp = 20
PAINSPLIT.accuracy = 0
PAINSPLIT.priority = 0
PAINSPLIT.target = 'NearOther'
PAINSPLIT.additional_effect_chance = 0
PAINSPLIT.description = "The user adds its HP to the targets HP, then equally shares the combined HP with the target."

##################
### PERISHSONG ###
##################

PERISHSONG = Move()
PERISHSONG.name = "Perish Song"
PERISHSONG.type = NORMAL
PERISHSONG.base_damage = 0
PERISHSONG.category = STATUS
PERISHSONG.pp = 5
PERISHSONG.accuracy = 0
PERISHSONG.priority = 0
PERISHSONG.target = 'AllBattlers'
PERISHSONG.additional_effect_chance = 0
PERISHSONG.description = "Any Pokémon that hears this song faints in three turns, unless it switches out of battle."

################
### PLAYNICE ###
################

PLAYNICE = Move()
PLAYNICE.name = "Play Nice"
PLAYNICE.type = NORMAL
PLAYNICE.base_damage = 0
PLAYNICE.category = STATUS
PLAYNICE.pp = 20
PLAYNICE.accuracy = 0
PLAYNICE.priority = 0
PLAYNICE.target = 'NearOther'
PLAYNICE.additional_effect_chance = 0
PLAYNICE.description = "The user and target become friends. The target loses its will to fight, lowering its Attack stat."

###############
### PROTECT ###
###############

PROTECT = Move()
PROTECT.name = "Protect"
PROTECT.type = NORMAL
PROTECT.base_damage = 0
PROTECT.category = STATUS
PROTECT.pp = 10
PROTECT.accuracy = 0
PROTECT.priority = 4
PROTECT.target = 'User'
PROTECT.additional_effect_chance = 0
PROTECT.description = "It enables the user to evade all attacks. Its chance of failing rises if it is used in succession."

###############
### PSYCHUP ###
###############

PSYCHUP = Move()
PSYCHUP.name = "Psych Up"
PSYCHUP.type = NORMAL
PSYCHUP.base_damage = 0
PSYCHUP.category = STATUS
PSYCHUP.pp = 10
PSYCHUP.accuracy = 0
PSYCHUP.priority = 0
PSYCHUP.target = 'NearOther'
PSYCHUP.additional_effect_chance = 0
PSYCHUP.description = "The user hypnotizes itself into copying any stat change made by the target."

###############
### RECOVER ###
###############

RECOVER = Move()
RECOVER.name = "Recover"
RECOVER.type = NORMAL
RECOVER.base_damage = 0
RECOVER.category = STATUS
RECOVER.pp = 10
RECOVER.accuracy = 0
RECOVER.priority = 0
RECOVER.target = 'User'
RECOVER.additional_effect_chance = 0
RECOVER.description = "Restoring its own cells, the user restores its own HP by half of its max HP."

###############
### RECYCLE ###
###############

RECYCLE = Move()
RECYCLE.name = "Recycle"
RECYCLE.type = NORMAL
RECYCLE.base_damage = 0
RECYCLE.category = STATUS
RECYCLE.pp = 10
RECYCLE.accuracy = 0
RECYCLE.priority = 0
RECYCLE.target = 'User'
RECYCLE.additional_effect_chance = 0
RECYCLE.description = "The user recycles a held item that has been used in battle so it can be used again."

###################
### REFLECTTYPE ###
###################

REFLECTTYPE = Move()
REFLECTTYPE.name = "Reflect Type"
REFLECTTYPE.type = NORMAL
REFLECTTYPE.base_damage = 0
REFLECTTYPE.category = STATUS
REFLECTTYPE.pp = 15
REFLECTTYPE.accuracy = 0
REFLECTTYPE.priority = 0
REFLECTTYPE.target = 'NearOther'
REFLECTTYPE.additional_effect_chance = 0
REFLECTTYPE.description = "The user reflects the targets type, making it the same type as the target."

###############
### REFRESH ###
###############

REFRESH = Move()
REFRESH.name = "Refresh"
REFRESH.type = NORMAL
REFRESH.base_damage = 0
REFRESH.category = STATUS
REFRESH.pp = 20
REFRESH.accuracy = 0
REFRESH.priority = 0
REFRESH.target = 'User'
REFRESH.additional_effect_chance = 0
REFRESH.description = "The user rests to cure itself of a poisoning, burn, or paralysis."

############
### ROAR ###
############

ROAR = Move()
ROAR.name = "Roar"
ROAR.type = NORMAL
ROAR.base_damage = 0
ROAR.category = STATUS
ROAR.pp = 20
ROAR.accuracy = 0
ROAR.priority = -6
ROAR.target = 'NearOther'
ROAR.additional_effect_chance = 0
ROAR.description = "The target is scared off and replaced by another Pokémon in its party. In the wild, the battle ends."

#################
### SAFEGUARD ###
#################

SAFEGUARD = Move()
SAFEGUARD.name = "Safeguard"
SAFEGUARD.type = NORMAL
SAFEGUARD.base_damage = 0
SAFEGUARD.category = STATUS
SAFEGUARD.pp = 25
SAFEGUARD.accuracy = 0
SAFEGUARD.priority = 0
SAFEGUARD.target = 'UserSide'
SAFEGUARD.additional_effect_chance = 0
SAFEGUARD.description = "The user creates a protective field that prevents status problems for five turns."

#################
### SCARYFACE ###
#################

SCARYFACE = Move()
SCARYFACE.name = "Scary Face"
SCARYFACE.type = NORMAL
SCARYFACE.base_damage = 0
SCARYFACE.category = STATUS
SCARYFACE.pp = 10
SCARYFACE.accuracy = 100
SCARYFACE.priority = 0
SCARYFACE.target = 'NearOther'
SCARYFACE.additional_effect_chance = 0
SCARYFACE.description = "The user frightens the target with a scary face to harshly reduce its Speed stat."

###############
### SCREECH ###
###############

SCREECH = Move()
SCREECH.name = "Screech"
SCREECH.type = NORMAL
SCREECH.base_damage = 0
SCREECH.category = STATUS
SCREECH.pp = 40
SCREECH.accuracy = 85
SCREECH.priority = 0
SCREECH.target = 'NearOther'
SCREECH.additional_effect_chance = 0
SCREECH.description = "An earsplitting screech harshly reduces the targets Defense stat."

###############
### SHARPEN ###
###############

SHARPEN = Move()
SHARPEN.name = "Sharpen"
SHARPEN.type = NORMAL
SHARPEN.base_damage = 0
SHARPEN.category = STATUS
SHARPEN.pp = 30
SHARPEN.accuracy = 0
SHARPEN.priority = 0
SHARPEN.target = 'User'
SHARPEN.additional_effect_chance = 0
SHARPEN.description = "The user reduces its polygon count to make itself more jagged, raising the Attack stat."

##################
### SHELLSMASH ###
##################

SHELLSMASH = Move()
SHELLSMASH.name = "Shell Smash"
SHELLSMASH.type = NORMAL
SHELLSMASH.base_damage = 0
SHELLSMASH.category = STATUS
SHELLSMASH.pp = 15
SHELLSMASH.accuracy = 0
SHELLSMASH.priority = 0
SHELLSMASH.target = 'User'
SHELLSMASH.additional_effect_chance = 0
SHELLSMASH.description = "The user breaks its shell, lowering its defenses but sharply raising attacking and Speed stats."

##################
### SIMPLEBEAM ###
##################

SIMPLEBEAM = Move()
SIMPLEBEAM.name = "Simple Beam"
SIMPLEBEAM.type = NORMAL
SIMPLEBEAM.base_damage = 0
SIMPLEBEAM.category = STATUS
SIMPLEBEAM.pp = 15
SIMPLEBEAM.accuracy = 100
SIMPLEBEAM.priority = 0
SIMPLEBEAM.target = 'NearOther'
SIMPLEBEAM.additional_effect_chance = 0
SIMPLEBEAM.description = "The users mysterious psychic wave changes the targets Ability to Simple."

############
### SING ###
############

SING = Move()
SING.name = "Sing"
SING.type = NORMAL
SING.base_damage = 0
SING.category = STATUS
SING.pp = 15
SING.accuracy = 55
SING.priority = 0
SING.target = 'NearOther'
SING.additional_effect_chance = 0
SING.description = "A soothing lullaby is sung in a calming voice that puts the target into a deep slumber."

##############
### SKETCH ###
##############

SKETCH = Move()
SKETCH.name = "Sketch"
SKETCH.type = NORMAL
SKETCH.base_damage = 0
SKETCH.category = STATUS
SKETCH.pp = 1
SKETCH.accuracy = 0
SKETCH.priority = 0
SKETCH.target = 'NearOther'
SKETCH.additional_effect_chance = 0
SKETCH.description = "It enables the user to permanently learn the move last used by the foe. Once used, Sketch disappears."

################
### SLACKOFF ###
################

SLACKOFF = Move()
SLACKOFF.name = "Slack Off"
SLACKOFF.type = NORMAL
SLACKOFF.base_damage = 0
SLACKOFF.category = STATUS
SLACKOFF.pp = 10
SLACKOFF.accuracy = 0
SLACKOFF.priority = 0
SLACKOFF.target = 'User'
SLACKOFF.additional_effect_chance = 0
SLACKOFF.description = "The user slacks off, restoring its own HP by up to half of its maximum HP."

#################
### SLEEPTALK ###
#################

SLEEPTALK = Move()
SLEEPTALK.name = "Sleep Talk"
SLEEPTALK.type = NORMAL
SLEEPTALK.base_damage = 0
SLEEPTALK.category = STATUS
SLEEPTALK.pp = 10
SLEEPTALK.accuracy = 0
SLEEPTALK.priority = 0
SLEEPTALK.target = 'User'
SLEEPTALK.additional_effect_chance = 0
SLEEPTALK.description = "While it is asleep, the user randomly uses one of the moves it knows."

###################
### SMOKESCREEN ###
###################

SMOKESCREEN = Move()
SMOKESCREEN.name = "Smokescreen"
SMOKESCREEN.type = NORMAL
SMOKESCREEN.base_damage = 0
SMOKESCREEN.category = STATUS
SMOKESCREEN.pp = 20
SMOKESCREEN.accuracy = 100
SMOKESCREEN.priority = 0
SMOKESCREEN.target = 'NearOther'
SMOKESCREEN.additional_effect_chance = 0
SMOKESCREEN.description = "The user releases an obscuring cloud of smoke or ink. It reduces the targets accuracy."

##################
### SOFTBOILED ###
##################

SOFTBOILED = Move()
SOFTBOILED.name = "Soft-Boiled"
SOFTBOILED.type = NORMAL
SOFTBOILED.base_damage = 0
SOFTBOILED.category = STATUS
SOFTBOILED.pp = 10
SOFTBOILED.accuracy = 0
SOFTBOILED.priority = 0
SOFTBOILED.target = 'User'
SOFTBOILED.additional_effect_chance = 0
SOFTBOILED.description = "The user restores its own HP by up to half of its maximum HP. May also be used in the field to heal HP."

##############
### SPLASH ###
##############

SPLASH = Move()
SPLASH.name = "Splash"
SPLASH.type = NORMAL
SPLASH.base_damage = 0
SPLASH.category = STATUS
SPLASH.pp = 40
SPLASH.accuracy = 0
SPLASH.priority = 0
SPLASH.target = 'User'
SPLASH.additional_effect_chance = 0
SPLASH.description = "The user just flops and splashes around to no effect at all..."

#################
### SPOTLIGHT ###
#################

SPOTLIGHT = Move()
SPOTLIGHT.name = "Spotlight"
SPOTLIGHT.type = NORMAL
SPOTLIGHT.base_damage = 0
SPOTLIGHT.category = STATUS
SPOTLIGHT.pp = 15
SPOTLIGHT.accuracy = 0
SPOTLIGHT.priority = 3
SPOTLIGHT.target = 'NearOther'
SPOTLIGHT.additional_effect_chance = 0
SPOTLIGHT.description = "The user shines a spotlight on the target so that only it will be attacked during the turn."

#################
### STOCKPILE ###
#################

STOCKPILE = Move()
STOCKPILE.name = "Stockpile"
STOCKPILE.type = NORMAL
STOCKPILE.base_damage = 0
STOCKPILE.category = STATUS
STOCKPILE.pp = 20
STOCKPILE.accuracy = 0
STOCKPILE.priority = 0
STOCKPILE.target = 'User'
STOCKPILE.additional_effect_chance = 0
STOCKPILE.description = "The user charges up power and raises both its Defense and Sp. Def. The move can be used three times."

##################
### SUBSTITUTE ###
##################

SUBSTITUTE = Move()
SUBSTITUTE.name = "Substitute"
SUBSTITUTE.type = NORMAL
SUBSTITUTE.base_damage = 0
SUBSTITUTE.category = STATUS
SUBSTITUTE.pp = 10
SUBSTITUTE.accuracy = 0
SUBSTITUTE.priority = 0
SUBSTITUTE.target = 'User'
SUBSTITUTE.additional_effect_chance = 0
SUBSTITUTE.description = "The user makes a copy of itself using some of its HP. The copy serves as the users decoy."

##################
### SUPERSONIC ###
##################

SUPERSONIC = Move()
SUPERSONIC.name = "Supersonic"
SUPERSONIC.type = NORMAL
SUPERSONIC.base_damage = 0
SUPERSONIC.category = STATUS
SUPERSONIC.pp = 20
SUPERSONIC.accuracy = 55
SUPERSONIC.priority = 0
SUPERSONIC.target = 'NearOther'
SUPERSONIC.additional_effect_chance = 0
SUPERSONIC.description = "The user generates odd sound waves from its body. It may confuse the target."

###############
### SWAGGER ###
###############

SWAGGER = Move()
SWAGGER.name = "Swagger"
SWAGGER.type = NORMAL
SWAGGER.base_damage = 0
SWAGGER.category = STATUS
SWAGGER.pp = 15
SWAGGER.accuracy = 85
SWAGGER.priority = 0
SWAGGER.target = 'NearOther'
SWAGGER.additional_effect_chance = 0
SWAGGER.description = "The user enrages and confuses the target. However, it also sharply raises the targets Attack stat."

###############
### SWALLOW ###
###############

SWALLOW = Move()
SWALLOW.name = "Swallow"
SWALLOW.type = NORMAL
SWALLOW.base_damage = 0
SWALLOW.category = STATUS
SWALLOW.pp = 10
SWALLOW.accuracy = 0
SWALLOW.priority = 0
SWALLOW.target = 'User'
SWALLOW.additional_effect_chance = 0
SWALLOW.description = "The power stored using the move Stockpile is absorbed by the user to heal its HP."

##################
### SWEETSCENT ###
##################

SWEETSCENT = Move()
SWEETSCENT.name = "Sweet Scent"
SWEETSCENT.type = NORMAL
SWEETSCENT.base_damage = 0
SWEETSCENT.category = STATUS
SWEETSCENT.pp = 20
SWEETSCENT.accuracy = 100
SWEETSCENT.priority = 0
SWEETSCENT.target = 'AllNearFoes'
SWEETSCENT.additional_effect_chance = 0
SWEETSCENT.description = "A sweet scent that lowers the foes evasiveness. It also lures wild Pokémon if used in grass, etc."

###################
### SWORDSDANCE ###
###################

SWORDSDANCE = Move()
SWORDSDANCE.name = "Swords Dance"
SWORDSDANCE.type = NORMAL
SWORDSDANCE.base_damage = 0
SWORDSDANCE.category = STATUS
SWORDSDANCE.pp = 10
SWORDSDANCE.accuracy = 0
SWORDSDANCE.priority = 0
SWORDSDANCE.target = 'User'
SWORDSDANCE.additional_effect_chance = 0
SWORDSDANCE.description = "A frenetic dance to uplift the fighting spirit. It sharply raises the users Attack stat."

################
### TAILWHIP ###
################

TAILWHIP = Move()
TAILWHIP.name = "Tail Whip"
TAILWHIP.type = NORMAL
TAILWHIP.base_damage = 0
TAILWHIP.category = STATUS
TAILWHIP.pp = 30
TAILWHIP.accuracy = 100
TAILWHIP.priority = 0
TAILWHIP.target = 'AllNearFoes'
TAILWHIP.additional_effect_chance = 0
TAILWHIP.description = "The user wags its tail cutely, making opposing Pokémon less wary and lowering their Defense stat."

###################
### TEARFULLOOK ###
###################

TEARFULLOOK = Move()
TEARFULLOOK.name = "Tearful Look"
TEARFULLOOK.type = NORMAL
TEARFULLOOK.base_damage = 0
TEARFULLOOK.category = STATUS
TEARFULLOOK.pp = 20
TEARFULLOOK.accuracy = 0
TEARFULLOOK.priority = 0
TEARFULLOOK.target = 'NearOther'
TEARFULLOOK.additional_effect_chance = 0
TEARFULLOOK.description = "The user gets teary eyed to make the target lose its combative spirit. This lowers the targets Attack and Sp. Atk stats."

###################
### TEETERDANCE ###
###################

TEETERDANCE = Move()
TEETERDANCE.name = "Teeter Dance"
TEETERDANCE.type = NORMAL
TEETERDANCE.base_damage = 0
TEETERDANCE.category = STATUS
TEETERDANCE.pp = 20
TEETERDANCE.accuracy = 100
TEETERDANCE.priority = 0
TEETERDANCE.target = 'AllNearOthers'
TEETERDANCE.additional_effect_chance = 0
TEETERDANCE.description = "The user performs a wobbly dance that confuses the Pokémon around it."

##############
### TICKLE ###
##############

TICKLE = Move()
TICKLE.name = "Tickle"
TICKLE.type = NORMAL
TICKLE.base_damage = 0
TICKLE.category = STATUS
TICKLE.pp = 20
TICKLE.accuracy = 100
TICKLE.priority = 0
TICKLE.target = 'NearOther'
TICKLE.additional_effect_chance = 0
TICKLE.description = "The user tickles the target into laughing, reducing its Attack and Defense stats."

#################
### TRANSFORM ###
#################

TRANSFORM = Move()
TRANSFORM.name = "Transform"
TRANSFORM.type = NORMAL
TRANSFORM.base_damage = 0
TRANSFORM.category = STATUS
TRANSFORM.pp = 10
TRANSFORM.accuracy = 0
TRANSFORM.priority = 0
TRANSFORM.target = 'NearOther'
TRANSFORM.additional_effect_chance = 0
TRANSFORM.description = "The user transforms into a copy of the target right down to having the same move set."

#################
### WHIRLWIND ###
#################

WHIRLWIND = Move()
WHIRLWIND.name = "Whirlwind"
WHIRLWIND.type = NORMAL
WHIRLWIND.base_damage = 0
WHIRLWIND.category = STATUS
WHIRLWIND.pp = 20
WHIRLWIND.accuracy = 0
WHIRLWIND.priority = -6
WHIRLWIND.target = 'NearOther'
WHIRLWIND.additional_effect_chance = 0
WHIRLWIND.description = "The foe is blown away, to be replaced by another Pokémon in its party. In the wild, the battle ends."

############
### WISH ###
############

WISH = Move()
WISH.name = "Wish"
WISH.type = NORMAL
WISH.base_damage = 0
WISH.category = STATUS
WISH.pp = 10
WISH.accuracy = 0
WISH.priority = 0
WISH.target = 'User'
WISH.additional_effect_chance = 0
WISH.description = "One turn after this move is used, the targets HP is restored by half the users maximum HP."

##############
### WORKUP ###
##############

WORKUP = Move()
WORKUP.name = "Work Up"
WORKUP.type = NORMAL
WORKUP.base_damage = 0
WORKUP.category = STATUS
WORKUP.pp = 30
WORKUP.accuracy = 0
WORKUP.priority = 0
WORKUP.target = 'User'
WORKUP.additional_effect_chance = 0
WORKUP.description = "The user is roused, and its Attack and Sp. Atk stats increase."

############
### YAWN ###
############

YAWN = Move()
YAWN.name = "Yawn"
YAWN.type = NORMAL
YAWN.base_damage = 0
YAWN.category = STATUS
YAWN.pp = 10
YAWN.accuracy = 0
YAWN.priority = 0
YAWN.target = 'NearOther'
YAWN.additional_effect_chance = 0
YAWN.description = "The user lets loose a huge yawn that lulls the target into falling asleep on the next turn."

#############
### BELCH ###
#############

BELCH = Move()
BELCH.name = "Belch"
BELCH.type = POISON
BELCH.base_damage = 120
BELCH.category = SPECIAL
BELCH.pp = 10
BELCH.accuracy = 90
BELCH.priority = 0
BELCH.target = 'NearOther'
BELCH.additional_effect_chance = 0
BELCH.description = "The user lets out a damaging belch at the target. The user must eat a held Berry to use this move."

################
### GUNKSHOT ###
################

GUNKSHOT = Move()
GUNKSHOT.name = "Gunk Shot"
GUNKSHOT.type = POISON
GUNKSHOT.base_damage = 120
GUNKSHOT.category = PHYSICAL
GUNKSHOT.pp = 5
GUNKSHOT.accuracy = 80
GUNKSHOT.priority = 0
GUNKSHOT.target = 'NearOther'
GUNKSHOT.additional_effect_chance = 30
GUNKSHOT.description = "The user shoots filthy garbage at the target to attack. It may also poison the target."

##################
### SLUDGEWAVE ###
##################

SLUDGEWAVE = Move()
SLUDGEWAVE.name = "Sludge Wave"
SLUDGEWAVE.type = POISON
SLUDGEWAVE.base_damage = 95
SLUDGEWAVE.category = SPECIAL
SLUDGEWAVE.pp = 10
SLUDGEWAVE.accuracy = 100
SLUDGEWAVE.priority = 0
SLUDGEWAVE.target = 'AllNearOthers'
SLUDGEWAVE.additional_effect_chance = 10
SLUDGEWAVE.description = "It swamps the area around the user with a giant sludge wave. It may also poison those hit."

##################
### SLUDGEBOMB ###
##################

SLUDGEBOMB = Move()
SLUDGEBOMB.name = "Sludge Bomb"
SLUDGEBOMB.type = POISON
SLUDGEBOMB.base_damage = 90
SLUDGEBOMB.category = SPECIAL
SLUDGEBOMB.pp = 10
SLUDGEBOMB.accuracy = 100
SLUDGEBOMB.priority = 0
SLUDGEBOMB.target = 'NearOther'
SLUDGEBOMB.additional_effect_chance = 30
SLUDGEBOMB.description = "Unsanitary sludge is hurled at the target. It may also poison the target."

#################
### POISONJAB ###
#################

POISONJAB = Move()
POISONJAB.name = "Poison Jab"
POISONJAB.type = POISON
POISONJAB.base_damage = 80
POISONJAB.category = PHYSICAL
POISONJAB.pp = 20
POISONJAB.accuracy = 100
POISONJAB.priority = 0
POISONJAB.target = 'NearOther'
POISONJAB.additional_effect_chance = 30
POISONJAB.description = "The target is stabbed with a tentacle or arm seeped with poison. It may also poison the target."

###################
### CROSSPOISON ###
###################

CROSSPOISON = Move()
CROSSPOISON.name = "Cross Poison"
CROSSPOISON.type = POISON
CROSSPOISON.base_damage = 70
CROSSPOISON.category = PHYSICAL
CROSSPOISON.pp = 20
CROSSPOISON.accuracy = 100
CROSSPOISON.priority = 0
CROSSPOISON.target = 'NearOther'
CROSSPOISON.additional_effect_chance = 10
CROSSPOISON.description = "A slashing attack with a poisonous blade that may also poison the foe. Critical hits land more easily."

##############
### SLUDGE ###
##############

SLUDGE = Move()
SLUDGE.name = "Sludge"
SLUDGE.type = POISON
SLUDGE.base_damage = 65
SLUDGE.category = SPECIAL
SLUDGE.pp = 20
SLUDGE.accuracy = 100
SLUDGE.priority = 0
SLUDGE.target = 'NearOther'
SLUDGE.additional_effect_chance = 30
SLUDGE.description = "Unsanitary sludge is hurled at the target. It may also poison the target."

#################
### VENOSHOCK ###
#################

VENOSHOCK = Move()
VENOSHOCK.name = "Venoshock"
VENOSHOCK.type = POISON
VENOSHOCK.base_damage = 65
VENOSHOCK.category = SPECIAL
VENOSHOCK.pp = 10
VENOSHOCK.accuracy = 100
VENOSHOCK.priority = 0
VENOSHOCK.target = 'NearOther'
VENOSHOCK.additional_effect_chance = 0
VENOSHOCK.description = "The user drenches the foe in a special poisonous liquid. Its power doubles if the target is poisoned."

#################
### CLEARSMOG ###
#################

CLEARSMOG = Move()
CLEARSMOG.name = "Clear Smog"
CLEARSMOG.type = POISON
CLEARSMOG.base_damage = 50
CLEARSMOG.category = SPECIAL
CLEARSMOG.pp = 15
CLEARSMOG.accuracy = 0
CLEARSMOG.priority = 0
CLEARSMOG.target = 'NearOther'
CLEARSMOG.additional_effect_chance = 0
CLEARSMOG.description = "The user attacks by throwing a clump of special mud. All status changes are returned to normal."

##################
### POISONFANG ###
##################

POISONFANG = Move()
POISONFANG.name = "Poison Fang"
POISONFANG.type = POISON
POISONFANG.base_damage = 50
POISONFANG.category = PHYSICAL
POISONFANG.pp = 15
POISONFANG.accuracy = 100
POISONFANG.priority = 0
POISONFANG.target = 'NearOther'
POISONFANG.additional_effect_chance = 50
POISONFANG.description = "The user bites the target with toxic fangs. It may also leave the target badly poisoned."

##################
### POISONTAIL ###
##################

POISONTAIL = Move()
POISONTAIL.name = "Poison Tail"
POISONTAIL.type = POISON
POISONTAIL.base_damage = 50
POISONTAIL.category = PHYSICAL
POISONTAIL.pp = 25
POISONTAIL.accuracy = 100
POISONTAIL.priority = 0
POISONTAIL.target = 'NearOther'
POISONTAIL.additional_effect_chance = 10
POISONTAIL.description = "The user hits the target with its tail. It may also poison the target. Critical hits land more easily."

############
### ACID ###
############

ACID = Move()
ACID.name = "Acid"
ACID.type = POISON
ACID.base_damage = 40
ACID.category = SPECIAL
ACID.pp = 30
ACID.accuracy = 100
ACID.priority = 0
ACID.target = 'AllNearFoes'
ACID.additional_effect_chance = 10
ACID.description = "The foe is attacked with a spray of harsh acid. It may also lower the targets Sp. Def stat."

#################
### ACIDSPRAY ###
#################

ACIDSPRAY = Move()
ACIDSPRAY.name = "Acid Spray"
ACIDSPRAY.type = POISON
ACIDSPRAY.base_damage = 40
ACIDSPRAY.category = SPECIAL
ACIDSPRAY.pp = 20
ACIDSPRAY.accuracy = 100
ACIDSPRAY.priority = 0
ACIDSPRAY.target = 'NearOther'
ACIDSPRAY.additional_effect_chance = 100
ACIDSPRAY.description = "The user spits fluid that works to melt the target. This harshly reduces the targets Sp. Def stat."

############
### SMOG ###
############

SMOG = Move()
SMOG.name = "Smog"
SMOG.type = POISON
SMOG.base_damage = 30
SMOG.category = SPECIAL
SMOG.pp = 20
SMOG.accuracy = 70
SMOG.priority = 0
SMOG.target = 'NearOther'
SMOG.additional_effect_chance = 40
SMOG.description = "The target is attacked with a discharge of filthy gases. It may also poison the target."

###################
### POISONSTING ###
###################

POISONSTING = Move()
POISONSTING.name = "Poison Sting"
POISONSTING.type = POISON
POISONSTING.base_damage = 15
POISONSTING.category = PHYSICAL
POISONSTING.pp = 35
POISONSTING.accuracy = 100
POISONSTING.priority = 0
POISONSTING.target = 'NearOther'
POISONSTING.additional_effect_chance = 30
POISONSTING.description = "The user stabs the target with a poisonous stinger. This may also poison the target."

#################
### ACIDARMOR ###
#################

ACIDARMOR = Move()
ACIDARMOR.name = "Acid Armor"
ACIDARMOR.type = POISON
ACIDARMOR.base_damage = 0
ACIDARMOR.category = STATUS
ACIDARMOR.pp = 20
ACIDARMOR.accuracy = 0
ACIDARMOR.priority = 0
ACIDARMOR.target = 'User'
ACIDARMOR.additional_effect_chance = 0
ACIDARMOR.description = "The user alters its cellular structure to liquefy itself, sharply raising its Defense stat."

#####################
### BANEFULBUNKER ###
#####################

BANEFULBUNKER = Move()
BANEFULBUNKER.name = "Baneful Bunker"
BANEFULBUNKER.type = POISON
BANEFULBUNKER.base_damage = 0
BANEFULBUNKER.category = STATUS
BANEFULBUNKER.pp = 10
BANEFULBUNKER.accuracy = 0
BANEFULBUNKER.priority = 4
BANEFULBUNKER.target = 'User'
BANEFULBUNKER.additional_effect_chance = 0
BANEFULBUNKER.description = "Protects the user from attacks. Also poisons any attacker that makes contact with the user."

############
### COIL ###
############

COIL = Move()
COIL.name = "Coil"
COIL.type = POISON
COIL.base_damage = 0
COIL.category = STATUS
COIL.pp = 20
COIL.accuracy = 0
COIL.priority = 0
COIL.target = 'User'
COIL.additional_effect_chance = 0
COIL.description = "The user coils up and concentrates. This raises its Attack and Defense stats as well as its accuracy."

##################
### GASTROACID ###
##################

GASTROACID = Move()
GASTROACID.name = "Gastro Acid"
GASTROACID.type = POISON
GASTROACID.base_damage = 0
GASTROACID.category = STATUS
GASTROACID.pp = 10
GASTROACID.accuracy = 100
GASTROACID.priority = 0
GASTROACID.target = 'NearOther'
GASTROACID.additional_effect_chance = 0
GASTROACID.description = "The user hurls up its stomach acids on the foe. The fluid negates the effect of the targets Ability."

#################
### POISONGAS ###
#################

POISONGAS = Move()
POISONGAS.name = "Poison Gas"
POISONGAS.type = POISON
POISONGAS.base_damage = 0
POISONGAS.category = STATUS
POISONGAS.pp = 40
POISONGAS.accuracy = 90
POISONGAS.priority = 0
POISONGAS.target = 'AllNearFoes'
POISONGAS.additional_effect_chance = 0
POISONGAS.description = "A cloud of poison gas is sprayed in the face of opposing Pokémon. It may poison those hit."

####################
### POISONPOWDER ###
####################

POISONPOWDER = Move()
POISONPOWDER.name = "Poison Powder"
POISONPOWDER.type = POISON
POISONPOWDER.base_damage = 0
POISONPOWDER.category = STATUS
POISONPOWDER.pp = 35
POISONPOWDER.accuracy = 75
POISONPOWDER.priority = 0
POISONPOWDER.target = 'NearOther'
POISONPOWDER.additional_effect_chance = 0
POISONPOWDER.description = "The user scatters a cloud of poisonous dust on the target. It may poison the target."

##############
### PURIFY ###
##############

PURIFY = Move()
PURIFY.name = "Purify"
PURIFY.type = POISON
PURIFY.base_damage = 0
PURIFY.category = STATUS
PURIFY.pp = 20
PURIFY.accuracy = 0
PURIFY.priority = 0
PURIFY.target = 'NearOther'
PURIFY.additional_effect_chance = 0
PURIFY.description = "The user heals the targets status condition. If so, it also restores the users own HP. "

#############
### TOXIC ###
#############

TOXIC = Move()
TOXIC.name = "Toxic"
TOXIC.type = POISON
TOXIC.base_damage = 0
TOXIC.category = STATUS
TOXIC.pp = 10
TOXIC.accuracy = 90
TOXIC.priority = 0
TOXIC.target = 'NearOther'
TOXIC.additional_effect_chance = 0
TOXIC.description = "A move that leaves the target badly poisoned. Its poison damage worsens every turn."

###################
### TOXICSPIKES ###
###################

TOXICSPIKES = Move()
TOXICSPIKES.name = "Toxic Spikes"
TOXICSPIKES.type = POISON
TOXICSPIKES.base_damage = 0
TOXICSPIKES.category = STATUS
TOXICSPIKES.pp = 20
TOXICSPIKES.accuracy = 0
TOXICSPIKES.priority = 0
TOXICSPIKES.target = 'FoeSide'
TOXICSPIKES.additional_effect_chance = 0
TOXICSPIKES.description = "The user lays a trap of poison spikes at the foes feet. They poison foes that switch into battle."

###################
### TOXICTHREAD ###
###################

TOXICTHREAD = Move()
TOXICTHREAD.name = "Toxic Thread"
TOXICTHREAD.type = POISON
TOXICTHREAD.base_damage = 0
TOXICTHREAD.category = STATUS
TOXICTHREAD.pp = 20
TOXICTHREAD.accuracy = 100
TOXICTHREAD.priority = 0
TOXICTHREAD.target = 'NearOther'
TOXICTHREAD.additional_effect_chance = 0
TOXICTHREAD.description = "The user shoots poisonous threads to poison the target and lower the targets Speed stat."

###################
### VENOMDRENCH ###
###################

VENOMDRENCH = Move()
VENOMDRENCH.name = "Venom Drench"
VENOMDRENCH.type = POISON
VENOMDRENCH.base_damage = 0
VENOMDRENCH.category = STATUS
VENOMDRENCH.pp = 20
VENOMDRENCH.accuracy = 100
VENOMDRENCH.priority = 0
VENOMDRENCH.target = 'AllNearFoes'
VENOMDRENCH.additional_effect_chance = 0
VENOMDRENCH.description = "Foes are drenched in an odd liquid that lowers the Attack, Sp. Atk, and Speed of poisoned Pokémon."

######################
### PRISMATICLASER ###
######################

PRISMATICLASER = Move()
PRISMATICLASER.name = "Prismatic Laser"
PRISMATICLASER.type = PSYCHIC
PRISMATICLASER.base_damage = 160
PRISMATICLASER.category = SPECIAL
PRISMATICLASER.pp = 10
PRISMATICLASER.accuracy = 100
PRISMATICLASER.priority = 0
PRISMATICLASER.target = 'NearOther'
PRISMATICLASER.additional_effect_chance = 0
PRISMATICLASER.description = "The user shoots powerful lasers using the power of a prism. The user cant move on the next turn."

###################
### PSYCHOBOOST ###
###################

PSYCHOBOOST = Move()
PSYCHOBOOST.name = "Psycho Boost"
PSYCHOBOOST.type = PSYCHIC
PSYCHOBOOST.base_damage = 140
PSYCHOBOOST.category = SPECIAL
PSYCHOBOOST.pp = 5
PSYCHOBOOST.accuracy = 90
PSYCHOBOOST.priority = 0
PSYCHOBOOST.target = 'NearOther'
PSYCHOBOOST.additional_effect_chance = 0
PSYCHOBOOST.description = "The user attacks the target at full power. The attacks recoil harshly reduces the users Sp. Atk stat."

###################
### FUTURESIGHT ###
###################

FUTURESIGHT = Move()
FUTURESIGHT.name = "Future Sight"
FUTURESIGHT.type = PSYCHIC
FUTURESIGHT.base_damage = 120
FUTURESIGHT.category = SPECIAL
FUTURESIGHT.pp = 10
FUTURESIGHT.accuracy = 100
FUTURESIGHT.priority = 0
FUTURESIGHT.target = 'NearOther'
FUTURESIGHT.additional_effect_chance = 0
FUTURESIGHT.description = "Two turns after this move is used, a hunk of psychic energy attacks the target."

####################
### SYNCHRONOISE ###
####################

SYNCHRONOISE = Move()
SYNCHRONOISE.name = "Synchronoise"
SYNCHRONOISE.type = PSYCHIC
SYNCHRONOISE.base_damage = 120
SYNCHRONOISE.category = SPECIAL
SYNCHRONOISE.pp = 10
SYNCHRONOISE.accuracy = 100
SYNCHRONOISE.priority = 0
SYNCHRONOISE.target = 'AllNearOthers'
SYNCHRONOISE.additional_effect_chance = 0
SYNCHRONOISE.description = "Using an odd shock wave, the user damages any Pokémon of the same type as the user."

##################
### DREAMEATER ###
##################

DREAMEATER = Move()
DREAMEATER.name = "Dream Eater"
DREAMEATER.type = PSYCHIC
DREAMEATER.base_damage = 100
DREAMEATER.category = SPECIAL
DREAMEATER.pp = 15
DREAMEATER.accuracy = 100
DREAMEATER.priority = 0
DREAMEATER.target = 'NearOther'
DREAMEATER.additional_effect_chance = 0
DREAMEATER.description = "The user eats the dreams of a sleeping foe. It absorbs half the damage caused to heal the users HP."

####################
### PHOTONGEYSER ###
####################

PHOTONGEYSER = Move()
PHOTONGEYSER.name = "Photon Geyser"
PHOTONGEYSER.type = PSYCHIC
PHOTONGEYSER.base_damage = 100
PHOTONGEYSER.category = SPECIAL
PHOTONGEYSER.pp = 5
PHOTONGEYSER.accuracy = 100
PHOTONGEYSER.priority = 0
PHOTONGEYSER.target = 'NearOther'
PHOTONGEYSER.additional_effect_chance = 0
PHOTONGEYSER.description = "The user attacks with a pillar of light. This move the higher of the users Attack or Sp. Atk stat."

#################
### PSYSTRIKE ###
#################

PSYSTRIKE = Move()
PSYSTRIKE.name = "Psystrike"
PSYSTRIKE.type = PSYCHIC
PSYSTRIKE.base_damage = 100
PSYSTRIKE.category = SPECIAL
PSYSTRIKE.pp = 10
PSYSTRIKE.accuracy = 100
PSYSTRIKE.priority = 0
PSYSTRIKE.target = 'NearOther'
PSYSTRIKE.additional_effect_chance = 0
PSYSTRIKE.description = "The user materializes an odd psychic wave to attack the target. This attack does physical damage."

###############
### PSYCHIC ###
###############

PSYCHIC = Move()
PSYCHIC.name = "Psychic"
PSYCHIC.type = PSYCHIC
PSYCHIC.base_damage = 90
PSYCHIC.category = SPECIAL
PSYCHIC.pp = 10
PSYCHIC.accuracy = 100
PSYCHIC.priority = 0
PSYCHIC.target = 'NearOther'
PSYCHIC.additional_effect_chance = 10
PSYCHIC.description = "The target is hit by a strong telekinetic force. It may also reduce the targets Sp. Def stat."

####################
### PSYCHICFANGS ###
####################

PSYCHICFANGS = Move()
PSYCHICFANGS.name = "Psychic Fangs"
PSYCHICFANGS.type = PSYCHIC
PSYCHICFANGS.base_damage = 85
PSYCHICFANGS.category = PHYSICAL
PSYCHICFANGS.pp = 10
PSYCHICFANGS.accuracy = 100
PSYCHICFANGS.priority = 0
PSYCHICFANGS.target = 'NearOther'
PSYCHICFANGS.additional_effect_chance = 0
PSYCHICFANGS.description = "The user bites the target using psychic capabilities. This can also destroy Light Screen and Reflect."

####################
### EXTRASENSORY ###
####################

EXTRASENSORY = Move()
EXTRASENSORY.name = "Extrasensory"
EXTRASENSORY.type = PSYCHIC
EXTRASENSORY.base_damage = 80
EXTRASENSORY.category = SPECIAL
EXTRASENSORY.pp = 20
EXTRASENSORY.accuracy = 100
EXTRASENSORY.priority = 0
EXTRASENSORY.target = 'NearOther'
EXTRASENSORY.additional_effect_chance = 10
EXTRASENSORY.description = "The user attacks with an odd, unseeable power. It may also make the target flinch."

######################
### HYPERSPACEHOLE ###
######################

HYPERSPACEHOLE = Move()
HYPERSPACEHOLE.name = "Hyperspace Hole"
HYPERSPACEHOLE.type = PSYCHIC
HYPERSPACEHOLE.base_damage = 80
HYPERSPACEHOLE.category = SPECIAL
HYPERSPACEHOLE.pp = 5
HYPERSPACEHOLE.accuracy = 0
HYPERSPACEHOLE.priority = 0
HYPERSPACEHOLE.target = 'NearOther'
HYPERSPACEHOLE.additional_effect_chance = 0
HYPERSPACEHOLE.description = "Using a hyperspace hole, the user appears right next to the target and strikes. Skips protections."

################
### PSYSHOCK ###
################

PSYSHOCK = Move()
PSYSHOCK.name = "Psyshock"
PSYSHOCK.type = PSYCHIC
PSYSHOCK.base_damage = 80
PSYSHOCK.category = SPECIAL
PSYSHOCK.pp = 10
PSYSHOCK.accuracy = 100
PSYSHOCK.priority = 0
PSYSHOCK.target = 'NearOther'
PSYSHOCK.additional_effect_chance = 0
PSYSHOCK.description = "The user materializes an odd psychic wave to attack the target. This attack does physical damage."

###################
### ZENHEADBUTT ###
###################

ZENHEADBUTT = Move()
ZENHEADBUTT.name = "Zen Headbutt"
ZENHEADBUTT.type = PSYCHIC
ZENHEADBUTT.base_damage = 80
ZENHEADBUTT.category = PHYSICAL
ZENHEADBUTT.pp = 15
ZENHEADBUTT.accuracy = 90
ZENHEADBUTT.priority = 0
ZENHEADBUTT.target = 'NearOther'
ZENHEADBUTT.additional_effect_chance = 20
ZENHEADBUTT.description = "The user focuses its willpower to its head and attacks the foe. It may also make the target flinch."

###################
### LUSTERPURGE ###
###################

LUSTERPURGE = Move()
LUSTERPURGE.name = "Luster Purge"
LUSTERPURGE.type = PSYCHIC
LUSTERPURGE.base_damage = 70
LUSTERPURGE.category = SPECIAL
LUSTERPURGE.pp = 5
LUSTERPURGE.accuracy = 100
LUSTERPURGE.priority = 0
LUSTERPURGE.target = 'NearOther'
LUSTERPURGE.additional_effect_chance = 50
LUSTERPURGE.description = "The user lets loose a damaging burst of light. It may also reduce the targets Sp. Def stat."

################
### MISTBALL ###
################

MISTBALL = Move()
MISTBALL.name = "Mist Ball"
MISTBALL.type = PSYCHIC
MISTBALL.base_damage = 70
MISTBALL.category = SPECIAL
MISTBALL.pp = 5
MISTBALL.accuracy = 100
MISTBALL.priority = 0
MISTBALL.target = 'NearOther'
MISTBALL.additional_effect_chance = 50
MISTBALL.description = "A mistlike flurry of down envelops and damages the target. It may also lower the targets Sp. Atk."

#################
### PSYCHOCUT ###
#################

PSYCHOCUT = Move()
PSYCHOCUT.name = "Psycho Cut"
PSYCHOCUT.type = PSYCHIC
PSYCHOCUT.base_damage = 70
PSYCHOCUT.category = PHYSICAL
PSYCHOCUT.pp = 20
PSYCHOCUT.accuracy = 100
PSYCHOCUT.priority = 0
PSYCHOCUT.target = 'NearOther'
PSYCHOCUT.additional_effect_chance = 0
PSYCHOCUT.description = "The user tears at the target with blades formed by psychic power. Critical hits land more easily."

###############
### PSYBEAM ###
###############

PSYBEAM = Move()
PSYBEAM.name = "Psybeam"
PSYBEAM.type = PSYCHIC
PSYBEAM.base_damage = 65
PSYBEAM.category = SPECIAL
PSYBEAM.pp = 20
PSYBEAM.accuracy = 100
PSYBEAM.priority = 0
PSYBEAM.target = 'NearOther'
PSYBEAM.additional_effect_chance = 10
PSYBEAM.description = "The target is attacked with a peculiar ray. It may also cause confusion."

##################
### HEARTSTAMP ###
##################

HEARTSTAMP = Move()
HEARTSTAMP.name = "Heart Stamp"
HEARTSTAMP.type = PSYCHIC
HEARTSTAMP.base_damage = 60
HEARTSTAMP.category = PHYSICAL
HEARTSTAMP.pp = 25
HEARTSTAMP.accuracy = 100
HEARTSTAMP.priority = 0
HEARTSTAMP.target = 'NearOther'
HEARTSTAMP.additional_effect_chance = 30
HEARTSTAMP.description = "The user unleashes a vicious blow after its cute act makes the foe less wary. It may also cause flinching."

#################
### CONFUSION ###
#################

CONFUSION = Move()
CONFUSION.name = "Confusion"
CONFUSION.type = PSYCHIC
CONFUSION.base_damage = 50
CONFUSION.category = SPECIAL
CONFUSION.pp = 25
CONFUSION.accuracy = 100
CONFUSION.priority = 0
CONFUSION.target = 'NearOther'
CONFUSION.additional_effect_chance = 10
CONFUSION.description = "The target is hit by a weak telekinetic force. It may also leave the target confused."

###################
### STOREDPOWER ###
###################

STOREDPOWER = Move()
STOREDPOWER.name = "Stored Power"
STOREDPOWER.type = PSYCHIC
STOREDPOWER.base_damage = 20
STOREDPOWER.category = SPECIAL
STOREDPOWER.pp = 10
STOREDPOWER.accuracy = 100
STOREDPOWER.priority = 0
STOREDPOWER.target = 'NearOther'
STOREDPOWER.additional_effect_chance = 0
STOREDPOWER.description = "The user attacks with stored power. The more the users stats are raised, the greater the damage."

##################
### MIRRORCOAT ###
##################

MIRRORCOAT = Move()
MIRRORCOAT.name = "Mirror Coat"
MIRRORCOAT.type = PSYCHIC
MIRRORCOAT.base_damage = 1
MIRRORCOAT.category = SPECIAL
MIRRORCOAT.pp = 20
MIRRORCOAT.accuracy = 100
MIRRORCOAT.priority = -5
MIRRORCOAT.target = 'None'
MIRRORCOAT.additional_effect_chance = 0
MIRRORCOAT.description = "A retaliation move that counters any special attack, inflicting double the damage taken."

###############
### PSYWAVE ###
###############

PSYWAVE = Move()
PSYWAVE.name = "Psywave"
PSYWAVE.type = PSYCHIC
PSYWAVE.base_damage = 1
PSYWAVE.category = SPECIAL
PSYWAVE.pp = 15
PSYWAVE.accuracy = 100
PSYWAVE.priority = 0
PSYWAVE.target = 'NearOther'
PSYWAVE.additional_effect_chance = 0
PSYWAVE.description = "The target is attacked with an odd psychic wave. The attack varies in intensity."

###############
### AGILITY ###
###############

AGILITY = Move()
AGILITY.name = "Agility"
AGILITY.type = PSYCHIC
AGILITY.base_damage = 0
AGILITY.category = STATUS
AGILITY.pp = 30
AGILITY.accuracy = 0
AGILITY.priority = 0
AGILITY.target = 'User'
AGILITY.additional_effect_chance = 0
AGILITY.description = "The user relaxes and lightens its body to move faster. It sharply boosts the Speed stat."

##################
### ALLYSWITCH ###
##################

ALLYSWITCH = Move()
ALLYSWITCH.name = "Ally Switch"
ALLYSWITCH.type = PSYCHIC
ALLYSWITCH.base_damage = 0
ALLYSWITCH.category = STATUS
ALLYSWITCH.pp = 15
ALLYSWITCH.accuracy = 0
ALLYSWITCH.priority = 2
ALLYSWITCH.target = 'User'
ALLYSWITCH.additional_effect_chance = 0
ALLYSWITCH.description = "The user teleports using a strange power and switches its place with one of its allies."

###############
### AMNESIA ###
###############

AMNESIA = Move()
AMNESIA.name = "Amnesia"
AMNESIA.type = PSYCHIC
AMNESIA.base_damage = 0
AMNESIA.category = STATUS
AMNESIA.pp = 20
AMNESIA.accuracy = 0
AMNESIA.priority = 0
AMNESIA.target = 'User'
AMNESIA.additional_effect_chance = 0
AMNESIA.description = "The user temporarily empties its mind to forget its concerns. It sharply raises the users Sp. Def stat."

###############
### BARRIER ###
###############

BARRIER = Move()
BARRIER.name = "Barrier"
BARRIER.type = PSYCHIC
BARRIER.base_damage = 0
BARRIER.category = STATUS
BARRIER.pp = 20
BARRIER.accuracy = 0
BARRIER.priority = 0
BARRIER.target = 'User'
BARRIER.additional_effect_chance = 0
BARRIER.description = "The user throws up a sturdy wall that sharply raises its Defense stat."

################
### CALMMIND ###
################

CALMMIND = Move()
CALMMIND.name = "Calm Mind"
CALMMIND.type = PSYCHIC
CALMMIND.base_damage = 0
CALMMIND.category = STATUS
CALMMIND.pp = 20
CALMMIND.accuracy = 0
CALMMIND.priority = 0
CALMMIND.target = 'User'
CALMMIND.additional_effect_chance = 0
CALMMIND.description = "The user quietly focuses its mind and calms its spirit to raise its Sp. Atk and Sp. Def stats."

###################
### COSMICPOWER ###
###################

COSMICPOWER = Move()
COSMICPOWER.name = "Cosmic Power"
COSMICPOWER.type = PSYCHIC
COSMICPOWER.base_damage = 0
COSMICPOWER.category = STATUS
COSMICPOWER.pp = 20
COSMICPOWER.accuracy = 0
COSMICPOWER.priority = 0
COSMICPOWER.target = 'User'
COSMICPOWER.additional_effect_chance = 0
COSMICPOWER.description = "The user absorbs a mystical power from space to raise its Defense and Sp. Def stats."

###############
### GRAVITY ###
###############

GRAVITY = Move()
GRAVITY.name = "Gravity"
GRAVITY.type = PSYCHIC
GRAVITY.base_damage = 0
GRAVITY.category = STATUS
GRAVITY.pp = 5
GRAVITY.accuracy = 0
GRAVITY.priority = 0
GRAVITY.target = 'BothSides'
GRAVITY.additional_effect_chance = 0
GRAVITY.description = "Gravity is intensified for five turns, making moves involving flying unusable and negating Levitation."

##################
### GUARDSPLIT ###
##################

GUARDSPLIT = Move()
GUARDSPLIT.name = "Guard Split"
GUARDSPLIT.type = PSYCHIC
GUARDSPLIT.base_damage = 0
GUARDSPLIT.category = STATUS
GUARDSPLIT.pp = 10
GUARDSPLIT.accuracy = 0
GUARDSPLIT.priority = 0
GUARDSPLIT.target = 'NearOther'
GUARDSPLIT.additional_effect_chance = 0
GUARDSPLIT.description = "The user employs its psychic power to average its Defense and Sp. Def stats with those of its target."

#################
### GUARDSWAP ###
#################

GUARDSWAP = Move()
GUARDSWAP.name = "Guard Swap"
GUARDSWAP.type = PSYCHIC
GUARDSWAP.base_damage = 0
GUARDSWAP.category = STATUS
GUARDSWAP.pp = 10
GUARDSWAP.accuracy = 0
GUARDSWAP.priority = 0
GUARDSWAP.target = 'NearOther'
GUARDSWAP.additional_effect_chance = 0
GUARDSWAP.description = "The user employs its psychic power to switch changes to its Defense and Sp. Def with the target."

#################
### HEALBLOCK ###
#################

HEALBLOCK = Move()
HEALBLOCK.name = "Heal Block"
HEALBLOCK.type = PSYCHIC
HEALBLOCK.base_damage = 0
HEALBLOCK.category = STATUS
HEALBLOCK.pp = 15
HEALBLOCK.accuracy = 100
HEALBLOCK.priority = 0
HEALBLOCK.target = 'AllNearFoes'
HEALBLOCK.additional_effect_chance = 0
HEALBLOCK.description = "For five turns, the foe is prevented from using any moves, Abilities, or held items that recover HP."

#################
### HEALPULSE ###
#################

HEALPULSE = Move()
HEALPULSE.name = "Heal Pulse"
HEALPULSE.type = PSYCHIC
HEALPULSE.base_damage = 0
HEALPULSE.category = STATUS
HEALPULSE.pp = 10
HEALPULSE.accuracy = 0
HEALPULSE.priority = 0
HEALPULSE.target = 'Other'
HEALPULSE.additional_effect_chance = 0
HEALPULSE.description = "The user emits a healing pulse which restores the targets HP by up to half of its max HP."

###################
### HEALINGWISH ###
###################

HEALINGWISH = Move()
HEALINGWISH.name = "Healing Wish"
HEALINGWISH.type = PSYCHIC
HEALINGWISH.base_damage = 0
HEALINGWISH.category = STATUS
HEALINGWISH.pp = 10
HEALINGWISH.accuracy = 0
HEALINGWISH.priority = 0
HEALINGWISH.target = 'User'
HEALINGWISH.additional_effect_chance = 0
HEALINGWISH.description = "The user faints. In return, the Pokémon taking its place will have its HP restored and status cured."

#################
### HEARTSWAP ###
#################

HEARTSWAP = Move()
HEARTSWAP.name = "Heart Swap"
HEARTSWAP.type = PSYCHIC
HEARTSWAP.base_damage = 0
HEARTSWAP.category = STATUS
HEARTSWAP.pp = 10
HEARTSWAP.accuracy = 0
HEARTSWAP.priority = 0
HEARTSWAP.target = 'NearOther'
HEARTSWAP.additional_effect_chance = 0
HEARTSWAP.description = "The user employs its psychic power to switch stat changes with the target."

################
### HYPNOSIS ###
################

HYPNOSIS = Move()
HYPNOSIS.name = "Hypnosis"
HYPNOSIS.type = PSYCHIC
HYPNOSIS.base_damage = 0
HYPNOSIS.category = STATUS
HYPNOSIS.pp = 20
HYPNOSIS.accuracy = 60
HYPNOSIS.priority = 0
HYPNOSIS.target = 'NearOther'
HYPNOSIS.additional_effect_chance = 0
HYPNOSIS.description = "The user employs hypnotic suggestion to make the target fall into a deep sleep."

################
### IMPRISON ###
################

IMPRISON = Move()
IMPRISON.name = "Imprison"
IMPRISON.type = PSYCHIC
IMPRISON.base_damage = 0
IMPRISON.category = STATUS
IMPRISON.pp = 10
IMPRISON.accuracy = 0
IMPRISON.priority = 0
IMPRISON.target = 'User'
IMPRISON.additional_effect_chance = 0
IMPRISON.description = "If the foe knows any move also known by the user, the foe is prevented from using it."

################
### INSTRUCT ###
################

INSTRUCT = Move()
INSTRUCT.name = "Instruct"
INSTRUCT.type = PSYCHIC
INSTRUCT.base_damage = 0
INSTRUCT.category = STATUS
INSTRUCT.pp = 15
INSTRUCT.accuracy = 0
INSTRUCT.priority = 0
INSTRUCT.target = 'NearOther'
INSTRUCT.additional_effect_chance = 0
INSTRUCT.description = "The user instructs the target to use the targets last move again."

###############
### KINESIS ###
###############

KINESIS = Move()
KINESIS.name = "Kinesis"
KINESIS.type = PSYCHIC
KINESIS.base_damage = 0
KINESIS.category = STATUS
KINESIS.pp = 15
KINESIS.accuracy = 80
KINESIS.priority = 0
KINESIS.target = 'NearOther'
KINESIS.additional_effect_chance = 0
KINESIS.description = "The user distracts the target by bending a spoon. It lowers the targets accuracy."

###################
### LIGHTSCREEN ###
###################

LIGHTSCREEN = Move()
LIGHTSCREEN.name = "Light Screen"
LIGHTSCREEN.type = PSYCHIC
LIGHTSCREEN.base_damage = 0
LIGHTSCREEN.category = STATUS
LIGHTSCREEN.pp = 30
LIGHTSCREEN.accuracy = 0
LIGHTSCREEN.priority = 0
LIGHTSCREEN.target = 'UserSide'
LIGHTSCREEN.additional_effect_chance = 0
LIGHTSCREEN.description = "A wondrous wall of light is put up to suppress damage from special attacks for five turns."

##################
### LUNARDANCE ###
##################

LUNARDANCE = Move()
LUNARDANCE.name = "Lunar Dance"
LUNARDANCE.type = PSYCHIC
LUNARDANCE.base_damage = 0
LUNARDANCE.category = STATUS
LUNARDANCE.pp = 10
LUNARDANCE.accuracy = 0
LUNARDANCE.priority = 0
LUNARDANCE.target = 'User'
LUNARDANCE.additional_effect_chance = 0
LUNARDANCE.description = "The user faints. In return, the Pokémon taking its place will have its status and HP fully restored."

#################
### MAGICCOAT ###
#################

MAGICCOAT = Move()
MAGICCOAT.name = "Magic Coat"
MAGICCOAT.type = PSYCHIC
MAGICCOAT.base_damage = 0
MAGICCOAT.category = STATUS
MAGICCOAT.pp = 15
MAGICCOAT.accuracy = 0
MAGICCOAT.priority = 4
MAGICCOAT.target = 'User'
MAGICCOAT.additional_effect_chance = 0
MAGICCOAT.description = "A barrier reflects back to the target moves like Leech Seed and moves that damage status."

#################
### MAGICROOM ###
#################

MAGICROOM = Move()
MAGICROOM.name = "Magic Room"
MAGICROOM.type = PSYCHIC
MAGICROOM.base_damage = 0
MAGICROOM.category = STATUS
MAGICROOM.pp = 10
MAGICROOM.accuracy = 0
MAGICROOM.priority = 0
MAGICROOM.target = 'BothSides'
MAGICROOM.additional_effect_chance = 0
MAGICROOM.description = "The user creates a bizarre area in which Pokémons held items lose their effects for five turns."

################
### MEDITATE ###
################

MEDITATE = Move()
MEDITATE.name = "Meditate"
MEDITATE.type = PSYCHIC
MEDITATE.base_damage = 0
MEDITATE.category = STATUS
MEDITATE.pp = 40
MEDITATE.accuracy = 0
MEDITATE.priority = 0
MEDITATE.target = 'User'
MEDITATE.additional_effect_chance = 0
MEDITATE.description = "The user meditates to awaken the power deep within its body and raise its Attack stat."

##################
### MIRACLEEYE ###
##################

MIRACLEEYE = Move()
MIRACLEEYE.name = "Miracle Eye"
MIRACLEEYE.type = PSYCHIC
MIRACLEEYE.base_damage = 0
MIRACLEEYE.category = STATUS
MIRACLEEYE.pp = 40
MIRACLEEYE.accuracy = 0
MIRACLEEYE.priority = 0
MIRACLEEYE.target = 'NearOther'
MIRACLEEYE.additional_effect_chance = 0
MIRACLEEYE.description = "Enables the user to hit a Dark type with any type of move. It also enables the user to hit an evasive foe."

##################
### POWERSPLIT ###
##################

POWERSPLIT = Move()
POWERSPLIT.name = "Power Split"
POWERSPLIT.type = PSYCHIC
POWERSPLIT.base_damage = 0
POWERSPLIT.category = STATUS
POWERSPLIT.pp = 10
POWERSPLIT.accuracy = 0
POWERSPLIT.priority = 0
POWERSPLIT.target = 'NearOther'
POWERSPLIT.additional_effect_chance = 0
POWERSPLIT.description = "The user employs its psychic power to average its Attack and Sp. Atk stats with those of the target."

#################
### POWERSWAP ###
#################

POWERSWAP = Move()
POWERSWAP.name = "Power Swap"
POWERSWAP.type = PSYCHIC
POWERSWAP.base_damage = 0
POWERSWAP.category = STATUS
POWERSWAP.pp = 10
POWERSWAP.accuracy = 0
POWERSWAP.priority = 0
POWERSWAP.target = 'NearOther'
POWERSWAP.additional_effect_chance = 0
POWERSWAP.description = "The user employs its psychic power to switch changes to its Attack and Sp. Atk with the target."

##################
### POWERTRICK ###
##################

POWERTRICK = Move()
POWERTRICK.name = "Power Trick"
POWERTRICK.type = PSYCHIC
POWERTRICK.base_damage = 0
POWERTRICK.category = STATUS
POWERTRICK.pp = 10
POWERTRICK.accuracy = 0
POWERTRICK.priority = 0
POWERTRICK.target = 'User'
POWERTRICK.additional_effect_chance = 0
POWERTRICK.description = "The user employs its psychic power to switch its Attack with its Defense stat."

######################
### PSYCHICTERRAIN ###
######################

PSYCHICTERRAIN = Move()
PSYCHICTERRAIN.name = "Psychic Terrain"
PSYCHICTERRAIN.type = PSYCHIC
PSYCHICTERRAIN.base_damage = 0
PSYCHICTERRAIN.category = STATUS
PSYCHICTERRAIN.pp = 10
PSYCHICTERRAIN.accuracy = 0
PSYCHICTERRAIN.priority = 0
PSYCHICTERRAIN.target = 'BothSides'
PSYCHICTERRAIN.additional_effect_chance = 0
PSYCHICTERRAIN.description = "Protects grounded Pokémon from priority moves and powers up Psychic-type moves for five turns."

###################
### PSYCHOSHIFT ###
###################

PSYCHOSHIFT = Move()
PSYCHOSHIFT.name = "Psycho Shift"
PSYCHOSHIFT.type = PSYCHIC
PSYCHOSHIFT.base_damage = 0
PSYCHOSHIFT.category = STATUS
PSYCHOSHIFT.pp = 10
PSYCHOSHIFT.accuracy = 100
PSYCHOSHIFT.priority = 0
PSYCHOSHIFT.target = 'NearOther'
PSYCHOSHIFT.additional_effect_chance = 0
PSYCHOSHIFT.description = "Using its psychic power of suggestion, the user transfers its status problems to the target."

###############
### REFLECT ###
###############

REFLECT = Move()
REFLECT.name = "Reflect"
REFLECT.type = PSYCHIC
REFLECT.base_damage = 0
REFLECT.category = STATUS
REFLECT.pp = 20
REFLECT.accuracy = 0
REFLECT.priority = 0
REFLECT.target = 'UserSide'
REFLECT.additional_effect_chance = 0
REFLECT.description = "A wondrous wall of light is put up to suppress damage from physical attacks for five turns."

############
### REST ###
############

REST = Move()
REST.name = "Rest"
REST.type = PSYCHIC
REST.base_damage = 0
REST.category = STATUS
REST.pp = 10
REST.accuracy = 0
REST.priority = 0
REST.target = 'User'
REST.additional_effect_chance = 0
REST.description = "The user goes to sleep for two turns. It fully restores the users HP and heals any status problem."

################
### ROLEPLAY ###
################

ROLEPLAY = Move()
ROLEPLAY.name = "Role Play"
ROLEPLAY.type = PSYCHIC
ROLEPLAY.base_damage = 0
ROLEPLAY.category = STATUS
ROLEPLAY.pp = 10
ROLEPLAY.accuracy = 0
ROLEPLAY.priority = 0
ROLEPLAY.target = 'NearOther'
ROLEPLAY.additional_effect_chance = 0
ROLEPLAY.description = "The user mimics the target completely, copying the targets natural Ability."

#################
### SKILLSWAP ###
#################

SKILLSWAP = Move()
SKILLSWAP.name = "Skill Swap"
SKILLSWAP.type = PSYCHIC
SKILLSWAP.base_damage = 0
SKILLSWAP.category = STATUS
SKILLSWAP.pp = 10
SKILLSWAP.accuracy = 0
SKILLSWAP.priority = 0
SKILLSWAP.target = 'NearOther'
SKILLSWAP.additional_effect_chance = 0
SKILLSWAP.description = "The user employs its psychic power to exchange Abilities with the target."

#################
### SPEEDSWAP ###
#################

SPEEDSWAP = Move()
SPEEDSWAP.name = "Speed Swap"
SPEEDSWAP.type = PSYCHIC
SPEEDSWAP.base_damage = 0
SPEEDSWAP.category = STATUS
SPEEDSWAP.pp = 10
SPEEDSWAP.accuracy = 0
SPEEDSWAP.priority = 0
SPEEDSWAP.target = 'NearOther'
SPEEDSWAP.additional_effect_chance = 0
SPEEDSWAP.description = "The user exchanges Speed stats with the target."

###################
### TELEKINESIS ###
###################

TELEKINESIS = Move()
TELEKINESIS.name = "Telekinesis"
TELEKINESIS.type = PSYCHIC
TELEKINESIS.base_damage = 0
TELEKINESIS.category = STATUS
TELEKINESIS.pp = 15
TELEKINESIS.accuracy = 0
TELEKINESIS.priority = 0
TELEKINESIS.target = 'NearOther'
TELEKINESIS.additional_effect_chance = 0
TELEKINESIS.description = "The user makes the target float with its psychic power. The target is easier to hit for three turns."

################
### TELEPORT ###
################

TELEPORT = Move()
TELEPORT.name = "Teleport"
TELEPORT.type = PSYCHIC
TELEPORT.base_damage = 0
TELEPORT.category = STATUS
TELEPORT.pp = 20
TELEPORT.accuracy = 0
TELEPORT.priority = 0
TELEPORT.target = 'User'
TELEPORT.additional_effect_chance = 0
TELEPORT.description = "Use it to flee from any wild Pokémon. It can also warp to the last Pokémon Center visited."

#############
### TRICK ###
#############

TRICK = Move()
TRICK.name = "Trick"
TRICK.type = PSYCHIC
TRICK.base_damage = 0
TRICK.category = STATUS
TRICK.pp = 10
TRICK.accuracy = 100
TRICK.priority = 0
TRICK.target = 'NearOther'
TRICK.additional_effect_chance = 0
TRICK.description = "The user catches the target off guard and swaps its held item with its own."

#################
### TRICKROOM ###
#################

TRICKROOM = Move()
TRICKROOM.name = "Trick Room"
TRICKROOM.type = PSYCHIC
TRICKROOM.base_damage = 0
TRICKROOM.category = STATUS
TRICKROOM.pp = 5
TRICKROOM.accuracy = 0
TRICKROOM.priority = -7
TRICKROOM.target = 'BothSides'
TRICKROOM.additional_effect_chance = 0
TRICKROOM.description = "The user creates a bizarre area in which slower Pokémon get to move first for five turns."

##################
### WONDERROOM ###
##################

WONDERROOM = Move()
WONDERROOM.name = "Wonder Room"
WONDERROOM.type = PSYCHIC
WONDERROOM.base_damage = 0
WONDERROOM.category = STATUS
WONDERROOM.pp = 10
WONDERROOM.accuracy = 0
WONDERROOM.priority = -7
WONDERROOM.target = 'BothSides'
WONDERROOM.additional_effect_chance = 0
WONDERROOM.description = "The user creates a bizarre area in which Pokémons Defense and Sp. Def stats are swapped for 5 turns."

#################
### HEADSMASH ###
#################

HEADSMASH = Move()
HEADSMASH.name = "Head Smash"
HEADSMASH.type = ROCK
HEADSMASH.base_damage = 150
HEADSMASH.category = PHYSICAL
HEADSMASH.pp = 5
HEADSMASH.accuracy = 80
HEADSMASH.priority = 0
HEADSMASH.target = 'NearOther'
HEADSMASH.additional_effect_chance = 0
HEADSMASH.description = "The user attacks the foe with a hazardous, full-power headbutt. The user also takes terrible damage."

###################
### ROCKWRECKER ###
###################

ROCKWRECKER = Move()
ROCKWRECKER.name = "Rock Wrecker"
ROCKWRECKER.type = ROCK
ROCKWRECKER.base_damage = 150
ROCKWRECKER.category = PHYSICAL
ROCKWRECKER.pp = 5
ROCKWRECKER.accuracy = 90
ROCKWRECKER.priority = 0
ROCKWRECKER.target = 'NearOther'
ROCKWRECKER.additional_effect_chance = 0
ROCKWRECKER.description = "The user launches a huge boulder at the target to attack. It must rest on the next turn, however."

####################
### DIAMONDSTORM ###
####################

DIAMONDSTORM = Move()
DIAMONDSTORM.name = "Diamond Storm"
DIAMONDSTORM.type = ROCK
DIAMONDSTORM.base_damage = 100
DIAMONDSTORM.category = PHYSICAL
DIAMONDSTORM.pp = 5
DIAMONDSTORM.accuracy = 95
DIAMONDSTORM.priority = 0
DIAMONDSTORM.target = 'AllNearFoes'
DIAMONDSTORM.additional_effect_chance = 50
DIAMONDSTORM.description = "The user whips up a storm of diamonds to damage foes. This may also sharply raise the users Defense stat."

#################
### STONEEDGE ###
#################

STONEEDGE = Move()
STONEEDGE.name = "Stone Edge"
STONEEDGE.type = ROCK
STONEEDGE.base_damage = 100
STONEEDGE.category = PHYSICAL
STONEEDGE.pp = 5
STONEEDGE.accuracy = 80
STONEEDGE.priority = 0
STONEEDGE.target = 'NearOther'
STONEEDGE.additional_effect_chance = 0
STONEEDGE.description = "The user stabs the foe with sharpened stones from below. It has a high critical-hit ratio."

################
### POWERGEM ###
################

POWERGEM = Move()
POWERGEM.name = "Power Gem"
POWERGEM.type = ROCK
POWERGEM.base_damage = 80
POWERGEM.category = SPECIAL
POWERGEM.pp = 20
POWERGEM.accuracy = 100
POWERGEM.priority = 0
POWERGEM.target = 'NearOther'
POWERGEM.additional_effect_chance = 0
POWERGEM.description = "The user attacks with a ray of light that sparkles as if it were made of gemstones."

#################
### ROCKSLIDE ###
#################

ROCKSLIDE = Move()
ROCKSLIDE.name = "Rock Slide"
ROCKSLIDE.type = ROCK
ROCKSLIDE.base_damage = 75
ROCKSLIDE.category = PHYSICAL
ROCKSLIDE.pp = 10
ROCKSLIDE.accuracy = 90
ROCKSLIDE.priority = 0
ROCKSLIDE.target = 'AllNearFoes'
ROCKSLIDE.additional_effect_chance = 30
ROCKSLIDE.description = "Large boulders are hurled at the foes to inflict damage. It may also make the targets flinch."

####################
### ANCIENTPOWER ###
####################

ANCIENTPOWER = Move()
ANCIENTPOWER.name = "Ancient Power"
ANCIENTPOWER.type = ROCK
ANCIENTPOWER.base_damage = 60
ANCIENTPOWER.category = SPECIAL
ANCIENTPOWER.pp = 5
ANCIENTPOWER.accuracy = 100
ANCIENTPOWER.priority = 0
ANCIENTPOWER.target = 'NearOther'
ANCIENTPOWER.additional_effect_chance = 10
ANCIENTPOWER.description = "The user attacks with a prehistoric power. It may also raise all the users stats at once."

################
### ROCKTOMB ###
################

ROCKTOMB = Move()
ROCKTOMB.name = "Rock Tomb"
ROCKTOMB.type = ROCK
ROCKTOMB.base_damage = 60
ROCKTOMB.category = PHYSICAL
ROCKTOMB.pp = 15
ROCKTOMB.accuracy = 95
ROCKTOMB.priority = 0
ROCKTOMB.target = 'NearOther'
ROCKTOMB.additional_effect_chance = 100
ROCKTOMB.description = "Boulders are hurled at the target. It also lowers the targets Speed by preventing its movement."

#################
### ROCKTHROW ###
#################

ROCKTHROW = Move()
ROCKTHROW.name = "Rock Throw"
ROCKTHROW.type = ROCK
ROCKTHROW.base_damage = 50
ROCKTHROW.category = PHYSICAL
ROCKTHROW.pp = 15
ROCKTHROW.accuracy = 90
ROCKTHROW.priority = 0
ROCKTHROW.target = 'NearOther'
ROCKTHROW.additional_effect_chance = 0
ROCKTHROW.description = "The user picks up and throws a small rock at the target to attack."

#################
### SMACKDOWN ###
#################

SMACKDOWN = Move()
SMACKDOWN.name = "Smack Down"
SMACKDOWN.type = ROCK
SMACKDOWN.base_damage = 50
SMACKDOWN.category = PHYSICAL
SMACKDOWN.pp = 15
SMACKDOWN.accuracy = 100
SMACKDOWN.priority = 0
SMACKDOWN.target = 'NearOther'
SMACKDOWN.additional_effect_chance = 0
SMACKDOWN.description = "The user throws a stone or projectile to attack. A flying Pokémon will fall to the ground when hit."

##################
### ACCELEROCK ###
##################

ACCELEROCK = Move()
ACCELEROCK.name = "Accelerock"
ACCELEROCK.type = ROCK
ACCELEROCK.base_damage = 40
ACCELEROCK.category = PHYSICAL
ACCELEROCK.pp = 20
ACCELEROCK.accuracy = 100
ACCELEROCK.priority = 1
ACCELEROCK.target = 'NearOther'
ACCELEROCK.additional_effect_chance = 0
ACCELEROCK.description = "The user smashes into the target at high speed. This move always goes first."

###############
### ROLLOUT ###
###############

ROLLOUT = Move()
ROLLOUT.name = "Rollout"
ROLLOUT.type = ROCK
ROLLOUT.base_damage = 30
ROLLOUT.category = PHYSICAL
ROLLOUT.pp = 20
ROLLOUT.accuracy = 90
ROLLOUT.priority = 0
ROLLOUT.target = 'NearOther'
ROLLOUT.additional_effect_chance = 0
ROLLOUT.description = "The user continually rolls into the target over five turns. It becomes stronger each time it hits."

#################
### ROCKBLAST ###
#################

ROCKBLAST = Move()
ROCKBLAST.name = "Rock Blast"
ROCKBLAST.type = ROCK
ROCKBLAST.base_damage = 25
ROCKBLAST.category = PHYSICAL
ROCKBLAST.pp = 10
ROCKBLAST.accuracy = 90
ROCKBLAST.priority = 0
ROCKBLAST.target = 'NearOther'
ROCKBLAST.additional_effect_chance = 0
ROCKBLAST.description = "The user hurls hard rocks at the target. Two to five rocks are launched in quick succession."

##################
### ROCKPOLISH ###
##################

ROCKPOLISH = Move()
ROCKPOLISH.name = "Rock Polish"
ROCKPOLISH.type = ROCK
ROCKPOLISH.base_damage = 0
ROCKPOLISH.category = STATUS
ROCKPOLISH.pp = 20
ROCKPOLISH.accuracy = 0
ROCKPOLISH.priority = 0
ROCKPOLISH.target = 'User'
ROCKPOLISH.additional_effect_chance = 0
ROCKPOLISH.description = "The user polishes its body to reduce drag. It can sharply raise the Speed stat."

#################
### SANDSTORM ###
#################

SANDSTORM = Move()
SANDSTORM.name = "Sandstorm"
SANDSTORM.type = ROCK
SANDSTORM.base_damage = 0
SANDSTORM.category = STATUS
SANDSTORM.pp = 10
SANDSTORM.accuracy = 0
SANDSTORM.priority = 0
SANDSTORM.target = 'BothSides'
SANDSTORM.additional_effect_chance = 0
SANDSTORM.description = "Summons a five-turn sandstorm to hurt all combatants except the Rock, Ground, and Steel types."

###################
### STEALTHROCK ###
###################

STEALTHROCK = Move()
STEALTHROCK.name = "Stealth Rock"
STEALTHROCK.type = ROCK
STEALTHROCK.base_damage = 0
STEALTHROCK.category = STATUS
STEALTHROCK.pp = 20
STEALTHROCK.accuracy = 0
STEALTHROCK.priority = 0
STEALTHROCK.target = 'FoeSide'
STEALTHROCK.additional_effect_chance = 0
STEALTHROCK.description = "The user lays a trap of levitating stones around the foe. The trap hurts foes that switch into battle."

#################
### WIDEGUARD ###
#################

WIDEGUARD = Move()
WIDEGUARD.name = "Wide Guard"
WIDEGUARD.type = ROCK
WIDEGUARD.base_damage = 0
WIDEGUARD.category = STATUS
WIDEGUARD.pp = 10
WIDEGUARD.accuracy = 0
WIDEGUARD.priority = 3
WIDEGUARD.target = 'UserSide'
WIDEGUARD.additional_effect_chance = 0
WIDEGUARD.description = "The user and its allies are protected from wide-ranging attacks for a turn. May fail if used in succession."

##################
### DOOMDESIRE ###
##################

DOOMDESIRE = Move()
DOOMDESIRE.name = "Doom Desire"
DOOMDESIRE.type = STEEL
DOOMDESIRE.base_damage = 140
DOOMDESIRE.category = SPECIAL
DOOMDESIRE.pp = 5
DOOMDESIRE.accuracy = 100
DOOMDESIRE.priority = 0
DOOMDESIRE.target = 'NearOther'
DOOMDESIRE.additional_effect_chance = 0
DOOMDESIRE.description = "Two turns after this move is used, the user blasts the target with a concentrated bundle of light."

################
### IRONTAIL ###
################

IRONTAIL = Move()
IRONTAIL.name = "Iron Tail"
IRONTAIL.type = STEEL
IRONTAIL.base_damage = 100
IRONTAIL.category = PHYSICAL
IRONTAIL.pp = 15
IRONTAIL.accuracy = 75
IRONTAIL.priority = 0
IRONTAIL.target = 'NearOther'
IRONTAIL.additional_effect_chance = 30
IRONTAIL.description = "The target is slammed with a steel-hard tail. It may also lower the targets Defense stat."

######################
### SUNSTEELSTRIKE ###
######################

SUNSTEELSTRIKE = Move()
SUNSTEELSTRIKE.name = "Sunsteel Strike"
SUNSTEELSTRIKE.type = STEEL
SUNSTEELSTRIKE.base_damage = 100
SUNSTEELSTRIKE.category = PHYSICAL
SUNSTEELSTRIKE.pp = 5
SUNSTEELSTRIKE.accuracy = 100
SUNSTEELSTRIKE.priority = 0
SUNSTEELSTRIKE.target = 'NearOther'
SUNSTEELSTRIKE.additional_effect_chance = 0
SUNSTEELSTRIKE.description = "The user slams into the target with the force of a meteor. Cant be stopped by the targets Ability."

##################
### METEORMASH ###
##################

METEORMASH = Move()
METEORMASH.name = "Meteor Mash"
METEORMASH.type = STEEL
METEORMASH.base_damage = 90
METEORMASH.category = PHYSICAL
METEORMASH.pp = 10
METEORMASH.accuracy = 90
METEORMASH.priority = 0
METEORMASH.target = 'NearOther'
METEORMASH.additional_effect_chance = 20
METEORMASH.description = "The target is hit with a hard punch fired like a meteor. It may also raise the users Attack."

##################
### ANCHORSHOT ###
##################

ANCHORSHOT = Move()
ANCHORSHOT.name = "Anchor Shot"
ANCHORSHOT.type = STEEL
ANCHORSHOT.base_damage = 80
ANCHORSHOT.category = PHYSICAL
ANCHORSHOT.pp = 20
ANCHORSHOT.accuracy = 100
ANCHORSHOT.priority = 0
ANCHORSHOT.target = 'NearOther'
ANCHORSHOT.additional_effect_chance = 100
ANCHORSHOT.description = "The user entangles the target with its anchor chain. The target becomes unable to flee."

###################
### FLASHCANNON ###
###################

FLASHCANNON = Move()
FLASHCANNON.name = "Flash Cannon"
FLASHCANNON.type = STEEL
FLASHCANNON.base_damage = 80
FLASHCANNON.category = SPECIAL
FLASHCANNON.pp = 10
FLASHCANNON.accuracy = 100
FLASHCANNON.priority = 0
FLASHCANNON.target = 'NearOther'
FLASHCANNON.additional_effect_chance = 10
FLASHCANNON.description = "The user gathers all its light energy and releases it at once. It may also lower the targets Sp. Def stat."

################
### IRONHEAD ###
################

IRONHEAD = Move()
IRONHEAD.name = "Iron Head"
IRONHEAD.type = STEEL
IRONHEAD.base_damage = 80
IRONHEAD.category = PHYSICAL
IRONHEAD.pp = 15
IRONHEAD.accuracy = 100
IRONHEAD.priority = 0
IRONHEAD.target = 'NearOther'
IRONHEAD.additional_effect_chance = 30
IRONHEAD.description = "The foe slams the target with its steel-hard head. It may also make the target flinch."

###################
### SMARTSTRIKE ###
###################

SMARTSTRIKE = Move()
SMARTSTRIKE.name = "Smart Strike"
SMARTSTRIKE.type = STEEL
SMARTSTRIKE.base_damage = 70
SMARTSTRIKE.category = PHYSICAL
SMARTSTRIKE.pp = 10
SMARTSTRIKE.accuracy = 0
SMARTSTRIKE.priority = 0
SMARTSTRIKE.target = 'NearOther'
SMARTSTRIKE.additional_effect_chance = 0
SMARTSTRIKE.description = "The user stabs the target with a sharp horn. This attack never misses."

#################
### STEELWING ###
#################

STEELWING = Move()
STEELWING.name = "Steel Wing"
STEELWING.type = STEEL
STEELWING.base_damage = 70
STEELWING.category = PHYSICAL
STEELWING.pp = 25
STEELWING.accuracy = 90
STEELWING.priority = 0
STEELWING.target = 'NearOther'
STEELWING.additional_effect_chance = 10
STEELWING.description = "The target is hit with wings of steel. It may also raise the users Defense stat."

######################
### DOUBLEIRONBASH ###
######################

DOUBLEIRONBASH = Move()
DOUBLEIRONBASH.name = "Double Iron Bash"
DOUBLEIRONBASH.type = STEEL
DOUBLEIRONBASH.base_damage = 60
DOUBLEIRONBASH.category = PHYSICAL
DOUBLEIRONBASH.pp = 5
DOUBLEIRONBASH.accuracy = 100
DOUBLEIRONBASH.priority = 0
DOUBLEIRONBASH.target = 'NearOther'
DOUBLEIRONBASH.additional_effect_chance = 30
DOUBLEIRONBASH.description = "The user rotates, centering the hex nut in its chest, and then strikes twice. May cause flinching."

##################
### MIRRORSHOT ###
##################

MIRRORSHOT = Move()
MIRRORSHOT.name = "Mirror Shot"
MIRRORSHOT.type = STEEL
MIRRORSHOT.base_damage = 65
MIRRORSHOT.category = SPECIAL
MIRRORSHOT.pp = 10
MIRRORSHOT.accuracy = 85
MIRRORSHOT.priority = 0
MIRRORSHOT.target = 'NearOther'
MIRRORSHOT.additional_effect_chance = 30
MIRRORSHOT.description = "The user looses a flash of energy from its polished body. It may also lower the targets accuracy."

##################
### MAGNETBOMB ###
##################

MAGNETBOMB = Move()
MAGNETBOMB.name = "Magnet Bomb"
MAGNETBOMB.type = STEEL
MAGNETBOMB.base_damage = 60
MAGNETBOMB.category = PHYSICAL
MAGNETBOMB.pp = 20
MAGNETBOMB.accuracy = 0
MAGNETBOMB.priority = 0
MAGNETBOMB.target = 'NearOther'
MAGNETBOMB.additional_effect_chance = 0
MAGNETBOMB.description = "The user launches steel bombs that stick to the target. This attack will not miss."

#################
### GEARGRIND ###
#################

GEARGRIND = Move()
GEARGRIND.name = "Gear Grind"
GEARGRIND.type = STEEL
GEARGRIND.base_damage = 50
GEARGRIND.category = PHYSICAL
GEARGRIND.pp = 15
GEARGRIND.accuracy = 85
GEARGRIND.priority = 0
GEARGRIND.target = 'NearOther'
GEARGRIND.additional_effect_chance = 0
GEARGRIND.description = "The user attacks by throwing two steel gears at its target."

#################
### METALCLAW ###
#################

METALCLAW = Move()
METALCLAW.name = "Metal Claw"
METALCLAW.type = STEEL
METALCLAW.base_damage = 50
METALCLAW.category = PHYSICAL
METALCLAW.pp = 35
METALCLAW.accuracy = 95
METALCLAW.priority = 0
METALCLAW.target = 'NearOther'
METALCLAW.additional_effect_chance = 10
METALCLAW.description = "The target is raked with steel claws. It may also raise the users Attack stat."

###################
### BULLETPUNCH ###
###################

BULLETPUNCH = Move()
BULLETPUNCH.name = "Bullet Punch"
BULLETPUNCH.type = STEEL
BULLETPUNCH.base_damage = 40
BULLETPUNCH.category = PHYSICAL
BULLETPUNCH.pp = 30
BULLETPUNCH.accuracy = 100
BULLETPUNCH.priority = 1
BULLETPUNCH.target = 'NearOther'
BULLETPUNCH.additional_effect_chance = 0
BULLETPUNCH.description = "The user strikes the target with tough punches as fast as bullets. This move always goes first."

################
### GYROBALL ###
################

GYROBALL = Move()
GYROBALL.name = "Gyro Ball"
GYROBALL.type = STEEL
GYROBALL.base_damage = 1
GYROBALL.category = PHYSICAL
GYROBALL.pp = 5
GYROBALL.accuracy = 100
GYROBALL.priority = 0
GYROBALL.target = 'NearOther'
GYROBALL.additional_effect_chance = 0
GYROBALL.description = "The user tackles the target with a high-speed spin. The slower the user, the greater the damage."

#################
### HEAVYSLAM ###
#################

HEAVYSLAM = Move()
HEAVYSLAM.name = "Heavy Slam"
HEAVYSLAM.type = STEEL
HEAVYSLAM.base_damage = 1
HEAVYSLAM.category = PHYSICAL
HEAVYSLAM.pp = 10
HEAVYSLAM.accuracy = 100
HEAVYSLAM.priority = 0
HEAVYSLAM.target = 'NearOther'
HEAVYSLAM.additional_effect_chance = 0
HEAVYSLAM.description = "The user slams into the foe with its heavy body. The heavier the user, the greater the damage."

##################
### METALBURST ###
##################

METALBURST = Move()
METALBURST.name = "Metal Burst"
METALBURST.type = STEEL
METALBURST.base_damage = 1
METALBURST.category = PHYSICAL
METALBURST.pp = 10
METALBURST.accuracy = 100
METALBURST.priority = 0
METALBURST.target = 'None'
METALBURST.additional_effect_chance = 0
METALBURST.description = "The user retaliates with much greater power against the target that last inflicted damage on it."

##################
### AUTOTOMIZE ###
##################

AUTOTOMIZE = Move()
AUTOTOMIZE.name = "Autotomize"
AUTOTOMIZE.type = STEEL
AUTOTOMIZE.base_damage = 0
AUTOTOMIZE.category = STATUS
AUTOTOMIZE.pp = 15
AUTOTOMIZE.accuracy = 0
AUTOTOMIZE.priority = 0
AUTOTOMIZE.target = 'User'
AUTOTOMIZE.additional_effect_chance = 0
AUTOTOMIZE.description = "The user sheds part of its body to make itself lighter and sharply raise its Speed stat."

##############
### GEARUP ###
##############

GEARUP = Move()
GEARUP.name = "Gear Up"
GEARUP.type = STEEL
GEARUP.base_damage = 0
GEARUP.category = STATUS
GEARUP.pp = 20
GEARUP.accuracy = 0
GEARUP.priority = 0
GEARUP.target = 'UserAndAllies'
GEARUP.additional_effect_chance = 0
GEARUP.description = "The user engages its gears to raise the Attack and Sp. Atk of allies with the Plus or Minus Ability."

###################
### IRONDEFENSE ###
###################

IRONDEFENSE = Move()
IRONDEFENSE.name = "Iron Defense"
IRONDEFENSE.type = STEEL
IRONDEFENSE.base_damage = 0
IRONDEFENSE.category = STATUS
IRONDEFENSE.pp = 15
IRONDEFENSE.accuracy = 0
IRONDEFENSE.priority = 0
IRONDEFENSE.target = 'User'
IRONDEFENSE.additional_effect_chance = 0
IRONDEFENSE.description = "The user hardens its bodys surface like iron, sharply raising its Defense stat."

###################
### KINGSSHIELD ###
###################

KINGSSHIELD = Move()
KINGSSHIELD.name = "King's Shield"
KINGSSHIELD.type = STEEL
KINGSSHIELD.base_damage = 0
KINGSSHIELD.category = STATUS
KINGSSHIELD.pp = 10
KINGSSHIELD.accuracy = 0
KINGSSHIELD.priority = 4
KINGSSHIELD.target = 'User'
KINGSSHIELD.additional_effect_chance = 0
KINGSSHIELD.description = "Protects itself from damage. It also harshly lowers the Attack of attackers that make contact."

##################
### METALSOUND ###
##################

METALSOUND = Move()
METALSOUND.name = "Metal Sound"
METALSOUND.type = STEEL
METALSOUND.base_damage = 0
METALSOUND.category = STATUS
METALSOUND.pp = 40
METALSOUND.accuracy = 85
METALSOUND.priority = 0
METALSOUND.target = 'NearOther'
METALSOUND.additional_effect_chance = 0
METALSOUND.description = "A horrible sound like scraping metal harshly reduces the targets Sp. Def stat."

#################
### SHIFTGEAR ###
#################

SHIFTGEAR = Move()
SHIFTGEAR.name = "Shift Gear"
SHIFTGEAR.type = STEEL
SHIFTGEAR.base_damage = 0
SHIFTGEAR.category = STATUS
SHIFTGEAR.pp = 10
SHIFTGEAR.accuracy = 0
SHIFTGEAR.priority = 0
SHIFTGEAR.target = 'User'
SHIFTGEAR.additional_effect_chance = 0
SHIFTGEAR.description = "The user rotates its gears, raising its Attack and sharply raising its Speed."

###################
### HYDROCANNON ###
###################

HYDROCANNON = Move()
HYDROCANNON.name = "Hydro Cannon"
HYDROCANNON.type = WATER
HYDROCANNON.base_damage = 150
HYDROCANNON.category = SPECIAL
HYDROCANNON.pp = 5
HYDROCANNON.accuracy = 90
HYDROCANNON.priority = 0
HYDROCANNON.target = 'NearOther'
HYDROCANNON.additional_effect_chance = 0
HYDROCANNON.description = "The target is hit with a watery blast. The user must rest on the next turn, however."

##################
### WATERSPOUT ###
##################

WATERSPOUT = Move()
WATERSPOUT.name = "Water Spout"
WATERSPOUT.type = WATER
WATERSPOUT.base_damage = 150
WATERSPOUT.category = SPECIAL
WATERSPOUT.pp = 5
WATERSPOUT.accuracy = 100
WATERSPOUT.priority = 0
WATERSPOUT.target = 'AllNearFoes'
WATERSPOUT.additional_effect_chance = 0
WATERSPOUT.description = "The user spouts water to damage the foe. The lower the users HP, the less powerful it becomes."

#################
### HYDROPUMP ###
#################

HYDROPUMP = Move()
HYDROPUMP.name = "Hydro Pump"
HYDROPUMP.type = WATER
HYDROPUMP.base_damage = 110
HYDROPUMP.category = SPECIAL
HYDROPUMP.pp = 5
HYDROPUMP.accuracy = 80
HYDROPUMP.priority = 0
HYDROPUMP.target = 'NearOther'
HYDROPUMP.additional_effect_chance = 0
HYDROPUMP.description = "The target is blasted by a huge volume of water launched under great pressure."

###################
### ORIGINPULSE ###
###################

ORIGINPULSE = Move()
ORIGINPULSE.name = "Origin Pulse"
ORIGINPULSE.type = WATER
ORIGINPULSE.base_damage = 110
ORIGINPULSE.category = SPECIAL
ORIGINPULSE.pp = 10
ORIGINPULSE.accuracy = 85
ORIGINPULSE.priority = 0
ORIGINPULSE.target = 'AllNearFoes'
ORIGINPULSE.additional_effect_chance = 0
ORIGINPULSE.description = "The user attacks opposing Pokémon with countless beams of light that glow a deep and brilliant blue."

#####################
### STEAMERUPTION ###
#####################

STEAMERUPTION = Move()
STEAMERUPTION.name = "Steam Eruption"
STEAMERUPTION.type = WATER
STEAMERUPTION.base_damage = 110
STEAMERUPTION.category = SPECIAL
STEAMERUPTION.pp = 5
STEAMERUPTION.accuracy = 95
STEAMERUPTION.priority = 0
STEAMERUPTION.target = 'NearOther'
STEAMERUPTION.additional_effect_chance = 30
STEAMERUPTION.description = "The user immerses the target in superheated steam. This may also leave the target with a burn."

##################
### CRABHAMMER ###
##################

CRABHAMMER = Move()
CRABHAMMER.name = "Crabhammer"
CRABHAMMER.type = WATER
CRABHAMMER.base_damage = 100
CRABHAMMER.category = PHYSICAL
CRABHAMMER.pp = 10
CRABHAMMER.accuracy = 90
CRABHAMMER.priority = 0
CRABHAMMER.target = 'NearOther'
CRABHAMMER.additional_effect_chance = 0
CRABHAMMER.description = "The target is hammered with a large pincer. Critical hits land more easily."

################
### AQUATAIL ###
################

AQUATAIL = Move()
AQUATAIL.name = "Aqua Tail"
AQUATAIL.type = WATER
AQUATAIL.base_damage = 90
AQUATAIL.category = PHYSICAL
AQUATAIL.pp = 10
AQUATAIL.accuracy = 90
AQUATAIL.priority = 0
AQUATAIL.target = 'NearOther'
AQUATAIL.additional_effect_chance = 0
AQUATAIL.description = "The user attacks by swinging its tail as if it were a vicious wave in a raging storm."

##################
### MUDDYWATER ###
##################

MUDDYWATER = Move()
MUDDYWATER.name = "Muddy Water"
MUDDYWATER.type = WATER
MUDDYWATER.base_damage = 90
MUDDYWATER.category = SPECIAL
MUDDYWATER.pp = 10
MUDDYWATER.accuracy = 85
MUDDYWATER.priority = 0
MUDDYWATER.target = 'AllNearFoes'
MUDDYWATER.additional_effect_chance = 30
MUDDYWATER.description = "The user attacks by shooting muddy water at the opposing team. It may also lower the targets accuracy."

#####################
### SPARKLINGARIA ###
#####################

SPARKLINGARIA = Move()
SPARKLINGARIA.name = "Sparkling Aria"
SPARKLINGARIA.type = WATER
SPARKLINGARIA.base_damage = 90
SPARKLINGARIA.category = SPECIAL
SPARKLINGARIA.pp = 10
SPARKLINGARIA.accuracy = 100
SPARKLINGARIA.priority = 0
SPARKLINGARIA.target = 'AllNearOthers'
SPARKLINGARIA.additional_effect_chance = 100
SPARKLINGARIA.description = "The user bursts into song, emitting many bubbles. Any burnt Pokémon will be healed by these bubbles."

############
### SURF ###
############

SURF = Move()
SURF.name = "Surf"
SURF.type = WATER
SURF.base_damage = 90
SURF.category = SPECIAL
SURF.pp = 15
SURF.accuracy = 100
SURF.priority = 0
SURF.target = 'AllNearOthers'
SURF.additional_effect_chance = 0
SURF.description = "It swamps the area around the user with a giant wave. It can also be used for crossing water."

###################
### LIQUIDATION ###
###################

LIQUIDATION = Move()
LIQUIDATION.name = "Liquidation"
LIQUIDATION.type = WATER
LIQUIDATION.base_damage = 85
LIQUIDATION.category = PHYSICAL
LIQUIDATION.pp = 10
LIQUIDATION.accuracy = 100
LIQUIDATION.priority = 0
LIQUIDATION.target = 'NearOther'
LIQUIDATION.additional_effect_chance = 20
LIQUIDATION.description = "The user slams into the target using a full-force blast of water. May lower the targets Defense."

############
### DIVE ###
############

DIVE = Move()
DIVE.name = "Dive"
DIVE.type = WATER
DIVE.base_damage = 80
DIVE.category = PHYSICAL
DIVE.pp = 10
DIVE.accuracy = 100
DIVE.priority = 0
DIVE.target = 'NearOther'
DIVE.additional_effect_chance = 0
DIVE.description = "Diving on the first turn, the user rises and hits on the next turn. It can be used to dive in the ocean."

#############
### SCALD ###
#############

SCALD = Move()
SCALD.name = "Scald"
SCALD.type = WATER
SCALD.base_damage = 80
SCALD.category = SPECIAL
SCALD.pp = 15
SCALD.accuracy = 100
SCALD.priority = 0
SCALD.target = 'NearOther'
SCALD.additional_effect_chance = 30
SCALD.description = "The user shoots boiling hot water at its target. It may also leave the target with a burn."

###################
### WATERPLEDGE ###
###################

WATERPLEDGE = Move()
WATERPLEDGE.name = "Water Pledge"
WATERPLEDGE.type = WATER
WATERPLEDGE.base_damage = 80
WATERPLEDGE.category = SPECIAL
WATERPLEDGE.pp = 10
WATERPLEDGE.accuracy = 100
WATERPLEDGE.priority = 0
WATERPLEDGE.target = 'NearOther'
WATERPLEDGE.additional_effect_chance = 0
WATERPLEDGE.description = "A column of water strikes the target. When combined with its fire equivalent, it makes a rainbow."

#################
### WATERFALL ###
#################

WATERFALL = Move()
WATERFALL.name = "Waterfall"
WATERFALL.type = WATER
WATERFALL.base_damage = 80
WATERFALL.category = PHYSICAL
WATERFALL.pp = 15
WATERFALL.accuracy = 100
WATERFALL.priority = 0
WATERFALL.target = 'NearOther'
WATERFALL.additional_effect_chance = 20
WATERFALL.description = "The user charges at the target and may make it flinch. It can also be used to climb a waterfall."

##################
### RAZORSHELL ###
##################

RAZORSHELL = Move()
RAZORSHELL.name = "Razor Shell"
RAZORSHELL.type = WATER
RAZORSHELL.base_damage = 75
RAZORSHELL.category = PHYSICAL
RAZORSHELL.pp = 10
RAZORSHELL.accuracy = 95
RAZORSHELL.priority = 0
RAZORSHELL.target = 'NearOther'
RAZORSHELL.additional_effect_chance = 50
RAZORSHELL.description = "The user cuts the foe with sharp shells. It may also lower the targets Defense stat."

#############
### BRINE ###
#############

BRINE = Move()
BRINE.name = "Brine"
BRINE.type = WATER
BRINE.base_damage = 65
BRINE.category = SPECIAL
BRINE.pp = 10
BRINE.accuracy = 100
BRINE.priority = 0
BRINE.target = 'NearOther'
BRINE.additional_effect_chance = 0
BRINE.description = "If the targets HP is down to about half, this attack will hit with double the power."

##################
### BUBBLEBEAM ###
##################

BUBBLEBEAM = Move()
BUBBLEBEAM.name = "Bubble Beam"
BUBBLEBEAM.type = WATER
BUBBLEBEAM.base_damage = 65
BUBBLEBEAM.category = SPECIAL
BUBBLEBEAM.pp = 20
BUBBLEBEAM.accuracy = 100
BUBBLEBEAM.priority = 0
BUBBLEBEAM.target = 'NearOther'
BUBBLEBEAM.additional_effect_chance = 10
BUBBLEBEAM.description = "A spray of bubbles is forcefully ejected at the target. It may also lower its Speed stat."

#################
### OCTAZOOKA ###
#################

OCTAZOOKA = Move()
OCTAZOOKA.name = "Octazooka"
OCTAZOOKA.type = WATER
OCTAZOOKA.base_damage = 65
OCTAZOOKA.category = SPECIAL
OCTAZOOKA.pp = 10
OCTAZOOKA.accuracy = 85
OCTAZOOKA.priority = 0
OCTAZOOKA.target = 'NearOther'
OCTAZOOKA.additional_effect_chance = 50
OCTAZOOKA.description = "The user attacks by spraying ink in the foes face or eyes. It may also lower the targets accuracy."

##################
### WATERPULSE ###
##################

WATERPULSE = Move()
WATERPULSE.name = "Water Pulse"
WATERPULSE.type = WATER
WATERPULSE.base_damage = 60
WATERPULSE.category = SPECIAL
WATERPULSE.pp = 20
WATERPULSE.accuracy = 100
WATERPULSE.priority = 0
WATERPULSE.target = 'Other'
WATERPULSE.additional_effect_chance = 20
WATERPULSE.description = "The user attacks the target with a pulsing blast of water. It may also confuse the target."

###############
### AQUAJET ###
###############

AQUAJET = Move()
AQUAJET.name = "Aqua Jet"
AQUAJET.type = WATER
AQUAJET.base_damage = 40
AQUAJET.category = PHYSICAL
AQUAJET.pp = 20
AQUAJET.accuracy = 100
AQUAJET.priority = 1
AQUAJET.target = 'NearOther'
AQUAJET.additional_effect_chance = 0
AQUAJET.description = "The user lunges at the target at a speed that makes it almost invisible. It is sure to strike first."

##############
### BUBBLE ###
##############

BUBBLE = Move()
BUBBLE.name = "Bubble"
BUBBLE.type = WATER
BUBBLE.base_damage = 40
BUBBLE.category = SPECIAL
BUBBLE.pp = 30
BUBBLE.accuracy = 100
BUBBLE.priority = 0
BUBBLE.target = 'AllNearFoes'
BUBBLE.additional_effect_chance = 10
BUBBLE.description = "A spray of countless bubbles is jetted at the opposing team. It may also lower the targets Speed stats."

################
### WATERGUN ###
################

WATERGUN = Move()
WATERGUN.name = "Water Gun"
WATERGUN.type = WATER
WATERGUN.base_damage = 40
WATERGUN.category = SPECIAL
WATERGUN.pp = 25
WATERGUN.accuracy = 100
WATERGUN.priority = 0
WATERGUN.target = 'NearOther'
WATERGUN.additional_effect_chance = 0
WATERGUN.description = "The target is blasted with a forceful shot of water."

#############
### CLAMP ###
#############

CLAMP = Move()
CLAMP.name = "Clamp"
CLAMP.type = WATER
CLAMP.base_damage = 35
CLAMP.category = PHYSICAL
CLAMP.pp = 15
CLAMP.accuracy = 85
CLAMP.priority = 0
CLAMP.target = 'NearOther'
CLAMP.additional_effect_chance = 0
CLAMP.description = "The target is clamped and squeezed by the users very thick and sturdy shell for four to five turns."

#################
### WHIRLPOOL ###
#################

WHIRLPOOL = Move()
WHIRLPOOL.name = "Whirlpool"
WHIRLPOOL.type = WATER
WHIRLPOOL.base_damage = 35
WHIRLPOOL.category = SPECIAL
WHIRLPOOL.pp = 15
WHIRLPOOL.accuracy = 85
WHIRLPOOL.priority = 0
WHIRLPOOL.target = 'NearOther'
WHIRLPOOL.additional_effect_chance = 0
WHIRLPOOL.description = "Traps foes in a violent swirling whirlpool for four to five turns."

#####################
### WATERSHURIKEN ###
#####################

WATERSHURIKEN = Move()
WATERSHURIKEN.name = "Water Shuriken"
WATERSHURIKEN.type = WATER
WATERSHURIKEN.base_damage = 15
WATERSHURIKEN.category = SPECIAL
WATERSHURIKEN.pp = 20
WATERSHURIKEN.accuracy = 100
WATERSHURIKEN.priority = 1
WATERSHURIKEN.target = 'NearOther'
WATERSHURIKEN.additional_effect_chance = 0
WATERSHURIKEN.description = "The user hits the target with throwing stars 2-5 times in a row. This move always goes first."

################
### AQUARING ###
################

AQUARING = Move()
AQUARING.name = "Aqua Ring"
AQUARING.type = WATER
AQUARING.base_damage = 0
AQUARING.category = STATUS
AQUARING.pp = 20
AQUARING.accuracy = 0
AQUARING.priority = 0
AQUARING.target = 'User'
AQUARING.additional_effect_chance = 0
AQUARING.description = "The user envelops itself in a veil made of water. It regains some HP on every turn."

#################
### RAINDANCE ###
#################

RAINDANCE = Move()
RAINDANCE.name = "Rain Dance"
RAINDANCE.type = WATER
RAINDANCE.base_damage = 0
RAINDANCE.category = STATUS
RAINDANCE.pp = 5
RAINDANCE.accuracy = 0
RAINDANCE.priority = 0
RAINDANCE.target = 'BothSides'
RAINDANCE.additional_effect_chance = 0
RAINDANCE.description = "The user summons a heavy rain that falls for five turns, powering up Water-type moves."

############
### SOAK ###
############

SOAK = Move()
SOAK.name = "Soak"
SOAK.type = WATER
SOAK.base_damage = 0
SOAK.category = STATUS
SOAK.pp = 20
SOAK.accuracy = 100
SOAK.priority = 0
SOAK.target = 'NearOther'
SOAK.additional_effect_chance = 0
SOAK.description = "The user shoots a torrent of water at the target and changes the targets type to Water."

##################
### WATERSPORT ###
##################

WATERSPORT = Move()
WATERSPORT.name = "Water Sport"
WATERSPORT.type = WATER
WATERSPORT.base_damage = 0
WATERSPORT.category = STATUS
WATERSPORT.pp = 15
WATERSPORT.accuracy = 0
WATERSPORT.priority = 0
WATERSPORT.target = 'BothSides'
WATERSPORT.additional_effect_chance = 0
WATERSPORT.description = "The user soaks itself with water. The move weakens Fire-type moves while the user is in the battle."

################
### WITHDRAW ###
################

WITHDRAW = Move()
WITHDRAW.name = "Withdraw"
WITHDRAW.type = WATER
WITHDRAW.base_damage = 0
WITHDRAW.category = STATUS
WITHDRAW.pp = 40
WITHDRAW.accuracy = 0
WITHDRAW.priority = 0
WITHDRAW.target = 'User'
WITHDRAW.additional_effect_chance = 0
WITHDRAW.description = "The user withdraws its body into its hard shell, raising its Defense stat."

