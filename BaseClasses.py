import re

class Champion:
    def __init__(self, fromString):
        self.attributes = fromString.split(":")
        self.attributes = [attr.split(",") if attr is not None else "" for attr in self.attributes]
        c = 0
        for a in self.attributes:
            for b in a:
                c += 1
        self.count = c
        aux = [item[0] if len(item) == 1 else item for item in self.attributes]
        self.attributes = aux

    def __str__(self):
        return f"{self.attributes}"


class Answer:
    def __init__(self, championsList, arcList):
        self.arcList = arcList
        self.possibleChampions = championsList
        self.possibleChampions.sort(key=lambda x: x.count, reverse=True)


    def getAttributesLength(self):
        return len(self.possibleChampions[0].attributes)

    def getChampByName(self, name):
        for champion in self.possibleChampions:
            if champion.attributes[0].strip() == name.strip():
                return champion

    def getChamp(self, attributes):
        for champion in self.possibleChampions:
            if all(attr == champ_attr for attr, champ_attr in zip(attributes, champion.attributes[1:])):
                return champion

    def gotGreen(self, champion, index):
        self.possibleChampions = [pc for pc in self.possibleChampions
                                  if len(pc.attributes) != 1 and pc.attributes[index] == champion.attributes[index]]

    def gotRed(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            possible_attrs = possibleChampion.attributes[index] if isinstance(possibleChampion.attributes[index], list) else possibleChampion.attributes[index].split(",")
            champion_attrs = champion.attributes[index] if isinstance(champion.attributes[index], list) else champion.attributes[index].split(",")
            if not any(attr in champion_attrs for attr in possible_attrs):
                newPossibleChampions.append(possibleChampion)
        self.possibleChampions = newPossibleChampions


    def gotYellow(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and index < len(possibleChampion.attributes):
                possible_attrs = possibleChampion.attributes[index] if isinstance(possibleChampion.attributes[index], list) else possibleChampion.attributes[index].split(",")
                champion_attrs = champion.attributes[index] if isinstance(champion.attributes[index], list) else champion.attributes[index].split(",")
                if any(attr in champion_attrs for attr in possible_attrs):
                    newPossibleChampions.append(possibleChampion)
        self.possibleChampions = newPossibleChampions


    def gotInferior(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:

                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index], self.arcList)
                givenChampionInt = convert_to_base_unit(champion.attributes[index], self.arcList)
                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperior(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index], self.arcList)
                givenChampionInt = convert_to_base_unit(champion.attributes[index], self.arcList)

                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) > float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions

    def remove(self, name):
        self.possibleChampions = [champ for champ in self.possibleChampions if champ.attributes[0] != name]

    def addTry(self, champion, combination):
        if combination == "ggggggg" or champion is None:
            return
        for i, char in enumerate(combination):
            k = i + 1
            if char == "g":
                self.gotGreen(champion, k)
            elif char == "b":
                self.gotRed(champion, k)
            elif char == "p":
                self.gotYellow(champion, k)
            elif char == "i":
                self.gotInferior(champion, k)
            elif char == "s":
                self.gotSuperior(champion, k)

    def __str__(self):
        return "\n".join(str(champ) for champ in self.possibleChampions) + "\n--------------------------------"



def convert_to_base_unit(input_str, arcList=[]):

    numbers = re.findall(r'\d+', input_str)
    if not numbers:
        return None

    content = int("".join(numbers))
    
    if arcList is not None:
        if input_str in arcList:
            return arcList.index(input_str)
        elif "base64" in input_str:
            return None

    if 'cm' in input_str:
        cm_value = int(re.sub(r'\D', '', input_str))
        value = cm_value / 100
    
    elif 'm' in input_str:
        parts = re.findall(r'\d+', input_str)
        meters = int(parts[0])
        centimeters = int(parts[1]) if len(parts) > 1 else 0
        value = meters + centimeters / 100

    elif 'kg' in input_str:
        kg_value = float(re.sub(r'\D', '', input_str))
        value = kg_value

    elif "B" in input_str or 'b' in input_str:
        value = str(int(content * math.pow(10, 9)))

    elif "M" in input_str:
        value = str(int(content * math.pow(10, 6)))
    
    else:
        return None

    return value

