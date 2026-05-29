import java.util.Scanner;

public class SolveA {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextInt()) {
            int n = scanner.nextInt();
            int[] left = new int[65];
            int[] right = new int[65];

            for (int i = 0; i < n; i++) {
                int size = scanner.nextInt();
                String side = scanner.next().trim().toUpperCase();
                if (side.equals("E")) {
                    left[size]++;
                } else {
                    right[size]++;
                }
            }

            int pairs = 0;
            for (int i = 30; i <= 60; i++) {
                pairs += Math.min(left[i], right[i]);
            }
            System.out.println(pairs);
        }
        scanner.close();
    }
}
