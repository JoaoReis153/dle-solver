from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
from utils import convert_to_base_unit
import re


class Pokedle(BaseAnswer):

    def __init__(self, championsList):
        super().__init__(championsList)


def runPokedle(driver):
  print("Solving Pokedle...")
  url = "https://pokedle.net/classic"
  getSolution(driver, url, Champion, Pokedle)
