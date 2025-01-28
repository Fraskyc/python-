import random

# Seznam slov pro hádání
slova = ['pes', 'batoh', 'ryba', 'had', 'vrtulník', 'klokan', 'florbal', 'mobil']

def vyber_slovo():
    return random.choice(slova)

def hra():
    slovo = vyber_slovo()
    hadane_pismeno = ['_'] * len(slovo)
    pokusy = 7
    uhodnute = False
    spatne_pismena = []

    print('Vítejte ve hře Šibenice!')
    print('Hádáte slovo: ' + ' '.join(hadane_pismeno))

    while pokusy > 0 and not uhodnute:
        # Vstup od uživatele
        hadane_pismeno_input = input('Hádejte písmeno: ')

        if len(hadane_pismeno_input) != 1:
            print('Zadejte pouze jedno písmeno!')
            continue

        if hadane_pismeno_input in slovo:
            # Uhodnuté písmeno
            for i in range(len(slovo)):
                if slovo[i] == hadane_pismeno_input:
                    hadane_pismeno[i] = hadane_pismeno_input

            if '_' not in hadane_pismeno:
                uhodnute = True
        else:
            # Chybné písmeno
            if hadane_pismeno_input not in spatne_pismena:
                spatne_pismena.append(hadane_pismeno_input)
                pokusy -= 1
                print('Špatné písmeno. Zbývající pokusy: {}'.format(pokusy))

        print('Hádáte slovo: ' + ' '.join(hadane_pismeno))
        print('Špatná písmena: ' + ', '.join(spatne_pismena))

    if uhodnute:
        print('Gratuluji, uhodli jste slovo: ' + ''.join(hadane_pismeno))
    else:
        print('Bohužel jste prohráli. Hledané slovo bylo: ' + slovo)
hra()
