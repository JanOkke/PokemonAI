from pokemon import Pokemon, EmptyPokemon
from errors import TeamSlotError, EmptyPartyError


class Team:
    def __init__(self):
        self.pokemons = {1: EmptyPokemon, 2: EmptyPokemon, 3: EmptyPokemon, 4: EmptyPokemon, 5: EmptyPokemon,
                         6: EmptyPokemon}

    def add_pokemon(self, pokemon: Pokemon, slot=None):
        if slot is not None:
            if 0 < slot < 7:
                self.pokemons[slot] = pokemon
            else:
                raise TeamSlotError(slot)
        else:
            for index in range(6):
                if self.pokemons[index + 1] == EmptyPokemon:
                    self.pokemons[index + 1] = pokemon
                    break

    def get_pokemon(self, slot: int) -> Pokemon:
        return self.pokemons[slot]

    def get_party(self) -> [Pokemon]:
        ret = []
        for index in range(6):
            if self.pokemons[index + 1] == EmptyPokemon:
                break
            else:
                ret.append(self.pokemons[index + 1])
        return ret

    def get_team_length(self) -> int:
        party_len = 0
        for index in range(6):
            if self.pokemons[index + 1] == EmptyPokemon:
                break
            else:
                party_len += 1
        return party_len

    def get_first_pokemon(self) -> Pokemon:
        if self.pokemons[1] == EmptyPokemon:
            raise EmptyPartyError
        else:
            return self.pokemons[1]

    def contains_typing(self, typing: str) -> bool:
        for mon in self.get_party():
            if mon.has_type(typing):
                return True
        return False

    def get_all_mons_with_typing(self, typing: str) -> [Pokemon]:
        ret = []
        for mon in self.get_party():
            if mon.has_type(typing):
                ret.append(mon)
        return ret


EmptyTeam = Team()
