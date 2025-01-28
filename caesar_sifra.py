# Funkce
def caesarova_sifra(text, posun):
    sifra = ""
    for char in text:
        if char.isalpha():
            
            if char.isupper():
                sifra += chr((ord(char) - 65 + posun) % 26 + 65)
            else:
                sifra += chr((ord(char) - 97 + posun) % 26 + 97)
        else:
            sifra += char
    return sifra

# Vstup
text = input("Zadej text k zašifrování: ")
posun = int(input("Zadej počet míst, o které chceš posunout písmena v abecedě: "))

# Zašifrovani
zasifrovany_text = caesarova_sifra(text, posun)

# Výpis textu
print(f"Zadaný text: ", text)
print(f"Zašifrovaný text: {zasifrovany_text}")
