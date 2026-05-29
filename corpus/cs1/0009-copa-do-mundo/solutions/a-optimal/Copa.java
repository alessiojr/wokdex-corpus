import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {
            
            int qtdTimes = sc.nextInt();
            int qtdpartidas = sc.nextInt();

            if (qtdTimes == 0) {
                break;
            }

            int totalPoints = 3 * qtdpartidas;
            int matchDraw = 0;

            for (int i = 0; i < qtdTimes; i++) {
                String str = sc.next();
                int point = sc.nextInt();
                matchDraw += point;
            }

            System.out.println(totalPoints - matchDraw);

        }

    }

}
