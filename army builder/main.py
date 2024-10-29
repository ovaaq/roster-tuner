import os

from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator
from md2pdf.core import md2pdf
from rich import print
from rich.console import Console
from rich.markdown import Markdown

from army import Army
from integration import Data


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def make_list_title(list_param):
    return_list = []
    for item in list_param:
        return_list.append(item.title())
    return return_list


data = Data()
roster = Army()

cls()
print("""
                                ░░██╗██╗░█████╗░██╗░░██╗
                                ░██╔╝██║██╔══██╗██║░██╔╝
                                ██╔╝░██║██║░░██║█████═╝░
                                ███████║██║░░██║██╔═██╗░
                                ╚════██║╚█████╔╝██║░╚██╗
                                ░░░░░╚═╝░╚════╝░╚═╝░░╚═╝""")
print("""
░█████╗░██████╗░███╗░░░███╗██╗░░░██╗  ██████╗░██╗░░░██╗██╗██╗░░░░░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║╚██╗░██╔╝  ██╔══██╗██║░░░██║██║██║░░░░░██╔══██╗██╔════╝██╔══██╗
███████║██████╔╝██╔████╔██║░╚████╔╝░  ██████╦╝██║░░░██║██║██║░░░░░██║░░██║█████╗░░██████╔╝
██╔══██║██╔══██╗██║╚██╔╝██║░░╚██╔╝░░  ██╔══██╗██║░░░██║██║██║░░░░░██║░░██║██╔══╝░░██╔══██╗
██║░░██║██║░░██║██║░╚═╝░██║░░░██║░░░  ██████╦╝╚██████╔╝██║███████╗██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═════╝░░╚═════╝░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝╝
""")

q = prompt({
    "type": "list",
    "message": "Select Faction:",
    "choices": make_list_title(data.get_faction_list()),
})
roster.faction = q[0].lower()

if len(data.get_detachment_rules(roster.get_faction())) > 1:
    q = prompt({
        "type": "list",
        "message": "Detachment rules:",
        "choices": make_list_title(data.get_detachment_rules(roster.get_faction())),
    })
    roster.detachment = q[0].lower()
else:
    roster.detachment = data.get_detachment_rules(roster.get_faction())[0]

q = prompt({"type": "input", "message": "Roster name:"})
roster.name = q[0]

q_size = prompt({
    "type": "list",
    "message": "Battle size:",
    "choices": ["2000", "1000", "3000", "Other"],
})
if q_size[0] == "Other":
    q_size_other = prompt({
        "type": "number",
        "message": "Custom size:",
        "min_allowed": 1,
        "max_allowed": 10000,
        "validate": EmptyInputValidator(),
    })
    roster.size = q_size_other[0]
else:
    roster.size = int(q_size[0])

console = Console()


def get_wargear_options(unit):
    return unit[9][1]


while True:
    cls()
    console.print(Markdown(roster.get_markdown()))

    choices = []
    unit_list = data.get_possible_unit_list(roster)

    if len(unit_list) > 0:
        choices.append("Add Unit")
    if len(roster.get_unit_list()) > 0:
        choices.append("Delete Unit")
    if len(roster.get_selectable_unit_list("enhancement")):
        choices.append("Add Enhancements")
    if len(roster.get_selectable_unit_list("warlord")) > 0 and roster.get_warlord() is None:
        choices.append("Select Warlord")
    if len(roster.get_selectable_unit_list("warlord")) > 0 and roster.get_warlord() is not None:
        choices.append("Change Warlord")
    if roster.is_legit_roster():
        choices.append("Export Roster")

    choices.append("Rename Roster")
    choices.append("Restart")
    choices.append("Quit")

    q = prompt({
        "type": "list",
        "message": "",
        "choices": choices,
    })

    if q[0] == "Quit":
        break

    elif q[0] == "Add Unit":
        q = prompt({
            "type": "list",
            "message": "Select unit",
            "choices": (unit_list)
        })
        tmp_unit = data.get_unit(q[0].split(" (")[0])

        tmp_cost = 0

        wargear_options = get_wargear_options(tmp_unit)
        selected_wargear = []
        if len(wargear_options) > 0:
            selected_wargear = []
            for option in wargear_options:
                q = prompt({
                    "type": "list",
                    "message": "Select one",
                    "choices": (option)
                })
                if " & " in q[0]:
                    two_weapons = q[0].split(" & ")
                    for weapon in two_weapons:
                        selected_wargear.append(weapon.lower())
                else:
                    selected_wargear.append(q[0].lower())
        roster.add_unit(tmp_unit, tmp_cost, selected_wargear)

    elif q[0] == "Delete Unit":
        q = prompt({
            "type": "list",
            "message": "Delete unit",
            "choices": roster.get_selectable_unit_list("delete")
        })
        index = int(q[0].split(" ")[0].split("#")[1]) - 1
        roster.delete_unit(index)

    elif q[0] == "Add Enhancements":
        q = prompt({
            "type": "list",
            "message": "Select Unit",
            "choices": (roster.get_selectable_unit_list("enhancement"))
        })
        index = int(q[0].split(" ")[0].split("#")[1])
        tmp_unit = roster.get_enhacement_unit(index)
        q = prompt({
            "type": "list",
            "message": "Select Enhancement",
            "choices": (data.get_enhancements(roster, tmp_unit))
        })
        e_cost = int(q[0].split("(")[1].split(" P")[0])
        e_name = q[0].split(" (")[0]
        tmp_unit.set_enhancement(e_name, e_cost)

    elif q[0] in ["Select Warlord", "Change Warlord"]:
        q = prompt({
            "type": "list",
            "message": "Select Warlord",
            "choices": (roster.get_selectable_unit_list("warlord"))
        })
        roster.remove_warlord_status()
        index = int(q[0].split(" ")[0].split("#")[1])
        tmp_unit = roster.get_warlord_unit(index)
        tmp_unit.make_warlord()

    elif q[0] == "Export Roster":
        name = str(roster.get_points()) + "_" + roster.get_name()
        name = name.replace(" ", "_")
        with open('docs/' + name + '.md', 'w') as f:
            f.write(roster.get_markdown())

        md2pdf(pdf_file_path='docs/' + name + '.pdf',
               md_file_path='docs/' + name + '.md',
               css_file_path='style.css')

    elif q[0] == "Rename Roster":
        pass

    elif q[0] == "Restart":
        pass
