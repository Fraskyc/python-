import tkinter as tk

def zkontrolovat():
    odpoved = vstup.get()
    if odpoved == "float":
        vysledek.config(text="Správně!")
    else:
        vysledek.config(text="Špatně!")

root = tk.Tk()

otazka = tk.Label(root, text="Jaký je datový typ pro čísla s desetinými čísly?")
otazka.pack()

vstup = tk.Entry(root)
vstup.pack()

tlacitko = tk.Button(root, text="Zkontrolovat", command=zkontrolovat)
tlacitko.pack()

vysledek = tk.Label(root, text="")
vysledek.pack()

root.mainloop()
