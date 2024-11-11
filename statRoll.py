import diceRoll

stat_list = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}
stat_mods = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}

stg_skills = ['athletics']
dex_skills = ['acrobatics', 'sleight of hand', 'stealth']
con_skills = []
itl_skills = ['arcana', 'history', 'investigation', 'nature', 'religion']
wis_skills = ['animal handling', 'insight', 'medicine', 'perception', 'survival']
chr_skills = ['deception', 'intimidation', 'performance', 'persuasion']

skill_list = {'stg':stg_skills, 'dex':dex_skills, 'con':con_skills, 'itl':itl_skills, 'wis':wis_skills, 'chr':chr_skills}


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


def roll_check(stat_mods, skill_list, skill=""):
    stat = ""
    if skill == "":
        skill = input("Enter skill to roll: ")
    for elt in skill_list:
        if skill in skill_list[elt]:
            stat = elt
    check = diceRoll.rollDice([20, 1, stat_mods[stat]], False)
    return check



def main(stat_list, stat_mods, skill_list):
    stat_list, stat_mods = roll_stats(stat_list, stat_mods)
    print(stat_list)
    print(stat_mods)

    print(roll_initiative(stat_mods))

    for stat in skill_list:
        print(stat)
        print(skill_list[stat])

    print(roll_check(stat_mods, skill_list, 'deception'))


if __name__ == "__main__":
    main(stat_list, stat_mods, skill_list)
