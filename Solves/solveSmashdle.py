from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
from utils import convert_to_base_unit
import re

class Smashdle(BaseAnswer):

    def __init__(self, championsList):
        super().__init__(championsList)



def runSmashdle(driver):
  print("Solving Smashdle...")
  url = "https://smashdle.net/classic"
  getSolution(driver, url, Champion, Smashdle)
