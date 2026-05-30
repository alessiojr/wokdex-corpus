import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class LetrasLIS {
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
                
                int[] dp = new int[n];
                int maxLen = 0;
                
                for (int i = 0; i < n; i++) {
                    dp[i] = 1;
                    for (int j = 0; j < i; j++) {
                        // Letras crescentes no alfabeto (permitindo letras iguais)
                        if (s.charAt(j) <= s.charAt(i)) {
                            dp[i] = Math.max(dp[i], dp[j] + 1);
                        }
                    }
                    maxLen = Math.max(maxLen, dp[i]);
                }
                
                System.out.println(maxLen);
            }
        }
    }
}
