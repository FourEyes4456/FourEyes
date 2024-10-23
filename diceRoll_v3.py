import random


def diceSelect(diceInfo):
    try:
        diceInfo[0] = int(input("Enter dice type: d"))
        diceInfo[1] = int(input("Enter number of dice to roll: "))
        diceInfo[2] = int(input("Enter a roll modifier, enter 0 for none: "))
    except:
        print("Values must be a number, enter again.")
        diceSelect(diceInfo)
    if diceInfo[2] != 0:
        dice
    return diceInfo

def main():
    diceInfo = [0, 0, 0]
    diceSelect(diceInfo) 
    

if __name__ == "__main__":
    main()