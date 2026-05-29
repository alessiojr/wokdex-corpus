# Dama

O jogo de xadrez possui várias peças com movimentos curiosos: uma delas é a Dama (ou Rainha), que pode se mover qualquer quantidade de casas na horizontal, na vertical ou nas diagonais.

O seu amigo quer saber se, dado um tabuleiro de xadrez padrão ($8 \times 8$), qual é o número mínimo de movimentos que uma Dama precisa fazer para sair de uma casa de origem $(X_1, Y_1)$ até uma casa de destino $(X_2, Y_2)$.

A Dama não tem restrições de peças bloqueando o caminho, ou seja, o tabuleiro estará sempre vazio.

## Entrada
A entrada contém vários casos de teste. 
Cada caso de teste é composto por uma linha contendo quatro inteiros: $X_1, Y_1, X_2, Y_2$ ($1 \leq X_1, Y_1, X_2, Y_2 \leq 8$). 

A entrada termina com uma linha contendo `0 0 0 0`, que não deve ser processada.

## Saída
Para cada caso de teste, imprima o número mínimo de movimentos necessários para a Dama chegar ao destino.

---
### Dica do Mestre (Step-by-step)

A chave para esse problema é não tentar simular os movimentos de xadrez de verdade com loops de busca! Tudo o que precisamos fazer é verificar 3 condições estáticas usando a lógica do plano cartesiano. 
Lembre-se: em um tabuleiro vazio, uma Dama sempre consegue chegar em **qualquer lugar** com no máximo $2$ movimentos!

**Caso 1: Origem == Destino**
Se $X_1 == X_2$ E $Y_1 == Y_2$, significa que a Dama já está no local correto. O custo é **$0$** movimentos.

**Caso 2: Linhas, Colunas ou Diagonais (1 Movimento)**
Como a Dama anda na horizontal, vertical e diagonal sem limites, se ela estiver perfeitamente alinhada com o destino, o custo é apenas **$1$** movimento.
* Alinhamento Horizontal: $Y_1 == Y_2$
* Alinhamento Vertical: $X_1 == X_2$
* Alinhamento Diagonal: A matemática de uma diagonal perfeita nos diz que a distância andada em X é igual à distância andada em Y. Ou seja: a diferença absoluta entre $X_1$ e $X_2$ é idêntica à diferença absoluta entre $Y_1$ e $Y_2$ (`abs(X1 - X2) == abs(Y1 - Y2)`).
Se qualquer uma dessas três regras for verdadeira, a resposta é $1$.

**Caso 3: Restante (2 Movimentos)**
Se a Dama não estiver no destino, e nem alinhada, não se desespere. Ela sempre pode ir para uma casa intermediária que sirva de intersecção, e depois para o destino. O custo será sempre **$2$** movimentos. 

Só isso! Um bloco `if/else if/else` resolve o problema matematicamente em `O(1)`.
