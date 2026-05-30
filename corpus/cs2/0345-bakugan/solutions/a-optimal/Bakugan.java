import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Bakugan {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;
            
            int r = Integer.parseInt(line);
            if (r == 0) break;
            
            int[] m = new int[r];
            int[] l = new int[r];
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < r; i++) {
                m[i] = Integer.parseInt(st.nextToken());
            }
            
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < r; i++) {
                l[i] = Integer.parseInt(st.nextToken());
            }
            
            int score_m = 0, score_l = 0;
            boolean bonus_given = false;
            
            for (int i = 0; i < r; i++) {
                score_m += m[i];
                score_l += l[i];
                
                if (!bonus_given && i >= 2) {
                    boolean m_consec = (m[i] == m[i-1] && m[i-1] == m[i-2]);
                    boolean l_consec = (l[i] == l[i-1] && l[i-1] == l[i-2]);
                    
                    if (m_consec && l_consec) {
                        bonus_given = true;
                    } else if (m_consec) {
                        score_m += 30;
                        bonus_given = true;
                    } else if (l_consec) {
                        score_l += 30;
                        bonus_given = true;
                    }
                }
            }
            
            if (score_m > score_l) {
                System.out.println("M");
            } else if (score_l > score_m) {
                System.out.println("L");
            } else {
                System.out.println("T");
            }
        }
    }
}
