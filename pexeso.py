import random
import time

import random
import time

# inicializace herních konstant
IMAGE_COUNT = 16
BOARD_SIZES = {
    "malé": 4,
    "střední": 8,
    "velké": 16
}

# výběr velikosti hrací plochy
board_size = None
while board_size is None:
    size_input = input(f"Vyberte velikost hrací plochy: {' / '.join(BOARD_SIZES.keys())} ")
    if size_input in BOARD_SIZES:
        board_size = BOARD_SIZES[size_input]
    else:
        print("Neplatný vstup. Zadejte jednu z nabízených možností.")

# inicializace hrací plochy
board = [[0 for _ in range(board_size)] for _ in range(board_size)]

# seznam s obrázky, každý obrázek se bude vyskytovat dvakrát
images = [i for i in range(1, IMAGE_COUNT+1)] * (board_size ** 2 // 2)

# náhodné rozmístění obrázků na hrací ploše
random.shuffle(images)
for i in range(board_size):
    for j in range(board_size):
        board[i][j] = images[i*board_size+j]

# inicializace herního stavu
revealed = [[False for _ in range(board_size)] for _ in range(board_size)]
selected = []

# vykreslení hrací plochy
def draw_board():
    for i in range(board_size):
        for j in range(board_size):
            if revealed[i][j]:
                print(f"{board[i][j]:2d}", end=" ")
            else:
                print("##", end=" ")
        print()

# získání vstupu od hráče
def get_input():
    i, j = input("Zadejte souřadnice (řádek sloupec): ").split()
    i = int(i) - 1
    j = int(j) - 1
    return i, j

# tah hráče
def player_turn():
    global selected
    i, j = get_input()
    if not revealed[i][j]:
        selected.append((i, j))
        revealed[i][j] = True

# tah počítače
def computer_turn():
    global selected
    options = [(i, j) for i in range(board_size) for j in range(board_size) if not revealed[i][j]]
    if len(options) < 2:
        return
    i1, j1 = random.choice(options)
    options.remove((i1, j1))
    i2, j2 = random.choice(options)
    selected = [(i1, j1), (i2, j2)]
    revealed[i1][j1] = True
    revealed[i2][j2] = True
    time.sleep(1)

#výběr režimu hry
while True:
    players = input("Chcete hrát proti počítači (1) nebo proti hráči (2)? ")
    if players in ["1", "2"]:
        break
    else:
        print("Neplatný vstup. Zadejte 1 pro hru s počítačem nebo 2 pro hru pro dva hráče.")

print(f"Zvolili jste režim hry pro {players} hráče/ů.")

#hra
while True:
        draw_board()

        if len(selected) == 2:
            i1, j1 = selected[0]
            i2, j2 = selected[1]
            if board[i1][j1] == board[i2][j2]:
                print("Správně!")
                revealed[i1][j1] = True    
                revealed[i2][j2] = True
            else:
                print("Špatně!")
                time.sleep(1)  
                revealed[i1][j1] = False
                revealed[i2][j2] = False
            selected = []
        else:
            i, j = input("Zadejte souřadnice (řádek sloupec): ").split()
            i = int(i) - 1
            j = int(j) - 1
            if not revealed[i][j]:
                selected.append((i, j))
                revealed[i][j] = True
        #konec
        if all(all(row) for row in revealed):
            print("Gratulujeme, vyhráli jste!")
            break
