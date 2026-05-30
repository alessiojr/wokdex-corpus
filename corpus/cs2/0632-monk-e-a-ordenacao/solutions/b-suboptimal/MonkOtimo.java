import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class MonkOtimo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Long[]>[] menor;
        int n = sc.nextInt();
        Long[][] vec = new Long[n][2];
        for (int i = 0; i < n; i++) { // processo: n
            vec[i][0] = vec[i][1] = sc.nextLong();
        }
        int soma = 1;
        while (soma != 0) { //5
            menor = new List[100000];
            soma = 0;
            for (int i = 0; i < n; i++) { //processo: n
                int index = Integer.parseInt(String.valueOf(vec[i][1] % 100000));
                if (menor[index] == null) {
                    menor[index] = new LinkedList<>();
                }
                menor[index].add(vec[i]);
                vec[i][1] = vec[i][1] / 100000;
                soma += vec[i][1];
            }
            int count = 0;
            for (List<Long[]> list : menor) { //1000000 + 2000000
                if (list != null) {
                    for (Long[] integer : list) {
                        vec[count++] = integer;
                    }
                }
            }
            int i = 0;
            for (; i < vec.length - 1; i++) {
                System.out.printf("%d ", vec[i][0]);
            }
            System.out.println(vec[i][0]);
        }
    }
}

