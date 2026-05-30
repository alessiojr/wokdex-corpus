# Mercado Interplanetário: Operação Abastecimento

Após meses patrulhando as bordas da Nebulosa de Andrômeda, a frota da Almirante Parcinova finalmente atracou no Posto de Trocas de Xandar. O estoque de rações sintéticas e células de energia está nas últimas, e a tripulação não aguenta mais comer pasta de algas de Kepler.

A Almirante designou sua oficial de logística, Mangojata, para uma missão crítica: descer ao mercado da superfície e adquirir todos os suprimentos da lista oficial. No entanto, os preços no setor flutuam mais que a gravidade em um buraco negro, e Mangojata precisa calcular exatamente quantos créditos a Federação deve transferir para o posto antes que a carga seja liberada.

Sua tarefa é processar os registros de preços do mercado e a lista de prioridades da Almirante para determinar o custo total de cada expedição de abastecimento.

## Entrada

A primeira linha contém um inteiro $N$, representando o número de expedições de abastecimento programadas.

Para cada expedição:
- Um inteiro $M$ indica a variedade de produtos disponíveis no posto de trocas.
- Seguem $M$ linhas, cada uma contendo o nome de um suprimento (até 50 caracteres) e seu respectivo preço em créditos galácticos.
- Após o catálogo, um inteiro $P$ ($1 \le P \le M$) indica quantos itens diferentes constam na lista de Mangojata.
- Seguem $P$ linhas, cada uma com o nome do suprimento desejado e a quantidade necessária.

## Saída

Para cada expedição, exiba o custo total com a precisão exigida pelo conselho financeiro, utilizando o prefixo de créditos R$ seguido de um espaço e o valor com duas casas decimais.

| Exemplo de Entrada                                                                                                                                                                                                                              | Exemplo de Saída      |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| 2<br>4<br>mamao 2.19<br>cebola 3.10<br>tomate 2.80<br>uva 2.73<br>3<br>mamao 2<br>tomate 1<br>uva 3<br>5<br>morango 6.70<br>repolho 1.12<br>brocolis 1.71<br>tomate 2.80<br>cebola 2.81<br>4<br>brocolis 2<br>tomate 1<br>cebola 1<br>morango 1 | R\$ 15.37<br>R$ 15.73 |
