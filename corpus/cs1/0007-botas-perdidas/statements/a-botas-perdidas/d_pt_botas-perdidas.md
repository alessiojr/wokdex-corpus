# Tutorial: Contando Pares

Este problema pede para contar quantos pares de botas corretos podem ser formados. Um par correto consiste em duas botas do mesmo tamanho $M$, uma para o pé esquerdo ($E$) e outra para o pé direito ($D$).

Para resolver o "Desafio do Sargento", precisamos organizar os dados das botas. Como $M$ varia apenas de 30 a 60, podemos usar essa informação a nosso favor.

## Passo a Passo

1.  **Ler a Quantidade de Botas:**
    Primeiro, leia o número inteiro $N$. Se não houver mais entrada (Fim de Arquivo), o programa deve terminar.

2.  **Inicializar Contadores:**
    Crie uma maneira de armazenar a contagem de botas para cada tamanho ($30$ a $60$) e para cada pé (Esquerdo e Direito).
    *   Sugestão: Crie dois vetores (arrays) de tamanho 61 (ou map), um para botas esquerdas (`E`) e outro para botas direitas (`D`). Inicialize todos com 0.

3.  **Processar Cada Bota:**
    Para cada uma das $N$ botas:
    *   Leia o tamanho $M$ e o lado $L$.
    *   Se $L = 'E'$, incremente o contador de botas esquerdas no índice $M$.
    *   Se $L = 'D'$, incremente o contador de botas direitas no índice $M$.

4.  **Calcular o Total de Pares:**
    Após ler todas as $N$ botas, precisamos calcular quantos pares podem ser formados.
    *   Para cada tamanho de bota possível (de $30$ a $60$):
        *   O número de pares desse tamanho é o menor valor entre a quantidade de botas esquerdas e a quantidade de botas direitas desse tamanho.
        *   Exemplo: Se temos 3 botas 40 E e 5 botas 40 D, podemos formar `min(3, 5) = 3` pares.
    *   Some o número de pares de todos os tamanhos para obter o resultado final.

5.  **Imprimir o Resultado:**
    Imprima o total calculado. Lembre-se de repetir o processo para cada caso de teste.

## Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso tem um inteiro **N** ($2 \leq N \leq 10^4$). As **N** linhas seguintes têm um inteiro **M** ($30 \leq M \leq 60$) e uma letra **L** ('D' ou 'E').

## Saída

Para cada caso, imprima um inteiro com o total de pares formados.

## Exemplo

| Entrada | Saída |
|:--- |:--- |
| 4 | 2 |
| 40 D | |
| 41 E | |
| 41 D | |
| 40 E | |
| 6 | 1 |
| 38 E | |
| 38 E | |
| 40 D | |
| 38 D | |
| 40 D | |
| 37 E | |
