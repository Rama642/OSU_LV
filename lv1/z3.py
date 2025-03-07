"""
Zadatak 1.4.3 Napišite program koji od korisnika zahtijeva unos brojeva u beskonacnoj petlji ˇ
sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
(npr. slovo umjesto brojke) na nacin da program zanemari taj unos i ispiše odgovaraju ˇ cu poruku.
"""
import math

def main():
    lista = []

    while True:
        unos = input()
        
        if unos == "Done":
            break
        else:
            try:
                lista.append(int(unos))
            except:
                print("unesi integer!")

    print(f"Korisnik je unjeo {len(lista)} brojeva!")
    print(f"Min: {min(lista)}")
    print(f"Max: {max(lista)}")
    print(f"Avg: {sum(lista)/len(lista)}")
    lista.sort()
    print(lista)

main()