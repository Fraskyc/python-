import random
from collections import deque

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 = zeď, 0 = cesta

    def generate(self):
        stack = []
        start = (0, 0)
        self.maze[start[1]][start[0]] = 0
        stack.append(start)

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Nahoru, dolů, vlevo, vpravo

        while stack:
            x, y = stack[-1]
            neighbors = []
            
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2  # Kontrolujeme 2 políčka dále
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 1:
                    neighbors.append((nx, ny))

            if neighbors:
                nx, ny = random.choice(neighbors)
                self.maze[ny][nx] = 0
                self.maze[y + (ny - y) // 2][x + (nx - x) // 2] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

    def solve(self):
        queue = deque()
        start = (0, 0)
        end = (self.width - 1, self.height - 1)
        queue.append((start, [start]))
        visited = set()
        visited.add(start)

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end:
                return path

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 0 and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    visited.add((nx, ny))
        return None

    def display(self, path=None):
        for y in range(self.height):
            for x in range(self.width):
                if path and (x, y) in path:
                    print("●", end=" ")  # Cesta řešení
                elif self.maze[y][x] == 1:
                    print("█", end=" ")  # Zeď
                else:
                    print(" ", end=" ")  # Cesta
            print()


# Použití
if __name__ == "__main__":
    width, height = 21, 21  # Rozměry bludiště
    maze = Maze(width, height)
    maze.generate()
    print("Generované bludiště:")
    maze.display()

    solution = maze.solve()
    if solution:
        print("\nVyřešené bludiště:")
        maze.display(solution)
    else:
        print("Bludiště nelze vyřešit.")
