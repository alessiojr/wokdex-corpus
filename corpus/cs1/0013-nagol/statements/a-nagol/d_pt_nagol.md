# Nagol – Tutorial

Neste tutorial, vamos derivar a lógica matemática necessária para determinar qual mão Nagol utiliza para riscar um azulejo específico sem precisar simular todo o processo.

### 1. Entendendo a Linearização
Nagol risca os azulejos linha por linha. Em uma grade com $C$ colunas, cada linha completa possui exatamente $C$ azulejos.
- Para chegar na linha $X$, Nagol já riscou todas as linhas de $0$ até $X-1$, totalizando $X \cdot C$ azulejos.
- Na linha $X$, ele risca as colunas de $0$ até $Y$. O azulejo na coluna $Y$ é o $(Y+1)$-ésimo azulejo daquela linha.

A posição global $k$ (começando em 0) do azulejo $(X, Y)$ é dada pela fórmula:
$$k = X \cdot C + Y$$

### 2. A Lógica da Alternância
Nagol alterna as mãos a cada azulejo, começando sempre com a **Direita**.
- Azulejo $k=0$: Direita (Par)
- Azulejo $k=1$: Esquerda (Ímpar)
- Azulejo $k=2$: Direita (Par)
- ... e assim por diante.

Portanto:
- Se $k$ é **par**, a mão é **Direita**.
- Se $k$ é **ímpar**, a mão é **Esquerda**.

### 3. Exemplo Prático
Parede $L=2, C=3$. Posição $(0, 1)$:
$k = 0 \cdot 3 + 1 = 1$. 
Como 1 é ímpar, a resposta é **Esquerda**.

Parede $L=4, C=4$. Posição $(2, 2)$:
$k = 2 \cdot 4 + 2 = 10$.
Como 10 é par, a resposta é **Direita**.

### 4. Dica de Implementação (Overflow)
As dimensões $L$ e $C$ podem chegar a $10^5$. O produto $X \cdot C$ pode chegar a $10^{10}$, o que ultrapassa o limite de um inteiro de 32 bits ($2 \cdot 10^9$).
**Importante**: Use tipos de dados de 64 bits para o cálculo do índice (ex: `long long` em C++, `long` em Java ou os inteiros nativos do Python).

---
[Retornar ao Desafio](nagol.md)
