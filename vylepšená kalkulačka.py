def kalkulacka():
    while True:
        print("Vyber operaci:")
        print("1. Sčítání")
        print("2. Odčítání")
        print("3. Násobení")
        print("4. Dělení")
        print("5. Zjištění intervalu")
        print("6. Konec")

        volba = input("Zadej číslo operace (1-6): ")

        if volba == '6':
            print("Konec programu.")
            break

        if volba in ('1', '2', '3', '4'):
            cislo1 = float(input("Zadej první číslo: "))
            cislo2 = float(input("Zadej druhé číslo: "))

            if volba == '1':
                vysledek = cislo1 + cislo2
                print("Výsledek: {}".format(vysledek))
            elif volba == '2':
                vysledek = cislo1 - cislo2
                print("Výsledek: {}".format(vysledek))
            elif volba == '3':
                vysledek = cislo1 * cislo2
                print("Výsledek: {}".format(vysledek))
            elif volba == '4':
                if cislo2 != 0:
                    vysledek = cislo1 / cislo2
                    print("Výsledek: {}".format(vysledek))
                else:
                    print("Nelze dělit nulou!")

        elif volba == '5':
            cislo = float(input("Zadej číslo: "))
            interval_min = float(input("Zadej minimum intervalu: "))
            interval_max = float(input("Zadej maximum intervalu: "))

            if interval_min <= cislo <= interval_max:
                print("{} se nachází v zadaném intervalu.".format(cislo))
            else:
                print("{} se nenachází v zadaném intervalu.".format(cislo))

        else:
            print("Neplatná volba. Zkus to znovu.")

# Spustíme kalkulačku
kalkulacka()
