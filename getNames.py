import time
import os
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementNotInteractableException, NoSuchElementException, NoSuchWindowException, WebDriverException

from utils import getFileFromLink, newDriver, removePopUp


start_time = time.time()

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

def loadDatabase(site):

    # Construct the file path
    file = getFileFromLink(site)

    print("Loading names into: " + str(file))

    # Ensure the existing file is removed before starting
    if os.path.exists(file):
        os.remove(file)

    options, driver, wait = newDriver(site)

    removePopUp(driver, wait)

    namesData = fetchAllNames(driver, wait)

    driver = spamNames(driver, namesData, site, wait)

    fetchInfo(driver, wait, file)

    driver.quit()

def fetchInfo(driver, wait, file):
    print("-> Fetching data\n")
    time.sleep(1)
    championsInfoList = driver.find_elements(By.CSS_SELECTOR, ".classic-answer")

    infos = []

    for championInfo in championsInfoList:

        attributes_squares = championInfo.find_elements(By.CSS_SELECTOR, ".square")

        nameElement = championInfo.find_element(By.CSS_SELECTOR, ".square-container .square .champion-icon-name")


        info = nameElement.get_attribute("textContent").strip() 

        print(info)

        info += ":"

        for square in attributes_squares:
            # Extract text from each 'square' which might contain the attribute information


            square_text = square.text.strip()

            if(square_text != ""):
                    info += square_text + ":"
            else:
                try:
                    images = square.find_elements(By.TAG_NAME, "img")
                    #.get_attribute("src")

                    keywords = ["Armament", "Observation", "Conqueror", "base64"]
                    owns = []
                    for keyword in keywords:
                        for image in images:
                            image_src = image.get_attribute("src")
                            if keyword in image_src:
                                owns.append(keyword)


                    info += ",".join(owns) + ":"


                except:
                    pass


        info = info.split(":")
        if len(info) > 9:
            del info[1]
        info = ":".join(info)



        infos.append(info[:-1].replace("\n", " "))

    infos.sort()

    print()
    print("Writing in the file...")
    with open(file, 'w') as f:
        f.write("\n".join(infos))

    # End timing
    end_time = time.time()

    # Calculate the duration
    duration = end_time - start_time

    print("Fetching data <-\n")

    print(f"The algorithm took {duration} seconds.\n")


def fetchAllNames(driver, wait, spamLettersRate = 0.1):

    data = []

    alphabet = list(string.ascii_lowercase)

    print("\n-> Fetching names")
    for letter in alphabet:

        print(RESET + letter.upper() + ":" + RESET)
        input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
        input_element.clear()
        input_element.send_keys(letter)

        time.sleep(spamLettersRate)
        champions = driver.find_elements(By.CLASS_NAME, 'IZ-select__item')

        for champion in champions:
            #Remove useless whitespaces
            driver.execute_script("arguments[0].scrollIntoView(true);", champion)


            if(len(champion.text) != 0):

                if(champion.text[0] == letter.upper()):
                    print(GREEN + champion.text + GREEN)
                    champion_name = champion.text.strip()


                    champion_name = champion_name.split(":")[0] if ":" in champion_name else champion_name

                    if champion_name not in data and champion_name != '':
                        data.append(champion_name.strip())

                else:
                    print(RED + champion.text + RED)



    print(RESET)
    input_element.clear()
    print("Fetching names <-")
    return data


def spamNames(driver, data,  site, wait, answer = "", spamNamesRate = 0):
    finished = False
    winnerName = ""
    newData = data.copy()
    while not finished:
        if winnerName == "": print("-> Looking for the winner\n")
        else: print("-> Spamming names \n")
        try:

            waitList = len(data)
            for name in newData:
                if finished:
                    break

                print(name)

                input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
                input_element.send_keys(name)

                send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "guess-button")))

                wait.until(EC.invisibility_of_element((By.CLASS_NAME, "tooltip-inner")))

                send_button.click()

                time.sleep(spamNamesRate)

            print("\nSpamming names <-")
            finished = True


        except (TimeoutException, StaleElementReferenceException, ElementNotInteractableException):

            if waitList == 0:
                finished = True

            else:
                winner = driver.find_elements(By.CLASS_NAME, "gg-name")
                if winner:
                    winnerName = winner[0].text
                    print("\nLooking for the winner <- (" + winnerName + ")")

                    time.sleep(1)

                    newData.remove(winnerName)
                    newData.append(winnerName)

                driver.quit()
                options, driver, wait = newDriver(driver, wait, site)

    return driver


