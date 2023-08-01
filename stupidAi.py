import random
import numpy as np

"""
How the brain works: for every number it has weights for the chance of it being each number
Example for guessing a num between 1 and 5:
[[20, 20, 20, 20, 20], [20, 20, 20, 20, 20], [20, 20, 20, 20, 20], [20, 20, 20, 20, 20], [20, 20, 20, 20, 20]]

what it will do is it will take in a number (e.g. 3)
so it will take list 3 (index 2) then pick a number between 0 and 100, for example, it will get 27 and find the index of the
number it will get (so in this case index 1 so it'll return 2 as its guess for the inputted number)

if wrong it'll subtract 4 from the index it chose (as a punishment) and give it to the others
if right it'll take 1 from the other indexes and add it to the index
"""

## SETUP

SIZE = 100
REWARDSTRENGTH = 0.1
PUNISHSTRENGTH = 0.1


prebrain = []
numscores = []

for _ in range(SIZE):
    numscores.append(100/SIZE)

for _ in range(SIZE):
    prebrain.append(numscores)

brain = np.array(prebrain)

def getGuess(numToGuess, shouldTrain = True) -> int: # amogus
    roughGuess = random.randint(1, 100)

    # Find where that is
    count = 0
    for guess in range(SIZE):
        count += brain[numToGuess-1][guess]
        if count >= roughGuess:
            # found
            finalGuess = guess+1

            if shouldTrain:
                if finalGuess == numToGuess:
                    # Reward
                    if brain[numToGuess-1][guess] <= 100 - (SIZE * REWARDSTRENGTH):
                        brain[numToGuess-1][guess] += (SIZE * REWARDSTRENGTH)

                    for n in range(SIZE):
                        if brain[numToGuess-1][n] > (1 * PUNISHSTRENGTH):
                            brain[numToGuess-1][n] -= (1 * PUNISHSTRENGTH)
                else:
                    # Punish
                    if brain[numToGuess-1][guess] > (SIZE * PUNISHSTRENGTH):
                        brain[numToGuess-1][guess] -= (SIZE * PUNISHSTRENGTH)
                    
                    for n in range(SIZE):
                        if brain[numToGuess-1][n] < (1 * REWARDSTRENGTH):
                            brain[numToGuess-1][n] += (1 * REWARDSTRENGTH)
                         
            return finalGuess
    
    
def train(count:int = 1000, output:bool = True):
    for test in range(count+1):
        testGuess = random.randint(1,SIZE)
        guess = getGuess(testGuess)
        if output:
            print(f"{test = }:\n{testGuess = }\n{guess = }\n")

if __name__ == '__main__':
    train(7500)
    print(f"{brain}\n\n")


    a = input("Trained! Would you like to test? (Y/n)")
    b = input("Would you like it to train as it goes too? (Y/n)")
    Continue = a.upper()[0] == 'Y'
    Train = b.upper()[0] == 'Y'
    while Continue:
        numToGuess = int(input(f"Enter a number between 1 and {SIZE}: "))
        print(getGuess(numToGuess, Train))
