import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Corredor {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        
        int n = Integer.parseInt(line.trim());
        StringTokenizer st = null;
        
        long maxSoFar = Long.MIN_VALUE;
        long currentMax = 0;
        
        for (int i = 0; i < n; i++) {
            while (st == null || !st.hasMoreTokens()) {
                line = br.readLine();
                if (line == null) break;
                st = new StringTokenizer(line);
            }
            if (st != null && st.hasMoreTokens()) {
                long val = Long.parseLong(st.nextToken());
                currentMax += val;
                if (currentMax > maxSoFar) {
                    maxSoFar = currentMax;
                }
                if (currentMax < 0) {
                    currentMax = 0;
                }
            }
        }
        
        System.out.println(maxSoFar);
    }
}
