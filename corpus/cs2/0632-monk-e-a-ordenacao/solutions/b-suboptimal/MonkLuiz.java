import java.util.ArrayList;
import java.util.Scanner;

public class MonkLuiz {

    private static long[] vetor;

    public static void main(String[] args) {
        Scanner leia = new Scanner(System.in);
        int tam = leia.nextInt();
        vetor = new long[tam];
        long maior = Integer.MIN_VALUE;
        for (int i = 0; i < tam; i++) {
            vetor[i] = leia.nextLong();
            if (maior < vetor[i]) {
                maior = vetor[i];
            }
        }

        String s = String.valueOf(maior);

        int size = s.length();

        radixSort(vetor, size);
    }

    private static void radixSort(long[] vetor, int qtd) {
        long mod = 10;
        int imp = 1;
        int repete = 0;

        long[] aux = new long[vetor.length];

        for (int i = 1; i <= qtd; i++) {
            mod = (long) Math.pow(10, i);
            countingSort(vetor, mod, i);
            if (i % 5 == 0 || i == qtd) {
                print(vetor);
            }
        }
    }

    private static boolean comaparaVetor(long[] v1, long[] v2) {
        int cont = 0;
        for (int i = 0; i < v1.length; i++) {
            if (v1[i] == v2[i]) {
                cont++;
            }
        }
        return cont == v1.length;
    }

    private static void countingSort(long[] vetor, long mod, long n) {
        long[] saida = new long[vetor.length];

        long[] aux = new long[10];

        // contagem da quantidade de digitos
        for (int i = 0; i < vetor.length; i++) {
            int pos = (int) ((vetor[i] % mod) / Math.pow(10, n - 1));
            if (pos < 0) {
                pos *= -1;
            }
            aux[pos] += 1;
        }

        // obtenção da posição dos dígitos
        for (int i = 1; i < aux.length; i++) {
            aux[i] += aux[i - 1];
        }

        // matriz de saída
        for (int i = vetor.length - 1; i > -1; i--) {
            int pos = (int) (((long) vetor[i] % mod) / (long) Math.pow(10, n - 1));
            if (pos < 0) {
                pos *= -1;
            }
            int posSaida = (int) aux[pos] - 1;
            int posAux = (int) (((long) vetor[i] % mod) / (long) Math.pow(10, n - 1));
            if (posAux < 0) {
                posAux *= -1;
            }
            if (posSaida < 0) {
                posAux *= -1;
            }
            saida[posSaida] = vetor[i];
            aux[posAux]--;
        }

        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = saida[i];
        }
    }

    // Uma função utilitária para imprimir uma matriz
    private static void print(long arr[]) {
        System.out.println("\n");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
