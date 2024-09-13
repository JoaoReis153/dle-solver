from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
from utils import convert_to_base_unit
import re



class Loldle(BaseAnswer):

    def gotInferiorDate(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1:

                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index])
                givenChampionInt = convert_to_base_unit(champion.attributes[index])

                if(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperiorDate(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index])
                givenChampionInt = convert_to_base_unit(champion.attributes[index])
                if(float(possibleChampionInt) > float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


def runLoldle(driver):
    print("Solving Loldle...")
    url = "https://loldle.net/classic"
    getSolution(driver, url, Champion, Loldle)
