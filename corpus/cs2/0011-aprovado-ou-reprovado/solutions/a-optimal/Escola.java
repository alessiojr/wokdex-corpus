import java.util.Scanner;

public class Escola {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextDouble()) {
            double a = sc.nextDouble();
            double b = sc.nextDouble();
            double media = (a + b) / 2.0;

            if (media >= 7.0) {
                System.out.println("Aprovado");
            } else if (media >= 4.0) {
                System.out.println("Recuperacao");
            } else {
                System.out.println("Reprovado");
            }
        }
        sc.close();
    }
}
