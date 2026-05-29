# 0003 - Divisão | **Version**: 1.0
`divisao` | Difficulty: **E** | **Updated**: 2026-04-15 20:22:13


## Overview
O algorítimo deve ler dois números e dividí-los, mas é preciso ter cuidado com a formatação dos números.

## Metadata
- **Author**: alessio
- **Editorial Author**: alessio
- **Editorial**: O problema consiste em ler dois números e exibir o resultado da  divisão com duas casas decimais.

**Pontos de Atenção para o Professor:**
 - **Tipos de Variáveis**: Em linguagens tipadas (C, Java), a divisão de dois inteiros  resulta em um inteiro (truncamento). O aluno deve fazer o *cast* ou declarar as variáveis  como `float`/`double`. O caso de teste `c-falso-positivo-inteiros` verifica esse erro.
 - **Arredondamento**: O sistema espera o rounding padrão para a segunda casa  (ex: 16/9 = 1.777... -> 1.78). O caso `b-arredonda` testa especificamente isso.
 - **Dízimas**: Entradas como 1 e 3 devem resultar em 0.33. O caso `a-dizima` verifica  se o aluno não está apenas truncando casas extras.
 - **Precisão**: Existem casos de borda com números pequenos ou que exigem precisão,  testados em `b-reais-precisao`.
- **Success Msg**: Além de trabalhar com a skill de operators matemáticos você deu alguns passos iniciais em formatação de números.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 128MB | O(1) | O(1) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 26 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-divisao` | ✅ | A | pt | wok, sci-fi |
| `a-wok` | ✅ | A | pt | wok |
| `a-metallurgy` | ✅ | A | pt | metallurgy |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dizimas** | Cenários com Dízimas periódicas. | 3 | TDD | A | operadores, variables |
| **Arredondamentos** | Testa os arredondamentos de terceira casa decimal para mais e menos. | 3 | TDD | B | operadores, io-formatacao-parsing |
| **Precisão Numérica** | Casos que exigem cuidado com precisão e rounding próximo de zero. | 3 | TDD | B | operadores |
| **Testes Simples** | Testes simples baseados nos exemplosdo exercício. | 5 | TDD | C | io |
| **Formatação - Falso Positivo** | Caso com exemplo de falso positivo, contempla erro de formatação da saída. | 3 | False-Green | C | io-formatacao-parsing |
| **Inteiros - Falso Positivo** | Caso com exemplo de falso positivo, contempla erro de declaração de variável. | 3 | False-Green | C | variables |
| **Reais Simples** | Divisões básicas com números decimas explícitos. | 3 | TDD | C | operadores |
| **Exemplos** | Entrada Básica de exemplo do exercício. | 3 | TDD | D | io, variables |

## Solutions
- **Solução completa** (`a-divisao`)
  - Languages: `java, py, cpp`
- **Soluções incompletas.** (`c-wa`)
  - Languages: `java, java`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases