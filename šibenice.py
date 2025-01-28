from tkinter import Tk, Label, Entry, Button, messagebox, Canvas
import random

root = Tk()
root.title("Hra šibenice")

#Slova pro hádání
slova = ["pes", "kočka", "auto", "strom", "tráva"]
slovo = random.choice(slova)
uhodnute_pismena = []

#Počet chyb hráče
pocet_chyb = 0

#Funkce pro hádání
def zkontrolovat_pismeno():
    global pocet_chyb

    pismeno = entry.get()
    entry.delete(0, 'end') 

    if len(pismeno) != 1:
        messagebox.showerror("Chyba", "Zadejte pouze jedno písmeno!")
        return

    if pismeno in uhodnute_pismena:
        messagebox.showinfo("Pozor", "Toto písmeno jste již hádal/a!")
        return

    uhodnute_pismena.append(pismeno)

    if pismeno in slovo:
        #Zobrazení správného písmena
        for i in range(len(slovo)):
            if slovo[i] == pismeno:
                uhodnute_label.config(text=uhodnute_label.cget("text")[:i] + pismeno + uhodnute_label.cget("text")[i+1:])
    else:
        pocet_chyb += 1
        vykreslit_sibenici()

    if uhodnute_label.cget("text") == slovo:
        messagebox.showinfo("Gratulace", "Vyhrál/a jste!")
        root.quit()

#vstup 
label = Label(root, text="Hádané slovo:")
label.pack()

uhodnute_label = Label(root, text="_" * len(slovo))
uhodnute_label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Hádat", command=zkontrolovat_pismeno)
button.pack()

#Vlastní input 
def zacit_hru():
    global slovo, uhodnute_pismena, pocet_chyb

    slovo = vlastni_slovo_entry.get().lower()
    vlastni_slovo_entry.delete(0, 'end') 
    label.config(text="Hádané slovo:")
    uhodnute_label.config(text="_" * len(slovo))
    button.config(state="normal")
    vlastni_slovo_button.config(state="disabled")
    pocet_chyb = 0
    vykreslit_sibenici()

vlastni_slovo_label = Label(root, text="Zadejte vlastní slovo:")
vlastni_slovo_label.pack()

vlastni_slovo_entry = Entry(root)
vlastni_slovo_entry.pack()

vlastni_slovo_button = Button(root, text="Začít hru", command=zacit_hru)
vlastni_slovo_button.pack()

#Vykreslení šibenice
def vykreslit_sibenici():
    canvas.delete("all")

    
    if pocet_chyb >= 1:
        canvas.create_oval(50, 50, 150, 150)

    
    if pocet_chyb >= 2:
        canvas.create_line(100, 150, 100, 300)

    
    if pocet_chyb >= 3:
        canvas.create_line(100, 200, 50, 250)

   
    if pocet_chyb >= 4:
        canvas.create_line(100, 200, 150, 250)

    
    if pocet_chyb >= 5:
        canvas.create_line(100, 300, 50, 350)

    
    if pocet_chyb >= 6:
        canvas.create_line(100, 300, 150, 350)

    
    if pocet_chyb >= 6:
        messagebox.showinfo("Konec hry", f"Slovo bylo: {slovo}")
        root.quit()

#vykreslení šibenice celé
canvas = Canvas(root, width=200, height=400)
canvas.pack()

root.mainloop()

