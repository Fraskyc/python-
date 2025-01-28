import random

# Funkce pro výběr velikosti hracího pole
def vyber_velikosti():
    while True:
        velikost = input("Vyberte velikost hracího pole (malé/střední/velké): ")
        if velikost.lower() == "malé":
            return 4
        elif velikost.lower() == "střední":
            return 8
        elif velikost.lower() == "velké":
            return 16
        else:
            print("Zadejte prosím platnou velikost (malé/střední/velké)")

def vygeneruj_pole(velikost):
    """Funkce pro vygenerování pole s náhodně rozmístěnými symboly"""
    cisla = list(range(1, velikost*velikost//2 + 1))
    random.shuffle(cisla)
    pole = [cisla[:velikost//2] for i in range(velikost)]
    pole = [radek + radek for radek in pole]
    random.shuffle(pole)
    return pole

def vypis_hraci_pole(pole, velikost):
    """Funkce pro vypsání hracího pole"""
    for i in range(velikost):
        print(f"{i+1:2}", end=" ")
        for symbol in pole[i]:
            print(symbol, end=" ")
        print()

def vyhodnot(pole):
    """Funkce pro vyhodnocení stavu hry"""
    if all("-" not in radek for radek in pole):
        return "remiza"
    if any("X" in radek for radek in pole):
        return "prohra"
    if any("-" in radek for radek in pole):
        return "hraje se"
    return "vyhra"

def hra(velikost):
    """Funkce pro spuštění hry"""
    pole = vygeneruj_pole(velikost)
    skryta_pole = [["-" for i in range(velikost)] for j in range(velikost)]
    vypis_hraci_pole(skryta_pole, velikost)
    hrac = random.choice(["X"])
    while True:
        if hrac == "X":
            print("Hraje hráč X.")
        else:
            print("Hraje počítač.")
        radek1 = int(input("Zadej číslo řádku prvního políčka: ")) - 1
        sloupec1 = int(input("Zadej číslo sloupce prvního políčka: ")) - 1
        radek2 = int(input("Zadej číslo řádku druhého políčka: ")) - 1
        sloupec2 = int(input("Zadej číslo sloupce druhého políčka: ")) - 1
        if skryta_pole[radek1][sloupec1] != "-" or skryta_pole[radek2][sloupec2] != "-" or (radek1 == radek2 and sloupec1 == sloupec2):
            print("Neplatný tah, zadej políčka znovu.")
            continue
        skryta_pole[radek1][sloupec1] = pole[radek1][sloupec1]
        skryta_pole[radek2][sloupec2] = pole[radek2][sloupec2]
        vypis_hraci_pole(skryta_pole)
        if vyhodnot(skryta_pole) != "hraje se":
            vypis_hraci_pole(skryta_pole, velikost)
            print(vyhodnot(skryta_pole))
            break
        if hrac == "O":
            vypis_hraci_pole(skryta_pole, velikost)
        else:
            print("\n" * 20)
        hrac = "X" if hrac == "O" else "O"


# Funkce pro vytvoření hracího pole
def vytvor_hraci_pole(velikost):
    pole = []
    cisla = list(range(1, (velikost**2)//2 + 1)) * 2
    random.shuffle(cisla)
    for i in range(velikost):
        radek = []
        for j in range(velikost):
            radek.append(cisla.pop())
        pole.append(radek)
    return pole

# Funkce pro vykreslení hracího pole
def vykresli_pole(pole, skryta_pole):
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            if not skryta_pole[i][j]:
                print(pole[i][j], end="\t")
            else:
                print("X", end="\t")
        print()

# Funkce pro zjištění souřadnic políčka na hracím poli
def ziskej_souradnice(velikost):
    while True:
        try:
            x = int(input("Zadejte číslo řádku (1-{0}): ".format(velikost)))
            y = int(input("Zadejte číslo sloupce (1-{0}): ".format(velikost)))
            if x < 1 or x > velikost or y < 1 or y > velikost:
                raise ValueError
            return (x-1, y-1)
        except ValueError:
            print("Zadejte prosím platné souřadnice (1-{0})".format(velikost))

# Funkce pro zjištění, zda jsou dvě políčka stejná
def stejna_policka(pole, pozice1, pozice2):
    return pole[pozice1[0]][pozice1[1]] == pole[pozice2[0]][pozice2[1]]

# Hlavní funkce pro spuštění hry
def hraj_pexeso():
    velikost = vyber_velikosti()
    hraci_pole = vytvor_hraci_pole(velikost)
    skryta_pole = [[True] * velikost for i in range(velikost)]
    hrac_na_tahu = random.choice(["počítač", "hráč"])
    print("Hráč na tahu: {0}".format(hrac_na_tahu))
    while True:
        vykresli_pole(hraci_pole, skryta_pole)
        if hrac_na_tahu == "hráč":
            
            if hrac_na_tahu == "počítač":
                # Počítač náhodně vybere dvě různá skrytá políčka
                pozice1, pozice2 = None, None
                while pozice1 is None or pozice2 is None or pozice1 == pozice2 or not skryta_pole[pozice1[0]][pozice1[1]] or not skryta_pole[pozice2[0]][pozice2[1]]:
                    pozice1 = (random.randint(0, velikost-1), random.randint(0, velikost-1))
                    pozice2 = (random.randint(0, velikost-1), random.randint(0, velikost-1))
                print("Počítač vybral políčka: ({0}, {1}) a ({2}, {3})".format(pozice1[0]+1, pozice1[1]+1, pozice2[0]+1, pozice2[1]+1))
                if stejna_policka(hraci_pole, pozice1, pozice2):
                    print("Počítač našel pár!")
                    skryta_pole[pozice1[0]][pozice1[1]] = False
                    skryta_pole[pozice2[0]][pozice2[1]] = False
                else:
                    print("Počítač se spletl.")
                hrac_na_tahu = "hráč"
            else:
                # Hráč zvolí dvě různá skrytá políčka
                print("Hráč, je tvůj tah.")
                pozice1 = ziskej_souradnice(velikost)
                while not skryta_pole[pozice1[0]][pozice1[1]]:
                    print("Toto políčko už bylo odhaleno, vyberte jiné.")
                    pozice1 = ziskej_souradnice(velikost)
                pozice2 = ziskej_souradnice(velikost)
                while pozice1 == pozice2 or not skryta_pole[pozice2[0]][pozice2[1]]:
                    print("Toto políčko už bylo odhaleno nebo už jste zvolili stejné políčko jako první, vyberte jiné.")
                    pozice2 = ziskej_souradnice(velikost)
                if stejna_policka(hraci_pole, pozice1, pozice2):
                    print("Správně, našel jsi pár!")
                    skryta_pole[pozice1[0]][pozice1[1]] = False
                    skryta_pole[pozice2[0]][pozice2[1]] = False
                else:
                    print("Bohužel, tohle nejsou stejná políčka.")
        
            # Skrytá pole budou znovu skryta
            for radek in range(velikost):
                for sloupec in range(velikost):
                    if skryta_pole[radek][sloupec]:
                        hraci_pole[radek][sloupec] = "-"
            print(hraci_pole, velikost)

        else:
            # Pokud hráč ukončil hru, vypišeme mu výsledky
            skore_hrace = sum([radek.count(False) for radek in skryta_pole])
            skore_pocitace = velikost**2 // 2 - skore_hrace
            print("Hra skončila!")
            print("Tvé skóre: {0}".format(skore_hrace))
            print("Skóre počítače: {0}".format(skore_pocitace))
            if skore_hrace > skore_pocitace:
                print("Gratuluji, vyhrál jsi!")
            elif skore_hrace < skore_pocitace:
                print("Bohužel, prohrál jsi. Snad příště budeš mít víc štěstí.")
            else:
                print("Hra skončila remízou.")
            break

if __name__ == "__main__":
    hraj_pexeso()

   




                
