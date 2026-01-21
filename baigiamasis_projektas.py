import random

# Pradiniai duomenys
banko_balansas = 100
vartotojas_vardas = ""
vartotojas_pavarde = ""

def navigacija():
    global vartotojas_vardas, vartotojas_pavarde
    print(f"Gerb. {vartotojas_vardas} {vartotojas_pavarde}, pasirinkite:")
    print("1. Patikrinti banko balansą.")
    print("2. Įsidėti pinigų į banką.")
    print("3. Išsigryninti pinigus.")
    print("4. Pasikeisti vardą ir pavardę.")
    print("5. Investuoti.")
    atsakymas = int(input("Įveskite pasirinkimo numerį: "))

    if(atsakymas == 1):
        patikrinti_balansa()
    elif(atsakymas == 2):
        isideti_pinigu()
    elif(atsakymas == 3):
        issiimti_pinigu()
    elif(atsakymas == 4):
        vardo_pavardes_keitimo_tvirtinimas()
    elif(atsakymas == 5):
        investavimas()
    else:
        print("Prašome pasirinkti TIK vieną iš pateiktų variantų ir NIEKO kito")
        navigacija()

def ivesti_varda_pavarde():
    global vartotojas_vardas, vartotojas_pavarde
    while True:
        vartotojas_vardas = input("Prašome įvesti vardą: ").strip()
        vartotojas_pavarde = input("Prašome įvesti pavarde: ").strip()
        if vartotojas_vardas and vartotojas_pavarde:
            break
        else:
            print("Vardas ir pavardė negali būti tušti. Bandykite dar kartą.")
    navigacija()

def pagrindine_funkcija():
    ivesti_varda_pavarde()

def patikrinti_balansa():
    global banko_balansas
    print(f"Jūsų banko balansas yra: {banko_balansas} eurų")
    navigacija()

def isideti_pinigu():
    global banko_balansas
    while True:
        try:
            inesta_suma = float(input("Kokią sumą pinigų norite įsidėti į savo sąskaitą?"))
            if inesta_suma > 0:
                banko_balansas += inesta_suma
                print(f"Sąskaita sėkmingai papildyta {inesta_suma} eurų.")
                break
            else:
                print("Prašome įvesti teigiamą skaičių.")
        except ValueError:
            print("Prašome įvesti tinkamą skaičių.")
    navigacija()

def issiimti_pinigu():
    global banko_balansas
    while True:
        try:
            isimta_suma = float(input("Kokią sumą pinigų norite išsiimti iš savo sąskaitos?"))
            if(isimta_suma < 0):
                if(isimta_suma <= banko_balansas):
                    banko_balansas -= isimta_suma
                    print(f"Iš sąskaitos sėkmingai išsiimta {isimta_suma} eurų.")
                    break
                else:
                    print("Negalite išsiimti daugiau pinigų negu turite savo sąskaitoje.")
            else:
                print("Prašome įvesti teigiamą skaičių.")
        except ValueError:
            print("Prašome įvesti tinkamą skaičių.")
    navigacija()

def vardo_pavardes_keitimo_tvirtinimas():
    global banko_balansas
    try:
        print("Ar tikrai norite keisti savo paskyros vardą ir pavardę? Tai kainuos 50 eurų.")
        print("1. Taip")
        print("2. Ne")
        atsakymas = int(input("Pasirinkite variantą: "))
        if(atsakymas == 1):
            if(banko_balansas >= 50):
                banko_balansas -= 50
                ivesti_varda_pavarde()
        elif(atsakymas == 2):
            navigacija()
        else:
            print("Prašome pasirinkti '1' arba '2'.")
            vardo_pavardes_keitimo_tvirtinimas()
    except ValueError:
        print("Prašome pasirinkti '1' arba '2'.")
        vardo_pavardes_keitimo_tvirtinimas()

def investavimas():
    global banko_balansas
    try:
        print("Pasirinkite investavimo būdą:")
        print("1. Kriptovaliuta (aukšta rizika)")
        print("2. Akcijos (vidutinė rizika)")
        atsakymas = int(input("Pasirinkite variantą:"))
        if(atsakymas == 1):
            while True:
                try:
                    investuojama_suma = float(input("Įveskite investuojamą sumą: "))
                    if(investuojama_suma > 0):
                        if(investuojama_suma <= banko_balansas):
                            banko_balansas -= investuojama_suma
                            if(random.random() < 0.35):
                                laimejimas = investuojama_suma * 3
                                banko_balansas += laimejimas
                                print("Sveikiname!!! Jūs sėkmingai investavote.")
                                print(f"Jūsų banko balansas padidėjo {laimejimas} eurų")
                                print(f"Dabartinis jūsų banko balansas yra {banko_balansas} eurų")
                                navigacija()
                            else:
                                print("Apgailestaujame... Jums nepasisekė investuoti...")
                                print(f"Dabartinis jūsų banko balansas yra {banko_balansas} eurų")
                                navigacija()
                        else:
                            print("Jūsų įvesta investuojama suma yra didesnė negu jūsų dabartinis banko balansas. Prašome įvesti mažesnę sumą.")
                    else:
                        print("Prašome įvesti teigiamą skaičių")
                except ValueError:
                    print("Prašome įvesti skaičių be jokių raidžių ar simbolių.")
        elif(atsakymas == 2):
            while True:
                try:
                    investuojama_suma = float(input("Įveskite investuojamą sumą: "))
                    if(investuojama_suma > 0):
                        if(investuojama_suma <= banko_balansas):
                            banko_balansas -= investuojama_suma
                            if(random.random() < 0.5):
                                laimejimas = investuojama_suma * 2
                                banko_balansas += laimejimas
                                print("Sveikiname!!! Jūs sėkmingai investavote.")
                                print(f"Jūsų banko balansas padidėjo {laimejimas} eurų")
                                print(f"Dabartinis jūsų banko balansas yra {banko_balansas} eurų")
                                navigacija()
                            else:
                                print("Apgailestaujame... Jums nepasisekė investuoti...")
                                print(f"Dabartinis jūsų banko balansas yra {banko_balansas} eurų")
                                navigacija()
                        else:
                            print("Jūsų įvesta investuojama suma yra didesnė negu jūsų dabartinis banko balansas. Prašome įvesti mažesnę sumą.")
                    else:
                        print("Prašome įvesti teigiamą skaičių")
                except ValueError:
                    print("Prašome įvesti skaičių be jokių raidžių ar simbolių.")
        else:
            print("Prašome pasirinkti '1' arba '2'.")
            investavimas()
    except ValueError:
        print("Prašome pasirinkti '1' arba '2'.")
        investavimas()

if __name__ == "__main__":
    pagrindine_funkcija()