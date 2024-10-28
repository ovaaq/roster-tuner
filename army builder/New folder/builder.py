from InquirerPy import prompt
import pandas as pd
import os
from InquirerPy.validator import EmptyInputValidator
import json
from types import SimpleNamespace
from collections import namedtuple
from json import JSONEncoder
import time
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.console import Group

from rich.console import Console
from rich.markdown import Markdown

army_list = {}
army_list["points"] = 0
army_list["enhancements"] = []
army_list["warlord_selected"] = False
army_list["characters"] = []
army_list["battleline"] = []
army_list["epic heroes"] = []

files = os.listdir()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

for file in files:
    if ".json" in file:
        str_file = open(file, 'r').read()
        data = json.loads(str_file, object_hook=customStudentDecoder)

def get_units():
    tmp_return = """
"""
    for unit_type in ["characters","battleline"]:
        for index,item in enumerate(army_list.get(unit_type)):
            addition = 0
            if index == 0 and unit_type == "battleline":
                addition = len(army_list.get("characters"))
            tmp = "#" + str(index + 1 + addition) + " " + str(item[0]) +""" ("""+ str(item[1]) + """ Points) |
--- |
"""
            for wargear in item[2]:
                if wargear == "warlord":
                    tmp = tmp + wargear + """ |
"""
                else:
                    tmp = tmp + """1x """ + wargear + """ |
"""
            tmp_return = tmp_return + tmp + """
"""
    return tmp_return
    
def get_enhancements(keywords):
    tmp_list = []
    for faction in data.general.factions:
        if faction[0] == army_list.get("faction"):
            for enhancement in faction[2]:
                add = False
                for keyword in enhancement[4]:
                    if keyword in keywords:
                        add = True
                if add and (army_list["size"]- army_list["points"] >= enhancement[1]) and (enhancement[0] not in army_list.get("enhancements")):
                    tmp = enhancement[0] + " (" + str(enhancement[1]) + " Points)"
                    tmp_list.append(tmp)
    return tmp_list

def get_selected_list(selection_type):
    tmp_list = []
    loop_list = ["characters","battleline"]
    cannot_warlord = ["vindicare assassin","culexus assassin", "eversor assassin", "calidus assassin"]

    if selection_type in ["warlord", "enhancements"]:
        loop_list = ["characters"]
    
    cannot_enhancement = []
    if selection_type == "enhancements":
        for index,item in enumerate(army_list.get("characters")):
            if len(get_enhancements(get_unit_keywords(item[0]))) == 0:
                cannot_enhancement.append(index)

    for unit_type in loop_list:
        for index,item in enumerate(army_list.get(unit_type)):
            addition = 1
            if unit_type == "battleline":
                addition = len(army_list.get("characters")) + 1
            if selection_type=="delete" or (selection_type=="enhancements" and not is_epic_hero(item[0]) and len(army_list.get("enhancements")) < 1 and not "enhancement:%" in item[2] and index not in cannot_enhancement) or (selection_type=="warlord" and item[0] not in cannot_warlord):
                x = "#" + str(index + addition) + " " + str(item[0]) +" ("+ str(item[1])+" Points)"
                tmp_list.append(x)
    return tmp_list

def get_battleline():
    if len(army_list.get("battleline")) == 0:
        return """"""
    else:
        tmp_return = """     BATTLELINE


"""

        for item in army_list.get("battleline"):
            tmp = str(item[0]) +""" ("""+ str(item[1]) + """ Points) |
--- |
"""
            for wargear in item[2]:
                tmp = tmp + """1x """ + wargear + """ |
"""
            tmp_return = tmp_return + tmp + """
"""
        return tmp_return

def get_units_with_values(faction_name, max_cost):
    tmp= []
    faction_names = get_possible_unit_factions(faction_name)
    for item in data.units:
        same_character_count = [x[0] for x in army_list.get("characters")].count(item[0])
        same_battleline_count = [x[0] for x in army_list.get("battleline")].count(item[0])
        if(item[9][0] in faction_names and item[0] not in army_list.get("epic heroes") and item[1] <= int(max_cost) and same_character_count < 2 and same_battleline_count < 6 ):
            tmp.append(str(item[0]) + " (" + str(item[1]) + " Points)")
    return tmp
 
