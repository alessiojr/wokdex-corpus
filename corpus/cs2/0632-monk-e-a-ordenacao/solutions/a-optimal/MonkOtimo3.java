
/**
 * ============================================================================
 * SOLUÇÃO ÓTIMA: RADIX SORT + FAST I/O + OFFSET (Deslocamento)
 * ============================================================================
 * 
 * Por que a versão baseada em Objetos (Scanner, LinkedList, Long) falhou?
 * Em problemas de programação competitiva ou processamento extremo, a complexidade
 * de tempo O(N) do Radix Sort não é suficiente se a "constante" do algoritmo for muito alta.
 * Instanciar milhares de LinkedLists e usar classes Wrapper (Long) fragmenta a memória
 * e sobrecarrega o Garbage Collector da JVM, resultando em TLE (Time Limit Exceeded)
 * ou MLE (Memory Limit Exceeded).
 * 
 * OTIMIZAÇÕES APLICADAS:
 * 1. Fast I/O: Substituição do `Scanner` (que usa regex pesadas) e `System.out`
 *    (sincronizado) por `BufferedReader`, `StringTokenizer` e `PrintWriter`. Isso
 *    lida com os dados em blocos de memória (buffers), reduzindo gargalos de leitura/escrita.
 * 2. Memória Contígua (Arrays Primitivos): Uso exclusivo de `long[]` e `int[]`. 
 *    Isso garante que a memória seja alocada em blocos sequenciais na RAM, 
 *    aproveitando ao máximo o cache L1/L2 do processador e evitando o GC.
 * 3. Truque do Offset (Deslocamento): O Java preserva o sinal em operações de
 *    módulo (%). Um número como -98347 causaria um ArrayIndexOutOfBounds. Em vez
 *    de criar "ifs" custosos para separar positivos e negativos, dobramos o tamanho
 *    do array de contagem (para 200.000) e somamos +100.000 a todos os índices.
 *    Assim, -99999 vira índice 1, 0 vira 100000, e +99999 vira 199999. Isso ordena
 *    os números negativos naturalmente, sem lógica condicional extra.
 * 
 * ============================================================================
 * COMO UM ALUNO PODE DESCOBRIR ESTES TRUQUES? (Mentalidade de Otimização)
 * ============================================================================
 * 
 * 1. Desconfie do "Motor" da Linguagem: Um aluno deve aprender que Big-O (O(N)) é
 *    apenas a teoria matemática. Na prática, a forma como a linguagem (JVM) gere a
 *    memória importa muito. O aluno descobre isso estudando como tipos primitivos 
 *    diferem de Objetos sob o capô.
 * 
 * 2. Identificação de Gargalos (Profiling mental): Se a lógica está certa (O(N)) e 
 *    ainda dá TLE, o gargalo está na entrada/saída ou na alocação de memória (o `new` 
 *    dentro de loops de alta frequência é sempre um suspeito). Pesquisar por 
 *    "Fast I/O in Java" é geralmente o primeiro rito de passagem de um programador.
 * 
 * 3. Pensamento Matemático de Mapeamento: O truque do "Offset" nasce quando paramos
 *    de pensar no array como uma "lista de gavetas a partir do zero" e passamos a 
 *    vê-lo como um plano cartesiano ou uma reta numérica que podemos "deslocar"
 *    (translação matemática) somando uma constante para que todos os valores caiam
 *    no quadrante positivo.
 * 
 * 4. Ler o Código dos Outros: A maior parte desses truques não se inventa do zero; 
 *    eles são padrões da comunidade. Ler os editoriais dos problemas e as soluções 
 *    aceitas dos primeiros colocados é a melhor forma de internalizar essas técnicas.
 */

import java.io.*;
import java.util.StringTokenizer;

public class MonkOtimo3 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        if (!st.hasMoreTokens())
            return;
        int n = Integer.parseInt(st.nextToken());

        long[] arr = new long[n];
        long[] output = new long[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        long mul = 1;
        boolean morePasses = true; // Substitui o maxVal para evitar Overflow

        // Radix Sort base 100.000 blindado para números negativos
        while (morePasses) {
            morePasses = false;

            // Tamanho 200.000 para acomodar resultados de -99999 até +99999
            int[] count = new int[200000];

            // Conta a frequência
            for (int i = 0; i < n; i++) {
                long quotient = arr[i] / mul;

                // Se algum quociente ainda for maior/menor que a base, precisaremos de mais uma
                // passada
                if (quotient >= 100000 || quotient <= -100000) {
                    morePasses = true;
                }

                int digit = (int) (quotient % 100000);

                // O offset de +100000 evita índice negativo e ordena os negativos organicamente
                count[digit + 100000]++;
            }

            // Transforma contagem em posições cumulativas
            for (int i = 1; i < 200000; i++) {
                count[i] += count[i - 1];
            }

            // Constrói o array de saída garantindo a estabilidade da ordenação
            for (int i = n - 1; i >= 0; i--) {
                long quotient = arr[i] / mul;
                int digit = (int) (quotient % 100000);
                output[count[digit + 100000] - 1] = arr[i];
                count[digit + 100000]--;
            }

            // Copia de volta e imprime a passada atual
            for (int i = 0; i < n; i++) {
                arr[i] = output[i];
                out.print(arr[i] + (i == n - 1 ? "" : " "));
            }
            out.println();

            if (morePasses) {
                mul *= 100000;
            }
        }

        // Descarrega o buffer no console
        out.flush();
    }
}