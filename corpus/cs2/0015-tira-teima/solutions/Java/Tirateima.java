import java.util.Scanner;

public class Tirateima {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int x = Integer.parseInt(input[0]);
        int y = Integer.parseInt(input[1]);

        if (x >= 0 && x <= 432 && y >= 0 && y <= 468) {
            System.out.println("dentro");
        } else {
            System.out.println("fora");
        }
    }
}
