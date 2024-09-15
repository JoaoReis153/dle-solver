from pathlib import Path
import re
import time
import os
import random
import sys
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager
from BaseClasses import Answer

def getFileFromLink(url):

    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    fileName = getFileNameFromLink(url)

    return Path(current_dir + "/Files/" + fileName)

def getFileNameFromLink(url):
    # Extract the part between '//' and the first '.'
    fileName = getNameFromUrl(url) + ".txt"
    return fileName

def getNameFromUrl(url):
    # Parse the URL to get the netloc (network location part)
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc

    # Extract the part between '//' and the first '.'
    name = hostname.split('.')[0] 
    return name


def sendGuess(driver, input_element, guess, answer):
    print("#Guess: " + guess)
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
        attributesDivs = lastElement.find_element(By.CLASS_NAME, "square-container").find_elements(By.XPATH, "./div")

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

    print_colored_squares(colors)

    return guess, colors

def find_first_zero(arr):
    for index, value in enumerate(arr):
        if "0" in str(value):
            return index
    return -1


# Define ANSI escape codes for colors
RED = "\033[41m  \033[0m"    # Red square
YELLOW = "\033[43m  \033[0m" # Yellow square
GREEN = "\033[42m  \033[0m"  # Green square

def print_colored_squares(sequence):
    print("(", end = "")
    for char in sequence:
        if char == 'b':
            print(RED, end='')      # Print red square for 'b'
        elif char == 'p':
            print(YELLOW, end='')   # Print yellow square for 'p'
        elif char == 'g':
            print(GREEN, end='')     # Print green square for 'g'
        elif char == 's':
            print("↑", end='')       # Print up arrow for 's'
        elif char == 'i':
            print("↓", end='')       # Print down arrow for 'i'
        else:
            print("  ", end='')      # Print space for any other character
    print(")")  # New line after printing all squares


def newDriver(site="https://www.google.com/", waitTime = 2, headless = False):
    
    options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    if headless:
        options.add_argument("--headless")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    


    driver.get(site)
    wait = WebDriverWait(driver, waitTime)

    removePopUp(driver, wait)

    return options, driver, wait



def removePopUp(driver, wait):
    try:
        pop_up_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-button-label")))
        pop_up_button.click()
    except TimeoutException:
        pass

    try:
        pop_up_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-button")))
        pop_up_button.click()
    except TimeoutException:
        pass


def extract_keywords_from_image_path(image_path):

    match = re.search(r'/([^.\/]+)\.', image_path)
    if match:
        return match.group(1)
    return "X"
