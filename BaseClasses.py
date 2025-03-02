import re
import copy

class Champion:
    def __init__(self, fromString):
        self.attributes = [attr.split(",") if attr else [] for attr in fromString.split(":")]
        self.score = sum(len(attr) for attr in self.attributes)
        self.attributes = [item[0] if len(item) == 1 else item for item in self.attributes]

    def __str__(self):
        return f"{self.attributes}"

class Database:
    def __init__(self, championsList, url):
        self.url = url
        self.possibleChampions = sorted(championsList, key=lambda x: x.score, reverse=True)

    def copy(self):
        return Database(copy.deepcopy(self.possibleChampions), self.url)

    def getAttributesLength(self):
        return len(self.possibleChampions[0].attributes)

    def getChampByName(self, name):
        return next((champ for champ in self.possibleChampions if champ.attributes[0].strip() == name.strip()), None)

    def filterChampions(self, condition):
        self.possibleChampions = [champ for champ in self.possibleChampions if condition(champ)]

    def gotGreen(self, champion, index):
        self.filterChampions(lambda champ: champ.attributes[index] == champion.attributes[index])
        
    def gotRed(self, champion, index):
        champion_attrs = self._getAttributes(champion, index)
        self.filterChampions(lambda champ: not any(attr in champion_attrs for attr in self._getAttributes(champ, index)))
        
    def gotYellow(self, champion, index):
        champion_attrs = self._getAttributes(champion, index)
        self.filterChampions(lambda champ: any(attr in champion_attrs for attr in self._getAttributes(champ, index)))
        
    def gotInferior(self, champion, index):
        given_value = convert_to_base_unit(champion.attributes[index], self.url)
        self.filterChampions(lambda champ: self._compareValues(champ.attributes[index], given_value, "inferior"))
        
    def gotSuperior(self, champion, index):
        given_value = convert_to_base_unit(champion.attributes[index], self.url)
        self.filterChampions(lambda champ: self._compareValues(champ.attributes[index], given_value, "superior"))
        
    def addTry(self, champion, combination):
        if not champion:
            return
        for i, char in enumerate(combination):
            index = i + 1
            if char == "g":
                self.gotGreen(champion, index)
            elif char == "b":
                self.gotRed(champion, index)
            elif char == "p":
                self.gotYellow(champion, index)
            elif char == "i":
                self.gotInferior(champion, index)
            elif char == "s":
                self.gotSuperior(champion, index)

    def __str__(self):
        return "\n".join(str(champ) for champ in self.possibleChampions) + "\n--------------------------------"

    def _getAttributes(self, champion, index):
        attr = champion.attributes[index]
        return attr if isinstance(attr, list) else attr.split(",")

    def _compareValues(self, champ_attr, given_value, comparison):
        champ_value = convert_to_base_unit(champ_attr, self.url)
        if champ_value is None:
            return True
        if comparison == "inferior":
            return float(champ_value) < float(given_value)
        elif comparison == "superior":
            return float(champ_value) > float(given_value)
        return False

def convert_to_base_unit(input_str, url):
    numbers = re.findall(r'\d+', input_str)
    arcList = []

    if "onepiecedle.net/classic" in url:
        arcList = [
            'Romance Dawn', 'Orange Town', 'Syrup Village', 'Baratie', 'Arlong Park', 'Loguetown',
            'Reverse Mountain', 'Whisky Peak', 'Little Garden', 'Drum Island', 'Arabasta', 'Jaya',
            'Skypiea', 'Long Ring Long Land', 'Water 7', 'Enies Lobby', 'Post-War', 'Thriller Bark',
            'Sabaody Archipelago', 'Amazon Lily', 'Impel Down', 'Return to Sabaody', 'Fish-Man Island',
            'Punk Hazard', 'Dressrosa', 'Zou', 'Whole Cake Island', 'Wano Country'
        ]
    elif "naruto.lol/classic" in input_str:
        arcList = [
            "Prologue", "Chūnin Exams", "Konoha Crush", "Search for Tsunade", "Sasuke Recovery Mission",
            "Kazekage Rescue Mission", "Tenchi Bridge Reconnaissance Mission", "Akatsuki Suppression Mission",
            "Itachi Pursuit Mission", "Fated Battle Between Brothers", "Tale of Jiraiya the Gallant",
            "Pain's Assault", "Five Kage Summit", "Countdown", "Climax", "Kakashi Gaiden",
            "Birth of the Ten-Tails' Jinchūriki", "Kaguya Ōtsutsuki Strikes"
        ]


    if input_str in arcList:
        return arcList.index(input_str)

    if not numbers:
        return None

    content = int("".join(numbers))

    if 'cm' in input_str:
        return int(re.sub(r'\D', '', input_str)) / 100
    elif 'm' in input_str:
        parts = re.findall(r'\d+', input_str)
        return int(parts[0]) + (int(parts[1]) / 100 if len(parts) > 1 else 0)
    elif 'kg' in input_str:
        return float(re.sub(r'\D', '', input_str))
    elif "B" in input_str or 'b' in input_str:
        return str(int(content * 10**9))
    elif "M" in input_str:
        return str(int(content * 10**6))
    else:
        return None