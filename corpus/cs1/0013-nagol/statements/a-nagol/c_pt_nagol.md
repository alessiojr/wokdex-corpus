# Nagol – Versão Educacional

Nagol, o designer de azulejos, preenche uma parede de $L \times C$ seguindo uma ordem linear rígida: linha por linha, da esquerda para a direita.

### Dica de Estratégia
Para resolver este problema de forma eficiente, você deve converter a posição bidimensional $(X, Y)$ em um **índice linear** $k$. 

Imagine que todos os azulejos foram colocados em uma fila única na ordem em que Nagol os risca. O azulejo $(0, 0)$ é o primeiro ($k=0$), o $(0, 1)$ é o segundo ($k=1$), e assim por diante. Quando Nagol termina a primeira linha (coluna $C-1$), ele passa para a linha 1, coluna 0.

**Perguntas para refletir:**
1. Qual é a fórmula matemática que calcula a posição $k$ de um azulejo $(X, Y)$ em uma grade com $C$ colunas?
2. Como a alternância de mão (sempre começando com a Direita) se relaciona com a paridade (ser par ou ímpar) do índice $k$?

### Complexidade Alvo
O limite de tempo e as dimensões da grade ($10^5$) exigem uma solução de **complexidade $O(1)$**. Evite usar laços de repetição (`loops`) para percorrer a grade.

---
[Acessar Enunciado Completo](nagol.md)
