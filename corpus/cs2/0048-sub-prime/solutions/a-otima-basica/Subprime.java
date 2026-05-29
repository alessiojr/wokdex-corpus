import java.util.Scanner;

public class Subprime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        
        while (sc.hasNextInt()) {
            int B = sc.nextInt();
            int N = sc.nextInt();
            if (B == 0 && N == 0) break;
            
            long[] saldo = new long[B + 1];
            for (int i = 1; i <= B; i++) {
                saldo[i] = sc.nextInt();
            }
            
            for (int j = 0; j < N; j++) {
                int D = sc.nextInt();
                int C = sc.nextInt();
                int V = sc.nextInt();
                saldo[D] -= V;
                saldo[C] += V;
            }
            
            boolean ok = true;
            for (int i = 1; i <= B; i++) {
                if (saldo[i] < 0) {
                    ok = false;
                    break;
                }
            }
            
            sb.append(ok ? "S" : "N").append("\n");
        }
        
        System.out.print(sb);
        sc.close();
    }
}
