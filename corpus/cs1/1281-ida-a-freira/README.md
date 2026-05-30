# 1281 - Ida à Feira | **Version**: 1.0
`ida-a-freira` | Difficulty: **D** | **Updated**: 2026-04-15 23:54:00


## Overview
Simulação de compra em uma feira, calculando o valor total gasto com base nos preços e quantidades de produtos.

## Metadata
- **Author**: andre
- **Editorial Author**: andre
- **Editorial**: O problema é um exercício clássico de mapeamento e acumulação. O foco é a utilização de uma estrutura de dados de busca rápida (Mapa/Dicionário/Hash) para associar nomes de produtos a seus preços.

**Pontos de Atenção:**
- **Precisão**: O uso de ponto flutuante exige cuidado. Recomenda-se `double` em C++ ou garantir que o acumulador não perca precisão em muitas somas.
- **Busca Eficiente**: Alunos que usam busca linear O(M) para cada um dos P itens podem ter problemas de performance se os limites forem altos.
- **Formatação**: O prefixo 'R$ ' e as duas casas decimais são obrigatórios.
- **Success Msg**: Parabéns! Você dominou o uso de estruturas de chave-valor (Mapas/Dicionários) para resolver problemas de busca e associação de dados de forma eficiente.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | 128MB | O(N) | O(N) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 16 |
| Solutions | 3 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-ida-a-feira` | ✅ | A | pt | daily-life |
| `a-mercado-interplanetario` | ✅ | A | pt | wok |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Itens Duplicados** | Situações onde o mesmo item pode aparecer mais de uma vez na lists de compras. | 2 | False-Green | A | hashing, logica |
| **Catálogo Incompleto** | Tenta comprar um item que não está disponível no catálogo da feira. | 2 | TDD | A | hashing, io |
| **Volume de Dados** | Teste de desempenho com muitos produtos e casos de teste. | 2 | TDD | B | hashing, loops |
| **Precisão Monetária** | Casos com muitos decimais pequenos para testar o acúmulo de erro de ponto flutuante. | 3 | TDD | B | logica, io |
| **Cenários Básicos** | Entradas pequenas para validar a soma e multiplicação básica. | 3 | TDD | C | logica, loops |
| **Preços Gratuitos** | Testar se o programa lida bem com itens que possuem valor 0.00. | 2 | TDD | C | logica |
| **Exemplos** | Casos fornecidos no enunciado original. | 2 | TDD | D | io, loops |

## Solutions
- **Solução Ótima (Hash Map)** (`a-optimal`)
  - Languages: `py, cpp, java`
- **Solução Bruta (Busca Linear)** (`b-suboptimal`)
  - Languages: `py`
- **Solução Incorreta (Sobrescrita de Duplicados)** (`c-falso-duplicados`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases