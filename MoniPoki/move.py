import _types
import category
import moves
import movedata
from pokemon import Pokemon
import abilities
import effectivity


class Move:
    def __init__(self):
        self.battle = None
        self.move_id = 0
        self.internal_name = ""
        self.name = ""
        self.function_code = None
        self.base_damage = 0
        self.type = _types.NORMAL  # Default
        self.category = category.STATUS  # Default
        self.accuracy = 100
        self.pp = 0
        self.total_pp = moves.get_max_pp_by_id(self.move_id)
        self.additional_effect_chance = 0
        self.target = 0  # 0 = User, 1 = Enemy, 2 = Both Enemies, 3 = Everyone
        self.priority = 0
        self.usable_asleep = False
        self.usable_in_gravity = True
        self.healing_move = False
        self.recoil_move = False
        self.flinching_move = False
        self.calls_another_move = False
        self.charging_move = False
        self.hits_flying_targets = False
        self.hits_digging_targets = False
        self.hits_diving_targets = False
        self.ignores_reflect = False  # Brick Break
        self.damage_reduced_when_burning = True  # Facade -> False
        self.contact_move = False
        self.can_protect_against = False
        self.can_magic_coated = False
        self.can_get_snatched = False
        self.can_get_mirror_moved = False
        self.can_use_kings_rock = False
        self.thaws_user = False
        self.high_critical_rate = False
        self.biting_move = False
        self.punching_move = False
        self.sound_move = False
        self.powder_move = False
        self.pulse_move = False
        self.bomb_move = False
        self.dance_move = False
        self.max_accuracy_when_minimized = False
        self.can_kill = True  # False Swipe
        self.power_boosted_by_type_change = False  # Aerilate, Pixilate etc
        self.snatched = False
        self.always_crits = False  # Wicked blow etc

    # ==============================================================================
    # Target / PP
    # ==============================================================================

    def get_target(self) -> int:
        return self.target

    def set_total_pp(self):
        self.total_pp = movedata.total_pp(self.move_id)

    # ==============================================================================
    # Category
    # ==============================================================================

    def is_physical(self) -> bool:
        return self.category == category.PHYSICAL

    def is_special(self) -> bool:
        return self.category == category.SPECIAL

    def is_status(self) -> bool:
        return self.category == category.STATUS

    # ==============================================================================
    # Flags
    # ==============================================================================

    def does_damage(self) -> bool:
        return self.category == category.STATUS

    def is_usable_in_gravity(self) -> bool:
        return self.usable_in_gravity

    def is_usable_when_sleeping(self) -> bool:
        return self.usable_asleep

    def is_healing(self) -> bool:
        return self.healing_move

    def does_recoil(self) -> bool:
        return self.recoil_move

    def is_flinching_move(self) -> bool:
        return self.flinching_move

    def is_calling_another_move(self) -> bool:
        return self.calls_another_move

    def is_charging_move(self) -> bool:
        return self.charging_move

    def is_hitting_flying_targets(self) -> bool:
        return self.hits_flying_targets

    def is_hitting_digging_targets(self) -> bool:
        return self.hits_digging_targets

    def is_hitting_diving_targets(self) -> bool:
        return self.hits_diving_targets

    def is_ignoring_reflect(self) -> bool:
        return self.ignores_reflect

    def is_reduced_when_burning(self) -> bool:
        return self.damage_reduced_when_burning

    def is_contact_move(self) -> bool:
        return self.contact_move

    def can_be_protected(self) -> bool:
        return self.can_protect_against

    def can_be_magic_coated(self) -> bool:
        return self.can_magic_coated

    def can_be_using_kings_rock(self) -> bool:
        return self.can_use_kings_rock

    def is_thawing_user(self) -> bool:
        return self.thaws_user

    def has_high_critical_rate(self) -> bool:
        return self.high_critical_rate

    def is_biting_move(self) -> bool:
        return self.biting_move

    def is_punching_move(self) -> bool:
        return self.punching_move

    def is_sound_move(self) -> bool:
        return self.sound_move

    def is_pulse_move(self) -> bool:
        return self.pulse_move

    def is_bomb_move(self) -> bool:
        return self.bomb_move

    def is_dance_move(self) -> bool:
        return self.dance_move

    def tramples_minimize(self) -> bool:
        return self.max_accuracy_when_minimized

    def can_kill_foe(self) -> bool:
        return self.can_kill

    def ignores_substitute(self, user: Pokemon) -> bool:
        return self.is_sound_move() or user.has_ability(abilities.INFILTRATOR)

    # ==============================================================================
    # Effectivity
    # ==============================================================================

    def is_super_effective(self, target_type: str, inverse=False) -> bool:
        return effectivity.is_super_effective(self.type, target_type, inverse)

    def is_ineffective(self, target_type: str, inverse=False) -> bool:
        return effectivity.is_ineffective(self.type, target_type, inverse)

    def is_immune(self, target_type: str) -> bool:
        return effectivity.is_immune(self.type, target_type)

    # ==============================================================================
    # Create a new Move
    # ==============================================================================

    @staticmethod
    def create_new_move(battle, move_id: int):
        # ==============================================================================
        # Data
        # ==============================================================================

        move = Move()
        move.battle = battle
        move.move_id = move_id
        move.name = movedata.name(move_id)
        move.internal_name = movedata.internal_name(move_id)
        move.function_code = movedata.function_code(move_id)
        move.base_damage = movedata.damage(move_id)
        move.type = movedata.move_type(move_id)
        move.category = movedata.category(move_id)
        move.accuracy = movedata.accuracy(move_id)
        move.additional_effect_chance = movedata.effect_chance(move_id)
        move.target = movedata.target(move_id)
        move.priority = movedata.priority(move_id)

        # ==============================================================================
        # Flags
        # ==============================================================================
        move.punching_move = True  # TODO!

        try:

            move.usable_asleep, move.usable_in_gravity, move.healing_move, move.recoil_move, move.flinching_move, \
            move.calls_another_move, move.charging_move, move.hits_flying_targets, move.hits_digging_targets, \
            move.hits_diving_targets, move.ignores_reflect, move.damage_reduced_when_burning, move.contact_move, \
            move.can_protect_against, move.can_magic_coated, move.can_get_snatched, move.can_get_mirror_moved, \
            move.can_use_kings_rock, move.thaws_user, move.high_critical_rate, move.biting_move, move.punching_move, \
            move.sound_move, move.powder_move, move.pulse_move, move.bomb_move, move.dance_move, \
            move.max_accuracy_when_minimized, move.can_kill, move.power_boosted_by_type_change = movedata.flags(move_id)

        except ValueError:
            pass  # TODO!!
        return move
