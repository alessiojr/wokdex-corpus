import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;

public class LetrasOptimal {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line != null) {
            String[] parts = line.split("\\s+");
            if (parts.length > 0) {
                String s = parts[0];
                if (s.isEmpty() && parts.length > 1) s = parts[1];
                ArrayList<Character> piles = new ArrayList<>();
                for (int i = 0; i < s.length(); i++) {
                    char c = s.charAt(i);
                    int left = 0, right = piles.size();
                    while (left < right) {
                        int mid = left + (right - left) / 2;
                        if (piles.get(mid) <= c) {
                            left = mid + 1;
                        } else {
                            right = mid;
                        }
                    }
                    if (left == piles.size()) {
                        piles.add(c);
                    } else {
                        piles.set(left, c);
                    }
                }
                System.out.println(piles.size());
            }
        }
    }
}
