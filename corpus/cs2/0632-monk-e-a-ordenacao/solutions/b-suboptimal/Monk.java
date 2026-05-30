
import java.util.Scanner;
import java.util.LinkedList;
import java.util.List;

public class Monk {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long vet[] = new long[n];

        List<Long> list[] = new List[200000];
        for (int i = 0; i < list.length; i++) {
            list[i] = new LinkedList();
        }

        for (int i = 0; i < n; i++) {
            vet[i] = sc.nextLong();
        }
        int parte = 1;
        while (true) {
            for (int i = 0; i < vet.length; i++) {
                long chave = (long) (vet[i] % Math.pow(100000, parte));
                chave /= (long) Math.pow(100000, parte - 1);
                chave += 100000;
                list[(int) chave].add(vet[i]);
            }
            if (list[100000].size() == n) {
                break;
            }
            int aux = 0;
            for (int i = 0; i < list.length; i++) {
                while (!list[i].isEmpty()) {
                    vet[aux] = list[i].remove(0);
                    System.out.print(vet[aux++] + " ");
                }
            }
            System.out.println("");
            parte++;
        }

    }
}
