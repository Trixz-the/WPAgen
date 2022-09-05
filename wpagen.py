import random
from art import *

# List of uppercase letters
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# letter-number sequence array
LNseq = ["L", "N", "N", "N", "L", "N", "N", "N", "L", "L"]
# number-number sequence array
NNseq = ["N", "N", "N", "N", "L", "N", "N", "N", "L", "L"]

# Start of program
tprint("WPAgen")
# sequence mode to choose
mode = input("Select a valid sequence mode:\n\nletter-number sequence [type: LN]\n\nnumber-number sequence [type: NN]\n\n>>> ")
# name of wordlist
name = input("Choose a name for your wordlist >>> ")
# length of wordlist
rng = input(f"Choose a range for {name}.txt >>> ")
# Generate sequence

def genSeq():
    genStr = []
    x = ""
    
    if(mode == "LN"):
        x = LNseq
    elif(mode == "NN"):
        x = NNseq
    else:
        print("Invalid input. Try again.")
        exit()
    
    for i in range(10):    
        for j in range(1):
            rl = upper[random.randint(0, 9)]
            rn = str(random.randint(0, 9))
        if (x[i] == "L"):
            genStr.append(rl)
        elif (x[i] == "N"):
            genStr.append(rn)
    
    return genStr


def makeFile(fileName, fileRange):
    with open(f"{fileName}.txt", "w") as f:
        for i in range(int(fileRange)):
            f.write(f"{genSeq()}\n")
        f.close()
    print(f"WPAgen wordlist {name}.txt generated!")

makeFile(name, rng)