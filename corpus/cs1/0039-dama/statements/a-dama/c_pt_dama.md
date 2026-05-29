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
