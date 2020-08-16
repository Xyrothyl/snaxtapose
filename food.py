class Food:

    def __init__(self, lst):
        self.name = lst[0]
        self.cost = int(lst[1])
        self.amnt = int(lst[2])
        self.unit = lst[3]
        self.cals = int(lst[4])
        self.fats = int(lst[5])
        self.carb = int(lst[6])
        self.prot = int(lst[7])
        self.upc = lst[8]
        self.metric = -1

    def __lt__(self, other):
        return self.metric < other.metric

    def __str__(self):
        return self.name
