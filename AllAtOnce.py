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


import concurrent.futures
from pathlib import Path

from utils import getFileFromLink, getLastChampGiven, processGuess, sendGuess, Print
from objects import Champion, Answer



def getWebConfig():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def runAllAtOnce(lst):
    # Use ThreadPoolExecutor to run multiple instances of getSolution concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
    # Map each site to the getSolution function and execute them
        futures = {executor.submit(getSolution, site, index): index for index, site in enumerate(lst)}


def getSolution(url, index, FIRSTGUESS = "", showPrints = True):
    print(index)
    file = getFileFromLink(url)
    # Your URL

    champions=[]

    #Load file
    with open(file, "r") as f:
        content = (f.read()).split("\n")

    for line in content:
        champions.append(Champion(line.replace(", ", ",")))

    answer = Answer(champions)

    driver = getWebConfig()
    driver.get(url)
    # Screen dimensions (you might want to adjust these based on your screen resolution)
    #screen_width = 1440
    #screen_height = 850
    screen_width = 1920
    screen_height = 1080
    # Window sizes (width, height)
    window_size = (screen_width/2, screen_height/2)

    d = index%2 == 0
    driverWindowPosition = (0,0)
    if(not d):
        if(index == 1):
            driverWindowPosition = (screen_width - window_size[0], 0 )
        else:
            driverWindowPosition = (screen_width - window_size[0], screen_height - window_size[1] )
    else:
       if(index == 0):
           driverWindowPosition = (0, 0 )
       else:
           driverWindowPosition = (0, screen_height - window_size[1] )

    #window_size = (screen_width, screen_height)
    #driverWindoPosition = (0,0)
    driver.set_window_size(*window_size)
    driver.set_window_position(*driverWindowPosition)
    print("size")



    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)

    driver.implicitly_wait(5)

    button = driver.find_element(By.CLASS_NAME, "fc-button-label")

    button.click()

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

    while(len(colors) != 7):
        guess, colors = processGuess(showPrints, answer, driver)

    while colors != "ggggggg" :
        answer.addTry(guess, colors)

        print(answer)
        if(len(answer.possibleChampions) == 0 or colors == "ggggggg"):
            Print(showPrints, "Answer not found")
            break

        guess = answer.possibleChampions[0].attributes[0]
        sendGuess(showPrints, driver, input_element, guess, answer)
        guess, colors = processGuess(showPrints, answer, driver)

    if colors == "ggggggg":
        Print(showPrints, ".")
        Print(showPrints, "You won")
        Print(showPrints, ".")


    time.sleep(5)

    driver.quit()



