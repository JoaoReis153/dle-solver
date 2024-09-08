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

from utils import getFileFromLink, getLastChampGiven, processGuess, sendGuess, colorsAllGreen
#from objects import Champion, Answer


def getSolution(driver, url, Champion, Answer, FIRSTGUESS = ""):

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
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-button-label"))
        )
        button.click()
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        pop_up_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-button")))
        pop_up_button.click()
    except TimeoutException:
        print('No one piece "are you up to date" pop-up found.')

    firstGuess = answer.possibleChampions[0]

    input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
    input_element.clear()


    sendGuess(driver, input_element, firstGuess.attributes[0], answer)
    


    guess, colors = processGuess(answer, driver)
    while(len(colors) != attrsLen - 1):        
        guess, colors = processGuess(answer, driver)
        
    

    while not colorsAllGreen(colors) :

        answer.addTry(guess, colors)

        if(len(answer.possibleChampions) == 0 or colors == "ggggggg"):
            print("Answer not found")
            break

        guess = answer.possibleChampions[0].attributes[0]
        sendGuess(driver, input_element, guess, answer)
        guess, colors = processGuess(answer, driver)
        

    if colorsAllGreen(colors):
        print()
        print("You won")
        print("")
    

