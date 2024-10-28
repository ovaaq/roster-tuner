import json
from collections import namedtuple


def decoder(dict_elem):
    return namedtuple('X', dict_elem.keys())(*dict_elem.values())


def is_keyword(unit, keyword):
    if keyword in unit[8]:
        return True
    return False


def get_unit_faction(unit):
    return unit[9][0]


def get_possible_unit_factions(faction):
    return_list = [faction]
    if faction == "imperial knights":
        return_list.append("agents of the imperium")
    return return_list


class Data:
    def __init__(self):
        self.factions = json.loads(open("factions.json", 'r').read(), object_hook=decoder)[0]
        self.weapons = json.loads(open("weapons.json", 'r').read(), object_hook=decoder)[0]
        self.units = json.loads(open("units.json", 'r').read(), object_hook=decoder)[0]

    def get_possible_units(self, roster):
        return_list = []
        faction_names = get_possible_unit_factions(roster.faction)
        max_cost = roster.get_remaining_points()

        for unit in self.units:
            formatted_unit = str(unit[0]) + " (" + str(unit[1]) + " Points)"
            if get_unit_faction(unit) in faction_names:
                if unit[1] <= max_cost:
                    unit_count = roster.get_same_unit_count(unit[0])
                    if is_keyword(unit, "character"):
                        if is_keyword(unit, "epic hero"):
                            if unit_count < 1:
                                return_list.append(formatted_unit)
                        else:
                            if unit_count < 1:
                                return_list.append(formatted_unit)
                    else:
                        if unit_count < 6:
                            return_list.append(formatted_unit)
        return_list.sort()
        return return_list

    def get_unit(self, unit_name):
        for unit in self.units:
            if unit_name == unit[0]:
                return unit
        return None

    def get_factions(self):
        return [str(item[0]) for item in self.factions]

    def get_detachment_rules(self, faction):
        for item in self.factions:
            if item[0] == faction:
                return item[1]
        return None

    def get_enhancements(self, roster, unit):
        return_list = []
        already_in_use = roster.get_selected_enhancements()
        for faction in self.factions:
            if faction[0] == roster.get_faction():
                for enhancement in faction[2]:
                    for keyword in unit.get_keywords():
                        if keyword in enhancement[4] and enhancement[0] not in already_in_use and enhancement[
                            1] <= roster.get_remaining_points():
                            tmp = enhancement[0] + " (" + str(enhancement[1]) + " Points)"
                            return_list.append(tmp)
        return return_list

    def get_weapon(self, weapon_name):
        for weapon in self.weapons:
            if weapon[0] == weapon_name:
                return weapon
        return "m"
