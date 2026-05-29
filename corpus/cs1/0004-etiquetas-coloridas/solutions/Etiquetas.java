package SBC_2016;

import java.util.Scanner;

public class Etiquetas {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {

            String r = "0x" + sc.next();
            String g = "0x" + sc.next();
            String b = "0x" + sc.next();

            long valorR = Long.decode(r);
            long valorG = Integer.decode(g);
            long valorB = Integer.decode(b);

            long azuis = (valorG / valorB) * (valorG / valorB);
            long verdes = (valorR / valorG) * (valorR / valorG);
            int vermelhas = 1;
            if (verdes == 0) {
                System.out.println(Long.toHexString(vermelhas));
            } else {
                if (azuis == 0) {
                    System.out.println(Long.toHexString(vermelhas + verdes));
                } else {
                    System.out.println(Long.toHexString(vermelhas + verdes * azuis + verdes));
                }
            }

        }

    }

}
