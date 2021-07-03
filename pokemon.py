import gender
import nature
import language
import settings
import errors
import species
import _types
import moves
import items
import bag
import status
import experience


class Pokemon:
    def __init__(self):
        self.nickname = ""
        self.dex_entry = ""
        self.species = 0  # DEX
        self.experience = 0
        self.hp = 0
        self.total_hp = 0
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.sp_atk = 0
        self.sp_def = 0
        self.status = status.NO_STATUS
        self.statusCount = 0
        self.ability_num = 0
        self.gender = gender.NO_GENDER
        self.nature = nature.NO_NATURE
        self.shiny = False
        self.moves = []
        self.item = None
        self.fused = False
        self.ivs = [0, 0, 0, 0, 0, 0]
        self.evs = [0, 0, 0, 0, 0, 0]
        self.happiness = 0
        self.ball = 0
        self.egg_steps = 0  # if 0 -> no egg
        self.poke_rus = False
        self.personalID = 0
        self.trainerID = 0
        self.obtainMap = ""
        self.obtainText = ""
        self.obtainLevel = 0
        self.hatchedMap = ""
        self.language = language.EN
        self.otName = ""  # official trainer name
        self.otGender = 3  # 0 -> male, 1 -> female, 2 -> mixed, 3 -> unknown
        self.growth_rate = ""
        self.level = 0
        self.abilities = []
        self.hidden_ability = ""
        self.types = []
        self.moves_pp = []
        self.form = 0
        self.accuracy_stat = 0
        self.evasion_stat = 0
        self.stat_stages = [0, 0, 0, 0, 0]  # -> ATK, DEF, SP_ATK, SP_DEF, SPEED
        self.evolution = ""
        self.is_drowsy = False
        self.is_confused = False
        self.is_attracted = False
        self.safeguard = False
        self.current_ability = ""

    # ==============================================================================
    # Experience / Level
    # ==============================================================================

    def set_level_by_exp(self):
        self.level = experience.get_level(self.growth_rate, self.experience)

    def set_level(self, level: int):
        if 0 < level <= settings.MAX_LEVEL:
            self.level = level
            self.experience = experience.get_exp(self.growth_rate, self.level)
        else:
            raise errors.WrongLevel(level)

    def exp_progress_bar(self) -> int:
        """

        :return: Progress bar in percentage of how much is filled.
        """
        min_exp, max_exp = experience.min_max_exp(self.growth_rate, self.level)
        exp_needed_for_lvl_up = max_exp - min_exp
        current_exp_fill = self.experience - min_exp
        return 100 * (current_exp_fill / exp_needed_for_lvl_up)

    # ==============================================================================
    # Eggs
    # ==============================================================================

    def is_egg(self) -> bool:
        if self.egg_steps < 0:
            raise errors.EggStepsLessThanZero(self.egg_steps)
        return self.egg_steps > 0

    # ==============================================================================
    # Gender
    # ==============================================================================

    def is_male(self) -> bool:
        return self.gender == gender.MALE

    def is_female(self) -> bool:
        return self.gender == gender.FEMALE

    def is_genderless(self) -> bool:
        return self.gender == gender.NO_GENDER

    def set_gender(self, _gender: str):
        if _gender in gender.GENDERS:
            self.gender = _gender
        else:
            raise errors.GenderError(_gender)

    # ==============================================================================
    # Ability
    # ==============================================================================

    def get_ability(self) -> str:
        if self.current_ability != "":
            return self.current_ability
        #print(self.ability_num)
        if self.ability_num >= 2:
            return self.hidden_ability
        return self.abilities[self.ability_num]

    def has_ability(self, ability: str) -> bool:
        return ability == self.get_ability() or ability == self.current_ability

    def has_hidden_ability(self) -> bool:
        return self.ability_num >= 2

    def get_ability_list(self) -> list:
        return self.abilities

    def make_ability_hidden(self):
        self.ability_num = 2

    def change_ability(self, ability_num: int):
        self.ability_num = ability_num

    def debug_ability_set(self, ability_name):
        self.current_ability = ability_name

    # ==============================================================================
    # Nature
    # ==============================================================================

    def set_nature(self, _nature: str):
        if _nature in nature.NATURES:
            self.nature = _nature

    def has_nature(self, _nature: str) -> bool:
        return self.nature == _nature

    # ==============================================================================
    # Shiny
    # ==============================================================================

    def is_shiny(self) -> bool:
        return self.shiny

    def make_shiny(self):
        self.shiny = True

    def make_not_shiny(self):
        self.shiny = False

    # ==============================================================================
    # Poke rus
    # ==============================================================================

    def give_poke_rus(self):
        self.poke_rus = True

    def has_poke_rus(self) -> bool:
        return self.poke_rus

    # ==============================================================================
    # Types
    # ==============================================================================

    def get_type_1(self) -> str:
        if type(self.types) == list or type(self.types) == tuple:
            return self.types[0]
        else:
            return self.types

    def get_type_2(self) -> str or None:
        if len(self.types) == 2:
            return self.types[1]
        else:
            return None

    def set_types(self, type1: str, type2: str = None):
        if type1 in _types.TYPES and (type2 in _types.TYPES or type2 is None):
            if type2 is None:
                self.types = type1
            else:
                self.types = type1, type2

    def has_type(self, _type: str) -> bool:
        return _type in self.types

    # ==============================================================================
    # Moves
    # ==============================================================================

    def count_moves(self) -> int:
        return len(self.moves)

    def has_move(self, _move) -> bool:
        return _move in self.moves

    def get_move_list(self) -> list:
        return self.moves

    def move_pool(self) -> list:
        return species.learn_set(self.species)

    def learn_move(self, move: str):
        if move in moves.MOVES:
            if self.count_moves() == 4:
                self.moves[0] = move
            else:
                self.moves.append(move)

    def delete_move(self, move: str):
        if move in self.moves:
            self.moves.remove(move)

    def delete_all_moves(self):
        self.moves = []

    def set_moves(self, _moves: list):
        for move in _moves:
            if move not in moves.MOVES and move.internal_name not in moves.MOVES:
                raise errors.InvalidMoveArgument(move)
        self.moves = _moves

    # ==============================================================================
    # Items
    # ==============================================================================

    def has_item(self, item: str) -> bool:
        return self.item == item

    def set_item(self, item: str):
        if item in items.ITEMS or item is None:
            self.item = item
        else:
            #print(items.CHOICE_BAND)
            raise errors.WrongItem(item)

    def give_item(self, item: str):
        """
        Basically set_item but throws
        :param item:
        :return:
        """
        if item in items.ITEMS:
            if self.item is None:
                self.item = item
            else:
                if self.nickname == "":
                    raise errors.PokemonHasItem(self.get_species_name())
                else:
                    raise errors.PokemonHasItem(self.nickname)

    def take_item(self):
        if self.item is not None:
            bag.add_to_bag(self.item)
            self.item = None

    def is_holding_item(self) -> bool:
        return self.item is not None

    # ==============================================================================
    # Name / Language
    # ==============================================================================

    def get_species_name(self) -> str:
        return species.name(self.species)

    def has_nickname(self) -> bool:
        return self.nickname == self.get_species_name()

    def get_language(self) -> str:
        return self.language

    # ==============================================================================
    # Dex Data
    # ==============================================================================

    def get_dex_height(self) -> int:
        return species.dex_height(self.species)

    def get_dex_weight(self) -> int:
        return species.dex_weight(self.species)

    # ==============================================================================
    # Stats / fainted
    # ==============================================================================

    def get_ev_yield(self) -> [str, int]:
        return species.ev_yield(self.species)

    def set_current_hp(self, hp: int):
        self.hp = hp
        if self.hp == 0:
            self.status = status.NO_STATUS
            self.statusCount = 0

    def is_fainted(self) -> bool:
        return self.is_egg() or self.hp == 0

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    # ==============================================================================
    # Heal
    # ==============================================================================

    def heal_hp(self, n: int):
        if self.hp + n > self.total_hp:
            self.hp = self.total_hp
        else:
            self.hp += n

    def full_heal_hp(self):
        self.hp = self.total_hp

    def heal_status(self):
        self.status = status.NO_STATUS
        self.statusCount = 0

    def heal_pp(self, move_index: int, n: int):
        if move_index > self.count_moves():
            raise errors.MoveIndexError(move_index, self.moves)
        else:
            if self.moves_pp[move_index] + n > moves.get_max_pp(self.moves[move_index]):
                self.moves_pp[move_index] = moves.get_max_pp(self.moves[move_index])
            else:
                self.moves_pp[move_index] += n

    def fully_heal_pp(self, move_index: int):
        if move_index > self.count_moves():
            raise errors.MoveIndexError(move_index, self.moves)
        else:
            self.moves_pp[move_index] = moves.get_max_pp(self.moves[move_index])

    def fully_heal_all_pp(self):
        for i in range(self.count_moves()):
            try:
                self.fully_heal_pp(i + 1)
            except IndexError:
                continue

    def heal(self):
        self.full_heal_hp()
        self.fully_heal_all_pp()

    def get_hp_percentage(self) -> int:
        return round(round(self.hp / self.total_hp, ndigits=2) * 100)

    # ==============================================================================
    # Happiness
    # ==============================================================================

    def change_happiness(self, value: int):
        self.happiness += value

    # ==============================================================================
    # Calculations
    # ==============================================================================

    def get_base_stats(self) -> list:
        return species.base_stats(self.species)

    def calc_hp(self) -> int:
        if self.get_base_stats()[0] == 1:
            return 1  # Shedinja
        return round(((2 * self.get_base_stats()[0] + self.ivs[0] + (round(self.evs[0]) / 4)) * self.level) / 100 - 0.499) + self.level + 10

    @staticmethod
    def calc_stat(base: int, ev: int, iv: int, nature_factor: int, level: int) -> int:
        return round(round(((2 * base + iv + round(ev / 4)) * level) / 100 + 5 - 0.499) * nature_factor - 0.499)

    def calc_stats(self):
        old_total = self.total_hp  # to add hp to a pokemon
        self.total_hp = self.calc_hp()
        hp_boost = self.total_hp - old_total
        self.hp += hp_boost
        if self.hp < 1:
            self.hp = 1  # preventing faint from po meg berries
        self.attack = self.calc_stat(self.get_base_stats()[1], self.evs[1], self.ivs[1],
                                     nature.nature_factor("Attack", self.nature), self.level)
        self.defense = self.calc_stat(self.get_base_stats()[2], self.evs[2], self.ivs[2],
                                      nature.nature_factor("Defense", self.nature), self.level)
        self.sp_atk = self.calc_stat(self.get_base_stats()[3], self.evs[3], self.ivs[3],
                                     nature.nature_factor("SpAtk", self.nature), self.level)
        self.sp_def = self.calc_stat(self.get_base_stats()[4], self.evs[4], self.ivs[4],
                                     nature.nature_factor("SpDef", self.nature), self.level)
        self.speed = self.calc_stat(self.get_base_stats()[5], self.evs[5], self.ivs[5],
                                    nature.nature_factor("Speed", self.nature), self.level)

    # ==============================================================================
    # Forms
    # ==============================================================================

    def get_form(self) -> int:
        return self.form

    def set_form(self, form: int):
        self.form = form

    # ==============================================================================
    # Evasion / Accuracy
    # ==============================================================================

    def get_evasion(self) -> int:
        evasion_table = {-6: 3/9, -5: 3/8, -4: 3/7, -3: 3/6, -2: 3/5, -1: 3/4, 0: 1, 1: 4/3, 2: 5/3, 3: 6/3, 4: 7/3, 5: 8/3, 6: 9/3}
        return evasion_table[self.evasion_stat]

    def get_accuracy(self) -> int:
        accuracy_table = {-6: 3/9, -5: 3/8, -4: 3/7, -3: 3/6, -2: 3/5, -1: 3/4, 0: 1, 1: 4/3, 2: 5/3, 3: 6/3, 4: 7/3, 5: 8/3, 6: 9/3}
        return accuracy_table[self.accuracy_stat]

    def change_evasion(self, change: int):
        self.evasion_stat += change
        if self.evasion_stat > 6:
            self.evasion_stat = 6
        if self.evasion_stat < 6:
            self.evasion_stat = -6

    def change_accuracy(self, change: int):
        self.accuracy_stat += change
        if self.accuracy_stat > 6:
            self.accuracy_stat = 6
        if self.accuracy_stat < 6:
            self.accuracy_stat = -6


    def can_evolve(self) -> bool:
        return self.evolution == ""

    def get_evolution_species(self) -> str:
        return self.evolution

    def evolves_into_species(self, _species: str):
        if _species in "Allspecies": # TODO!
            self.evolution = _species

    # ==============================================================================
    # Create a new Pokemon
    # ==============================================================================

    @staticmethod
    def create_new_pokemon(_species: int, level: int, nickname: str = ""):
        pokemon = Pokemon()
        pokemon.species = _species
        pokemon.dex_entry = species.dex_entry(_species)
        pokemon.growth_rate = species.growth_rate(_species)
        pokemon.set_level(level)
        if nickname != "":
            pokemon.nickname = nickname
        pokemon.calc_stats()
        #print(pokemon.species, "THE MON")
        #pokemon.set_moves(species.moves(_species, level))
        pokemon.abilities = species.abilities(_species)
        pokemon.hidden_ability = species.hidden_ability(_species)
        if len(species.types(_species)) == 2:
            pokemon.set_types(species.types(_species)[0], species.types(_species)[1])
        else:
            pokemon.set_types(species.types(_species)[0])
        pokemon.heal()
        return pokemon

EmptyPokemon = Pokemon()