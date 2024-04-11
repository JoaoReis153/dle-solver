from pathlib import Path
import time
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def getFileFromLink(url):
# Print the current working directory
    fileName = getFileNameFromLink(url)
    
    return Path("./Files/" + fileName)

def getFileNameFromLink(url):
    # Parse the URL to get the netloc (network location part)
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc

    # Extract the part between '//' and the first '.'
    fileName = hostname.split('.')[0] + ".txt"
    return fileName



def Print(showPrints, phrase):
    if showPrints:
        print(phrase)

def sendGuess(showPrints, driver, input_element, guess, answer):
    Print(showPrints, "#Guess: " + guess + "\n")
    time.sleep(0.1)
    input_element.clear()
    input_element.send_keys(guess)
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "guess-button")))
    #wait.until(EC.invisibility_of_element((By.CLASS_NAME, "tooltip-inner"))) 
    send_button.click()
    time.sleep(1)


def getLastChampGiven(answer, driver):
    championsInfoList = driver.find_elements(By.CSS_SELECTOR, ".classic-answer")

    lastElement = championsInfoList[len(championsInfoList)-1]

    nameElement = lastElement.find_element(By.CSS_SELECTOR, ".square-container .square .champion-icon-name")

    info = nameElement.get_attribute("textContent").strip()

    champ = answer.getChampByName(info)

    return champ, lastElement

def colorsAllGreen(colors):
    for c in colors:
        if c != "g":
            return False
    return True

def processGuess(showPrints, answer, driver):

    guess, lastElement = getLastChampGiven(answer, driver)
 
    #square 6 animate__animated animate__flipInY square-inferior

    # Find all 'div' elements inside the 'square-container'
    attributesDivs = lastElement.find_element(By.CLASS_NAME, "square-container").find_elements(By.TAG_NAME, "div")

    # Loop through the found 'div' elements and print their class names
    info = ""
    for div in attributesDivs:
        info += div.get_attribute("class") + "\n"


    geral = info.split("\n")

    while geral[-4].strip() == "square 6":

        time.sleep(0.2)
        # Find all 'div' elements inside the 'square-container'
        attributesDivs = lastElement.find_element(By.CLASS_NAME, "square-container").find_elements(By.TAG_NAME, "div")

        # Loop through the found 'div' elements and print their class names
        info = ""
        for div in attributesDivs:
            info += div.get_attribute("class") + "\n"

        geral = info.split("\n")

    array_of_lists = info.replace("square-content", "").replace("square", "").replace("champion-icon-names",  "").replace(" animate__animated animate__flipInY -", "").split("\n")
    cleaned_list = [item for item in array_of_lists if item != '']

    colors = cleaned_list[1:]
    colors = "".join([s[2:3] for s in colors])

    colors = colors.replace("a", "")

    
    Print(showPrints, "Colors: " + str(colors))


    return guess, colors

