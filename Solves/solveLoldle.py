from getSolution import getSolution
from .BaseClasses import BaseAnswer, Champion
from utils import convert_to_base_unit
import re



class Loldle(BaseAnswer):

    def __init__(self, championsList):
        super().__init__(championsList)


def runLoldle(driver):
    print("Solving Loldle...")
    url = "https://loldle.net/classic"
    getSolution(driver, url, Champion, Loldle)
