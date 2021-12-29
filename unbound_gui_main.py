import wx
import unbound_gui

import loader
import unbound_reader
import _pokemon
import battle
import weather
import terrain
import growth
import datetime

def percentage(target_hp, damage):
    return round(damage / target_hp * 100 - 0.499)



class MainFrame(unbound_gui.MainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.Calcs = []
    def start( self, event ):
        self.main_list.Clear()
        self.Calcs = []
        LEVEL_CAP = int(self.level.Value)
        ENEMY_TEAM = self.team.Value
        WEATHER = weather.NO_WEATHER
        TERRAIN = terrain.NO_TERRAIN

        LEGENDARY_POKEMON = ['Articuno', 'Zapdos', 'Moltres', 'Mewtwo', 'Entei', 'Suicune', 'Raikou', 'Ho-Oh', 'Lugia',
                             'Regice', 'Registeel', 'Regirock', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza',
                             'Deoxys', 'Uxie',
                             'Mesprit', 'Azelf', 'Palkia', 'Dialga', 'Giratina', 'Cresselia', 'Darkrai', 'Heatran',
                             'Regigigas', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Thundurus', 'Landorus',
                             'Zekrom', 'Reshiram',
                             'Kyurem', 'Xerneas', 'Yveltal', 'Zygarde', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu',
                             'Tapu Fini', 'Solgaleo', 'Lunala', 'Necrozma', 'Zacian', 'Zamazenta', 'Eternatus', 'Kubfu',
                             'Urshifu', 'Regieleki',
                             'Regidrago', 'Glastrier', 'Spectrier', 'Calyrex', 'Mew', 'Celebi', 'Jirachi', 'Manaphy',
                             'Phione', 'Shaymin', 'Arceus', 'Victini', 'Keldeo', 'Meloetta', 'Genesect', 'Diancie',
                             'Hoopa', 'Volcanion',
                             'Magearna', 'Marshadow', 'Zeraora', 'Meltan', 'Melmetal', 'Zarude']
        OHKO_MOVES = ['Fissure', 'Guillotine', 'Sheer Cold', 'Horn Drill']

        special_mon = False
        for pkmn in _pokemon.ALL_POKEMON:
            if ENEMY_TEAM == pkmn.get_species_name():
                special_mon = True
                print("Found", ENEMY_TEAM)
                pkmn.growth_rate = growth.MEDIUM_SLOW  # DEBUG
                pkmn.set_level(LEVEL_CAP)
                pkmn.heal()
                pkmn.calc_stats()
                enemies = [pkmn]
        if not special_mon:
            enemies = (loader.load_from_poke_paste(open(ENEMY_TEAM)))
        print("Started Calculations - ", datetime.datetime.now())
        for enemy in enemies:
            if self.enemyiv.IsChecked():
                enemy.ivs = [31, 31, 31, 31, 31, 31]
            if self.enemyev.IsChecked():
                enemy.evs = [252, 252, 252, 252, 252, 252]
            enemy.calc_stats()
            # print(enemy.get_species_name(),enemy.hp,enemy.attack,enemy.defense,enemy.sp_atk,enemy.sp_def,enemy.speed, enemy.level)
            for pokemon in _pokemon.ALL_POKEMON:
                if pokemon.get_species_name() in LEGENDARY_POKEMON:
                    continue
                pokemon.growth_rate = growth.MEDIUM_SLOW  # DEBUG
                pokemon.set_level(LEVEL_CAP)
                pokemon.heal()
                if self.useriv.IsChecked():
                    pokemon.ivs = [31, 31, 31, 31, 31, 31]
                if self.userev.IsChecked():
                    pokemon.evs = [252, 252, 252, 252, 252, 252]
                pokemon.calc_stats()
                # print(pokemon.get_species_name(),pokemon.hp,pokemon.attack,pokemon.defense,pokemon.sp_atk,pokemon.sp_def,pokemon.speed, pokemon.level)
                available_moves = unbound_reader.available_level_up_moves(pokemon.get_species_name(), LEVEL_CAP)
                for move in available_moves:
                    if move.name in OHKO_MOVES:
                        continue
                    min_roll = battle.calculate_damage(pokemon, enemy, WEATHER, TERRAIN, move, can_crit=False,
                                                  printing=False, rand_num=85)
                    max_roll = battle.calculate_damage(pokemon, enemy, WEATHER, TERRAIN, move, can_crit=False,
                                                  printing=False, rand_num=100)
                    if percentage(enemy.total_hp, max_roll) < 30:
                        continue
                    self.Calcs.append([pokemon.get_species_name(), percentage(enemy.total_hp, min_roll), percentage(enemy.total_hp, max_roll),
                                  '{1} (Lv {4}) deals {0}/{6} ({7}%) - {8}/{6} ({9}%) damage to {2} (Lv {5}) with move {3}'.format(
                                      min_roll, pokemon.get_species_name(), enemy.get_species_name(), move.name, LEVEL_CAP,
                                      enemy.level, enemy.total_hp, percentage(enemy.total_hp, min_roll), max_roll, percentage(enemy.total_hp, max_roll))])
                    self.main_list.AppendItems('{1} (Lv {4}) deals {0}/{6} ({7}%) - {8}/{6} ({9}%) damage to {2} (Lv {5}) with move {3}'.format(
                                      min_roll, pokemon.get_species_name(), enemy.get_species_name(), move.name, LEVEL_CAP,
                                      enemy.level, enemy.total_hp, percentage(enemy.total_hp, min_roll), max_roll, percentage(enemy.total_hp, max_roll)))
                    self.Update()
        print("Finished Calculations - ", datetime.datetime.now())
        #Calcs.sort(reverse=True)
        #for calc in Calcs:
            #self.main_list.AppendItems(calc[1])
        #    print(calc[1])
    def sort_user( self, event ):
        self.main_list.Clear()
        self.Calcs.sort()
        for usr, minroll, maxroll, txt in self.Calcs:
            self.main_list.AppendItems(txt)

    def sort_damage( self, event ):
        self.main_list.Clear()
        clone_of_calcs = []
        for usr, minroll, maxroll, txt in self.Calcs:
            clone_of_calcs.append([minroll,maxroll,usr,txt])
        clone_of_calcs.sort(reverse=True)
        for minroll, maxroll, usr, txt in clone_of_calcs:
            self.main_list.AppendItems(txt)



app = wx.App()
MainFrame(None).Show()
app.MainLoop()