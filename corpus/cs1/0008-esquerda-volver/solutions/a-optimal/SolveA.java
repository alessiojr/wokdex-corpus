import java.util.Scanner;

public class SolveA {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Mapeamento: 0: N, 1: L, 2: S, 3: O
        char[] dirs = { 'N', 'L', 'S', 'O' };

        while (scanner.hasNext()) {
            int N = scanner.nextInt();
            if (N == 0)
                break;

            String commands = scanner.next();
            int currentDir = 0; // Norte

            for (int i = 0; i < commands.length(); i++) {
                char cmd = commands.charAt(i);
                if (cmd == 'D') {
                    currentDir = (currentDir + 1) % 4;
                } else if (cmd == 'E') {
                    currentDir = (currentDir - 1 + 4) % 4;
                }
            }

            System.out.println(dirs[currentDir]);
        }

        scanner.close();
    }
}
