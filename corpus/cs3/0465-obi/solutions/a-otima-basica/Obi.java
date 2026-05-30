import java.util.Scanner;

public class Obi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int p = sc.nextInt();
            int passCount = 0;
            for (int i = 0; i < n; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                if (x + y >= p) {
                    passCount++;
                }
            }
            System.out.println(passCount);
        }
        sc.close();
    }
}
