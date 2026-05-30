# Toca do Saci

Depois de muito procurar, Emília finalmente conseguiu encontrar a toca do Saci. A toca tem formato retangular e é formada por um quadriculado de salas de mesmo tamanho, com $N$ salas em uma dimensão e $M$ salas na outra dimensão. 

A figura abaixo mostra um exemplo de mapa da toca, com quatro salas na dimensão horizontal e cinco salas na dimensão vertical. Há uma única entrada, pela sala marcada com o número 3 no mapa. As salas da toca têm portas que comunicam-se apenas com salas vizinhas nas direções horizontal e vertical do mapa.

```text
0 1 1 1 0
0 2 0 1 1
0 0 0 0 1
3 1 1 1 1
```

Emília entrou na toca com o objetivo de pegar o chapéu do Saci. Muito esperta, ela foi deixando estrelinhas coloridas pelas salas por que passou, marcadas com o número `1` no mapa. Ela pegou o chapéu na sala onde o Saci dormia e iniciou o caminho de volta. Está muito escuro e ela precisa acender um fósforo em cada sala. Como os fósforos estão acabando, ela quer saber exatamente quantos fósforos gastará!

Atualmente, ela está na sala marcada com o número `2` no mapa e vai seguir o caminho das estrelinhas até sair pela entrada original, a sala de número `3`. Dado o mapa da toca, escreva um programa para saber por quantas salas Emília deve passar até encontrar a saída.

## Entrada
A primeira linha contém dois inteiros $N$ e $M$ ($1 \le N, M \le 1000$), indicando as dimensões da toca.
Cada uma das $N$ linhas seguintes contém $M$ números inteiros:
- `0`: sala sem estrelinhas.
- `1`: sala com estrelinhas.
- `2`: sala com estrelinhas (posição atual da Emília).
- `3`: sala com estrelinhas (saída da toca).

**Nota importante:** Durante o trajeto até a sala 2, Emília **não passou mais do que uma vez** pela mesma sala. Assim, não há ambiguidades no caminho de volta.

## Saída
Seu programa deve imprimir uma única linha contendo o número total de salas por que Emília passará até chegar à saída.

## Exemplo de Entrada 1
```text
4 5
0 1 1 1 0
0 2 0 1 1
0 0 0 0 1
3 1 1 1 1
```

## Exemplo de Saída 1
```text
12
```

## Exemplo de Entrada 2
```text
4 5
0 0 0 1 0
0 0 0 1 1
0 0 0 0 2
0 3 1 1 1
```

## Exemplo de Saída 2
```text
5
```

## Exemplo de Entrada 3
```text
4 5
0 1 2 1 0
0 1 0 1 1
0 0 0 0 1
3 1 1 1 1
```

## Exemplo de Saída 3
```text
10
```

> **Atenção:** No exemplo 3, a Emília está no **meio** do corredor (posição 2 na linha 1, coluna 3). Isso significa que ela precisa passar por salas em **ambas as direções** do corredor até encontrar a saída. O número total de salas inclui a sala em que ela está e a sala de saída.
