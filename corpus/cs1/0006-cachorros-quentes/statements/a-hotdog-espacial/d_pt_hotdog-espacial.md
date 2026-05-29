# Tutorial: Média de Consumo na HotDog Nexus

Entender como trabalhar com divisões que resultam em números decimais é
fundamental em programação — especialmente quando os auditores da galáxia
exigem precisão. Neste problema, vamos praticar isso calculando a média
de consumo em uma competição espacial de *dogs cósmicos*.

O objetivo é calcular a média de unidades consumidas por participante.
Você receberá:

- `H`: o total de unidades de dogs cósmicos consumidas;  
- `P`: o número de participantes.

No final, você deve imprimir a média `H / P` com exatamente duas casas
decimais.

## Passo a passo

1. **Ler a entrada**
   - Leia dois inteiros `H` e `P` da mesma linha.
   - Limites: `1 ≤ H, P ≤ 1000`.

2. **Evitar divisão inteira**
   - Em linguagens como C, C++ e Java, `H / P` usando inteiros faz divisão
     inteira e descarta a parte decimal.
   - Solução: converta `H` ou `P` para ponto flutuante antes de dividir.
     - Exemplo em C/C++: `double media = (double) H / P;`

3. **Calcular a média**
   - Depois de garantir que está usando ponto flutuante, faça a conta:

     ```text
     media = H / P
     ```

4. **Formatar a saída com duas casas decimais**
   - O valor deve ser impresso com **exatamente duas casas** depois do
     ponto decimal, com arredondamento padrão.
   - Exemplos:
     - Em C: `printf("%.2f\n", media);`
     - Em Python: `print(f"{media:.2f}")`

5. **Imprimir o resultado**
   - Imprima apenas o número formatado, seguido de quebra de linha.

## Entrada

Uma única linha contendo dois inteiros `H` e `P` (`1 ≤ H, P ≤ 1000`).

## Saída

Um único número com duas casas decimais representando a média `H / P`.

## Exemplos

| Input | Output |
| :---- | -----: |
| `10 90` | `0.11` |

| Input | Output |
| :---- | -----: |
| `840 11` | `76.36` |

| Input | Output |
| :---- | -----: |
| `1 50` | `0.02` |

| Input | Output |
| :---- | -----: |
| `34 1000` | `0.03` |

| Input | Output |
| :---- | -----: |
| `35 1000` | `0.04` |

| Input | Output |
| :---- | -----: |
| `36 1000` | `0.04` |

