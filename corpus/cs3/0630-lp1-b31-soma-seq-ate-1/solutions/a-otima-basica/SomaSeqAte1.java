import java.util.Scanner;

public class SomaSeqAte1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int soma = 0;
        while (sc.hasNextInt()) {
            int a = sc.nextInt();
            if (a == -1) break;
            soma += a;
        }
        System.out.println("A soma dos valores eh: " + soma);
        sc.close();
    }
}
