class Unit:
    def __init__(self, data, tmp_cost=0, wargear=[], size=1):
        self.unit_size = size
        self.enhancement = ""
        self.name = data[0]
        self.is_warlord = False
        self.cost = int(tmp_cost)
        wargear.extend(data[9][0])
        self.wargear = wargear
        self.wargear.sort()
        self.keywords = data[7]

    def get_cost(self):
        return self.cost

    def get_keywords(self):
        return self.keywords

    def get_name(self):
        return self.name

    def get_wargear(self):
        #        return_list = []
        #       return_list.extend(unit[0][10][0])
        #      return_list.extend(unit[1])
        #     return_list.sort()
        return self.wargear

    def get_enhancement(self):
        return self.enhancement

    def set_enhancement(self, name, cost):
        self.cost = self.cost + cost
        self.enhancement = name

    def get_warlord_status(self):
        return self.is_warlord

    def make_warlord(self):
        self.is_warlord = True

    def remove_warlord_status(self):
        self.is_warlord = False
