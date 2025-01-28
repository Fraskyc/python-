import random

body = 0

 

while True:

    question = input("Chcete začít akci?: ")

    if question == ("ne"):

        break

    print()

    text = ("Vítej ve hře hráči.")

    text2 = ("Mám tady pro tebe hru jménem Číselný Svět.")

    text3 = ("Pravidla jsou jednoduchá.")

    text4 = ("Stačí psát čísla od 1-5 a jen doufat, že jsou dobře. Pokud budeš mít 5 bodů dostaneš překvapení.")

    print(text)

    print(text2)

    print(text3)

    print(text4)

    print()

 

    random_number = random.randint(1, 5)

    quest = int(input("Zadej číslo: "))

   

    print("Počítač si myslí:", random_number)

 

   

    if int(quest) == random_number:

        body += 1

        print("Nice, máš", body, "bodů")

    else:

        print("Smůla, máš", body, "bodů")