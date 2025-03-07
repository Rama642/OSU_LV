"""
Zadatak 1.4.2 Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja
nekakvu ocjenu i nalazi se izmedu 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju ¯
sljedecih uvjeta: 
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
Takoder, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovaraju ¯ cu poruku.
"""

def main():
    print("Unesi broj")
    broj = input()


    try:
        broj = float(broj)
    
    except:
        print("Nije unesen broj")1

    
    if broj > 1 or broj < 0:
        print(f"Broj {broj} je van intervala [0, 1]")
        return

    if broj <= 1.0 and broj >= 0.9:
        print("A")
    elif broj < 0.9 and broj >= 0.8:
        print("B")
    elif broj < 0.8 and broj >= 0.7:
        print("C")
    elif broj < 0.7 and broj >= 0.6:
        print("D")
    elif broj < 0.6 and broj >= 0.0:
        print("F")




main()