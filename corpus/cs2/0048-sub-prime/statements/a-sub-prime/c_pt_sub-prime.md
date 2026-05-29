# Sub-prime

## Descrição

Existem $B$ bancos, cada um com uma reserva monetária $R_i$. Existem $N$ debêntures: cada uma indica que um banco devedor $D$ deve um valor $V$ a um banco credor $C$.

Cada banco pode pagar suas dívidas usando suas reservas mais os créditos que recebe de outros bancos. Determine se **todos** os bancos conseguem liquidar suas dívidas.

## Entrada

Vários casos de teste. Cada caso começa com $B$ e $N$ ($1 \leq B, N \leq 20$).

A segunda linha contém $B$ inteiros $R_i$ ($0 \leq R_i \leq 10^4$), as reservas de cada banco.

As próximas $N$ linhas contêm três inteiros: $D$ (devedor), $C$ (credor), $V$ (valor da debênture).

Termina com `0 0`.

## Saída

`S` se todos os bancos podem liquidar suas dívidas, `N` caso contrário.

## Exemplo

| Entrada | Saída |
|---|---|
| 3 3 | S |
| 1 1 1 | N |
| 1 2 1 | S |
| 2 3 2 | |
| 3 1 3 | |
| 3 3 | |
| 1 1 1 | |
| 1 2 1 | |
| 2 3 2 | |
| 3 1 4 | |
| 3 3 | |
| 1 1 1 | |
| 1 2 2 | |
| 2 3 2 | |
| 3 1 2 | |
| 0 0 | |
