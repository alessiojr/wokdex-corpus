import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    static class Consulta {
        int inicio, fim;
        Consulta(int inicio, int fim) {
            this.inicio = inicio;
            this.fim = fim;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int N = sc.nextInt();
        
        Consulta[] consultas = new Consulta[N];
        for (int i = 0; i < N; i++) {
            consultas[i] = new Consulta(sc.nextInt(), sc.nextInt());
        }
        
        Arrays.sort(consultas, new Comparator<Consulta>() {
            @Override
            public int compare(Consulta a, Consulta b) {
                if (a.fim != b.fim) return Integer.compare(a.fim, b.fim);
                return Integer.compare(a.inicio, b.inicio);
            }
        });
        
        int atendidas = 0;
        int ultimoFim = 0;
        
        for (int i = 0; i < N; i++) {
            if (consultas[i].inicio >= ultimoFim) {
                atendidas++;
                ultimoFim = consultas[i].fim;
            }
        }
        
        System.out.println(atendidas);
    }
}
