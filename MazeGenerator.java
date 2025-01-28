import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.Random;

public class MazeGenerator{
    private static final int CELL_SIZE = 20;
    private int width, height;
    private Cell[][] maze;
    private Random random = new Random();

    public MazeGenerator(int width, int height) {
        this.width = width;
        this.height = height;
        this.maze = new Cell[height][width];
        setPreferredSize(new Dimension(width * CELL_SIZE, height * CELL_SIZE));
        generateMaze();
    }

    private void generateMaze() {
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                maze[y][x] = new Cell();
            }
        }

        Deque<Point> stack = new ArrayDeque<>();
        stack.push(new Point(0, 0));
        maze[0][0].visited = true;

        while (!stack.isEmpty()) {
            Point current = stack.pop();
            List<Point> neighbors = getUnvisitedNeighbors(current.x, current.y);

            if (!neighbors.isEmpty()) {
                stack.push(current);
                Point next = neighbors.get(random.nextInt(neighbors.size()));
                removeWall(current.x, current.y, next.x, next.y);
                maze[next.y][next.x].visited = true;
                stack.push(next);
            }
        }
        repaint();
    }

    private List<Point> getUnvisitedNeighbors(int x, int y) {
        List<Point> neighbors = new ArrayList<>();
        if (y > 0 && !maze[y - 1][x].visited) neighbors.add(new Point(x, y - 1));
        if (x > 0 && !maze[y][x - 1].visited) neighbors.add(new Point(x - 1, y));
        if (y < height - 1 && !maze[y + 1][x].visited) neighbors.add(new Point(x, y + 1));
        if (x < width - 1 && !maze[y][x + 1].visited) neighbors.add(new Point(x + 1, y));
        return neighbors;
    }

    private void removeWall(int x1, int y1, int x2, int y2) {
        if (x1 == x2) {
            if (y1 > y2) {
                maze[y1][x1].topWall = false;
                maze[y2][x2].bottomWall = false;
            } else {
                maze[y1][x1].bottomWall = false;
                maze[y2][x2].topWall = false;
            }
        } else if (y1 == y2) {
            if (x1 > x2) {
                maze[y1][x1].leftWall = false;
                maze[y2][x2].rightWall = false;
            } else {
                maze[y1][x1].rightWall = false;
                maze[y2][x2].leftWall = false;
            }
        }
    }

    private List<Point> solutionPath = new ArrayList<>();

    private void solveMaze() {
        boolean[][] visited = new boolean[height][width];
        Deque<Point> queue = new ArrayDeque<>();
        Deque<List<Point>> paths = new ArrayDeque<>();

        queue.add(new Point(0, 0));
        paths.add(new ArrayList<>(List.of(new Point(0, 0))));
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            Point current = queue.remove();
            List<Point> path = paths.remove();

            if (current.x == width - 1 && current.y == height - 1) {
                solutionPath = path; // Uložení cesty do cíle
                repaint();
                return;
            }

            for (Point neighbor : getPassableNeighbors(current.x, current.y)) {
                if (!visited[neighbor.y][neighbor.x]) {
                    visited[neighbor.y][neighbor.x] = true;
                    queue.add(neighbor);
                    List<Point> newPath = new ArrayList<>(path);
                    newPath.add(neighbor);
                    paths.add(newPath);
                }
            }
        }
        solutionPath.clear(); // Pokud cesta neexistuje
        repaint();
    }

    private List<Point> getPassableNeighbors(int x, int y) {
        List<Point> neighbors = new ArrayList<>();
        if (!maze[y][x].topWall && y > 0) neighbors.add(new Point(x, y - 1));
        if (!maze[y][x].rightWall && x < width - 1) neighbors.add(new Point(x + 1, y));
        if (!maze[y][x].bottomWall && y < height - 1) neighbors.add(new Point(x, y + 1));
        if (!maze[y][x].leftWall && x > 0) neighbors.add(new Point(x - 1, y));
        return neighbors;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Vykreslení bludiště
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                Cell cell = maze[y][x];
                int px = x * CELL_SIZE;
                int py = y * CELL_SIZE;

                if (cell.topWall) g.drawLine(px, py, px + CELL_SIZE, py);
                if (cell.rightWall) g.drawLine(px + CELL_SIZE, py, px + CELL_SIZE, py + CELL_SIZE);
                if (cell.bottomWall) g.drawLine(px, py + CELL_SIZE, px + CELL_SIZE, py + CELL_SIZE);
                if (cell.leftWall) g.drawLine(px, py, px, py + CELL_SIZE);
            }
        }

        // Vykreslení cesty
        if (!solutionPath.isEmpty()) {
            g.setColor(Color.RED);
            Graphics2D g2d = (Graphics2D) g;
            g2d.setStroke(new BasicStroke(2));
            for (int i = 1; i < solutionPath.size(); i++) {
                Point from = solutionPath.get(i - 1);
                Point to = solutionPath.get(i);
                int x1 = from.x * CELL_SIZE + CELL_SIZE / 2;
                int y1 = from.y * CELL_SIZE + CELL_SIZE / 2;
                int x2 = to.x * CELL_SIZE + CELL_SIZE / 2;
                int y2 = to.y * CELL_SIZE + CELL_SIZE / 2;
                g.drawLine(x1, y1, x2, y2);
            }
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Maze Generator and Solver");
        MazeGenerator mazePanel = new MazeGenerator(20, 20);

        JButton generateButton = new JButton("Generate Maze");
        generateButton.addActionListener(e -> mazePanel.generateMaze());

        JButton solveButton = new JButton("Solve Maze");
        solveButton.addActionListener(e -> mazePanel.solveMaze());

        JPanel controlPanel = new JPanel();
        controlPanel.add(generateButton);
        controlPanel.add(solveButton);

        frame.setLayout(new BorderLayout());
        frame.add(mazePanel, BorderLayout.CENTER);
        frame.add(controlPanel, BorderLayout.SOUTH);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    static class Cell {
        boolean topWall = true;
        boolean rightWall = true;
        boolean bottomWall = true;
        boolean leftWall = true;
        boolean visited = false;
    }
}
