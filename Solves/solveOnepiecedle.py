from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
import math
import re
from utils import convert_to_base_unit

class OnePiecedle(BaseAnswer):

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


def runOnepiecedle(driver):
  print("Solving OnePiecedle...")
  url = "https://onepiecedle.net/classic"
  getSolution(driver, url, Champion, OnePiecedle)





arcList = [
  'Romance Dawn',
  'Orange Town',
  'Syrup Village',
  'Baratie',
  'Arlong Park',
  'Loguetown',
  'Reverse Mountain',
  'Whisky Peak',
  'Little Garden',
  'Drum Island',
  'Arabasta',
  'Jaya',
  'Skypiea',
  'Long Ring Long Land',
  'Water 7',
  'Enies Lobby',
  'Post-War',
  'Thriller Bark',
  'Sabaody Archipelago',
  'Amazon Lily',
  'Impel Down',
  'Return to Sabaody',
  'Fish-Man Island',
  'Punk Hazard',
  'Dressrosa',
  'Zou',
  'Whole Cake Island',
  'Wano Country'
]
