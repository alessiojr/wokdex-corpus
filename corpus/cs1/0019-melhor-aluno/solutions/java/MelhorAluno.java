import java.util.Scanner;

public class MelhorAluno {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        float tempoPedro = scn.nextFloat();
        float tempoPaulo = scn.nextFloat();

        if (tempoPedro <= tempoPaulo) {
            System.out.println("Pedro");
        } else {
            System.out.println("Paulo");
        }

        scn.close();
    }
}