def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

def has_options(unit_name):
    for x in data.units:
        if x.name == unit_name:
                if len(x.wargear.options) > 0:
                    return True
    return False

def is_character(unit_name):
    for x in data.units:
        if x.name == unit_name:
            if "character" in x.keywords:
                return True
    return False 
    
def is_epic_hero(unit_name):
    for x in data.units:
        if x.name == unit_name:
            if "epic hero" in x.keywords:
                return True
    return False 
    
def is_warlord(unit_name):
    return False 
    
def get_warlord_potentials():
    character_list = [str(item[0]) for item in army_list.get("characters")]
    cannot_warlord = ["vindicare assassin","culexus assassin", "eversor assassin", "callidus assassin"]
    return [x for x in character_list if x not in cannot_warlord]
    

def get_wargear_options(unit_name):
    for x in data.units:
        if x.name == unit_name:
            return x.wargear.options
    return []
  
def get_given_wargear(unit_name):
    for x in data.units:
        if x.name == unit_name:
            return x.wargear.always
    return [] 
    
def has_detachment_options(faction):
    return False
    
def get_detachment_rule(faction):
    for item in data.general.factions:
        if item[0] == faction:
            return item[1][0]
    return None

def get_factions():
    return [str(item[0]) for item in data.general.factions]
    
def get_possible_unit_factions(faction_name):
    if faction_name == "imperial knights":
        return ["imperial knights","agents of the imperium"]
    else:
        return []
        
def get_unit_keywords(unit_name):
    for x in data.units:
        if x.name == unit_name:
            return x.keywords
    return []

def get_potential_enhancements(unit_keywords, faction):
    return []
    
    
def deselect_warlord():
    for character in army_list["characters"]:
        if "warlord" in character[2]:
            character[2].remove("warlord")
    return None

def get_army_list():
    warnings = """"""
    if len(army_list.get("characters")) < 1:
        warnings = warnings + """
* *You must have at least one character*
"""
    if not army_list.get("warlord_selected"):
        warnings = warnings + """* *You must have a warlord*
"""
    warnings = warnings + """

"""

    return """""" + army_list.get("name") + """ (""" + str(army_list.get("points")) + """/"""+ str(army_list.get("size")) +""" Points) |
--- |
Faction: """+army_list.get("faction")+""" |
Detachment rule: """+army_list.get("detachment")+""" |
""" + get_units()


# ARMY FACTION
q_faction = prompt({
        "type": "list",
        "message": "Army faction:",
        "choices": get_factions(),
    })
army_list["faction"] = q_faction[0]

if has_detachment_options(army_list.get("faction")):
    # ARMY DETACHMENT RULE
    q_faction = prompt({
            "type": "list",
            "message": "Detachment rules:",
            "choices": data.general.factions,
        })
else:
    army_list["detachment"] = get_detachment_rule(army_list.get("faction"))

# ARMY LIST NAME
q_name = prompt({"type": "input", "message": "Roster name:"})
army_list["name"] = q_name[0]

# ARMY SIZE
q_size = prompt({
        "type": "list",
        "message": "Battle size:",
        "choices": ["1000", "2000", "3000", "Other"],
    })
if q_size[0] == "Other":
    q_size_other = prompt({
            "type": "number",
            "message": "Custom size:",
            "min_allowed": 1,
            "max_allowed": 10000,
            "validate": EmptyInputValidator(),
    })
    army_list["size"] = q_size_other[0]
else:
    army_list["size"] = int(q_size[0])

console = Console()

