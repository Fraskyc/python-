import random
i = 1
e = 12
inpu = input("if you want a hint type hint: ")
nabídka = ("pes" , "tabule" , "fyzika", "pouzdro", "wc","mobil","florbal")
slovo = random.choice(nabídka)
hrac = input("zadejte pismeno: ")
hadane_pismeno = ['_'] * len(slovo)

print('Hádáte slovo: ' + ' '.join(hadane_pismeno))

while i < 13:
    if hrac == slovo:
        print("výhra!")
        break
    elif hrac in slovo:
        print("je to ve slově")
        result = slovo.index(hrac)
        result += 1
        print("písmeno je na ", result,"pozici")



    else:
        print("neni")
    if i == 12:
        print("Prohra")
    i += 1
    e -= 1
    print("máte",  e , "pokusů")


    if inpu == "hint":
        g = str(len(slovo))
        print("slovo má " + g + " písmen")
    else:
        continue



