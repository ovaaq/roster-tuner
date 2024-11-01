import json
from collections import namedtuple


def decoder(dict_elem):
    return namedtuple('X', dict_elem.keys())(*dict_elem.values())


def is_keyword(unit, keyword):
    if keyword in unit[7]:
        return True
    return False


def get_unit_faction(unit):
    return unit[8][0]


def get_possible_unit_factions(faction):
    return_list = [faction]
    if faction == "imperial knights":
        return_list.append("agents of the imperium")
    return return_list


class Data:
    def __init__(self):
        self.faction_list = json.loads(open("faction_list.json", 'r').read(), object_hook=decoder)[0]
        self.unit_list = json.loads(open("unit_list.json", 'r').read(), object_hook=decoder)[0]
        self.unit_cost_list = json.loads(open("unit_cost_list.json", 'r').read(), object_hook=decoder)[0]

    def get_cost_option_list(self, tmp_unit):
        for unit_cost_options in self.unit_cost_list:
            if unit_cost_options[0] == tmp_unit[0]:
                return unit_cost_options[1]
        return []

    def cost_format(self, cost_min, cost_max):
        if cost_min == cost_max:
            return " (" + str(cost_max) + " Points)"
        return " (" + str(cost_min) + "-" + str(cost_max) + " Points)"


    def get_possible_unit_list(self, roster):
        

        return_list = []
        faction_names = get_possible_unit_factions(roster.faction)
        max_cost = roster.get_remaining_points()

        for unit in self.unit_cost_list:
            formatted_unit = str(unit[0]) + " (" + str(unit[1]) + " Points)"

            for unit_stat_tmp in self.unit_list:
                if unit_stat_tmp[0] == unit[0]:
                    unit_stat = unit_stat_tmp

                    if get_unit_faction(unit_stat) in faction_names:
                        tmp_max_cost = 0
                        tmp_min_cost = 9000
                        for unit_cost_option in unit[1]:
                            if unit_cost_option[1] <= max_cost:
                                if unit_cost_option[1] > tmp_max_cost:
                                    tmp_max_cost = unit_cost_option[1]
                                if unit_cost_option[1] < tmp_min_cost:
                                    tmp_min_cost = unit_cost_option[1]

                        formatted_unit = str(unit[0]) + self.cost_format(tmp_min_cost, tmp_max_cost)
                        unit_count = roster.get_same_unit_count(unit_stat[0])
                        if is_keyword(unit_stat, "character"):
                            if is_keyword(unit_stat, "epic hero"):
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
        for unit in self.unit_list:
            if unit_name == unit[0]:
                return unit
        return None

    def get_faction_list(self):
        return [str(item[0]) for item in self.faction_list]

    def get_detachment_rules(self, faction):
        for item in self.faction_list:
            if item[0] == faction:
                return item[1]
        return None

    def get_enhancements(self, roster, unit):
        return_list = []
        already_in_use = roster.get_selected_enhancements()
        for faction in self.faction_list:
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
