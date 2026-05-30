import java.util.*;

public class Ajuda {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (n == 0) break;
            
            Map<String, Integer> solvedAt = new HashMap<>();
            Map<String, Integer> incorrectCounts = new HashMap<>();
            
            for (int i = 0; i < n; i++) {
                String prob = sc.next();
                int time = sc.nextInt();
                String result = sc.next();
                
                // Rule: Ignore submissions for problems already solved
                if (!solvedAt.containsKey(prob)) {
                    if (result.equals("correct")) {
                        solvedAt.put(prob, time);
                    } else if (result.equals("incorrect")) {
                        incorrectCounts.put(prob, incorrectCounts.getOrDefault(prob, 0) + 1);
                    }
                }
            }
            
            int totalSolved = 0;
            int totalPenalty = 0;
            
            for (String prob : solvedAt.keySet()) {
                totalSolved++;
                int time = solvedAt.get(prob);
                int penalty = incorrectCounts.getOrDefault(prob, 0) * 20;
                totalPenalty += time + penalty;
            }
            
            System.out.println(totalSolved + " " + totalPenalty);
        }
        sc.close();
    }
}
