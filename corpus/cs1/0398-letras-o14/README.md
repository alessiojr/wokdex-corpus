# 0398 - Letras | **Version**: 1.0
`letras` | Difficulty: **D** | **Updated**: 2026-05-07 09:56:32


## Overview
Você foi contratado pela Booble para analisar textos! Dada uma letra específica e uma frase completa, sua tarefa é identificar a porcentagem de palavras nessa frase que contêm a letra procurada. Uma ótima oportunidade para praticar formatação de E/S e manipulação básica de caracteres.

## Metadata
- **Editorial Author**: alessio
- **Editorial**: **Briefing do Professor:**
Este problema é ideal para turmas que estão iniciando o módulo de manipulação de strings. O exercício exige que o aluno saiba fazer a leitura de uma linha inteira (lidando com espaços em branco), realize a separação da string em tokens (split) e faça buscas de caracteres dentro de substrings. Ele se encaixa perfeitamente como um exercício prático introdutório de nível D (Iniciante), testando fundamentos clássicos de E/S, laços de repetição e conversão de tipos para o cálculo de porcentagens em ponto flutuante.

**Resumo da Estratégia:**
A solução requer processamento linear O(N) sobre o texto fornecido. O primeiro passo é ler o caractere alvo e, depois, ler a linha do texto completamente. O texto deve ser fatiado em uma lista de palavras utilizando o espaço como delimitador. Com a lista em mãos, basta iterar sobre cada palavra verificando se o caractere alvo está presente. O total de palavras que contém o caractere dividido pelo número total de palavras na frase, multiplicado por 100, fornece o resultado final. Um ponto de atenção crítico comum é o arredondamento inadvertido ao fazer divisões de números inteiros, além do cuidado com formatação de saída para exatamente uma casa decimal.
*Para os detalhes completos de implementação, consulte o statement de nível D.*

- **Success Msg**: Excelente! Sua lógica de manipulação de strings funcionou perfeitamente para extrair as palavras e analisar o texto.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | -MB | O(N) | O(1) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 67 |
| Solutions | 1 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-letras` | ✅ | A | pt | portuguese |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Carga e Desempenho (Max Chars)** | Texto com o máximo de 1000 caracteres. Teste para confirmar que não está iterando palavras desnecessariamente. | 3 | Performance | A | strings-percorrer-contar |
| **Fuzzing Randômico** | Texto com palavras diversas. | 17 | Input | B | io-formatacao-parsing, arredondamento |
| **Casos Extremos (Edge Cases)** | Uma única palavra que não possui a letra alvo. Resultado de contagem zero esperado. | 44 | TDD | C | strings-percorrer-contar, arredondamento |
| **Exemplos** | Casos de teste de exemplo do enunciado. | 3 | TDD | D | arredondamento |

## Solutions
- **Solução Ótima (Python)** (`a-otima-basica`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases