# O Sargento Rigoroso

Este ano, o sargento está tendo mais trabalho do que de costume para treinar os recrutas. Um deles é muito atrapalhado e, ocasionalmente, faz tudo errado – por exemplo, ao invés de virar à direita quando comandado, vira à esquerda, causando grande confusão no batalhão.

O sargento tem fama de durão e não vai deixar o recruta em paz enquanto ele não aprender a executar corretamente os comandos. Na tarde de sábado, enquanto todos os outros recrutas estavam de folga, ele obrigou o recruta a fazer um treinamento extra. Com o recruta marchando parado no mesmo lugar, o sargento emitiu uma série de comandos "Esquerda, Volver!" e "Direita, Volver!". 

A cada comando, o recruta deve girar sobre o mesmo ponto e dar um quarto de volta na direção correspondente ao comando. O recruta inicia o treinamento com a face voltada para o **Norte**.

No entanto, durante o treinamento, o sargento emitiu uma série de comandos tão extensa e tão rapidamente que até ele ficou confuso e não sabe para qual direção o recruta deve estar olhando após a execução de todos os comandos. Você pode ajudar o sargento a descobrir a posição final do recruta?

## Entrada

A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro $N$ indicando o número de comandos emitidos pelo sargento ($1 \leq N \leq 1000$). 
A segunda linha contém $N$ caracteres, descrevendo a série de comandos emitidos pelo sargento. Cada comando é representado por uma letra: 
*   'E' (para "Esquerda, Volver!")
*   'D' (para "Direita, Volver!")

O final da entrada é indicado por $N = 0$.

## Saída

Para cada caso de teste da entrada, seu programa deve produzir uma linha de saída, indicando a direção para a qual o recruta deve ter sua face voltada após realizar a série de comandos, considerando que no início o recruta tem sua face voltada para o **Norte**. A linha deve conter uma letra entre 'N', 'L', 'S' e 'O', representando respectivamente as direções Norte, Leste, Sul e Oeste.

## Exemplos

| Entrada | Saída |
|:--------|:------|
| 3       | L     |
| DDE     |       |
| 2       | S     |
| EE      |       |
| 0       |       |
