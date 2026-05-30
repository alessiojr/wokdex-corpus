# Tutorial: Logística de Compras Intergalácticas

Dona Parcinova precisa ir regularmente ao Mercado Central de Órbiton para comprar suprimentos e peças. Ela pediu ajuda para sua filha, Mangojata, para criar um programa que calcule o valor total que ela deve levar em créditos para comprar tudo na sua lista.

Para resolver este desafio, siga este passo a passo:
1. Comece lendo o número de viagens ($N$).
2. Para cada viagem, leia o total de produtos disponíveis ($M$).
3. Armazene o preço de cada produto em um **Dicionário (ou Mapa)**, onde a chave é o nome do produto e o valor é o preço dele.
4. Leia a quantidade de suprimentos que Dona Parcinova deseja comprar ($P$).
5. Para cada um dos $P$ itens desejados, leia o nome dele e a quantidade necessária.
6. Multiplique o preço do produto (que você guardou no dicionário) pela quantidade desejada e some esse valor ao custo total da viagem.

## Entrada

A primeira linha contém um inteiro $N$ (número de casos de teste).
Cada caso de teste inicia com um inteiro $M$ (quantidade de produtos à venda).
Seguem $M$ linhas com o nome do produto e seu preço em créditos galácticos.
A próxima linha contém um inteiro $P$ ($1 \le P \le M$) representando a quantidade de itens na lista de compras.
Seguem $P$ linhas com o nome de cada produto e a quantidade inteira desejada.

## Saída

Para cada viagem, imprima o valor total que será gasto por Dona Parcinova no formato: `R$ ` seguido do valor formatado com 2 casas decimais.

| Exemplo de Entrada | Exemplo de Saída |
| :--- | :--- |
| 2<br>4<br>mamao 2.19<br>cebola 3.10<br>tomate 2.80<br>uva 2.73<br>3<br>mamao 2<br>tomate 1<br>uva 3<br>5<br>morango 6.70<br>repolho 1.12<br>brocolis 1.71<br>tomate 2.80<br>cebola 2.81<br>4<br>brocolis 2<br>tomate 1<br>cebola 1<br>morango 1 | R$ 15.37<br>R$ 15.73 |
