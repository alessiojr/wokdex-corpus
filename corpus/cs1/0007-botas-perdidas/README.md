# 0007 - Botas perdidas | **Version**: 0.1
`botas-perdidas` | Difficulty: **D** | **Updated**: 2026-04-15 09:34:18


## Overview
O botas perdidas é um problema que parece ser leve, mas que apresenta vários desafios para alunos iniciantes.

## Metadata
- **Author**: alessio
- **Editorial Author**: alessio
- **Editorial**: O botas perdidas é um problema que é necesário um domino de laço de repetição, tem muitos casos diferntes que o aluno não percebe. Basicamente é um laço de repetição que usa string e número o aluno deve armazenar de alguma forma estas informações comprar e dar a resposta Existe uma resposta hiper eficiente que se passa usando um devor com o tamanho das botas e somando e subtraindo  de cada posição para ter o número de botas existentes.
- **Success Msg**: Parabéns dentro dos exercício de loop simples você teve um resultado bem interessante manipulando strings e números

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
|:-----------|:-------------|:----------------|:-----------------|
| 1s         | 128MB        | O(N)            | O(1)             |

## Stats
| Metric         | Count |
|:---------------|:------|
| Test Scenarios | 55    |
| Solutions      | 2     |

## Statements
| ID                 | Status | Level | Natural Languages | Skills   |
|:-------------------|:-------|:------|:------------------|:---------|
| `a-botas-perdidas` | ✅      | A     | pt                | military |

## Test Scenarios
| Name                                         | Description                                                                                                                                                                                       | Count | Type | Level |
|:---------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|:-----|:------|:--------------------|
| **Testes de Performance**                    | Casos de teste extremos para verificar a eficiência da solução.                                                                                                                                   | 2     | TDD  | A     | complexity-analysis |
| **Limite de botas (N = 10000)**              | Casos com o máximo de botas permitido pelo problema (N = 10000), para garantir que a solução respeita o limite e não sofre estouro de buffer ou timeout.                                          | 4     | TDD  | A     | complexity-analysis |
| **Muitos pares do mesmo tamanho**            | Lista com milhares de botas de um único tamanho, metade esquerdas e metade direitas, exercitando a contagem correta de pares quando há muitas combinações possíveis do mesmo tamanho.             | 4     | TDD  | B     | arrays              |
| **Vários tamanhos, pares bem distribuídos**  | Casos com diferentes tamanhos entre 30 e 60, cada um com quantidades variadas de botas esquerdas e direitas, exigindo que a solução some corretamente min(E, D) para cada tamanho.                | 30    | TDD  | B     | arrays              |
| **Pares Repetidos**                          | Casos com múltiplos pares do mesmo tamanho para testar a contagem.                                                                                                                                | 2     | TDD  | B     | loops               |
| **Entrada desordenada por tamanho e lado**   | As botas chegam em ordem totalmente aleatória de tamanhos e lados, de modo que soluções que dependem de uma ordenação prévia da entrada podem falhar se não organizarem ou contarem corretamente. | 1     | TDD  | B     | arrays              |
| **Nenhum par: todas as botas do mesmo lado** | Casos em que todas as botas são do mesmo lado (todas 'E' ou todas 'D'), garantindo que o número de pares seja zero mesmo com muitos elementos.                                                    | 1     | TDD  | C     | loops               |
| **Múltiplos casos até EOF**                  | Vários conjuntos de N e listas de botas em sequência, sem linha sentinela especial, terminando apenas no fim do arquivo.                                                                          | 1     | TDD  | C     | io, loops           |
| **Looping**                                  | Casos de teste focados em laços de repetição.                                                                                                                                                     | 2     | TDD  | C     | loops               |
| **Menor N possível e poucos pares**          | Casos com N próximo do mínimo (por exemplo, 2, 3 ou 4 botas) para garantir que a solução trata corretamente listas muito pequenas e não faz acessos indevidos ou laços vazios.                    | 6     | TDD  | C     | io                  |
| **Exemplos do Enunciado**                    | Casos de teste básicos fornecidos como exemplo no problema.                                                                                                                                       | 2     | TDD  | D     | io                  |

## Solutions
- **Solução Ótima** (`a-optimal`)
  - Languages: `java, cpp, py`
- **Solução Sub-ótima** (`b-suboptimal`)
  - Languages: `py`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases