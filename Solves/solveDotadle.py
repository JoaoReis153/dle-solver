from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
from utils import convert_to_base_unit
import re


class Dotadle(BaseAnswer):

    def __init__(self, championsList):
        super().__init__(championsList)


def runDotadle(driver):
  print("Solving Dotadle...")
  url = "https://dotadle.net/classic"
  getSolution(driver, url, Champion, Dotadle)
