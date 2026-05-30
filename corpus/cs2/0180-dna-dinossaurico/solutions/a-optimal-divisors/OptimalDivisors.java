import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class OptimalDivisors {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        if (s == null) return;
        s = s.trim();
        int n = s.length();
        
        ArrayList<Integer> divisors = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.add(i);
                if (i * i != n) divisors.add(n / i);
            }
        }
        Collections.sort(divisors);
        
        for (int k : divisors) {
            int d = n / k;
            boolean valid = true;
            for (int i = 0; i < d / 2; i++) {
                for (int j = 0; j < k; j++) {
                    if (s.charAt(i * k + j) != s.charAt((d - 1 - i) * k + j)) {
                        valid = false;
                        break;
                    }
                }
                if (!valid) break;
            }
            if (valid) {
                System.out.println(d);
                return;
            }
        }
    }
}
