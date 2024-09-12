from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

from Solves.solveLoldle import runLoldle
from Solves.solvePokedle import runPokedle
from Solves.solveSmashdle import runSmashdle
from Solves.solveDotadle import runDotadle
from Solves.solveOnepiecedle import runOnepiecedle
from Solves.solveNarutodle import runNarutodle

import time

def runOneAtATime(lst):

    options = webdriver.ChromeOptions()
    #ptions.add_argument("--headless")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    #runLoldle(driver)
    #runPokedle(driver)
    #runSmashdle(driver)
    #runDotadle(driver)
    #runOnepiecedle(driver)
    runNarutodle(driver)

    driver.quit()
