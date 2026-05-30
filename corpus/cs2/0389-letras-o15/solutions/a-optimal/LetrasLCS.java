import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class LetrasLCS {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line != null) {
            String[] parts = line.split("\\s+");
            if (parts.length > 0) {
                String s = parts[0];
                if (s.isEmpty() && parts.length > 1) s = parts[1];
                
                int n = s.length();
                if (n == 0) return;
                
                // 1. Cria a cópia ordenada alfabeticamente
                char[] sArr = s.toCharArray();
                char[] sortedArr = s.toCharArray();
                Arrays.sort(sortedArr);
                
                // 2. Roda a DP do LCS otimizada em O(N) memória
                int[] prev = new int[n + 1];
                int[] curr = new int[n + 1];
                
                for (int i = 1; i <= n; i++) {
                    for (int j = 1; j <= n; j++) {
                        if (sArr[i - 1] == sortedArr[j - 1]) {
                            curr[j] = prev[j - 1] + 1;
                        } else {
                            curr[j] = Math.max(prev[j], curr[j - 1]);
                        }
                    }
                    System.arraycopy(curr, 0, prev, 0, n + 1);
                }
                
                System.out.println(curr[n]);
            }
        }
    }
}
