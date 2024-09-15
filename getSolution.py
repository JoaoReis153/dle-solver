import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from BaseClasses import Answer
from utils import getFileFromLink, processGuess, sendGuess, colorsAllGreen, newDriver, removePopUp

def getSolution(options, driver, wait, url, Champion, arcList, FIRSTGUESS = ""):
    
    if driver: 
        driver.get(url)
    else:
        print("Failed to load the page")
        options, driver, wait = newDriver(url)
        return

    try:

        file = getFileFromLink(url)
        # Your URL

        champions=[]

        with open(file, "r") as f:
            content = (f.read()).split("\n")

        for line in content:
            champions.append(Champion(line.replace(", ", ",")))

        answer = Answer(champions, arcList)

        attrsLen = answer.getAttributesLength()

     

        removePopUp(driver, wait)

        firstGuess = answer.possibleChampions[0]
        
        input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
        input_element.clear()

        allGreen = False
        while not allGreen :
            if not answer.possibleChampions or not answer.possibleChampions[0]:
                print("Something's not right!!")
                exit()
            guess = answer.possibleChampions[0].attributes[0]

            print("\n")

            sendGuess(driver, input_element, guess, answer)

            guess, colors = processGuess(answer, driver)

            answer.addTry(guess, colors)

            allGreen = colorsAllGreen(colors)

            if (not allGreen and (answer.possibleChampions) == 0):
                print("Answer not found")
                return 

        if allGreen:
            print("\nWinner found\n")
            return

    except NoSuchWindowException:
        print("The browser window was closed unexpectedly.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")


