import java.util.*;

public class Pexeso {
    private static final int SIZE = 4;
    private static char[][] board = new char[SIZE][SIZE];
    private static boolean[][] revealed = new boolean[SIZE][SIZE];
    private static char[] symbols = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'};
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        do {
            initializeGame();
            playGame(scanner);
        } while (playAgain(scanner));
        scanner.close();
    }

    private static void initializeGame() {
//zamíchání karet
        List<Character> cards = new ArrayList<>();
        for (char symbol : symbols) {
            cards.add(symbol);
            cards.add(symbol);
        }
        Collections.shuffle(cards);
        
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                board[i][j] = cards.remove(0);
                revealed[i][j] = false; // všechny karty jsou skryté na začátku
            }
        }
    }
// funkce hry
    private static void playGame(Scanner scanner) {
        int matches = 0;
        while (matches < SIZE * SIZE / 2) {
            drawBoard();
            System.out.println("Zadejte souřadnice první karty (řádek sloupec):");
            int[] firstCard = getCoordinates(scanner);
            revealed[firstCard[0]][firstCard[1]] = true;
            drawBoard();
            
            System.out.println("Zadejte souřadnice druhé karty (řádek sloupec):");
            int[] secondCard = getCoordinates(scanner);
            revealed[secondCard[0]][secondCard[1]] = true;
            drawBoard();

            if (board[firstCard[0]][firstCard[1]] == board[secondCard[0]][secondCard[1]]) {
                System.out.println("Našli jste pár!");
                matches++;
            } else {
                System.out.println("Nenalezli jste pár. Karty se opět skryjí.");
                try {
                    Thread.sleep(1000); 
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                revealed[firstCard[0]][firstCard[1]] = false;
                revealed[secondCard[0]][secondCard[1]] = false;
            }
        }
        System.out.println("Gratulujeme, našli jste všechny páry!");
    }

    private static void drawBoard() {
        System.out.println("Herní deska:");
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (revealed[i][j]) {
                    System.out.print(board[i][j] + " ");
                } else {
                    System.out.print("* ");
                }
            }
            System.out.println();
        }
    }

    private static int[] getCoordinates(Scanner scanner) {
        int row, col;
        while (true) {
            row = scanner.nextInt() - 1;
            col = scanner.nextInt() - 1;
            if (row >= 0 && row < SIZE && col >= 0 && col < SIZE && !revealed[row][col]) {
                break;
            } else {
                System.out.println("Neplatné souřadnice nebo karta již byla otočena. Zkuste to znovu.");
            }
        }
        return new int[]{row, col};
    }
// nový začátek
    private static boolean playAgain(Scanner scanner) {
        System.out.println("Chcete hrát znovu? (ano/ne):");
        String answer = scanner.next().toLowerCase();
        return answer.equals("ano");
    }
}
