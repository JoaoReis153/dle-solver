import re
from utils import convert_to_base_unit

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


class BaseAnswer:
    def __init__(self, championsList):
        self.possibleChampions = championsList
        self.possibleChampions.sort(key=lambda x: x.count, reverse=True)

    def arcList(self):
        """This property should be implemented by child classes to provide the arcList."""
        pass


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


    def gotInferiorDate(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            print(possibleChampion)
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:

                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index], self.arcList())
                givenChampionInt = convert_to_base_unit(champion.attributes[index], self.arcList())

                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperiorDate(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index], self.arcList())
                givenChampionInt = convert_to_base_unit(champion.attributes[index], self.arcList())

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
                self.gotInferiorDate(champion, k)
            elif char == "s":
                self.gotSuperiorDate(champion, k)

    def __str__(self):
        return "\n".join(str(champ) for champ in self.possibleChampions) + "\n--------------------------------"

