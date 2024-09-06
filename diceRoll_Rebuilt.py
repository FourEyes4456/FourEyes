import random
import keyboard

diceType = 0
diceAmount = 0
diceModifier = 0
# Variables for the dice
rollCount = 0
singleRoll = 0
finalRoll = 0
averageRoll = 0
# Variables for the rolling process
correct = ""
# Confirmation to roll
diceCounting = True
# Enables counting of the individual dice rolls


def diceInput():
    global diceType, diceAmount, diceModifier
    diceType = int(input("\nPlease enter dice type: d"))
    diceAmount = int(input("Please enter dice amount: "))
    diceModifier = int(input("Please enter any modifier (enter 0 if none): "))
    diceCheck = ("\n(y/n) Is this correct? " + str(diceAmount) + "d" + str(diceType))
    # Inputs are finished and check text is generated
    while True:
        if diceModifier >> 0:
            correct = input(diceCheck + "+" + str(diceModifier) + "  ")
            # Line for if a modifier is added
        else:
            correct = input(diceCheck + "  ")
            # Line for if a modifier is not added
        if correct == "y" or "n":
            print()
            break
        else:
            print()
    if correct == "y":
        diceRolling()
        # Roll the dice
    else:
        print()
        # Wrong dice



def diceRolling():
    global rollCount, singleRoll, finalRoll, diceCounting
    while diceCounting is True:
        if int(rollCount) <= int(diceAmount)-1:
            singleRoll = random.randint(1, int(diceType))
            # Rolls a single dice
            finalRoll += singleRoll
            # Adds the last roll to the total roll
            print(str(rollCount+1) + ": " + str(singleRoll) + " -> " + str(finalRoll))
            # Prints: Dice number, Number rolled, Total amount rolled
            rollCount += 1
        else:
            diceCounting = False
            # Breaks the loop after the proper number of dice is rolled
            finalRoll += diceModifier
            # Adding the modifier to the final roll
            if diceModifier >> 0:
                print("Modifier: " + str(diceModifier) + " -> " + str(finalRoll))
                # Adds another line to the diceCounting if there is a modifier
    diceAddup()


def diceAddup():
    global diceModifier, rollCount, finalRoll, averageRoll
    averageRoll = (finalRoll - diceModifier) // rollCount
    # Calculating the average roll
    print("\nFinal roll: " + str(finalRoll))
    print("Average roll: " + str(averageRoll))
    rollAgain()


def rollAgain():
    global rollCount
    while True:
        moreDice = input("(y/n) Roll again? ")
        if moreDice == "y" or "n":
            break
        else:
            print()
    if moreDice == "y":
        rollCount = 0
        diceInput()
    else:
        print()


diceInput()