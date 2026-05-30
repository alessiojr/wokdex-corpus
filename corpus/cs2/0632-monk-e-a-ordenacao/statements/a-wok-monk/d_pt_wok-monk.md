# Tutorial: Organizando a Frota de Monk

![Hangar da Estação Espacial](../assets/monk_logistics.png)

Monk está ensinando os novos recrutas como implementar um **Radix Sort** eficiente para organizar identificadores de naves espaciais. Siga estas instruções passo a passo para completar o programa de logística:

### Passo a Passo

1. **Leitura**: Receba a quantidade $N$ de identificadores e a lista de números $A$.
2. **Loop de Blocos**: Inicie um contador de iterações $i = 0$.
3. **Cálculo de Pesos**: Para cada número $X$ no array, calcule seu peso na iteração atual:
   $$\text{peso} = (X \mathbin{//} 10^{5 \times i}) \pmod{10^5}$$
   *Dica: O operador `//` representa a divisão inteira e `%` o resto da divisão.*
4. **Condição de Parada**: Se **todos** os pesos calculados na etapa anterior forem iguais a 0, o algoritmo termina sua execução.
5. **Ordenação Estável**: Caso contrário, ordene o array original de forma **estável** usando os pesos como critério. A ordenação estável é aquela que mantém a ordem relativa entre elementos de mesmo peso.
6. **Exibição**: Imprima o estado atual do array em uma única linha, com os elementos separados por espaço.
7. **Incremento**: Aumente $i$ em 1 e retorne ao passo 3.

## Entrada

A primeira linha contém $N$ ($1 \le N \le 10^6$).
A segunda linha contém os $N$ inteiros $A_i$ ($-10^{18} \le A_i \le 10^{18}$).

## Saída

O array $A$ após cada etapa de ordenação estável.

## Restrições

- $1 \le N \le 10^6$
- $-10^{18} \le A_i \le 10^{18}$
- Use métodos de entrada e saída rápidos para lidar com $10^6$ elementos.

## Exemplos

| Entrada | Saída |
| :--- | :--- |
| `3`<br>`213456789 167890 123456789` | `213456789 123456789 167890 `<br>`167890 123456789 213456789 ` |
