import java.io.*;
import java.util.*;

public class DNA {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int K = sc.nextInt();
            if (K == 0) break;
            
            String s1 = sc.next();
            String s2 = sc.next();
            
            int n = s1.length();
            int m = s2.length();
            
            int[][] match = new int[n + 1][m + 1];
            int[][] dp = new int[n + 1][m + 1];
            int[][] f = new int[n + 1][m + 1];
            
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                        match[i][j] = match[i - 1][j - 1] + 1;
                    } else {
                        match[i][j] = 0;
                    }
                    
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                    f[i][j] = 0;
                    
                    if (match[i][j] >= K) {
                        f[i][j] = Math.max(dp[i - K][j - K] + K, f[i - 1][j - 1] + 1);
                        dp[i][j] = Math.max(dp[i][j], f[i][j]);
                    }
                }
            }
            
            System.out.println(dp[n][m]);
        }
        sc.close();
    }
}
