import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                if (line.isEmpty()) continue;
                
                int i = 0;
                int len = line.length();
                boolean temSaida = false;
                
                while (i < len) {
                    if (line.charAt(i) == '!') {
                        System.out.print("\n");
                        temSaida = true;
                        i++;
                        continue;
                    }
                    
                    int total = 0;
                    while (i < len && Character.isDigit(line.charAt(i))) {
                        total += (line.charAt(i) - '0');
                        i++;
                    }
                    
                    if (i < len && line.charAt(i) == '!') {
                        System.out.print("\n");
                        temSaida = true;
                        i++;
                    } else if (total > 0 && i < len) {
                        char atual = line.charAt(i);
                        if (atual == 'b') atual = ' ';
                        for (int j = 0; j < total; j++) {
                            System.out.print(atual);
                            temSaida = true;
                        }
                        i++;
                    } else if (i < len) {
                        i++;
                    }
                }
                
                if (!temSaida) {
                    System.out.print("Entrada errada");
                }
                System.out.print("\n-------------\n");
            }
        }
    }
}
