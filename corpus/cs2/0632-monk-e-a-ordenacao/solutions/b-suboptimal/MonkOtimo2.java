import java.io.*;
import java.util.StringTokenizer;

public class MonkOtimo2 {

    public static void main(String[] args) throws IOException {
        // Fast I/O: Essencial para problemas com leitura/saída extremas
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        if (!st.hasMoreTokens())
            return;
        int n = Integer.parseInt(st.nextToken());

        long[] arr = new long[n];
        long[] output = new long[n];
        long maxVal = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
            if (arr[i] > maxVal) {
                maxVal = arr[i]; // Descobrir o maior número dita quantas passadas faremos
            }
        }

        long mul = 1;
        // Radix Sort base 100.000
        while (maxVal / mul > 0) {
            int[] count = new int[100000];

            // Conta a frequência de cada "dígito" na base 100000
            for (int i = 0; i < n; i++) {
                int digit = (int) ((arr[i] / mul) % 100000);
                count[digit]++;
            }

            // Transforma contagem em posições cumulativas
            for (int i = 1; i < 100000; i++) {
                count[i] += count[i - 1];
            }

            // Constrói o array de saída (iterando de trás para frente para manter a
            // estabilidade)
            for (int i = n - 1; i >= 0; i--) {
                int digit = (int) ((arr[i] / mul) % 100000);
                output[count[digit] - 1] = arr[i];
                count[digit]--;
            }

            // Copia de volta para o array original e já imprime a passada
            for (int i = 0; i < n; i++) {
                arr[i] = output[i];
                out.print(arr[i] + (i == n - 1 ? "" : " "));
            }
            out.println();

            mul *= 100000;
        }

        // Garante que todo o texto em buffer seja impresso
        out.flush();
    }
}