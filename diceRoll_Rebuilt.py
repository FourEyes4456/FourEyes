import random
import time


diceType = 0
diceAmount = 0
diceModifier = 0
rollCount = 0
singleRoll = 0
finalRoll = 0
averageRoll = 0
diceCounting = True
version = "0.2.7"

"""
To Do:
* Figure out a way to replace the constant "global" variables within every function
* Simplify the if-elif-else functions within the diceConfirm / rollAgain functions
"""

def diceInput():
    # Provides user input for the dice rolls
    global diceType, diceAmount, diceModifier
    diceType = int(input("Please enter dice type: d"))
    diceAmount = int(input("Please enter dice amount: "))
    diceModifier = int(input("Please enter any modifier (enter 0 if none): "))
    diceConfirm()
   
def diceConfirm():
    # Replaces original confirmation code, allows repeats if not
    global diceType, diceAmount, diceModifier
    diceCheck = ("\n(y/n) Is this correct? " + str(diceAmount) + "d" + str(diceType))
    while True:
        if diceModifier >> 0:
            correct = input(diceCheck + "+" + str(diceModifier) + "  ")
        else:
            correct = input(diceCheck + "  ")
        if correct == "y":
            break
        elif correct == "n":
            break
        else:
            print("Input not recognized, please try again.")
    if correct == "y":
        diceRolling()
    else:
        diceInput()

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
    #replaces messed up "repeat" function from original
    global rollCount, finalRoll, averageRoll, diceCounting
    time.sleep(2)
    while True:
        moreDice = input("\n(y/n) Roll again? ")
        if moreDice == "y":
            break
        elif moreDice == "n":
            break
        else:
            rollAgain()
    if moreDice == "y":
        rollCount = 0
        finalRoll = 0
        averageRoll = 0
        diceCounting = True
        print("\n")
        diceInput()
    else:
        print()

print("DnD Dice Roller ver" + version)
time.sleep(1)
diceInput()