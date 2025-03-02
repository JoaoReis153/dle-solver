from utils import getFileFromLink
from BaseClasses import Champion, Database, convert_to_base_unit
import re 

def getBestGuess(db, url): 
    bestGuess = None
    bestGuessCount = {}  # Track how many times each champion is the best guess

    for possibleAnswer in db.possibleChampions:
        hashmap = {}
        for champion in db.possibleChampions:
            testdb = db.copy()
            # Initialize the champion's score to 0 if it doesn't exist
            if champion.attributes[0] not in hashmap:
                hashmap[champion] = 0
            # Add the score for this champion
            score = getScore(possibleAnswer, champion, testdb, url)
            hashmap[champion] += score

        # Find the champion name (key) with the maximum score for this possibleAnswer
        currentBestGuess = max(hashmap, key=hashmap.get)

        # Update the count for the current best guess
        if currentBestGuess in bestGuessCount:
            bestGuessCount[currentBestGuess] += 1
        else:
            bestGuessCount[currentBestGuess] = 1

        print(f"If the answer was {possibleAnswer.attributes[0]}, the best guess is {currentBestGuess}")

    # Add champions to the hashmap only if they were the best guess more than once
    for champion, count in bestGuessCount.items():
        hashmap[champion] = count  # Store the count as the score

    # Find the final best guess based on the hashmap
    if hashmap:
        bestGuess = max(hashmap, key=hashmap.get)
        print(f"Final best guess is {bestGuess} with a score of {hashmap[bestGuess]}")
    else:
        print("No champion was the best guess more than once.")
    
    #print(hashmap)

    return bestGuess

def getScore(answer, champion, db, url):
    championsListLength = len(db.possibleChampions)
    score = 0
    #print(len(db.possibleChampions))

    size = len(db.possibleChampions)
    combination = getGuessColor(answer, champion, url)[1:]
    db.addTry(champion, combination)
    sizeAfterCut = len(db.possibleChampions)
    #print("Cut with champion " + champion.attributes[0] + " the db by " + str((size - sizeAfterCut)*100/size) + "%")
    #print("Rest " + str(sizeAfterCut) + " champions in the db")
    #if(len(db.possibleChampions) == 1):
    #    print(db.possibleChampions[0].attributes[0])
    return (size - sizeAfterCut)/size
    

def translateForComparison(guess:Champion, url):
    converted_attributes = []
    for attr in guess.attributes:
        if isinstance(attr, list):
            converted_attributes.append([convert_to_base_unit(elem, url) for elem in attr])
        else:
            converted_attributes.append(convert_to_base_unit(attr, url))
    return converted_attributes

def getOneColor(answerAttr, guessAttr):
    if answerAttr == guessAttr:
        return "g"
    elif isinstance(answerAttr, list) and guessAttr in answerAttr:
        return "p"
    elif isinstance(answerAttr, list) and guessAttr not in answerAttr:
        return "b"
    numbers = re.findall(r'\d+', answerAttr)
    if not numbers:
        return "b"
    elif answerAttr > guessAttr:
        return "s"
    elif answerAttr < guessAttr:
        return "i"
   

def getGuessColor(answer: Champion, guess: Champion, url):
    guessColor = ""
    answer = translateForComparison(answer, url)
    guess = translateForComparison(guess, url)
    for i, attr in enumerate(guess): 
        guessColor += getOneColor(answer[i], attr)
    return guessColor


"""

url = "https://loldle.net/classic"
file = getFileFromLink(url)

champions=[]

with open(file, "r") as f:
    content = (f.read()).split("\n")

for line in content:
    champions.append(Champion(line.replace(", ", ",")))

db = Database(champions, url)


print(getBestGuess(db, url))~
"""
