class Food:

    def __init__(self, lst):
        self.name = lst[0]
        self.cost_per_unit = lst[1]
        self.unit = lst[2]
        self.cals = lst[3]
        self.fats = lst[4]
        self.carb = lst[5]
        self.prot = lst[6]
        self.upc = lst[7]
        self.metric = -1

    def __lt__(self, other):
        return self.metric < other.metric

    def __str__(self):
        return self.name
