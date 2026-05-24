def main():
    number = input("Enter any 3- or 4-digit number: ")
    digits = numcount(number)
    kaprekar(number, digits, 0)
    
    
def kaprekar(number1, digits, iterations):
    count = 0
    split = list(number1)
    for item in split:
        count += 1
    if count < digits:
        split.append("0")
    kap1 = sorted(split)
    kap2 = sorted(split, reverse=True)
    smaller = int("".join(kap1))
    bigger = int("".join(kap2))
    subtract = bigger - smaller
    result = str(subtract)
    print(result)
    iterations += 1
    if result == number1:
        print("Final number:", result)
        print("Iterations:", iterations-1)
    else:
        kaprekar(result, digits, iterations)
    
    
def numcount(number):
    digits = 0
    digitcount = list(number)
    for item in digitcount:
        digits += 1
    return digits
    
   
main()