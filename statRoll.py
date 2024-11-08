import diceRoll


def roll_stats(stat_list, stat_mods):
    for stat in stat_list:
        stat_list[stat] = diceRoll.rollDice([10, 2, 0], False)
    for stat in stat_mods:
        stat_mods[stat] = (stat_list[stat]-10)//2
    return stat_list, stat_mods
    

def roll_damage(dice, number, modifier=0):
    damage = 0
    to_roll = [dice, number, modifier]
    damage = diceRoll.rollDice(to_roll, False)
    return damage


def roll_initiative(stat_mods):
    initiative = diceRoll.rollDice([20, 1, stat_mods["dex"]], False)
    return initiative


def roll_check(stat_mods):
    stat = input("Enter stat: ")
    if stat.lower() in stat_mods:
        check = diceRoll.rollDice([20, 1, stat_mods[stat.lower()]], False)
        return check
    print("Stat does not exist, try again.")
    roll_check(stat_mods)


def main():
    stat_list = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}
    stat_mods = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}
    stat_list, stat_mods = roll_stats(stat_list, stat_mods)
    print(stat_list)
    print(stat_mods)

    print(roll_initiative(stat_mods))


if __name__ == "__main__":
    main()
