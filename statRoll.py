import diceRoll


def rollStats(statList, statMods):
    for stat in statList:
        statList[stat] = diceRoll.rollDice([10, 2, 0], False)
    for stat in statMods:
        statMods[stat] = (statList[stat]-10)//2
    return statList, statMods
    

def main():
    statList = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}
    statMods = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}
    statList, statMods = rollStats(statList, statMods)
    print(statList)
    print(statMods)


if __name__ == "__main__":
    main()
