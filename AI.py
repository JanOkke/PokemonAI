"""

AI logic:

-> Check all moves. If you can OHKO, choose that move.

#########################
###### OHKO logic #######
#########################

->  If multiple moves can OHKO, choose the one with highest priority unless you're faster and the opponent has no
    priority damaging move.
->  If multiple moves have the same priority, choose that one that hits possible switches as hard as possible.

#########################
### Stat change moves ###
#########################

->  Calculate highest damage over multiple turns until you win (as example: Leer to 4hko instead of 6hko is smarter)
->  Same goes for setup moves
->  Prefer setup + kill over attack and kill
->  Prefer attack and kill over lowering and kill

#########################
##### Protect logic #####
#########################

->  Use protect to scout a move and switch eventually?
->  Don't use protect if your opponent can setup on the protect turn
->  Prefer protecting when you have self-heal, your opponent has a damaging status condition or you have speed boost
->  Don't spam protect unless you're going to die and your opponent is faster

#########################
##### Kings Shield ######
#########################

->  Use Kings Shield more often if your opponent has effective contact moves
->  Prefer to use Kings Shield when you're in blade form unless you can kill with priority
    and your opponent doesnt have priority

#########################
###### Status moves #####
#########################

->  Don't status a guts user / lower value for quick feet
->  Don't poison a toxic boost / burn a flare boost user
->  Burning physical attackers is more valuable than special attackers
->  Poisoning defensive mons is very efficient

#########################
##### Entry hazards #####
#########################

->  Setting up sticky webs value is higher for each grounded pokemon
->  Pokemon with a base speed of below 50 count half value
->  Stealth rocks value increases drastically if the enemy has multiscale / focus sash
->  Toxic spikes layer 1 is more valuable than layer 2
->  Toxic spikes value decreases drastically if the enemy has a poison type
->  Toxic spikes value increases for each grounded / non-steel type pokemon
->  Spikes value decreases with each additional layer
->  Defog value increases if the enemy has more hazards than you
->  Don't use hazards on a magic bounce pokemon

#########################
####### Screens #########
#########################

->  Prefer the screen that blocks the higher damage first
->  Lower value if the enemy has brick break / psychic fangs
->  Prefer brick break / psychic fangs if enemy has screens

#########################
######## Taunt ##########
#########################

->  Prefer if the enemy has status moves
->  Don't use status moves if the enemy has taunt and is faster (except for prankster and priority status moves)
->  Don't use taunt if you have magic bounce and it won't help too much

#########################
#### Reflecting moves ###
#########################

->  If the reflect move is more damage, prefer it
->  If the enemy has a reflect move, prefer to weaken before going for highest damage with the safest 2hko combo

#########################
###### Substitute #######
#########################

->  If the enemy has substitute and is faster, don't go for a status move that would fail due to substitute
->  Prefer to switch if you can't break the sub within one attack
->  Prefer to use substitute if your opponent has a lot of status condition moves like substitute
->  Prefer to use substitute if your opponent can not break the substitute within one attack

"""


def percentage(target_hp, damage):
    return round(damage / target_hp * 100 - 0.499)


from legal import is_legal
import action
import battle


def choose_move(player, ai):
    pass  # TODO


def get_all_enemy_actions(_battle: battle.Battle) -> list:
    party_enemy = _battle.team2.get_party()
    current_mon = _battle.team2.get_first_pokemon()
    actions = []
    for move in current_mon.moves:
        if is_legal(move, _battle, current_mon):
            actions.append(action.Action(type=action.MoveAction, user=current_mon, act=move, _battle=_battle,
                                         opponent=_battle.team1.get_first_pokemon()))
    for party_member in range(_battle.team2.get_team_length()):
        if party_member == 0:
            continue
        actions.append(
            action.Action(type=action.SwitchAction, user=current_mon, act=party_enemy[party_member], _battle=_battle,
                          opponent=_battle.team1.get_first_pokemon()))
    return actions


