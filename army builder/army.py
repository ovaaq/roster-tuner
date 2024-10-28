from integration import Data
from unit import Unit


class Army:
    def __init__(self):
        self.size = 0
        self.units = []
        self.faction = ""
        self.name = ""
        self.detachment = ""
        self.data = Data()

    def get_faction(self):
        return self.faction

    def add_unit(self, unit, selected_wargear):
        tmp_unit = Unit(unit, selected_wargear)
        self.units.append(tmp_unit)

    def get_same_unit_count(self, unit_name):
        count = 0
        for unit in self.units:
            if unit.get_name() == unit_name:
                count = + 1
        return count

    def get_units(self, keyword="all", not_keyword=""):
        if keyword == "all":
            return_list = []
            for unit in self.units:
                if not_keyword not in unit.get_keywords():
                    return_list.append(unit)
        else:
            return_list = []
            for unit in self.units:
                if keyword in unit.get_keywords() and not_keyword not in unit.get_keywords():
                    return_list.append(unit)
        return return_list

    def get_warlord(self):
        for unit in self.units:
            if unit.get_warlord_status():
                return unit
        return None

    def get_points(self):
        total = 0
        for unit in self.units:
            total = total + unit.get_cost()
        return total

    def get_remaining_points(self):
        total = 0
        for unit in self.units:
            total = total + unit.get_cost()
        return self.size - total

    def get_enhancements(self):
        return []

    def get_markdown(self):
        return_string = """# """ + self.name + """
""" + """ (""" + str(self.get_points()) + """/""" + str(self.size) + """ Points) |
--- |
Faction: """ + self.faction.title() + """ |
Detachment rule: """ + self.detachment.title() + """ |
"""
        index = 1
        if len(self.get_units("character")) > 0:
            return_string = return_string + """
### CHARACTERS
        
"""
        for unit in self.get_units("character"):
            tmp_unit = "(" + str(index) + ") " + str(unit.get_name()).title() + """ (""" + str(unit.get_cost()) + """ Points) |
--- |
"""
            for wargear in unit.get_wargear():
                tmp_unit = tmp_unit + """1x """ + wargear.title() + """ |
"""
            if unit.get_enhancement() != "":
                tmp_unit = tmp_unit + """Enhancement: """ + unit.get_enhancement().title() + """ |
"""
            if unit.get_warlord_status():
                tmp_unit = tmp_unit + """Warlord""" + """ |
"""
            tmp_unit = tmp_unit + """""" + """ |
"""
            return_string = return_string + tmp_unit + """
"""
            index = index + 1

        if len(self.get_units("battleline")) > 0:
            return_string = return_string + """
### BATTLELINE
        
"""

        for unit in self.get_units("battleline"):
            tmp_unit = "(" + str(index) + ") " + str(unit.get_name()).title() + """ (""" + str(unit.get_cost()) + """ Points) |
--- |
"""
            for wargear in unit.get_wargear():
                tmp_unit = tmp_unit + """1x """ + wargear.title() + """ |
"""
            tmp_unit = tmp_unit + """""" + """ |
"""
            return_string = return_string + tmp_unit + """
"""
            index = index + 1

        return return_string

    def delete_unit(self, index):
        del self.units[index]

    def get_selectable_units(self, selection_type):
        return_list = []
        index = 1
        if selection_type == "delete":
            for unit in self.get_units():
                tmp_unit = "#" + str(index) + " " + str(unit.get_name())
                return_list.append(tmp_unit)
                index = index + 1
        elif selection_type == "enhancement":
            for unit in self.get_units("character", "epic hero"):
                if unit.get_enhancement() == "" and len(self.data.get_enhancements(self, unit)):
                    tmp_unit = "#" + str(index) + " " + str(unit.get_name())
                    return_list.append(tmp_unit)
                    index = index + 1
        elif selection_type == "warlord":
            cannot_warlord = ["vindicare assassin", "culexus assassin", "eversor assassin", "calidus assassin"]
            for unit in self.get_units("character"):
                if not unit.get_warlord_status() and not unit.get_name() in cannot_warlord:
                    tmp_unit = "#" + str(index) + " " + str(unit.get_name())
                    return_list.append(tmp_unit)
                    index = index + 1
        return return_list

    def get_enhacement_unit(self, index):
        count = 1
        for unit in self.get_units("character", "epic hero"):
            if unit.get_enhancement() == "" and len(self.data.get_enhancements(self, unit)) > 0:
                if count == index:
                    return unit
                count = count + 1
        return None

    def get_warlord_unit(self, index):
        count = 1
        for unit in self.get_units("character"):
            cannot_warlord = ["vindicare assassin", "culexus assassin", "eversor assassin", "calidus assassin"]
            for unit in self.get_units("character"):
                if not unit.get_warlord_status() and not unit.get_name() in cannot_warlord:
                    if count == index:
                        return unit
                    count = count + 1
        return None

    def remove_warlord_status(self):
        if self.get_warlord() is not None:
            self.get_warlord().remove_warlord_status()

    def is_legit_roster(self):
        if self.get_warlord() is not None and len(self.get_units("character")) > 0:
            return True
        return False

    def get_selected_enhancements(self):
        return_list = []
        for unit in self.units:
            if unit.get_enhancement() != "":
                return_list.extend(unit.get_enhancement())
        return return_list

    def get_name(self):
        return self.name

    def get_all_different_weapons(self):
        return_list = []
        for unit in self.units:
            for weapon in unit.get_wargear():
                if weapon not in return_list:
                    tmp = self.data.get_weapon(weapon)
                    return_list.append(tmp)
        return_list.sort()
        return return_list
