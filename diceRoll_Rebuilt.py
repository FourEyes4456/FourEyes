import random
import time


diceType = 0
diceAmount = 0
diceModifier = 0
rollCount = 0
singleRoll = 0
finalRoll = 0
averageRoll = 0
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
    # Replaces original confirmation code. Allows repeating dice input if incorrect.
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
    # "Rolls" the selected dice, along with displaying rolls and totals.
    global rollCount, singleRoll, finalRoll, diceCounting
    diceCounting = True
    print("\n")
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
    # Calculates the average roll
    global diceModifier, diceAmount, finalRoll, averageRoll
    averageRoll = (finalRoll - diceModifier) // diceAmount
    print("\nFinal roll: " + str(finalRoll))
    print("Average roll: " + str(averageRoll))
    time.sleep(2)
    rollAgain()

def rollAgain():
    # Provides user the chance to rerun the program.
    global rollCount, singleRoll, finalRoll
    rollCount = 0
    singleRoll = 0
    finalRoll = 0
    while True:
        moreDice = str(input("\n1) Roll the same dice again.\n2) Roll different dice.\n3) Exit.\n: "))
        if moreDice == "1":
            break
        elif moreDice == "2":
            break
        elif moreDice == "3":
            break
        else:
            print("Input not recognized, please try again.")
    if moreDice == "1":
        diceRolling()
    elif moreDice == "2":
        print("\n")
        diceInput()
    else:
        print()

print("DnD Dice Roller ver" + version)
time.sleep(1)
diceInput()