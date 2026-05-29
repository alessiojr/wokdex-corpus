# Sub-prime — Dica do Mestre

## Entendendo o Problema

Você tem $B$ bancos, cada um com uma reserva (dinheiro em caixa). Existem $N$ debêntures, cada uma dizendo "banco D deve V reais ao banco C". A pergunta é: se todos os bancos usarem suas reservas e o dinheiro que outros devem a eles, todos conseguem pagar suas dívidas?

## Estratégia de Solução

### A sacada principal

Para cada banco, o que importa é o **saldo final**:

$$\text{saldo}[i] = R_i + \sum(\text{créditos que i recebe}) - \sum(\text{dívidas que i deve})$$

Se **todos** os saldos forem ≥ 0, a resposta é `S`. Se qualquer banco ficar com saldo negativo, é `N`.

### Por que funciona?

Se banco A deve R\$5 ao banco B, e banco B deve R\$3 ao banco C:
- O banco B recebe R\$5 de crédito e paga R\$3 de dívida → saldo positivo.
- A ordem de pagamento não importa: o que importa é o balanço total de cada banco.

### Implementação

1. Leia as reservas em um array `saldo[1..B]`.
2. Para cada debênture $(D, C, V)$: subtraia $V$ de `saldo[D]` e some $V$ a `saldo[C]`.
3. Verifique se todos os saldos são ≥ 0.

## Complexidade

$O(B + N)$ — percorre as reservas e debêntures uma única vez.

## Armadilhas Comuns

- **Esquecer que a saída é `S` ou `N`** (maiúsculo), não `sim`/`não` ou `YES`/`NO`.
- **Confundir devedor com credor** — o devedor ($D$) paga, o credor ($C$) recebe.
- **Não tratar múltiplos casos de teste** — a entrada termina com `0 0`.
- **Índices começam em 1**, não em 0.
