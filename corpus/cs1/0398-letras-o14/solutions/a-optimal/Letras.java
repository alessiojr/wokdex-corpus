import java.util.Scanner;

public class Letras {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNext()) {
            return;
        }
        
        char target = scanner.next().charAt(0);
        int total = 0;
        int count = 0;
        
        while (scanner.hasNext()) {
            String word = scanner.next();
            total++;
            if (word.indexOf(target) != -1) {
                count++;
            }
        }
        
        if (total == 0) {
            System.out.printf(java.util.Locale.US, "%.1f\n", 0.0);
        } else {
            double percent = (double) count / total * 100.0;
            System.out.printf(java.util.Locale.US, "%.1f\n", percent);
        }
        scanner.close();
    }
}
