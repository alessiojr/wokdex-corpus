import java.util.Scanner;
import java.util.Locale;

public class Solution {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        if (sc.hasNext()) {
            String op = sc.next();
            double a = sc.nextDouble();
            double b = sc.nextDouble();

            double res = 0;
            if (op.equals("M")) {
                res = a * b;
            } else if (op.equals("D")) {
                res = a / b;
            }

            System.out.printf("%.2f\n", res);
        }
        sc.close();
    }
}
