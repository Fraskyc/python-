while True:
    try:
        znamenko = input("Zadejte operaci (+, -, *, /) nebo 'spoj' pro spojení řetězců: ")

        if znamenko == '+':
            cislo1 = float(input("Zadejte první číslo: "))
            cislo2 = float(input("Zadejte druhé číslo: "))
            vysledek = cislo1 + cislo2
        elif znamenko == '-':
            cislo1 = float(input("Zadejte první číslo: "))
            cislo2 = float(input("Zadejte druhé číslo: "))
            vysledek = cislo1 - cislo2
        elif znamenko == '*':
            cislo1 = float(input("Zadejte první číslo: "))
            cislo2 = float(input("Zadejte druhé číslo: "))
            vysledek = cislo1 * cislo2
        elif znamenko == '/':
            cislo1 = float(input("Zadejte první číslo: "))
            cislo2 = float(input("Zadejte druhé číslo: "))
            if cislo2 == 0:
                print("Nelze dělit nulou!")
                continue
            vysledek = cislo1 / cislo2
        elif znamenko == 'spoj':
            retezec1 = input("Zadejte první řetězec: ")
            retezec2 = input("Zadejte druhý řetězec: ")
            vysledek = retezec1 + " " + retezec2
        else:
            print("Neplatný operátor!")
            continue

        print("Výsledek: ", vysledek)

    except ValueError:
        print("Zadejte platné číslo!")
