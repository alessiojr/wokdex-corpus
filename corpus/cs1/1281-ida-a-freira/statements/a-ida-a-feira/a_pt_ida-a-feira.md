# Ida à Feira

Dona Parcinova costuma ir regularmente à feira para comprar frutas e legumes. Ela pediu então à sua filha, Mangojata, que a ajudasse com as contas e que fizesse um programa que calculasse o valor que precisa levar para poder comprar tudo que está em sua lista de compras, considerando a quantidade de cada tipo de fruta ou legume e os preços destes itens.

## Entrada

A primeira linha de entrada contém um inteiro $N$ que indica a quantidade de idas à feira de dona Parcinova (que nada mais é do que o número de casos de teste que vem a seguir). Cada caso de teste inicia com um inteiro $M$ que indica a quantidade de produtos que estão disponíveis para venda na feira. Seguem os $M$ produtos com seus preços respectivos por unidade ou Kg. A próxima linha de entrada contém um inteiro $P$ ($1 \leq P \leq M$) que indica a quantidade de diferentes produtos que dona Parcinova deseja comprar. Seguem $P$ linhas contendo cada uma delas um texto (com até 50 caracteres) e um valor inteiro, que indicam respectivamente o nome de cada produto e a quantidade deste produto.

## Saída

Para cada caso de teste, imprima o valor que será gasto por dona Parcinova no seguinte formato: `R$` seguido de um espaço e seguido do valor, com 2 casas decimais, conforme o exemplo abaixo.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| 2<br>4<br>mamao 2.19<br>cebola 3.10<br>tomate 2.80<br>uva 2.73<br>3<br>mamao 2<br>tomate 1<br>uva 3<br>5<br>morango 6.70<br>repolho 1.12<br>brocolis 1.71<br>tomate 2.80<br>cebola 2.81<br>4<br>brocolis 2<br>tomate 1<br>cebola 1<br>morango 1 | R$ 15.37<br>R$ 15.73 |
