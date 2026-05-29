import java.util.Scanner;

public class SolveA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int f = sc.nextInt();
            if (n == 0 && f == 0)
                break;
            double litros = (f * 50.0) / (n * 1000.0);
            System.out.printf("%.2f%n", litros);
        }
        sc.close();
    }
}
