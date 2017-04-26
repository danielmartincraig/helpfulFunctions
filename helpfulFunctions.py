# Helpful Functions!
# Daniel Craig

#This function prints the powers of 2 up until the 20th power 
def printPow():
    for key, power in {i : 2**i for i in range(0, 21)}.items():
        print(key, power)