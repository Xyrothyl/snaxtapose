class Food:

    def __init__(self, lst):
        self.name = lst[0]
        self.cost = lst[1]
        self.amnt = lst[2]
        self.unit = lst[3]
        self.cals = lst[4]
        self.fats = lst[5]
        self.carb = lst[6]
        self.prot = lst[7]
        self.upc = lst[8]
        self.metric = -1

    def __lt__(self, other):
        return self.metric < other.metric

    def __str__(self):
        return self.name
