from food import Food


def openPantry():
    cnt = 0
    with open("pantry.txt") as f:
        for line in f:
            item = line.split(',')
            item[-1] = item[-1].strip()
            pantry.append(Food(item))
            cnt += 1

    # for entry in pantry:
    #     print(entry)

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


def shop():
    cart = []
    # TODO: SQL database for this
    # with open("branded_food.csv") as store_f:
    #     for line in store_f:
    #         x = 1  # temp filler

    print("Shopping. Enter 'checkout' to exit.")

    while True:
        s = input("Food name: ").lower()
        if s == "checkout":
            break

        f = [s, -1, -1, -1, -1, -1, -1, -1, -1]

        f[1] = input("Price: ")
        f[3] = input("Amount unit: ")
        f[2] = input("Amount: ")
        f[4] = input("Calories: ")
        f[5] = input("Fat: ")
        f[6] = input("Carbohydrates: ")
        f[7] = input("Protein: ")
        '''
        food[8] = input("UPC: ")
        '''
        # TODO: Ask for confirmation of data & correct mistakes
        food = Food(f)
        food.printInfo()
        print("Adding food to cart...", end='')
        cart.append(food)
        print(" added!")
        print("_\\|/_ _\\|/_ _\\|/_ _\\|/_ ")

    return cart


# TODO
def setMetric():
    return 0


# TODO
def compare():
    return 0


pantry = []
pantry_cnt = openPantry()

# TODO: Full list of commands w/ functionality
while True:
    command = input("What would you like to do? ").lower()
    if command == "exit" or command == "quit":
        break
    elif command == "shop":
        shop()

# This might want to go in the while loop, idk yet
if len(pantry) > pantry_cnt:
    updatePantry()

# TESTING
