import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLong()) {
            long a = sc.nextLong();
            if (a == 0) break;
            long b = sc.nextLong();
            long c = sc.nextLong();
            
            long area = a * b;
            long total = (area * 100) / c;
            long side = (long) Math.sqrt(total);
            System.out.println(side);
        }
        sc.close();
    }
}
