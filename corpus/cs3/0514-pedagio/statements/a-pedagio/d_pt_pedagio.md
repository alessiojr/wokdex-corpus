# Pedágio — Dica do Mestre

## Entendendo o Problema

O problema pede para calcular o custo total de uma viagem, que é composto por duas partes:
1. **Custo da distância:** $L \times K$, ou seja, os quilômetros rodados vezes o custo por quilômetro.
2. **Custo dos pedágios:** A cada $D$ quilômetros há um pedágio que custa $P$.

## Estratégia de Solução

Para calcular o número de pedágios, basta dividir a distância total $L$ pela distância entre pedágios $D$. Como queremos apenas o número inteiro de pedágios, a divisão inteira é exatamente o que precisamos:
$$\text{Quantidade de pedágios} = \left\lfloor \frac{L}{D} \right\rfloor$$

Em programação (como C, C++, Python e Java), a operação de divisão `/` entre dois inteiros já realiza a divisão inteira (truncando a parte decimal). Portanto, a quantidade de pedágios é simplesmente `L / D`.

O custo total então será:
$$\text{Custo Total} = (L \times K) + \left( \frac{L}{D} \times P \right)$$

## Complexidade

Este problema envolve apenas uma fórmula matemática simples, portanto sua complexidade é constante $O(1)$.

## Armadilhas Comuns

* **Tamanho das variáveis:** Os valores máximos dão como resultado algo na ordem de $2 \times 10^8$, o que cabe confortavelmente numa variável inteira padrão de 32 bits (como o `int` nas linguagens modernas). Não há risco de overflow.
* **Divisão:** Usar divisão em ponto flutuante seria incorreto caso ocorressem arredondamentos. A divisão inteira direta fornece o comportamento de truncamento que esse cálculo exige perfeitamente.
