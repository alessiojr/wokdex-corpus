# Abastecimento na Estação Espacial

A Almirante Parcinova e sua oficial de logística, Mangojata, estão em uma missão de longo prazo na Estação Espacial de Órbiton. Para garantir que a tripulação tenha suprimentos suficientes, elas precisam calcular o custo exato das compras em créditos galácticos antes de autorizar o teletransporte dos itens para a nave.

Para resolver este problema de forma eficiente, você deve associar cada item disponível ao seu preço. Uma estratégia recomendada é utilizar uma estrutura de dados de **Mapa ou Dicionário** para armazenar o catálogo de preços, permitindo que você recupere o valor de cada item da lista de compras rapidamente.

## Entrada

A primeira linha contém um inteiro $N$, representando o número de idas ao mercado (casos de teste).

Cada caso de teste começa com um inteiro $M$, a quantidade de produtos disponíveis.
Seguem $M$ linhas com o nome do produto e seu preço em créditos.

Abaixo, um inteiro $P$ ($1 \le P \le M$) indica a quantidade de itens que Mangojata deseja comprar.
Seguem $P$ linhas com o nome do produto e a quantidade desejada.

## Saída

Para cada caso de teste, imprima o total gasto formatado como `R$ ` seguido do valor com 2 casas decimais.

| Exemplo de Entrada | Exemplo de Saída |
| :--- | :--- |
| 2<br>4<br>mamao 2.19<br>cebola 3.10<br>tomate 2.80<br>uva 2.73<br>3<br>mamao 2<br>tomate 1<br>uva 3<br>5<br>morango 6.70<br>repolho 1.12<br>brocolis 1.71<br>tomate 2.80<br>cebola 2.81<br>4<br>brocolis 2<br>tomate 1<br>cebola 1<br>morango 1 | R$ 15.37<br>R$ 15.73 |
