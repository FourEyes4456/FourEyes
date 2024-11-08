import random

# diceRoll.py - Version 3

# File can be run standalone, however it is designed to run within other files.
# If running from a separate file, call the "rollDice()" function.
# A set of numbers can be passed through the rollDice function if already known.
# Format for this is as follows:

# [Type, Number, Modifier] --> [20, 5, 6]
# This will roll 5 d20s and add 6 to the final number.



def diceSelect(dice_info):
    try:
        dice_info[0] = int(input("Enter dice type: d"))
        dice_info[1] = int(input("Enter number of dice to roll: "))
        dice_info[2] = int(input("Enter a roll modifier, enter 0 for none: "))
    except:
        print("Values must be a number, enter again.")
        diceSelect(dice_info)
    checking(dice_info)
    return dice_info


def checking(dice_info):
    if dice_info[2] != 0:
        check = input("Is this correct: " + str(dice_info[1]) + "d" + str(dice_info[0]) + "+" + str(dice_info[2]) + "? (y/n) ")
    else:
        check = input("Is this correct: " + str(dice_info[1]) + "d" + str(dice_info[0]) + "? (y/n)")
    if check == "n" or check == "N":
        diceSelect(dice_info)
    elif check == "y" or check == "Y":
        print()
    else:
        print("Invalid input, please try again")
        checking(dice_info)
        

def rolling(dice_info, text=True):
    total = 0
    if text is True:
        if dice_info[2] != 0:
            print("\n" + str(dice_info[1]) + "d" + str(dice_info[0]) + "+" + str(dice_info[2]))
        else:
            print("\n" + str(dice_info[1]) + "d" + str(dice_info[0]))
    for number in range(1, dice_info[1]+1):
        roll = random.randrange(1, dice_info[0]+1)
        total += roll
        if text is True:
            print(str(number) + ":", roll, "-->", total)
    if dice_info[2] != 0:
        total += dice_info[2]
        if text is True:
            print("Modifier:", dice_info[2], "-->", total)
    return total


def final_output(dice_info, total):
    print("\n\nFinal Roll:", total)
    average = (total - dice_info[2]) // dice_info[1]
    print("Average Roll:", average)
    return total
    
    
def main(dice_info = [0, 0, 0], text=True):
    if dice_info[0] == 0:
        diceSelect(dice_info)
    if text is True:
        total = rolling(dice_info)
        final_output(dice_info, total)
    else:
        total = rolling(dice_info, False)
    return total
    

def rollDice(dice_info = [0, 0, 0], text=True):
    if text is True:
        total = main(dice_info)
    else:
        total = main(dice_info, False)
    return total


if __name__ == "__main__":
    main()