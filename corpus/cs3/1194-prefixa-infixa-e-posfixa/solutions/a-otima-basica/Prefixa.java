import java.io.*;
import java.util.*;

public class Prefixa {

    static String solve(String pre, String in) {
        if (pre.isEmpty()) {
            return "";
        }
        
        char root = pre.charAt(0);
        int pos = in.indexOf(root);
        
        String inLeft = in.substring(0, pos);
        String inRight = in.substring(pos + 1);
        
        String preLeft = pre.substring(1, pos + 1);
        String preRight = pre.substring(pos + 1);
        
        return solve(preLeft, inLeft) + solve(preRight, inRight) + root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int C = sc.nextInt();
        while (C-- > 0) {
            int N = sc.nextInt();
            String pre = sc.next();
            String in = sc.next();
            
            System.out.println(solve(pre, in));
        }
    }
}
