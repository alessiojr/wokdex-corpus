# Construindo Casas

Sr. Pi é um construtor famoso na cidade de Programolândia. Ele precisa de sua ajuda para encontrar os melhores terrenos da cidade para os vários projetos que ele possui.
Por exemplo, ele tem um projeto para construir uma casa de 8 metros por 10 metros, mas a legislação do município só permite construir, neste bairro, em no máximo 20% do terreno. 
Todos os terrenos nesta cidade são **perfeitamente quadrados**. 
Sabendo que os valores dos lados da casa servem apenas como referência para o cálculo da área total a ser construída. (Ex: Uma casa de 1 metro por 10 metros onde é permitido ocupar 100% do terreno, o sr PI precisaria de um terreno de 10m². O valor do lado do terreno, neste caso, seria 3 metros, pois a raiz quadrada é truncada no final para jogar as casas decimais fora).

Ajude o sr. PI a determinar o tamanho exato da medida do lado do terreno que ele deverá comprar.

## Entrada
A entrada é composta de vários casos de testes. Cada caso de teste é composto de três números inteiros $A$, $B$ ($1 \le A, B \le 1000$) e $C$ separados por um espaço. Estes números representam as medidas da casa ($A$ e $B$) e o percentual máximo liberado para construir nesse bairro ($C$ Inteiro). 
Um único valor igual a `0` indica o fim das entradas, não devendo ser processado.

## Saída
Você deverá informar um número inteiro para cada linha de entrada, o qual representa a medida do lado do terreno. Este valor deverá ter suas casas decimais truncadas.

## Exemplo
| Entrada | Saída |
| :-- | :-- |
| 8 10 20<br>1 10 100<br>10 3 100<br>0 | 20<br>3<br>5 |
