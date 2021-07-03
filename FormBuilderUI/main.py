import FormBuilderUI.gui as gui
import wx
import battle
import items
import movedata
import species
def percentage(target_hp, damage):
    return round(damage / target_hp * 100 - 0.499)
app = wx.App()
class MainFrame(gui.CalculatorFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def calculate( self, event ):
        print("Calculating...")
        left_mon = battle.Pokemon.create_new_pokemon(species.get_dex_number(self.leftmonname.Value), int(self.leftmonlevel.Value))
        right_mon = battle.Pokemon.create_new_pokemon(species.get_dex_number(self.rightmonname.Value), int(self.rightmonlevel.Value))
        move1 = battle.Move.create_new_move(None, movedata.get_id(self.leftmonmove1.Value))
        move2 = battle.Move.create_new_move(None, movedata.get_id(self.leftmonmove2.Value))
        move3 = battle.Move.create_new_move(None, movedata.get_id(self.leftmonmove3.Value))
        move4 = battle.Move.create_new_move(None, movedata.get_id(self.leftmonmove4.Value))
        move5 = battle.Move.create_new_move(None, movedata.get_id(self.rightmonmove1.Value))
        move6 = battle.Move.create_new_move(None, movedata.get_id(self.rightmonmove2.Value))
        move7 = battle.Move.create_new_move(None, movedata.get_id(self.rightmonmove3.Value))
        move8 = battle.Move.create_new_move(None, movedata.get_id(self.rightmonmove4.Value))

        left_mon.debug_ability_set(self.leftmonability.Value)
        right_mon.debug_ability_set(self.rightmonability.Value)
        left_mon.set_item(items.get_item(self.leftmonitem.Value))
        right_mon.set_item(items.get_item(self.rightmonitem.Value))
        left_mon.moves.append(move1)
        left_mon.moves.append(move2)
        left_mon.moves.append(move3)
        left_mon.moves.append(move4)
        right_mon.moves.append(move5)
        right_mon.moves.append(move6)
        right_mon.moves.append(move7)
        right_mon.moves.append(move8)

        min_roll_1 = battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[0], rand_num=85, can_crit=False, printing=False)
        max_roll_1 =battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[0], rand_num=100, can_crit=False, printing=False)
        min_roll_2 = battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[1], rand_num=85, can_crit=False, printing=False)
        max_roll_2 =battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[1], rand_num=100, can_crit=False, printing=False)
        min_roll_3 = battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[2], rand_num=85, can_crit=False, printing=False)
        max_roll_3 =battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[2], rand_num=100, can_crit=False, printing=False)
        min_roll_4 = battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[3], rand_num=85, can_crit=False, printing=False)
        max_roll_4 =battle.calculate_damage(left_mon, right_mon, self.weather.Value, self.terrain.Value, left_mon.moves[3], rand_num=100, can_crit=False, printing=False)
        min_roll_5 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[0], rand_num=85, can_crit=False, printing=False)
        max_roll_5 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[0], rand_num=100, can_crit=False, printing=False)
        min_roll_6 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[1], rand_num=85, can_crit=False, printing=False)
        max_roll_6 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[1], rand_num=100, can_crit=False, printing=False)
        min_roll_7 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[2], rand_num=85, can_crit=False, printing=False)
        max_roll_7 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[2], rand_num=100, can_crit=False, printing=False)
        min_roll_8 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[3], rand_num=85, can_crit=False, printing=False)
        max_roll_8 = battle.calculate_damage(right_mon, left_mon, self.weather.Value, self.terrain.Value, right_mon.moves[3], rand_num=100, can_crit=False, printing=False)
        """
        output = ''
        output += left_mon.get_species_name() + "'s Moves:" + "\n"
        output += "\n"
        output += left_mon.moves[0].name + ": " + str(min_roll_1) + " - " + str(max_roll_1) + " (" + str(percentage(right_mon.hp, min_roll_1)) + "% - " + str(percentage(right_mon.hp, max_roll_1)) + "%)" + "\n"
        output += left_mon.moves[1].name + ": " + str(min_roll_2) + " - " + str(max_roll_2) + " (" + str(percentage(right_mon.hp, min_roll_2)) + "% - " + str(percentage(right_mon.hp, max_roll_2)) + "%)" + "\n"
        output += left_mon.moves[2].name + ": " + str(min_roll_3) + " - " + str(max_roll_3) + " (" + str(percentage(right_mon.hp, min_roll_3)) + "% - " + str(percentage(right_mon.hp, max_roll_3)) + "%)" + "\n"
        output += left_mon.moves[3].name + ": " + str(min_roll_4) + " - " + str(max_roll_4) + " (" + str(percentage(right_mon.hp, min_roll_4)) + "% - " + str(percentage(right_mon.hp, max_roll_4)) + "%)" + "\n"
        output += "\n"
        output += right_mon.get_species_name() + "'s Moves:" + "\n"
        output += "\n"
        output += right_mon.moves[0].name + ": " + str(min_roll_5) + " - " + str(max_roll_5) + " (" + str(percentage(left_mon.hp, min_roll_5)) + "% - " + str(percentage(left_mon.hp, max_roll_5)) + "%)" + "\n"
        output += right_mon.moves[1].name + ": " + str(min_roll_6) + " - " + str(max_roll_6) + " (" + str(percentage(left_mon.hp, min_roll_6)) + "% - " + str(percentage(left_mon.hp, max_roll_6)) + "%)" + "\n"
        output += right_mon.moves[2].name + ": " + str(min_roll_7) + " - " + str(max_roll_7) + " (" + str(percentage(left_mon.hp, min_roll_7)) + "% - " + str(percentage(left_mon.hp, max_roll_7)) + "%)" + "\n"
        output += right_mon.moves[3].name + ": " + str(min_roll_8) + " - " + str(max_roll_8) + " (" + str(percentage(left_mon.hp, min_roll_8)) + "% - " + str(percentage(left_mon.hp, max_roll_8)) + "%)" + "\n"
        self.output.SetValue(output)
        """
        self.leftside_movename1.SetLabel(left_mon.moves[0].name + ": " + str(min_roll_1) + " - " + str(max_roll_1) + " (" + str(percentage(right_mon.hp, min_roll_1)) + "% - " + str(percentage(right_mon.hp, max_roll_1)) + "%)")
        self.leftside_movename2.SetLabel(left_mon.moves[1].name + ": " + str(min_roll_2) + " - " + str(max_roll_2) + " (" + str(percentage(right_mon.hp, min_roll_2)) + "% - " + str(percentage(right_mon.hp, max_roll_2)) + "%)")
        self.leftside_movename3.SetLabel(left_mon.moves[2].name + ": " + str(min_roll_3) + " - " + str(max_roll_3) + " (" + str(percentage(right_mon.hp, min_roll_3)) + "% - " + str(percentage(right_mon.hp, max_roll_3)) + "%)")
        self.leftside_movename4.SetLabel(left_mon.moves[3].name + ": " + str(min_roll_4) + " - " + str(max_roll_4) + " (" + str(percentage(right_mon.hp, min_roll_4)) + "% - " + str(percentage(right_mon.hp, max_roll_4)) + "%)")
        self.rightside_movename1.SetLabel(right_mon.moves[0].name + ": " + str(min_roll_5) + " - " + str(max_roll_5) + " (" + str(percentage(left_mon.hp, min_roll_5)) + "% - " + str(percentage(left_mon.hp, max_roll_5)) + "%)")
        self.rightside_movename2.SetLabel(right_mon.moves[1].name + ": " + str(min_roll_6) + " - " + str(max_roll_6) + " (" + str(percentage(left_mon.hp, min_roll_6)) + "% - " + str(percentage(left_mon.hp, max_roll_6)) + "%)")
        self.rightside_movename3.SetLabel(right_mon.moves[2].name + ": " + str(min_roll_7) + " - " + str(max_roll_7) + " (" + str(percentage(left_mon.hp, min_roll_7)) + "% - " + str(percentage(left_mon.hp, max_roll_7)) + "%)")
        self.rightside_movename4.SetLabel(right_mon.moves[3].name + ": " + str(min_roll_8) + " - " + str(max_roll_8) + " (" + str(percentage(left_mon.hp, min_roll_8)) + "% - " + str(percentage(left_mon.hp, max_roll_8)) + "%)")
        print(left_mon.get_ability(), right_mon.get_ability())


MainFrame(None).Show()
app.MainLoop()