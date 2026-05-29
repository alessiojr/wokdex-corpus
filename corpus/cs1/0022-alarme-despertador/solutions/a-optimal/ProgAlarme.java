import java.util.Scanner;

public class ProgAlarme {

    public static void main(String[] args) {
        int h1, m1, h2, m2, hora, hora2, tempo;
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {

            h1 = sc.nextInt();
            m1 = sc.nextInt();
            h2 = sc.nextInt();
            m2 = sc.nextInt();

            hora = h1 * 60 + m1;
            hora2 = h2 * 60 + m2;
            if (hora < hora2) {
                tempo = hora2 - hora;
                System.out.println(tempo);
            } else if (hora > hora2) {
                tempo = hora2 - hora + 24 * 60;
                System.out.println(tempo);
            } else {
                //((h1 == 0) && (h2 == 0) && (m1 == 0) && (m2 == 0)
                break;

            }

        }
    }
}
