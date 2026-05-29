// @author Arthur Baltar Eler

import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MedalhasOlimpicas {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter consoleOutput = new PrintWriter(System.out);

        int o1 = 0, p1 = 0, b1 = 0, o2 = 0, p2 = 0, b2 = 0;

        for (int i = 0; i < 6; i++) {
            int medalhas = Integer.parseInt(br.readLine());

            if (i < 3) {
                if (i == 0) o1 = medalhas;
                else if (i == 1) p1 = medalhas;
                else b1 = medalhas;
            } else {
                if (i == 3) o2 = medalhas;
                else if (i == 4) p2 = medalhas;
                else b2 = medalhas;
            }
        }

        if (o1 > o2 || (o1 == o2 && p1 > p2) || (o1 == o2 && p1 == p2 && b1 > b2)) {
            consoleOutput.println("A");
        } else {
            consoleOutput.println("B");
        }

        consoleOutput.flush();
        consoleOutput.close();
    }

}
