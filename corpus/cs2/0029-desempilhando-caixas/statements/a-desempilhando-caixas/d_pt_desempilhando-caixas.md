# Desempilhando Caixas — Dica do Mestre

## Entendendo o Problema

Imagine que as pilhas de caixas estão arrumadas em fila, uma ao lado da outra. Você quer pegar a caixa 1 com o mínimo de esforço.

Uma caixa só pode ser removida do topo de sua pilha se pelo menos um de seus lados (esquerdo ou direito) está "exposto" — ou seja, não há caixa adjacente na mesma altura ou acima.

## Estratégia de Solução

### Passo 1: Localize a caixa 1
Descubra em qual pilha (índice `col`) e em que altura (índice `row`) a caixa 1 se encontra. Lembre-se: as caixas são listadas da base ao topo.

### Passo 2: Escolha o melhor lado
A caixa 1 precisa estar com um lado livre. Para isso, pode ser necessário remover caixas acima dela E caixas de pilhas vizinhas que bloqueiam o lado.

Para cada lado (esquerda ou direita), calcule o custo:
- **Custo acima:** Todas as caixas acima da caixa 1 na mesma pilha precisam ser removidas primeiro (são `altura_da_pilha - row - 1` caixas).
- **Custo lateral:** Partindo da pilha onde está a caixa 1 em direção à borda escolhida, para cada pilha adjacente cuja altura ultrapassa a posição (row) da caixa 1, você precisa remover o excesso.

### Passo 3: Calcule o mínimo
O resultado é `min(custo_esquerda, custo_direita)` — o melhor dos dois caminhos.

## Complexidade
A solução ótima processa cada caso de teste em $O(N)$, pois basta percorrer as pilhas uma vez para cada direção.

## Armadilhas Comuns
- **Esquecer que a caixa 1 não conta na resposta** — a resposta é quantas caixas *além* da caixa 1 são removidas.
- **Não considerar que as pilhas das bordas têm um lado automaticamente livre.**
- **Tratar múltiplos casos de teste** — lembre-se que a entrada termina com `0 0`.
