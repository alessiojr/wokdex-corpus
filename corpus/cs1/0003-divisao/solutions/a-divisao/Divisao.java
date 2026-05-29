import java.util.Locale;
import java.util.Scanner;

public class Divisao {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in).useLocale(Locale.US);
        double a;
        int b;
        a = scn.nextDouble();
        b = scn.nextInt();
        System.out.printf(Locale.US, "%.2f%n", a / b);
    }
}
