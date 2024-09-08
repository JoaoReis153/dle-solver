from pathlib import Path
import time
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def getFileFromLink(url):

    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    fileName = getFileNameFromLink(url)
        
    return Path(current_dir + "/Files/" + fileName)

def getFileNameFromLink(url):
    # Parse the URL to get the netloc (network location part)
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc

    # Extract the part between '//' and the first '.'
    fileName = hostname.split('.')[0] + ".txt"
    return fileName


def sendGuess(driver, input_element, guess, answer):
    print("#Guess: " + guess + "\n")
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

def processGuess(answer, driver):

    guess, lastElement = getLastChampGiven(answer, driver)

    # Find all 'div' elements inside the 'square-container'
    attributesDivs = lastElement.find_element(By.CLASS_NAME, "square-container").find_elements(By.TAG_NAME, "div")

    info = ""
    for div in attributesDivs:
        info += div.get_attribute("class") + "\n"


    geral = info.split("\n")
    loaded = False
    cleaned_list = []
    while not loaded:

        time.sleep(0.2)
        # Find all 'div' elements inside the 'square-container'
        attributesDivs = lastElement.find_element(By.CLASS_NAME, "square-container").find_elements(By.TAG_NAME, "div")

        info = ""
        for div in attributesDivs:
            info += div.get_attribute("class") + "\n"

        geral = info.split("\n")


        array_of_lists = info.replace("square-content", "").replace("square", "").replace("champion-icon-names",  "").replace(" animate__animated animate__flipInY -", "").split("\n")

        cleaned_list = [item for item in array_of_lists if item != '']

        loaded = any(c.isalpha() for c in cleaned_list[-1])

    firstCharacteristicIndex = find_first_zero(cleaned_list)

    colors = cleaned_list[firstCharacteristicIndex:]

    colors = "".join([s[2:3] for s in colors])

    colors = colors.replace("a", "")

    print("Colors: " + str(colors))

    return guess, colors

def find_first_zero(arr):
    for index, value in enumerate(arr):
        if "0" in str(value):
            return index
    return -1

