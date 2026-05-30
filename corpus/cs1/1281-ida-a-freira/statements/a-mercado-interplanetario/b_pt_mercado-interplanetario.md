# Posto de Trocas Galáctico

Dona Parcinova é uma exploradora veterana que viaja entre sistemas estelares para abastecer sua nave com suprimentos frescos. Ela pediu à sua filha, Mangojata, que desenvolvesse um sistema para calcular automaticamente o total de créditos galácticos necessários para cada expedição ao mercado de um planeta.

O objetivo é simples: dado um catálogo de itens disponíveis com seus respectivos preços e uma lista de compras contendo as quantidades desejadas, o programa deve gerar o valor total que Parcinova precisa desembolsar.

## Entrada

A primeira linha contém um inteiro $N$, que indica a quantidade de paradas em postos de trocas (número de casos de teste).

Cada caso de teste inicia com um inteiro $M$, indicando a quantidade de tipos de suprimentos disponíveis para venda.
Seguem $M$ linhas, cada uma contendo o nome do produto (até 50 caracteres) e seu preço unitário (em créditos).

A próxima linha contém um inteiro $P$ ($1 \le P \le M$), que indica a quantidade de diferentes produtos da lista de compras.
Seguem $P$ linhas, cada uma contendo o nome do produto e a quantidade inteira desejada.

## Saída

Para cada caso de teste, imprima o valor total gasto no formato: `R$ ` seguido do valor com 2 casas decimais.

| Exemplo de Entrada | Exemplo de Saída |
| :--- | :--- |
| 2<br>4<br>mamao 2.19<br>cebola 3.10<br>tomate 2.80<br>uva 2.73<br>3<br>mamao 2<br>tomate 1<br>uva 3<br>5<br>morango 6.70<br>repolho 1.12<br>brocolis 1.71<br>tomate 2.80<br>cebola 2.81<br>4<br>brocolis 2<br>tomate 1<br>cebola 1<br>morango 1 | R$ 15.37<br>R$ 15.73 |
