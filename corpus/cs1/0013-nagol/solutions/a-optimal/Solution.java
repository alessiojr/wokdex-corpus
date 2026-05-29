import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLong()) {
            long l = sc.nextLong();
            long c = sc.nextLong();
            long x = sc.nextLong();
            long y = sc.nextLong();
            
            long index = x * c + y;
            if (index % 2 == 0) {
                System.out.println("Direita");
            } else {
                System.out.println("Esquerda");
            }
        }
        sc.close();
    }
}
