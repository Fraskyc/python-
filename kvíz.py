from tkinter import *
import tkinter.font as font
from random import randrange

root = Tk()
root.winfo_toplevel().title("Tic Tac Toe")
root.geometry("900x900")
root.protocol('WM_DELETE_WINDOW', lambda: quit())

map = []
buttons = []
player_one_turn = True
pvp = False

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def print_menu():
    clear()

    Button(root, width=24, height=2, text="Player vs Player", command=lambda: play("PvP")).pack(pady=5)
    Button(root, width=24, height=2, text="Player vs Computer", command=lambda: play("PvC")).pack(pady=5)
    Button(root, width=24, height=2, text="Quit", command=quit).pack(pady=5)

def play(mode):
    global map
    global buttons
    global player_one_turn
    global pvp
    global btn_font

    clear()
    map = [0 for i in range(9)]
    buttons.clear()
    player_one_turn = True

    pvp = False
    if mode == "PvP":
        pvp = True

    for i in range(9):
        buttons.append(Button(root, text="", font=font.Font(family='Helvetica', size=128, weight='bold'), command=lambda i=i: btn_handler(i)))
        x = (i % 3) * 300
        y= ((i - i % 3) / 3) * 300
        buttons[i].place(width=300, height=300, x=x, y=y)

def btn_handler(btn_num):
    global map
    global buttons
    global player_one_turn

    buttons[btn_num].config(state="disabled")
    map[btn_num] = 1 if player_one_turn else 2
    buttons[btn_num]['text'] = 'X' if player_one_turn else 'O'

    check_win()

    player_one_turn ^= True

    if pvp == False:
        done = False
        while not done:
            i = randrange(9)
            if map[i] == 0:
                done = True
                buttons[i]['text'] = 'X' if player_one_turn else 'O'
                buttons[i].config(state="disabled")
                map[i] = 1 if player_one_turn else 2
                check_win()
                player_one_turn ^= True

def check_win():
    global map
    global player_one_turn

    if (
        map[0] != 0 and map[0] == map[1] == map[2] or
        map[3] != 0 and map[3] == map[4] == map[5] or
        map[6] != 0 and map[6] == map[7] == map[8] or
        map[0] != 0 and map[0] == map[3] == map[6] or
        map[1] != 0 and map[1] == map[4] == map[7] or
        map[2] != 0 and map[2] == map[5] == map[8] or
        map[0] != 0 and map[0] == map[4] == map[8] or
        map[2] != 0 and map[2] == map[4] == map[6]
    ):
        winner = ''

        if pvp:
            winner = 'Player 1 won!' if player_one_turn else 'Player 2 won!'
        else:
            winner = 'Player won!' if player_one_turn else 'Computer won!'

        print_winner(winner)
    elif map.count(0) == 0:
        print_winner("Draw!")

def print_winner(message):
    for widget in root.winfo_children():
            widget.config(state="disabled")
    Label(root, text=message, font=font.Font(family='Helvetica', size=32, weight='bold')).pack()
    Button(root, width=24, height=2, text="Restart", command=print_menu).pack()
    root.mainloop()

print_menu()

root.resizable(False, False)
root.mainloop()