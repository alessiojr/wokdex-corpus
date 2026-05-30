# Letras

Considere as definições abaixo:

- Uma palavra é uma sequência de letras consecutivas.
- Um texto é um conjunto de palavras separadas pelo caractere espaço em branco.

Você foi contratado pela empresa Booble para escrever um programa que, dados uma letra e um texto, determina a porcentagem de palavras do texto que contém a letra dada.

## Tutorial / Passo a Passo

O problema pede para encontrarmos a porcentagem de palavras em um texto que possuem uma letra específica. Você, como funcionário da Booble, precisa processar frases para extrair essa métrica. Este é um exercício clássico de **manipulação de strings e vetores**.

Para resolver, podemos quebrar a solução em passos lógicos:

**Passo 1: Leitura da Entrada**
- Primeiro, leia um único caractere que será a nossa letra de interesse.
- Em seguida, você deve ler uma linha inteira contendo o texto. *Atenção:* muitas linguagens leem strings parando no primeiro espaço. Utilize métodos de leitura de linha completa (como `getline` no C++, `input()` no Python, ou `nextLine()` no Java).

**Passo 2: Separação em Palavras**
- Precisamos analisar cada palavra isoladamente. A maneira mais fácil de fazer isso é "quebrar" ou "dividir" o texto usando o caractere espaço (`' '`) como delimitador. Isso nos dará uma lista ou vetor onde cada elemento é uma palavra.

**Passo 3: Contagem e Verificação**
- Crie uma variável para guardar o **total de palavras**. (Isso equivale ao tamanho da lista gerada no passo anterior).
- Crie uma variável `contagem_sucesso = 0` para guardar quantas palavras contêm a letra procurada.
- Faça um laço de repetição (`for` ou `foreach`) iterando por cada palavra da lista.
- Para cada palavra, percorra as letras que a compõem. Se encontrar a letra de interesse, incremente a variável `contagem_sucesso` em `1` e passe imediatamente para a próxima palavra (pois basta aparecer uma vez na palavra para ela contar na estatística).

**Passo 4: Cálculo da Porcentagem**
- A porcentagem é calculada pela fórmula: `(contagem_sucesso / total_palavras) * 100.0`.
- *Atenção à divisão inteira:* Garanta que o cálculo seja feito entre valores do tipo ponto flutuante (`float` ou `double`), caso contrário a linguagem pode arredondar `5/10` para `0` antes de multiplicar por 100!

**Passo 5: Saída Formatada**
- O problema exige que o resultado seja impresso com exatamente uma casa decimal (por exemplo, `57.1`). Utilize funções de formatação específicas da sua linguagem, como `printf("%.1f\n", resultado)` no C/C++ ou formato `f"{resultado:.1f}"` no Python.

Seguindo esses passos, a sua solução rodará rapidamente em uma complexidade linear $O(N)$, lendo as palavras uma única vez.

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
