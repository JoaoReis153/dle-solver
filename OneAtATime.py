from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from utils import getNameFromUrl
from getSolution import getSolution
import time
from BaseClasses import Champion

def runOneAtATime(lst):

    options = webdriver.ChromeOptions()
    #ptions.add_argument("--headless")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    arcList = []
    for site in lst:
        print("------------------------------------------")
        print("Solving " + getNameFromUrl(site) + "...")
        name = getNameFromUrl(site)
        if "onepiece" in name:
            arcList =  [
                        'Romance Dawn',
                        'Orange Town',
                        'Syrup Village',
                        'Baratie',
                        'Arlong Park',
                        'Loguetown',
                        'Reverse Mountain',
                        'Whisky Peak',
                        'Little Garden',
                        'Drum Island',
                        'Arabasta',
                        'Jaya',
                        'Skypiea',
                        'Long Ring Long Land',
                        'Water 7',
                        'Enies Lobby',
                        'Post-War',
                        'Thriller Bark',
                        'Sabaody Archipelago',
                        'Amazon Lily',
                        'Impel Down',
                        'Return to Sabaody',
                        'Fish-Man Island',
                        'Punk Hazard',
                        'Dressrosa',
                        'Zou',
                        'Whole Cake Island',
                        'Wano Country'
                    ]

            getSolution(driver, site, Champion, arcList)
        elif "naruto" in name: 
            arcList = [
                        "Prologue",
                        "Chūnin Exams",
                        "Konoha Crush",
                        "Search for Tsunade",
                        "Sasuke Recovery Mission",
                        "Kazekage Rescue Mission",
                        "Tenchi Bridge Reconnaissance Mission",
                        "Akatsuki Suppression Mission",
                        "Itachi Pursuit Mission",
                        "Fated Battle Between Brothers",
                        "Tale of Jiraiya the Gallant",
                        "Pain's Assault",
                        "Five Kage Summit",
                        "Countdown",
                        "Climax",
                        "Kakashi Gaiden",  # Flashback arc
                        "Birth of the Ten-Tails' Jinchūriki",
                        "Kaguya Ōtsutsuki Strikes"
                    ]

        getSolution(driver, site, Champion, arcList)

    driver.quit()
