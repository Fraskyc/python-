filmy = []
videoteka = []

def pridat_film():
    název = input("Název filmu: ")
    režisér = input("Režisér: ")
    délka = input("Délka filmu: ")
    rok = input("Rok: ")
    kategorie = input("Kategorie: ")
    film = {
        "název": název,
        "režisér": režisér,
        "délka": délka,
        "rok": rok,
        "kategorie": kategorie
    }
    filmy.append(film)
    print(f"Film '{název}' byl přidán do videotéky.")

def upravit_film():
    název = input("Zadejte název filmu, který chcete upravit: ")
    for film in filmy:
        if film["název"] == název:
            nový_název = input("Nový název (nechte prázdné pro ponechání původní hodnoty): ")
            nový_režisér = input("Nový režisér (nechte prázdné pro ponechání původní hodnoty): ")
            nová_délka = input("Nová délka (nechte prázdné pro ponechání původní hodnoty): ")
            nový_rok = input("Nový rok (nechte prázdné pro ponechání původní hodnoty): ")
            nová_kategorie = input("Nová kategorie (nechte prázdné pro ponechání původní hodnoty): ")
            if nový_název != "":
                film["název"] = nový_název
            if nový_režisér != "":
                film["režisér"] = nový_režisér
            if nová_délka != "":
                film["délka"] = nová_délka
            if nový_rok != "":
                film["rok"] = nový_rok
            if nová_kategorie != "":
                film["kategorie"] = nová_kategorie
            print(f"Film '{název}' byl upraven.")
            return
    print(f"Film '{název}' nebyl nalezen.")

def smazat_film():
    název = input("Zadejte název filmu, který chcete smazat: ")
    for film in filmy:
        if film["název"] == název:
            filmy.remove(film)
            print(f"Film '{název}' byl smazán z videotéky.")
            return
    print(f"Film '{název}' nebyl nalezen.")

def vyhledat_film():
    
    název = input("Zadejte název filmu, který chcete najít: ")
    nalezeno = False
    for film in filmy:
        if název in film["název"]:
            print(f"- {film['název']}, {film['režisér']}, {film['délka']} minut, {film['rok']}, {film['kategorie']}")
        nalezeno = True
    if not nalezeno:
        print(f"Film s názvem '{název}' nebyl nalezen.")

def zobrazit_videotéku():
        if len(filmy) == 0:
            print("Videotéka je prázdná.")
        else:
            print("Filmy v videotéce:")
        for film in filmy:
            print(f"- {film['název']}, {film['režisér']}, {film['délka']} minut, {film['rok']}, {film['kategorie']}")


def menu():
    while True:
        print("\nCo chcete udělat?")
        print("1 - Přidat film")
        print("2 - Upravit film")
        print("3 - Smazat film")
        print("4 - Vyhledat film")
        print("5 - Zobrazit videotéku")
        print("0 - Ukončit program")
        volba = input("Vaše volba: ")
        if volba == "1":
            pridat_film()
        elif volba == "2":
            upravit_film()
        elif volba == "3":
            smazat_film()
        elif volba == "4":
            vyhledat_film()
        elif volba == "5":
            zobrazit_videotéku()
    
        elif volba == "0":
            print("Děkujeme za použití programu.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")

menu()
