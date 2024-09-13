from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
import math
import re
from utils import convert_to_base_unit

class OnePiecedle(BaseAnswer):

    def __init__(self, championsList):
            super().__init__(championsList)

    def arcList():
        return  [
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



def runOnepiecedle(driver):
  print("Solving OnePiecedle...")
  url = "https://onepiecedle.net/classic"
  getSolution(driver, url, Champion, OnePiecedle)


