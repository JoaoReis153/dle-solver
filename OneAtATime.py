import time
from utils import getNameFromUrl
from getSolution import getSolution
from BaseClasses import Champion
from getNames import newDriver
def runOneAtATime(lst):

    arcList = []
    options, driver, wait = newDriver()

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

        getSolution(options, driver, wait, site, Champion, arcList)
        print("------------------------------------------")

    driver.quit()
