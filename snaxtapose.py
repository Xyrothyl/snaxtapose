from food import Food


def openPantry():
    cnt = 0
    with open("pantry.txt") as f:
        for line in f:
            item = line.split(',')
            item[-1] = item[-1].strip()
            pantry.append(Food(item))
            cnt += 1

    for entry in pantry:
        print(entry)
    return cnt


def writeFood(f, food):
    f.write("{},{},{},{},{},{},{},{},{}\n".format(food.name, food.cost, food.amnt, food.unit,
                                                  food.cals, food.fats, food.carb, food.prot,
                                                  food.upc))


def updatePantry():
    f = open("pantry.txt", 'a')
    for i in range(pantry_cnt, len(pantry)):
        writeFood(f, pantry[i])
    f.close()
    print("Pantry updated.")


def shop(shopping_list):
    cart = []
    with open ("branded_food.csv") as store_f:
        for line in store_f:


    return cart


pantry = []
pantry_cnt = openPantry()

if len(pantry) > pantry_cnt:
    updatePantry()

# TESTING


