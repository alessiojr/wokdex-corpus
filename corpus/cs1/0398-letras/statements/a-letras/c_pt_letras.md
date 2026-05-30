# Letras

Considere as definições abaixo:

- Uma palavra é uma sequência de letras consecutivas.
- Um texto é um conjunto de palavras separadas pelo caractere espaço em branco.

Você foi contratado pela empresa Booble para escrever um programa que, dados uma letra e um texto, determina a porcentagem de palavras do texto que contém a letra dada.

## Estratégia e Dicas

Para resolver este problema de forma eficiente (em complexidade de tempo `O(N)`, onde `N` é o número de caracteres do texto):
1. **Leia a entrada corretamente:** A primeira linha contém a letra alvo. A segunda linha contém a frase inteira. Tenha cuidado: a função de leitura para a frase precisa capturar os espaços!
2. **Separe as palavras:** Uma abordagem simples é usar métodos nativos da sua linguagem (como `split()` em Python, Java ou C++) para dividir o texto em uma lista de palavras.
3. **Contagem:** Percorra cada palavra da lista e verifique se a letra alvo está contida nela. Lembre-se de contar o número de palavras que possuem a letra, e o número total de palavras.
4. **Formatação:** Cuidado com a divisão inteira! Garanta que o cálculo da porcentagem seja feito com números de ponto flutuante e que a saída seja impressa com exatamente uma casa decimal.

## Entrada

A primeira linha da entrada contém um único caractere, a letra de interesse na pesquisa. A segunda linha contém um texto, como definido acima.

## Saída

Seu programa deve produzir uma única linha, contendo um único número real, a porcentagem de palavras do texto que contêm a letra dada, com precisão de uma casa decimal.

## Observações

- O texto é composto apenas por letras minúsculas e o caractere espaço em branco.
- O texto é formado por no mínimo um caractere, e no máximo 1000 caracteres.
- O texto não contém dois espaços em branco consecutivos.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| p | 100.0 |
| papagaio | |

<br>

| Entrada | Saída |
| :-- | :-- |
| o | 57.1 |
| no meio do caminho tinha uma pedra tinha uma pedra no meio do caminho | |

<br>

| Entrada | Saída |
| :-- | :-- |
| b | 0.0 |
| nunca me esquecerei que no meio do caminho tinha uma pedra | |
