# Maratona de Programação da SBC/2016

## B – Concurso de contos (Edição Educacional)

Machado está escrevendo um conto e precisa otimizar sua diagramação para um concurso com regras rígidas de caracteres por linha e linhas por página. Sua tarefa é calcular o número mínimo de páginas necessárias para acomodar todas as palavras do conto, sem quebrá-las entre linhas e respeitando os espaços obrigatórios.

### Estratégia de Solução

A abordagem ideal para este problema é uma **simulação gulosa (greedy simulation)**. Como a ordem das palavras é fixa, basta preencher cada linha com o máximo de palavras possível antes de passar para a próxima:

1.  **Iteração sobre Palavras**: Percorra a lista de palavras mantendo o controle do comprimento atual da linha, do número de linhas na página atual e do total de páginas.
2.  **Lógica de Linha**:
    *   Para a primeira palavra de uma linha, o espaço ocupado é apenas o seu comprimento.
    *   Para as palavras seguintes na mesma linha, deve-se somar o comprimento da palavra + 1 (referente ao espaço em branco).
    *   Se a palavra atual não couber no limite $C$, ela deve iniciar uma nova linha.
3.  **Lógica de Página**:
    *   Ao iniciar uma nova linha, verifique se ela ainda cabe no limite $L$ da página atual.
    *   Se o limite de linhas for atingido, uma nova página deve ser iniciada.

### Complexidade

*   **Tempo**: **O(N)**, onde $N$ é o número de palavras, pois processamos cada palavra exatamente uma vez.
*   **Espaço**: **O(N)** para armazenar as palavras do conto.

---

### Entrada

A primeira linha contém três inteiros $N$, $L$ e $C$ ($2 \le N \le 1000$, $1 \le L \le 30$ e $1 \le C \le 70$). A segunda linha contém o conto composto de $N$ palavras separadas por espaços em branco. Cada palavra tem entre 1 e $C$ letras.

### Saída

Um único número inteiro indicando o número mínimo de páginas ocupadas.

### Exemplos de Entrada e Saída

| Entrada | Saída |
| :--- | :--- |
| 14 4 20<br>Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral | 2 |
| 16 3 30<br>No dia seguinte entrou a dizer de mim nomes feios e acabou alcunhando me Dom Casmurro | 1 |
| 5 2 2<br>a de i de o | 3 |
