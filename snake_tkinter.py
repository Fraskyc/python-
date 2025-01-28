import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20

BG_COLOR = "green"
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"
TEXT_COLOR = "white"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Had")

        self.running = False
        self.score = 0

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def start_game(self):
        """Inicializace hry."""
        self.running = True
        self.start_button.pack_forget()
        self.quit_button.pack_forget()

        self.snake = [(5, 5)]  
        self.food = self.place_food()
        self.direction = "Right"
        self.score = 0

        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))
        self.root.bind("w", lambda event: self.change_direction("Up"))
        self.root.bind("s", lambda event: self.change_direction("Down"))
        self.root.bind("a", lambda event: self.change_direction("Left"))
        self.root.bind("d", lambda event: self.change_direction("Right"))

        self.run_game()

    def place_food(self):
        """Umístí jídlo na náhodné místo."""
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1)
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, new_direction):
        """Změní směr pohybu hada."""
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def move_snake(self):
        """Pohybuje hadem v aktuálním směru."""
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)

        if (
            new_head in self.snake or  
            new_head[0] < 0 or new_head[0] >= WIDTH // CELL_SIZE or  
            new_head[1] < 0 or new_head[1] >= HEIGHT // CELL_SIZE  
        ):
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.place_food()
            self.score += 1  
        else:
            self.snake.pop()

    def draw(self):
        """Vykreslí hada, jídlo a skóre."""
        self.canvas.delete("all")

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * CELL_SIZE, y * CELL_SIZE,
                (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                fill=SNAKE_COLOR
            )

        fx, fy = self.food
        self.canvas.create_oval(
            fx * CELL_SIZE, fy * CELL_SIZE,
            (fx + 1) * CELL_SIZE, (fy + 1) * CELL_SIZE,
            fill=FOOD_COLOR
        )

        self.canvas.create_text(
            10, 10,
            anchor="nw",
            text=f"Score: {self.score}",
            fill=TEXT_COLOR,
            font=("Arial", 16)
        )

    def show_game_over(self):
        """Zobrazí obrazovku Game Over."""
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 - 20,
            text="Game Over",
            fill=TEXT_COLOR,
            font=("Arial", 24)
        )
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 + 20,
            text=f"Final Score: {self.score}",
            fill=TEXT_COLOR,
            font=("Arial", 16)
        )
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 + 50,
            text="Play Again or Quit?",
            fill=TEXT_COLOR,
            font=("Arial", 14)
        )

        self.start_button.pack()
        self.quit_button.pack()

    def run_game(self):
        """Hlavní smyčka hry."""
        if self.running:
            self.move_snake()
            self.draw()
            self.root.after(100, self.run_game)
        else:
            self.show_game_over()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
