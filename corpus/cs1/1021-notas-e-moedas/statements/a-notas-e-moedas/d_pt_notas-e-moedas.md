# Notas e Moedas — Tutorial Passo a Passo

Neste tutorial, vamos entender como decompor um valor monetário em notas e moedas da forma mais eficiente (usando a menor quantidade de cédulas e moedas).

## 1. O Conceito: Estratégia Gulosa (Greedy)
Para usar o menor número de notas, devemos sempre tentar usar a maior nota disponível primeiro. Por exemplo, se temos R$ 150,00, é melhor usar uma nota de R$ 100,00 e uma de R$ 50,00 do que três notas de R$ 50,00.

## 2. O Problema da Imprecisão Decimal
Computadores representam números de ponto flutuante (como `1.03`) usando o padrão IEEE 754, que pode causar pequenas imprecisões. Por exemplo, `1.03 * 100` pode resultar em `102.99999999999999`. Se você simplesmente transformar isso em um número inteiro, terá `102`, e perderá um centavo!

### Como resolver?
A forma mais segura é converter o valor lido para **centavos** (um número inteiro) logo no início.
```python
# Em Python
valor = float(input())
centavos = int(valor * 100 + 0.5) # O + 0.5 ajuda no arredondamento
```

## 3. Passo a Passo da Lógica

### Passo 1: Notas
Defina uma lista com os valores das notas em centavos: `[10000, 5000, 2000, 1000, 500, 200]`.
Para cada nota:
1.  Quantidade = `centavos // valor_da_nota`
2.  `centavos = centavos % valor_da_nota` (o que sobrou)
3.  Imprima o resultado.

### Passo 2: Moedas
Repita o mesmo processo para as moedas: `[100, 50, 25, 10, 5, 1]`.

## 4. Exemplo Prático
Entrada: `91.01`
- Centavos: `9101`
- Notas de 50: `1` (Sobra `4101`)
- Notas de 20: `2` (Sobra `101`)
- Moedas de 1.00: `1` (Sobra `1`)
- Moedas de 0.01: `1` (Sobra `0`)

---

| Entrada | Saída |
| :-- | :-- |
| 576.73 | (Decomposição completa conforme exemplo) |
