from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion

import re



class Loldle(BaseAnswer):

    def gotInferiorDate(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1:

                possibleChampionInt = "".join(re.findall(r'\d+\.\d+|\d+', possibleChampion.attributes[index]))
                givenChampionInt = "".join(re.findall(r'\d+\.\d+|\d+', champion.attributes[index]))
                if(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperiorDate(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = "".join(re.findall(r'\d+', possibleChampion.attributes[index]))
                givenChampionInt = "".join(re.findall(r'\d+', champion.attributes[index]))
                if(float(possibleChampionInt) > float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


def runCopyLoldle(driver):
    print("Running Loldle...")
    url = "https://loldle.net/classic"
    getSolution(driver, url, Champion, Loldle)