def get_all_possible_actions(_battle: battle.Battle, with_switching=True) -> list:
    party_enemy = _battle.team1.get_party()
    current_mon = _battle.team1.get_first_pokemon()
    actions = []
    for move in current_mon.moves:
        if is_legal(move, _battle, current_mon):
            actions.append(action.Action(type=action.MoveAction, user=current_mon, act=move, _battle=_battle,
                                         opponent=_battle.team2.get_first_pokemon()))
    if with_switching:
        for party_member in range(_battle.team1.get_team_length()):
            if party_member == 0:
                continue
            actions.append(
                action.Action(type=action.SwitchAction, user=current_mon, act=party_enemy[party_member], _battle=_battle,
                              opponent=_battle.team2.get_first_pokemon()))
    return actions


def get_likely_move(_battle: battle.Battle):
    enemy = _battle.team2.get_first_pokemon()
    own = _battle.team1.get_first_pokemon()
    ...  # todo im tired


def get_roaster(_battle: battle.Battle):
    ROASTER = []
    ROASTER_2 = []
    options_atk = get_all_possible_actions(_battle)
    options_def = get_all_enemy_actions(_battle)
    for option_x in options_atk:
        for option_y in options_def:
            option_path = action.ActionOrder()
            option_path.add_action(option_x)
            option_path.add_action(option_y)
            out_coms = option_path.handle_actions(ignore_prio=True)
            for outcome in out_coms:
                #print(outcome)
                action_type, damage, user, opponent, act, other_action = outcome
                damage = percentage(opponent.total_hp, damage)
                if other_action.type == action.SwitchAction:
                    act2 = '{} switched into {}'.format(other_action.user.get_species_name(), other_action.act.get_species_name())
                elif other_action.type == action.MoveAction:
                    act2 = '{} used move {}'.format(other_action.user.get_species_name(), other_action.act)
                else:
                    act2 = 'Something went wrong.'
                if action_type == action.MoveAction:
                    ROASTER.append('{} can deal {} % damage to {} with move {}. The opposing {}.'.format(user.get_species_name(), damage, opponent.get_species_name(), act, act2))
                if action_type == action.SwitchAction:
                    ROASTER.append('{} can switch into {}. The opposing {}.'.format(user.get_species_name(), act.get_species_name(), act2))


                options_atk = get_all_possible_actions(_battle)
                options_def = get_all_enemy_actions(_battle)
                for option_x in options_atk:
                    for option_y in options_def:
                        option_path = action.ActionOrder()
                        option_path.add_action(option_x)
                        option_path.add_action(option_y)
                        out_coms = option_path.handle_actions(ignore_prio=True)
                        for outcome in out_coms:
                            # print(outcome)
                            action_type, damage, user, opponent, act, other_action = outcome
                            damage = percentage(opponent.total_hp, damage)
                            if other_action.type == action.SwitchAction:
                                act2 = '{} switched into {}'.format(other_action.user.get_species_name(),
                                                                    other_action.act.get_species_name())
                            elif other_action.type == action.MoveAction:
                                act2 = '{} used move {}'.format(other_action.user.get_species_name(), other_action.act)
                            else:
                                act2 = 'Something went wrong.'
                            if action_type == action.MoveAction:
                                ROASTER_2.append('{} can deal {} % damage to {} with move {}. The opposing {}.'.format(
                                    user.get_species_name(), damage, opponent.get_species_name(), act, act2))
                            if action_type == action.SwitchAction:
                                ROASTER_2.append('{} can switch into {}. The opposing {}.'.format(user.get_species_name(),
                                                                                               act.get_species_name(),
                                                                                               act2))
    ROASTER.sort()
    ROASTER_2.sort()
    for text in ROASTER:
        print('Turn {}: {}'.format(1, text))
    for text in ROASTER_2:
        print('Turn {}: {}'.format(2, text))
