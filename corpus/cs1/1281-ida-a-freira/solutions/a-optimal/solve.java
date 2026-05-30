import java.util.Scanner;
import java.util.HashMap;
import java.util.Locale;

public class solve {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US);

        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        while (n-- > 0) {
            int m = sc.nextInt();
            HashMap<String, Double> catalog = new HashMap<>();
            for (int i = 0; i < m; i++) {
                String name = sc.next();
                double price = sc.nextDouble();
                catalog.put(name, price);
            }

            int p = sc.nextInt();
            double total = 0.0;
            for (int i = 0; i < p; i++) {
                String name = sc.next();
                int qty = sc.nextInt();
                if (catalog.containsKey(name)) {
                    total += catalog.get(name) * qty;
                }
            }

            System.out.printf(Locale.US, "R$ %.2f\n", total);
        }
        sc.close();
    }
}
