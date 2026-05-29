import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Desempilhando {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        
        while (sc.hasNextInt()) {
            int N = sc.nextInt();
            int P = sc.nextInt();
            if (N == 0 && P == 0) break;
            
            List<List<Integer>> piles = new ArrayList<>();
            int targetPile = -1, targetRow = -1;
            
            for (int i = 0; i < P; i++) {
                int Q = sc.nextInt();
                List<Integer> pile = new ArrayList<>();
                for (int j = 0; j < Q; j++) {
                    int val = sc.nextInt();
                    pile.add(val);
                    if (val == 1) {
                        targetPile = i;
                        targetRow = j;
                    }
                }
                piles.add(pile);
            }
            
            int above = piles.get(targetPile).size() - targetRow - 1;
            
            // Custo pela esquerda
            long costLeft = above;
            for (int i = targetPile - 1; i >= 0; i--) {
                int h = piles.get(i).size();
                if (h > targetRow) {
                    costLeft += h - targetRow;
                } else {
                    break;
                }
            }
            
            // Custo pela direita
            long costRight = above;
            for (int i = targetPile + 1; i < P; i++) {
                int h = piles.get(i).size();
                if (h > targetRow) {
                    costRight += h - targetRow;
                } else {
                    break;
                }
            }
            
            sb.append(Math.min(costLeft, costRight)).append("\n");
        }
        
        System.out.print(sb);
        sc.close();
    }
}
