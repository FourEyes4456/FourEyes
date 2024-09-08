import random

diceType = 0
diceAmount = 0
diceModifier = 0
rollCount = 0
singleRoll = 0
finalRoll = 0
averageRoll = 0
correct = ""
diceCounting = True


def diceInput():
    global diceType, diceAmount, diceModifier
    diceType = int(input("\nPlease enter dice type: d"))
    diceAmount = int(input("Please enter dice amount: "))
    diceModifier = int(input("Please enter any modifier (enter 0 if none): "))
    diceCheck = ("\n(y/n) Is this correct? " + str(diceAmount) + "d" + str(diceType))
    while True:
        if diceModifier >> 0:
            correct = input(diceCheck + "+" + str(diceModifier) + "  ")
        else:
            correct = input(diceCheck + "  ")
        if correct == "y" or "n":
            print()
            break
        else:
            print()
    if correct == "y":
        diceRolling()
    else:
        print()

def diceRolling():
    global rollCount, singleRoll, finalRoll, diceCounting
    while diceCounting is True:
        if int(rollCount) <= int(diceAmount)-1:
            singleRoll = random.randint(1, int(diceType))
            finalRoll += singleRoll
            print(str(rollCount+1) + ": " + str(singleRoll) + " -> " + str(finalRoll))
            rollCount += 1
        else:
            diceCounting = False
            finalRoll += diceModifier
            if diceModifier >> 0:
                print("Modifier: " + str(diceModifier) + " -> " + str(finalRoll))
    diceAddup()

def diceAddup():
    global diceModifier, diceAmount, finalRoll, averageRoll
    averageRoll = (finalRoll - diceModifier) // diceAmount
    print("\nFinal roll: " + str(finalRoll))
    print("Average roll: " + str(averageRoll))
    rollAgain()

def rollAgain():
    global rollCount, finalRoll, averageRoll, diceCounting
    while True:
        moreDice = input("(y/n) Roll again? ")
        if moreDice == "y" or "n":
            break
        else:
            print()
    if moreDice == "y":
        rollCount = 0
        finalRoll = 0
        averageRoll = 0
        diceCounting = True
        diceInput()
    else:
        print()

diceInput()