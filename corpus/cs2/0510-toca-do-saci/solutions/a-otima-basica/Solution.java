import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) return;
        
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        
        int[][] grid = new int[n + 2][m + 2];
        int x = -1, y = -1;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                grid[i][j] = scanner.nextInt();
                if (grid[i][j] == 3) {
                    x = i;
                    y = j;
                }
            }
        }
        
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        int passos = 1;
        while (grid[x][y] != 2) {
            grid[x][y] = 0;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (grid[nx][ny] > 0) {
                    passos++;
                    x = nx;
                    y = ny;
                    break;
                }
            }
        }
        
        System.out.println(passos);
        scanner.close();
    }
}
