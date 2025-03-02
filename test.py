from utils import getFileFromLink
from BaseClasses import Champion, Database, convert_to_base_unit
import re 

def getBestGuess(db, url):
    bestGuess = None

    hashmap = {}

    for possibleAnswer in set(db.possibleChampions):
        for champion in db.possibleChampions:
            testdb = db.copy()
            if champion not in hashmap:
                hashmap[champion] = 0
            score = getScore(possibleAnswer, champion, testdb, url)

            hashmap[champion] += score

        currentBestGuess = min(hashmap, key=hashmap.get)


    jstNamesHahsmap = {champion.attributes[0]: score for champion, score in hashmap.items()}
    jstNamesHahsmap = dict(sorted(jstNamesHahsmap.items(), key=lambda item: item[1]))
    print(jstNamesHahsmap)
    # Find the final best guess based on the bestGuessCount
    bestGuess = min(hashmap, key=hashmap.get)
    print(f"Final best guess is {bestGuess.attributes[0]} with a count of {hashmap[bestGuess]}")

    return bestGuess

def getScore(answer, champion, db, url):
    championsListLength = len(db.possibleChampions)
    size = len(db.possibleChampions)
    combination = getGuessColor(answer, champion, url)[1:]
    #print(combination)
    db.addTry(champion, combination)
    sizeAfterCut = len(db.possibleChampions)
    return sizeAfterCut
    

def translateForComparison(guess:Champion, url):
    converted_attributes = []
    for attr in guess.attributes:
        if isinstance(attr, list):
            converted_attributes.append([convert_to_base_unit(elem, url) for elem in attr])
        else:
            converted_attributes.append(convert_to_base_unit(attr, url))
    return converted_attributes

def getOneColor(answerAttr, guessAttr):
    # Case 1: Exact match (green)
    if answerAttr == guessAttr:
        return "g"
    
    # Case 2: Partial match (yellow)
    # If either answerAttr or guessAttr is a list, check for overlap
    if isinstance(answerAttr, list) and guessAttr in answerAttr:
        return "p"
    if isinstance(guessAttr, list) and answerAttr in guessAttr:
        return "p"
    if (isinstance(answerAttr, list) and isinstance(guessAttr, list) and set(answerAttr).intersection(guessAttr)):
        return "p"
    
    # Case 3: No match (black)
    if isinstance(answerAttr, list) and guessAttr not in answerAttr:
        return "b"
    if isinstance(guessAttr, list) and answerAttr not in guessAttr:
        return "b"
    
    # Case 4: Numeric comparison
    # Extract numbers from answerAttr and guessAttr (if they are strings)
    answer_num = re.findall(r'\d+', str(answerAttr))
    guess_num = re.findall(r'\d+', str(guessAttr))
    
    if not answer_num or not guess_num:
        return "b"  # No numbers to compare
    
    # Convert extracted numbers to integers
    answer_num = int(answer_num[0])
    guess_num = int(guess_num[0])
    
    if answer_num > guess_num:
        return "s"  # Superior (answer is greater)
    elif answer_num < guess_num:
        return "i"  # Inferior (answer is smaller)
    
    # Default case: No match
    return "b"
   

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

c1 = db.getChampByName("Zilean")
c2 = db.getChampByName("Vladimir")

print(c1)
print(c2)
print(getScore(c1, c2, db, url))
"""