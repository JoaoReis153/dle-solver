import math
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

from utils import getFileFromLink, getLastChampGiven, processGuess, sendGuess, Print, colorsAllGreen
#from objects import Champion, Answer


def getSolution(driver, url, Champion, Answer, FIRSTGUESS = "", showPrints = True):

    file = getFileFromLink(url)
    # Your URL

    champions=[]

    #Load file
    with open(file, "r") as f:
        content = (f.read()).split("\n")

    for line in content:
        champions.append(Champion(line.replace(", ", ",")))

    answer = Answer(champions)
    
    attrsLen = answer.getAttributesLength()

    driver.get(url)

    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)

    try:
        # Wait for up to 10 seconds for the button to be clickable
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-button-label"))
        )
        button.click()
    except Exception as e:
        print(f"Error: {e}")
    #firstGuess = champions[random.randint(0, len(champions) - 1)]
    #most optimal: Varus
    if FIRSTGUESS != "":
        firstGuess = answer.getChampByName(FIRSTGUESS)
    else:
        firstGuess = answer.possibleChampions[0]

    input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
    input_element.clear()

    sendGuess(showPrints, driver, input_element, firstGuess.attributes[0], answer)

    guess, colors = processGuess(showPrints, answer, driver)

    while(len(colors) != attrsLen - 1):
        guess, colors = processGuess(showPrints, answer, driver)

    while not colorsAllGreen(colors) :
        print("gugugu")
        answer.addTry(guess, colors)

        print(answer)
        if(len(answer.possibleChampions) == 0 or colors == "ggggggg"):
            Print(showPrints, "Answer not found")
            break

        guess = answer.possibleChampions[0].attributes[0]
        sendGuess(showPrints, driver, input_element, guess, answer)
        guess, colors = processGuess(showPrints, answer, driver)

    if colorsAllGreen(colors):
        Print(showPrints, ".")
        Print(showPrints, "You won")
        Print(showPrints, ".")


    time.sleep(30)

#    quit()



