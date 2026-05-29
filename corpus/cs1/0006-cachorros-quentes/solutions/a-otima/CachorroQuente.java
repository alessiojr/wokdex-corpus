import java.util.Scanner;
import java.util.Locale;

public class CachorroQuente {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        if (sc.hasNextInt()) {
            int h = sc.nextInt();
            if (sc.hasNextInt()) {
                int p = sc.nextInt();
                double media = (double) h / p;
                System.out.printf("%.2f%n", media);
            }
        }

        sc.close();
    }
}
