# O Protocolo de Carga de Monk

![Hangar da Estação Espacial](monk_logistics.png "Hangar Espacial"){width=150px align=right}

Monk é o coordenador de logística na Estação Espacial K-06, responsável por organizar milhares de contêineres de carga antes de cada salto dimensional. Cada contêiner possui um Código de Identificação Estelar (CIE) de até 18 dígitos. O porto de carga utiliza um scanner de protocolo antigo que só consegue processar "assinaturas" de 5 dígitos de cada vez, começando pela extremidade menos significativa do código.

O protocolo funciona em ciclos: a cada passagem, o scanner lê uma janela de 5 dígitos (posições 1 a 5 no primeiro ciclo, 6 a 10 no segundo, e assim por diante) e reorganiza a frota de forma que os contêineres com assinaturas menores fiquem à frente. Uma regra crítica é que o sistema é de baixa latência e deve ser estável: se dois contêineres apresentarem a mesma assinatura em um ciclo, sua ordem relativa original deve ser mantida para evitar colisões no hangar. O procedimento se encerra quando uma leitura completa de um ciclo não encontra mais dígitos significativos em nenhum contêiner da frota (ou seja, todas as assinaturas lidas são zero).

Sua tarefa é simular o comportamento do porto de carga e imprimir o estado da frota após cada ajuste realizado pelo scanner.

## Entrada

A primeira linha contém um inteiro $N$ ($1 \le N \le 10^6$), representando o número de contêineres.
A segunda linha contém $N$ inteiros $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$), representando os identificadores (CIE) dos contêineres.

## Saída

Para cada ciclo em que o scanner realizar uma ordenação, imprima uma linha contendo os $N$ identificadores na ordem atual, separados por um espaço.

## Restrições

- $1 \le N \le 10^6$
- $-10^{18} \le A_i \le 10^{18}$
- O tempo limite é rigoroso; utilize métodos de entrada/saída eficientes.

## Exemplos

| Entrada                         | Saída                                                     |
|:--------------------------------|:----------------------------------------------------------|
| 3<br>213456789 167890 123456789 | 213456789 123456789 167890 <br>167890 123456789 213456789 |
