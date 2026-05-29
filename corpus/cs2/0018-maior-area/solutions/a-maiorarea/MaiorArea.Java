import java.util.Scanner;

public class MaiorArea {
    public static void main(String[] args) {
        int l1, a1, l2, a2;
        Scanner scanner = new Scanner(System.in);
        
        l1 = scanner.nextInt();
        a1 = scanner.nextInt();
        l2 = scanner.nextInt();
        a2 = scanner.nextInt();
        
        System.out.println(maiorArea(l1, a1, l2, a2));
    }
    
    public static String maiorArea(int l1, int a1, int l2, int a2) {
        int area1 = l1 * a1;
        int area2 = l2 * a2;
        
        if (area1 > area2) {
            return "Primeiro";
        } else if (area2 > area1) {
            return "Segundo";
        } else {
            return "Empate";
        }
    }
}