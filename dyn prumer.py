def dynamic_average(novy_cislo, okno, dy_prumer):
    return ((dy_prumer * okno) + novy_cislo) / (okno + 1)

pocet_cisel = int(input("Zadej počet čísel: "))
okno = int(input("Zadej délku okna pro výpočet dynamického průměru: "))
cisla = []
for i in range(pocet_cisel):
    cislo = float(input(f"Zadejte {i+1}. číslo: "))
    cisla.append(cislo)

dy_prumer = 0
for i, cislo in enumerate(cisla):
    if i < okno:
        dy_prumer = dynamic_average(cislo, i, dy_prumer)
    else:
        dy_prumer = dynamic_average(cislo, okno, dy_prumer)
    print("Dynamický průměr:", dy_prumer)