# O Manual do Recruta

Este ano, o sargento está tendo mais trabalho do que de costume para treinar os recrutas. Um deles é muito atrapalhado e precisa de um manual passo-a-passo para não errar.

O sargento emite comandos "Esquerda, Volver!" ('E') e "Direita, Volver!" ('D'). O recruta começa sempre olhando para o **Norte**.

Para ajudar o recruta, podemos seguir este manual de instruções (algoritmo):

1.  Crie uma lista com as direções em ordem horária: `['N', 'L', 'S', 'O']`.
2.  Use uma variável para guardar o índice da direção atual. Como ele começa no Norte, o índice inicial é **0**.
3.  Para cada comando recebido:
    *   Se for **'D' (Direita)**: O recruta gira no sentido horário. Aumente o índice em 1. Lembre-se que depois do Oeste (índice 3), vem o Norte (índice 0). Você pode usar o operador de resto da divisão (`% 4`) para isso.
    *   Se for **'E' (Esquerda)**: O recruta gira no sentido anti-horário. Diminua o índice em 1. Se o índice ficar negativo, volte para o final da lista.
4.  Ao final de todos os comandos, a direção correspondente ao índice final é a resposta.

## Entrada

A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro $N$ ($1 \leq N \leq 1000$). 
A segunda linha contém $N$ caracteres ('E' ou 'D').
O final da entrada é indicado por $N = 0$.

## Saída

Para cada caso de teste, imprima a letra da direção final ('N', 'L', 'S' ou 'O').

## Exemplos

| Entrada | Saída |
|:--- |:--- |
| 3 | L |
| DDE | |
| 2 | S |
| EE | |
| 0 | |
