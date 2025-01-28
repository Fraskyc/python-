import os
from tkinter import *

obraz = os.path.dirname(__file__)

okno = Tk()
w = Canvas(okno, width= 500, height=400)
w.pack()

body = [100, 25, 50, 40, 200, 40]
w.create_polygon(body)


mainloop()