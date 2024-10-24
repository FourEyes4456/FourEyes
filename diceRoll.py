import random

# diceRoll.py - Version 3

# File can be run standalone, however it is designed to run within other files.
# If running from a separate file, call the "rollDice()" function.
# A set of numbers can be passed through the rollDice function if already known.
# Format for this is as follows:

# [Type, Number, Modifier] --> [20, 5, 6]
# This will roll 5 d20s and add 6 to the final number.



def diceSelect(diceInfo):
    try:
        diceInfo[0] = int(input("Enter dice type: d"))
        diceInfo[1] = int(input("Enter number of dice to roll: "))
        diceInfo[2] = int(input("Enter a roll modifier, enter 0 for none: "))
    except:
        print("Values must be a number, enter again.")
        diceSelect(diceInfo)
    checking(diceInfo)
    return diceInfo


def checking(diceInfo):
    if diceInfo[2] != 0:
        check = input("Is this correct: " + str(diceInfo[1]) + "d" + str(diceInfo[0]) + "+" + str(diceInfo[2]) + "? (y/n) ")
    else:
        check = input("Is this correct: " + str(diceInfo[1]) + "d" + str(diceInfo[0]) + "? (y/n)")
    if check == "n" or check == "N":
        diceSelect(diceInfo)
    elif check == "y" or check == "Y":
        print()
    else:
        print("Invalid input, please try again")
        checking(diceInfo)
        

def rolling(diceInfo):
    total = 0
    if diceInfo[2] != 0:
        print("\n" + str(diceInfo[1]) + "d" + str(diceInfo[0]) + "+" + str(diceInfo[2]))
    else:
        print("\n" + str(diceInfo[1]) + "d" + str(diceInfo[0]))
    for number in range(1, diceInfo[1]+1):
        roll = random.randrange(1, diceInfo[0]+1)
        total += roll
        print(str(number) + ":", roll, "-->", total)
    if diceInfo[2] != 0:
        total += diceInfo[2]
        print("Modifier:", diceInfo[2], "-->", total)
    return total


def final_output(diceInfo, total):
    print("\n\nFinal Roll:", total)
    average = (total - diceInfo[2]) // diceInfo[1]
    print("Average Roll:", average)
    
    
def main(diceInfo = [0, 0, 0]):
    if diceInfo[0] == 0:
        diceSelect(diceInfo)
    total = rolling(diceInfo)
    final_output(diceInfo, total)
    

def rollDice(diceInfo = [0, 0, 0]):
    main(diceInfo)


if __name__ == "__main__":
    main()