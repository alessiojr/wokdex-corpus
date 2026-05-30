import java.util.Scanner;
import java.util.Locale;

public class NotasMoedas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US);
        if (sc.hasNextDouble()) {
            double n = sc.nextDouble();
            int cents = (int) Math.round(n * 100);
            
            int[] notes = {10000, 5000, 2000, 1000, 500, 200};
            int[] coins = {100, 50, 25, 10, 5, 1};
            
            System.out.println("NOTAS:");
            for (int note : notes) {
                int qty = cents / note;
                cents %= note;
                System.out.printf(Locale.US, "%d nota(s) de R$ %.2f\n", qty, note / 100.0);
            }
            
            System.out.println("MOEDAS:");
            for (int coin : coins) {
                int qty = cents / coin;
                cents %= coin;
                System.out.printf(Locale.US, "%d moeda(s) de R$ %.2f\n", qty, coin / 100.0);
            }
        }
        sc.close();
    }
}
