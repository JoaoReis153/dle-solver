from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
import math
import re


class Narutodle(BaseAnswer):

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


def runNarutodle(driver):
  url = "https://Narutodle.net/classic"
  getSolution(driver, url, Champion, Narutodle)



def convert_to_base_unit(input_str):

    numbers = re.findall(r'[0-9.]+', input_str)
    try:
        index = arcList.index(input_str)
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