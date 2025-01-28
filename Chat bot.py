import random 

print("Vítej chtovací místnosti pro konec napiš," )

zákaz=("hovno","prdel","píča")
otázky=("jak se máš",)
odpověďi=("dobře")

def hlavni ():
    while True:
        zpráva = input("Ty: ")
        if zpráva.lower() == 'konec':
            print ("Děkuji za povídání. ")
            break
        if zpráva.lower == zákaz:
            zákaz = ("BEEP")
        if zpráva.lower == otázky:
            odpověď = random(odpověďi)
            print(odpověď)