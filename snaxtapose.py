pantry = []


def loadPantry():
    with open("pantry.txt") as f:
        for line in f:
            pantry.append(line.split(','))
            pantry[-1][-1] = pantry[-1][-1].strip()

    for entry in pantry:
        print(entry)

loadPantry()