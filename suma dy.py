suma = 0
while True:
    cislo = input("Zadejte číslo pro sečtení (nebo 'konec' pro ukončení): ")
    if cislo.lower() == "konec":
        break
    try:
         cislo = int(cislo)
    except ValueError:
          print("Zadaná hodnota není platné číslo.")
          continue

    suma += cislo
print(f"Výsledná suma: ", (suma))


