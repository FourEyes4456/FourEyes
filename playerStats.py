import diceRoll

playerName = "Levi"
characterName = ""
statList = [0, 0, 0, 0, 0, 0]

stg = statList[0]
stg_mod = (stg-10)//2

dex = statList[1]
dex_mod = (dex-10)//2

con = statList[2]
con_mod = (con-10)//2

itl = statList[3]
itl_mod = (itl-10)//2

wis = statList[4]
wis_mod = (wis-10)//2

chr = statList[5]
chr_mod = (chr-10)//2


def rollStat(stat):
    print(stat)
    dice = [10, 2, 0]
    stat = diceRoll.rollDice(dice)
    return stat


stg, dex, con, itl, wis, chr

