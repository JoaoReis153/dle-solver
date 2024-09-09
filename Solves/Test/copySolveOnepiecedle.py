from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
import math
import re


class OnePiecedle(BaseAnswer):

    def gotInferiorDate(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            print(possibleChampion)
            if len(possibleChampion.attributes) != 1:

                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index])
                givenChampionInt = convert_to_base_unit(champion.attributes[index])

                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperiorDate(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index])
                givenChampionInt = convert_to_base_unit(champion.attributes[index])

                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) > float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


def runCopyOnepiecedle(driver):
  url = "https://onepiecedle.net/classic"
  getSolution(driver, url, Champion, OnePiecedle)



def convert_to_base_unit(input_str):

    numbers = re.findall(r'[0-9.]+', input_str)
    try:
        index = islandsOrder.index(input_str)
        return index
    except ValueError:
        if "base64" in input_str:
            return None
        #return input_str

        input_str = input_str.strip().lower()
        content = int("".join(numbers))

        if 'cm' in input_str or 'm' in input_str or 'M' in input_str:
            return str(int(content * math.pow(10,6)))

        if "B" in input_str or 'b' in input_str:
            return str(int(content * math.pow(10,9)))

        if any(not char.isdigit() for char in input_str):
            return None

        return input_str



islandsOrder = [
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