while True:
    cls()
    MARKDOWN = get_army_list()
    md = Markdown(MARKDOWN)
    console.print(md)
    
    units = get_units_with_values(army_list.get("faction"), army_list["size"]- army_list["points"])
    warlord_potentials = get_selected_list("warlord")  
    enhancement_potentials = get_selected_list("enhancements")
    choices = []
    if len(units) > 0:
        choices.append("Add unit")
    if len(army_list.get("characters")) > 0 or len(army_list.get("battleline")) > 0:
        choices.append("Delete unit")
    if len(warlord_potentials) > 0 and not army_list.get("warlord_selected"):
        choices.append("Select warlord")
    if len(warlord_potentials) > 1 and army_list.get("warlord_selected"):
        choices.append("Reselect warlord")
    if len(enhancement_potentials) > 0:
        choices.append("Add enhancements")
    
    q_update = prompt({
            "type": "list",
            "message": "",
            "choices": choices,
        })
    if q_update[0] == "Add unit":
        q_update = prompt({
            "type": "list",
            "message": "Select unit",
            "choices": units
        })
        temp_unit = q_update[0].split(" (")[0]
        temp_unit_cost = int(q_update[0].split(" (")[1].split(" P")[0])
        temp_unit_wargear = []
        temp_unit_wargear.extend(get_given_wargear(temp_unit))
        if has_options(temp_unit):
            wargear_option_list = get_wargear_options(temp_unit)
            for option in wargear_option_list:
                q_update = prompt({
                    "type": "list",
                    "message": "Select one",
                    "choices": option
                })
                if " & " in q_update[0]:
                    two_weapons = q_update[0].split(" & ")
                    for weapon in two_weapons:
                        temp_unit_wargear.append(weapon)
                else:
                    temp_unit_wargear.append(q_update[0])
            
        army_list["points"] = army_list["points"] + temp_unit_cost
        if is_character(temp_unit):
            army_list["characters"].append([temp_unit,temp_unit_cost, temp_unit_wargear])
        else:
            army_list["battleline"].append([temp_unit,temp_unit_cost, temp_unit_wargear])
        
        if is_epic_hero(temp_unit):
            army_list["epic heroes"].append(temp_unit)

    elif q_update[0] in ["Select warlord", "Reselect warlord"]:
        if q_update[0] == "Reselect warlord":
            deselect_warlord()
        q_update = prompt({
            "type": "list",
            "message": "Select warlord",
            "choices": get_selected_list("warlord")
        })
        index = int(q_update[0].split(" ")[0].split("#")[1]) -1
        army_list["characters"][index][2].append("warlord")
        army_list["warlord_selected"] = True
        
    elif q_update[0] == "Delete unit":
        q_update = prompt({
            "type": "list",
            "message": "Delete unit",
            "choices": get_selected_list("delete")
        })
        index = int(q_update[0].split(" ")[0].split("#")[1]) -1
        cost = int(q_update[0].split("(")[1].split(" P")[0])
        name = q_update[0].split(" (")[0].split(" ", 1)[1]
        army_list["points"] = army_list["points"] - cost
        if index < len(army_list.get("characters")):
            if(is_epic_hero(name)):
                army_list["epic heroes"].remove(name)
            if "warlord" in army_list.get("characters")[index][2]:
                army_list["warlord_selected"] = False
            del army_list["characters"][index]
        else:
            index = index - len(army_list.get("characters"))
            del army_list["battleline"][index]

    elif q_update[0] == "Add enhancements":
        q_update = prompt({
            "type": "list",
            "message": "Select character for enhancement",
            "choices": get_selected_list("enhancements")
        })
        name = q_update[0].split(" (")[0].split(" ", 1)[1]
        unit_keywords = get_unit_keywords(name)
        index = int(q_update[0].split(" ")[0].split("#")[1]) -1
        tmp = q_update[0]
        q_update = prompt({
            "type": "list",
            "message": "Select enhancement",
            "choices": get_enhancements(unit_keywords)
        })
        e_cost = int(q_update[0].split("(")[1].split(" P")[0])
        e_name = q_update[0].split(" (")[0].split(" ", 1)[1]
        army_list["points"] = army_list["points"] + e_cost
        text = "enhancement: " + e_name
        army_list["characters"][index][2].append(text)
        army_list["characters"][index][1] = army_list["characters"][index][1] + e_cost
        army_list["enhancements"].append(e_name)


