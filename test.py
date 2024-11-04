import diceRoll
import statRoll

r_5d20 = [20, 5, 0]
r_5d20_6 = [20, 5, 6]
stats = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}
modifiers = {"stg":0, "dex":0, "con":0, "itl":0, "wis":0, "chr":0}

diceRoll.rollDice(r_5d20)
diceRoll.rollDice(r_5d20_6)

print("\nSilent Rolling")
print(diceRoll.rollDice(r_5d20, False))
print(diceRoll.rollDice(r_5d20_6, False))

statRoll.rollStats(stats, modifiers)
print(stats)
print(modifiers)

