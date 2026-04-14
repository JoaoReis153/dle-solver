import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from BaseClasses import Database
from utils import getFileFromLink, processGuess, sendGuess, colorsAllGreen, newDriver, removePopUp
from test import getBestGuess
from BaseClasses import Champion

def get_solution(options, driver, wait, url, arcList = [], FIRSTGUESS = ""):
    
    if driver: 
        driver.get(url)
    else:
        print("Failed to load the page")
        options, driver, wait = newDriver(url)
        return

    try:

        print("Preparing to find out the answer...")

        file = getFileFromLink(url)
        
        champions=[]

        with open(file, "r") as f:
            content = (f.read()).split("\n")

        for line in content:
            champions.append(Champion(line.replace(", ", ",")))

        db = Database(champions, url)

        attrsLen = db.getAttributesLength()

        removePopUp(driver, wait)
        
        input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
        input_element.clear()

        allGreen = False
        while not allGreen :
            if not db.possibleChampions or not db.possibleChampions[0]:
                print("Something's not right!!")
                exit()
            guess = db.possibleChampions[0].attributes[0]
            
            guess = getBestGuess(db, url)

            sendGuess(driver, input_element, guess, db)

            guess, colors = processGuess(db, driver)

            db.addTry(guess, colors)

            allGreen = colorsAllGreen(colors)

            if (not allGreen and (db.possibleChampions) == 0):
                print("Database not found")
                return 

        if allGreen:
            print("\nWinner found\n")
            return

    except NoSuchWindowException:
        print("The browser window was closed unexpectedly.")
        sys.exit(0)



