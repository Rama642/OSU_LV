"""
Zadatak 1.4.5 Napišite Python skriptu koja ce u ´ citati tekstualnu datoteku naziva ˇ SMSSpamCollection.txt
[1]. Ova datoteka sadrži 5574 SMS poruka pri cemu su neke ozna ˇ cene kao ˇ spam, a neke kao ham.
Primjer dijela datoteke:
ham Yup next stop.
ham Ok lar... Joking wif u oni...
spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken’s stuff!
12 Poglavlje 1. Uvod u programski jezik Python
a) Izracunajte koliki je prosje ˇ can broj rije ˇ ci u SMS porukama koje su tipa ham, a koliko je ˇ
prosjecan broj rije ˇ ci u porukama koje su tipa spam. ˇ
b) Koliko SMS poruka koje su tipa spam završava usklicnikom ?
"""

def main():

    fhand = open ("SMSSpamCollection.txt")

    hamList = []
    spamList = []
    all = []
    for line in fhand:
        all.append(line)
        if line.startswith("ham"):
            hamList.append(line)
        if line.startswith("spam"):
            spamList.append(line)




    fhand.close()

    sumHam = 0
    sumSpam = 0
    countExclamation = 0

    for message in hamList:
        sumHam += len(message.split(" "))

    for message in spamList:
        sumSpam += len(message.split(" "))
        if message.strip()[-1] == "!":
            countExclamation += 1

    print(f"Prosjek rijeci u ham: {sumHam/len(hamList)}")
    print(f"Prosjek rijeci u spam: {sumSpam/len(spamList)}")
    print(f"Broj usklicnika na kraju poruke u spam: {countExclamation}")
main()