# Desempilhando Caixas

## Descrição

Há $N$ caixas numeradas de 1 a $N$ dispostas em $P$ pilhas arrumadas em fila (uma ao lado da outra). Você quer recuperar a caixa de número 1.

**Regra para remover uma caixa:** uma caixa só pode ser removida se:
1. Ela estiver no **topo** de sua pilha.
2. Pelo menos **um dos lados** (esquerdo ou direito) estiver livre, ou seja, a pilha adjacente nesse lado é mais baixa que a posição da caixa, ou não existe pilha nesse lado.

Determine o **número mínimo de caixas que precisam ser removidas**, além da caixa 1, para que a caixa 1 possa ser retirada.

## Entrada

A entrada contém vários casos de teste. Cada caso de teste inicia com uma linha contendo dois inteiros $N$ e $P$ ($1 \leq P \leq N \leq 1000$).

As $P$ linhas seguintes descrevem cada pilha: um inteiro $Q_i$ seguido de $Q_i$ inteiros, representando as caixas de baixo para cima.

A entrada termina com $N = P = 0$.

## Saída

Para cada caso de teste, imprima uma linha contendo um inteiro: o número mínimo de caixas removidas (sem contar a caixa 1) para que ela possa ser retirada.

## Exemplo

| Entrada | Saída |
|---|---|
| 4 3 | 2 |
| 1 3 | 0 |
| 2 1 2 | |
| 1 4 | |
| 4 3 | |
| 1 3 | |
| 2 2 1 | |
| 1 4 | |
| 0 0 | |
