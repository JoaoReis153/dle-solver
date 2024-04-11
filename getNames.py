import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import string
import pyautogui

import os, types

from utils import getFileFromLink, getFileNameFromLink

start_time = time.time()

def loadDatabase(answer, site):

    #fileName = "C:/Users/joaos/My Drive/Pessoal/Coding/Webscrapping/database.txt"
    print(getFileFromLink(site))

    # Construct the file path
    file = getFileFromLink(site)
    #file = os.path.join("./Database", file_name)

    print(file)
    # Ensure the existing file is removed before starting
    if os.path.exists(file):
        print("ola")
        os.remove(file)

    data = []

    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(site)

    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 5)

    try:
        pop_up_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-button-label")))
        pop_up_button.click()
    except TimeoutException:
        print("No pop-up found or error in closing pop-up.")

    alphabet = list(string.ascii_lowercase)

    print("Fetching names...")
    for a in alphabet:
        input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='IZ-select__input-wrap']//input")))
        input_element.clear()
        input_element.send_keys(a)
        
        time.sleep(2)
        champions = driver.find_elements(By.CLASS_NAME, 'IZ-select__item')

        for champion in champions:
            print("")
            print(champion.text)
            champion_name = champion.text.strip().replace("\nAlias", "")

            champion_name = champion_name.split(":")[0] if ":" in champion_name else champion_name
            

            if champion_name not in data and champion_name != '':
                data.append(champion_name.strip())

    for a in data:
        print("-")
        print(a)



    input_element.clear()

    if(answer in data):
        data.remove(answer)
        data.append(answer)

    print("Waiting for data...")
    

    
    
    for name in data:
        input_element.send_keys(name)
        wait = WebDriverWait(driver, 10)
        send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "guess-button")))
        wait.until(EC.invisibility_of_element((By.CLASS_NAME, "tooltip-inner")))  
        #actions.move_to_element(send_button).perform()
        send_button.click()
        #if send_button != None: send_button.click()
        #else: input_element.send_keys(Keys.ENTER)
        

    time.sleep(1)


    championsInfoList = driver.find_elements(By.CSS_SELECTOR, ".classic-answer")

    infos = []

    print("Fetching data...")
    for championInfo in championsInfoList:

        attributes_squares = championInfo.find_elements(By.CSS_SELECTOR, ".square")

        nameElement = championInfo.find_element(By.CSS_SELECTOR, ".square-container .square .champion-icon-name")

        info = nameElement.get_attribute("textContent").strip() + ":"

        for square in attributes_squares:
            # Extract text from each 'square' which might contain the attribute information
            if(square.text.strip() != ""):
                    info += square.text.strip() + ":"

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

    driver.quit()