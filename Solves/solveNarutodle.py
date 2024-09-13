from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
import math
import re
from utils import convert_to_base_unit


class Narutodle(BaseAnswer):

    def gotInferiorDate(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            print(possibleChampion)
            if len(possibleChampion.attributes) != 1:

                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index], arcList)
                givenChampionInt = convert_to_base_unit(champion.attributes[index], arcList)

                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperiorDate(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index], arcList)
                givenChampionInt = convert_to_base_unit(champion.attributes[index], arcList)

                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) > float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


def runNarutodle(driver):
  print("Solving Narutodle...")
  url = "https://Narutodle.net/classic"
  getSolution(driver, url, Champion, Narutodle)




arcList = [
    "Prologue",
    "Chūnin Exams",
    "Konoha Crush",
    "Search for Tsunade",
    "Sasuke Recovery Mission",
    "Kazekage Rescue Mission",
    "Tenchi Bridge Reconnaissance Mission",
    "Akatsuki Suppression Mission",
    "Itachi Pursuit Mission",
    "Fated Battle Between Brothers",
    "Tale of Jiraiya the Gallant",
    "Pain's Assault",
    "Five Kage Summit",
    "Countdown",
    "Climax",
    "Kakashi Gaiden",  # Flashback arc
    "Birth of the Ten-Tails' Jinchūriki",
    "Kaguya Ōtsutsuki Strikes"
]