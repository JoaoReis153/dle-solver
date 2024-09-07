from getSolution import getSolution

import re



class Champion:
    def __init__(self, fromString):
       self.attributes = fromString.split(":")

        # Now, apply split only to those attributes that are still strings
       self.attributes = [attr.split(",") if attr is not None else "" for attr in self.attributes]


       c = 0
       for a in self.attributes:
           for b in a:
               c+=1
       self.count = c
       aux = [item[0] if len(item) == 1 else item for item in self.attributes]
       self.attributes = aux

    def __str__(self):
        return f"{self.attributes}"



class Answer:
    def __init__(self, championsList):
        self.possibleChampions = championsList
        self.possibleChampions.sort(key=lambda x: x.count, reverse = True)

    def getAttributesLength(self):
        return len(self.possibleChampions[0].attributes)

    def getChampByName(self, name):
        for champion in self.possibleChampions:
            if champion.attributes[0].strip() == name.strip():
                return champion

    def getChamp(self, attributes):
        found = False
        for champion in self.possibleChampions:
            for i in range(len(attributes)):
                if(attributes[i] != champion.attributes[i+1]):
                    found = False
                    break
                else:
                    found = True

            if found:
                return champion

    def gotGreen(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1:
                
                if(possibleChampion.attributes[index] == champion.attributes[index]):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions

    def gotRed(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:

            possible_attrs = possibleChampion.attributes[index] if isinstance(possibleChampion.attributes[index], list) else possibleChampion.attributes[index].split(",")

                
            champion_attrs = champion.attributes[index] if isinstance(champion.attributes[index], list) else champion.attributes[index].split(",")

            for possibleAttribute in possible_attrs:
                    condition = any(possibleAttribute in sublist if isinstance(sublist, list) else possibleAttribute == sublist for sublist in champion_attrs)
            
                    if not condition:
                        newPossibleChampions.append(possibleChampion)
                        break
                    else:
                        break



        self.possibleChampions = newPossibleChampions

    def gotYellow(self, champion, index):

        newPossibleChampions = []



        for possibleChampion in self.possibleChampions:

            if len(possibleChampion.attributes) != 1 and index < len(possibleChampion.attributes):

                possible_attrs = possibleChampion.attributes[index] if isinstance(possibleChampion.attributes[index], list) else possibleChampion.attributes[index].split(",")

                champion_attrs = champion.attributes[index] if isinstance(champion.attributes[index], list) else champion.attributes[index].split(",")

                for attribute in possible_attrs:
                    if attribute in champion_attrs:
                        newPossibleChampions.append(possibleChampion)
                        break

        self.possibleChampions = newPossibleChampions





    def gotInferiorDate(self, champion, index):
        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            print(possibleChampion)
            if len(possibleChampion.attributes) != 1:

                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index])
                givenChampionInt = convert_to_base_unit(champion.attributes[index])
            
                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) < float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def gotSuperiorDate(self, champion, index):

        newPossibleChampions = []
        for possibleChampion in self.possibleChampions:
            if len(possibleChampion.attributes) != 1 and len(possibleChampion.attributes) != 0:
                possibleChampionInt = convert_to_base_unit(possibleChampion.attributes[index])
                givenChampionInt = convert_to_base_unit(champion.attributes[index])

                if possibleChampionInt is None:
                    newPossibleChampions.append(possibleChampion)

                elif(float(possibleChampionInt) > float(givenChampionInt)):
                    newPossibleChampions.append(possibleChampion)

        self.possibleChampions = newPossibleChampions


    def remove(self, name):
        for champ in self.possibleChampions:
            if champ.attributes[0] == name:
                self.possibleChampions.remove(champ)
                return

    def addTry(self, champion, combination):
        combination = str(combination)

        if(combination == "ggggggg" or champion == None):
            return

        for i in range(0, len(combination)):
            k = i+1
            print(k)

            if(combination[i] == "g"):
                self.gotGreen(champion, k)
            if(combination[i] == "b"):
                self.gotRed(champion, k)
            if(combination[i] == "p"):
                self.gotYellow(champion, k)
            if(combination[i] == "i"):
                self.gotInferiorDate(champion, k)
            if(combination[i] == "s"):
                self.gotSuperiorDate(champion, k)



    def __str__(self):

        re=""
        for champ in self.possibleChampions:
            re += str(champ) + "\n"


        return f"{re}\n--------------------------------"


def runOnepiecedle(driver):
  url = "https://onepiecedle.net/classic"
  getSolution(driver, url, Champion, Answer)



def convert_to_base_unit(input_str):

    numbers = re.findall(r'[0-9.]+', input_str)
    if not numbers or "base64" in input_str:
        return None
        #return input_str

    input_str = input_str.strip().lower() 

    if 'cm' in input_str or 'm' in input_str or 'M' in input_str:
        return "".join(numbers) 

    if "B" in input_str or 'b' in input_str:
        value = float(input_str.replace('b', '').replace('B', '').strip())
        return str(int(value * 1000))
    
    return input_str




print(2 not in [1, [2, 4], 3])