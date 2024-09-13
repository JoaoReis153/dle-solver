from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
import math
import re
from utils import convert_to_base_unit


class Narutodle(BaseAnswer):



    def __init__(self, championsList):
        super().__init__(championsList)

    def arcList():
        return [
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




def runNarutodle(driver):
  print("Solving Narutodle...")
  url = "https://Narutodle.net/classic"
  getSolution(driver, url, Champion, Narutodle)




