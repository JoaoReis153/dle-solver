from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion

import re

class Smashdle(BaseAnswer):


    def gotInferiorDate(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1:

                possibleChampionInt = "".join(re.findall(r'[0-9.]+', possibleChampion.attributes[index]))
                givenChampionInt = "".join(re.findall(r'[0-9.]+', champion.attributes[index]))

                if(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperiorDate(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = "".join(re.findall(r'[0-9.]+', possibleChampion.attributes[index]))
                givenChampionInt = "".join(re.findall(r'[0-9.]+', champion.attributes[index]))

                if(float(possibleChampionInt) > float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions



def runSmashdle(driver):
  url = "https://smashdle.net/classic"
  getSolution(driver, url, Champion, Smashdle)
