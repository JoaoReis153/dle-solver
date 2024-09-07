import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import string
import pyautogui

import os, types

from utils import getFileFromLink, getFileNameFromLink

start_time = time.time()

showProcess = False

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'  

waitTimeToLookForInputBox = 5  # seconds to wait for input box to appear

def loadDatabase(site):

    # Construct the file path
    file = getFileFromLink(site)

    print("Loading names into: " + str(file))

    # Ensure the existing file is removed before starting
    if os.path.exists(file):
        os.remove(file)

    options = webdriver.ChromeOptions()
    if(showProcess == True): options.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(site)

    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 5)

    removePopUp(driver, wait)

    namesData = fetchAllNames(driver, wait)
    
    print("Waiting for data...")

    driver = spamNames(driver, namesData, site, wait)

    fetchInfo(driver, wait, file)

    driver.quit()

def fetchInfo(driver, wait, file):
    print("-> Fetching data")
    time.sleep(1)
    championsInfoList = driver.find_elements(By.CSS_SELECTOR, ".classic-answer")

    infos = []

    for championInfo in championsInfoList:

        attributes_squares = championInfo.find_elements(By.CSS_SELECTOR, ".square")

        nameElement = championInfo.find_element(By.CSS_SELECTOR, ".square-container .square .champion-icon-name")
        
        info = nameElement.get_attribute("textContent").strip() + ":"

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

    print("Writing in the file...")
    with open(file, 'w') as f:
        f.write("\n".join(infos))

    # End timing
    end_time = time.time()

    # Calculate the duration
    duration = end_time - start_time

    print(f"The algorithm took {duration} seconds.")


def fetchAllNames(driver, wait, spamLettersRate = 0.1):

    data = []

    alphabet = list(string.ascii_lowercase)

    print("-> Fetching names")
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
                print(champion.text)

                if(champion.text[0] == letter.upper()): 
                    print(GREEN + champion.text + GREEN)
                    champion_name = champion.text.strip()
                      

                    champion_name = champion_name.split(":")[0] if ":" in champion_name else champion_name

                    if champion_name not in data and champion_name != '':
                        data.append(champion_name.strip())

                else: 
                    print(RED + champion.text + RED) 

          
        print("\n")


    input_element.clear()
    print("Fetching names <-")
    return data

def resetDriver(driver, wait, site):
    driver.quit()

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    driver.get(site)
    wait = WebDriverWait(driver, waitTimeToLookForInputBox)

    removePopUp(driver, wait)

    return options, driver, wait



def spamNames(driver, data,  site, wait, answer = "", spamNamesRate = 0):
    print("-> Spamming names")
    finished = False
    winnerName = ""
    newData = data.copy()
    while not finished:
        try:  
            print("Try")
            waitList = len(data)
            for name in newData:
                if finished: 
                    break
                
                input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
                input_element.send_keys(name)

                send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "guess-button")))
                        
                wait.until(EC.invisibility_of_element((By.CLASS_NAME, "tooltip-inner")))  
            
                send_button.click()

                time.sleep(spamNamesRate)


            finished = True
            print("Finished 1")    
            

        except (TimeoutException, StaleElementReferenceException, ElementNotInteractableException):
            print("Exception")

            if waitList == 0: 
                finished = True
            
            else:
                winner = driver.find_elements(By.CLASS_NAME, "gg-name")
                if winner: 
                    winnerName = winner[0].text     
                    print("Winner: " + winnerName)

                    time.sleep(1)   

                    newData.remove(winnerName)                
                    newData.append(winnerName)

                options, driver, wait = resetDriver(driver, wait, site)
        
    return driver
    

 

def removePopUp(driver, wait):
    try:
        pop_up_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-button-label")))
        pop_up_button.click()
    except TimeoutException:
        print("No pop-up found or error in closing pop-up.")

    try:
        pop_up_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-button")))
        pop_up_button.click()
    except TimeoutException:
        print('No one piece "are you up to date" pop-up found.')


def extract_keywords_from_image_path(image_path):
    # Use regex to extract the word before the first dot in the filename
    match = re.search(r'/([^.\/]+)\.', image_path)
    if match:
        return match.group(1)
    return "X"
