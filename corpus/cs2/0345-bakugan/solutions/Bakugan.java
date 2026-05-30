import java.util.ArrayList;
import java.util.Scanner;

public class Bakugan {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r, m, l, sM, sL, t;
        char res;

        while (sc.hasNextInt()) {
            ArrayList<Integer> mF = new ArrayList<Integer>();
            ArrayList<Integer> lF = new ArrayList<Integer>();
            r = sc.nextInt();
            if (r == 0) {
                System.exit(0);
            }
            sM = 0;
            sL = 0;
            t = 0;
            for (int i = 0; i < r; i++) {
                m = sc.nextInt();
                mF.add(m);
            }
            for (int j = 0; j < r; j++) {
                l = sc.nextInt();
                lF.add(l);
            }
            for (int k = 0; k < r; k++) {
                sM += mF.get(k);
                sL += lF.get(k);
                if (k < r - 2 && t == 0) {
                    if (mF.get(k) == mF.get(k + 1) && mF.get(k) == mF.get(k + 2) && lF.get(k) == lF.get(k + 1)
                            && lF.get(k) == lF.get(k + 2)) {
                        sM += 0;
                        t = 1;
                    } else if (mF.get(k) == mF.get(k + 1) && mF.get(k) == mF.get(k + 2)) {
                        sM += 30;
                        t = 1;
                    } else if (lF.get(k) == lF.get(k + 1) && lF.get(k) == lF.get(k + 2)) {
                        sL += 30;
                        t = 1;
                    }

                }
            }
            if (sM == sL) {
                res = 'T';
            } else if (sM > sL) {
                res = 'M';
            } else {
                res = 'L';
            }

            System.out.println(res);
        }

    }

}
