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


while True:
    while True:
        diceType = int(input("\nPlease enter dice type: d"))
        diceAmount = int(input("Please enter dice amount: "))
        diceModifier = int(input("Please enter any modifier (enter 0 if none): "))
        while True:
            if diceModifier >> 0:
                correct = input("\nIs this correct? " + str(diceAmount) + "d" + str(diceType) + "+" + str(diceModifier) + " (y/n) ")
                # Line for if a modifier is added
            else:
                correct = input("\nIs this correct? " + str(diceAmount) + "d" + str(diceType) + " (y/n) ")
                # Line for if a modifier is not added
            if correct == "y":
                print()
                break
            elif correct == "n":
                break
            else:
                print()
        if correct == "y":
            break
            # Roll the dice
        else:
            print()
            # Wrong dice

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

    averageRoll = (finalRoll - diceModifier) // rollCount
    # Calculating the average roll
    print("\nFinal roll: " + str(finalRoll))
    print("Average roll: " + str(averageRoll))
    print("\n\nPress the 'Enter' key to reroll.")
    keyboard.wait('Enter')
    input()
    # This line prevents the program from breaking.
    diceCounting = True
    rollCount = 0
    # Resets variables so that the diceCounting script can run again
