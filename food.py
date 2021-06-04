# food_nutrient.csv has amounts per 100g of food

class Food:

    def __init__(self, lst):
        self.name = lst[0]
        self.cost = float(lst[1])
        self.amnt = int(lst[2])
        self.unit = lst[3]
        self.cals = int(lst[4])
        self.fats = int(lst[5])
        self.carb = int(lst[6])
        self.prot = int(lst[7])
        self.upc = lst[8]
        self.metric = -1  # Should always be set back to -1 after use

    def __lt__(self, other):
        return self.metric < other.metric

    def __str__(self):
        return self.name

    def printInfo(self):
        print("{}: ${:.2f} for {} {}".format(self.name, self.cost, self.amnt, self.unit))
        print("{} calories, {} g fat, {} g carbs, {} g protein".format(self.cals, self.fats, self. carb, self.prot))
