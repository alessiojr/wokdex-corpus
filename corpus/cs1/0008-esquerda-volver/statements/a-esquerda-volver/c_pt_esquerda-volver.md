# Treinamento com Bússola

Este ano, o sargento está tendo mais trabalho do que de costume para treinar os recrutas. Um deles é muito atrapalhado e, ocasionalmente, faz tudo errado – por exemplo, ao invés de virar à direita quando comandado, vira à esquerda, causando grande confusão no batalhão.

O sargento tem fama de durão e não vai deixar o recruta em paz enquanto ele não aprender a executar corretamente os comandos. Com o recruta marchando parado no mesmo lugar, o sargento emitiu uma série de comandos "Esquerda, Volver!" e "Direita, Volver!". 

Você pode imaginar as direções como os pontos cardeais de uma bússola: Norte (N), Leste (L), Sul (S) e Oeste (O). 
*   Se o recruta está olhando para o **Norte** e vira à **Direita**, ele passa a olhar para o **Leste**.
*   Se ele vira mais uma vez à **Direita**, passa a olhar para o **Sul**, e assim por diante.
*   Virar à **Esquerda** faz o movimento contrário (sentido anti-horário).

Uma dica útil: Você pode associar cada direção a um número:
*   0: Norte
*   1: Leste
*   2: Sul
*   3: Oeste

Assim, virar à Direita é somar 1, e virar à Esquerda é subtrair 1 (ou somar 3).

## Entrada

A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro $N$ indicando o número de comandos ($1 \leq N \leq 1000$). 
A segunda linha contém $N$ caracteres, descrevendo a série de comandos:
*   'E' (Esquerda)
*   'D' (Direita)

O final da entrada é indicado por $N = 0$.

## Saída

Para cada caso de teste, imprima uma linha indicando a direção final do recruta ('N', 'L', 'S' ou 'O').

## Exemplos

| Entrada | Saída |
|:--- |:--- |
| 3 | L |
| DDE | |
| 2 | S |
| EE | |
| 0 | |
