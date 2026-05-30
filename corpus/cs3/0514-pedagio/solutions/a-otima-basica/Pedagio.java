import java.util.Scanner;

public class Pedagio {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int l = sc.nextInt();
        int d = sc.nextInt();
        int k = sc.nextInt();
        int p = sc.nextInt();

        int valor = (l/d)*p + l*k;
        System.out.println(valor);
    }
}