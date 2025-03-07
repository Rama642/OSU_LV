"""
Zadatak 1.4.4 Napišite Python skriptu koja ce u  citati tekstualnu datoteku naziva ˇ song.txt.
Potrebno je napraviti rjecnik koji kao klju ˇ ceve koristi sve razli ˇ cite rije ˇ ci koje se pojavljuju u ˇ
datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijec (klju ˇ c) pojavljuje u datoteci. ˇ
Koliko je rijeci koje se pojavljuju samo jednom u datoteci? Ispišite ih.
"""

def main():
    dict = {}

    fhand = open ("song.txt")
    for line in fhand:
        #print(line)
        words = line.split(" ")
        #print(words)

        for word in words:
            word = word.strip()
            if word.endswith(','):
                word = word[0:-1]
            #print(word)
            dict[word] = 1 + dict.get(word, 0)

    fhand.close()

    #print(dict)

    lista = []
    for el in dict:
        if dict[el] == 1:
            lista.append(el)
         
    print(len(lista))
    print(lista)
    


main()