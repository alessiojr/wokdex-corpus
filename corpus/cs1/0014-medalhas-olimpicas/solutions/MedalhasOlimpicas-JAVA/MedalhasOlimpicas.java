// @author Arthur Baltar Eler

import java.util.Scanner;

public class MedalhasOlimpicas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int o1 = sc.nextInt();
        int p1 = sc.nextInt();
        int b1 = sc.nextInt();

        int o2 = sc.nextInt();
        int p2 = sc.nextInt();
        int b2 = sc.nextInt();

        if (o1 > o2) {
            System.out.println("A");
        } else if (o2 > o1) {
            System.out.println("B");
        } else if (p1 > p2) {
            System.out.println("A");
        } else if (p2 > p1) {
            System.out.println("B");
        } else {
            System.out.println(b1 > b2 ? "A" : "B");
        }

        sc.close();
    }
}
