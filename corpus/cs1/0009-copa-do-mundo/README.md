# 0009 - Copa do Mundo | **Version**: 1.0
`copa-do-mundo` | Difficulty: **D** | **Updated**: 2026-04-15 20:58:30


## Overview
Dado o número de times, o número total de partidas e a pontuação final de todos os times combinados, o desafio consiste em determinar, por meio de abstração matemática simples, a quantidade total de jogos que terminaram empatados. Uma demonstração clássica de como encontrar a resposta por meio de invariantes e propriedades de uma soma algébrica, sem a necessidade de simulação.

## Metadata
- **Author**: Unknown
- **Editorial Author**: alessio
- **Editorial**: Seja N o número total de jogos disputados e P_i os pontos do time i. Se todos os N jogos tivessem um vencedor, a soma máxima de pontos distribuídos seria 3 × N. Cada empate reduz essa soma em 1 ponto, pois distribui apenas 2 pontos (1 para cada time). Assim, se S = Σ P_i, então o número de empates é dado por: Empates = 3 × N − S. Basta ler T e N, somar os pontos de todos os T times e aplicar essa fórmula para cada caso de teste.

- **Success Msg**: Resolução validada! Sua modelagem matemática deduziu as diferenças absolutas e processou perfeitamente os limites de tempo propostos.

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1.0s | 128MB | O(N) | O(1) |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 26 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-copa-do-mundo` | ✅ | A | pt | soccer |
| `a-wok-copa-do-mundo` | ✅ | A | pt | wok |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Limite máximo de times e partidas** | Casos próximos dos limites superiores (T = 200 e N grande), com muitos pontos somados, para forçar a necessidade de uma solução O(T) e evidenciar implementações O(T^2) lentas. | 1 | TDD | A | loops |
| **Somente vitórias, sem empates** | Setores onde a soma dos pontos é exatamente 3 × N, indicando que todas as partidas terminaram com um vencedor e nenhum empate ocorreu. | 4 | TDD | B | mathematical-abstraction |
| **Todos os jogos empatados** | Setores em que cada partida terminou empatada, de forma que a soma de pontos é exatamente 2 × N e o número de empates é N. | 3 | TDD | B | operadores |
| **Vitórias e empates misturados** | Torneios com combinação de vitórias e empates, em que a soma de pontos não é nem 3 × N nem 2 × N, forçando o uso correto da fórmula em vez de suposições. | 10 | TDD | B | mathematical-abstraction, operadores |
| **Nenhuma partida disputada** | Setores da Copa Galáctica em que N = 0: nenhum duelo aconteceu, todos os times terminam com 0 pontos e a resposta deve ser 0 empates. | 2 | TDD | C | io |
| **Apenas uma nave-time no setor** | Casos com T = 1 e N = 0, em que só existe uma nave-time registrada e nenhum confronto pode ter sido disputado. | 1 | TDD | C | loops |
| **Múltiplos setores seguidos e caso sentinela** | Vários casos de teste em sequência, seguidos de um setor T = 0 que apenas encerra a entrada e não gera saída. | 1 | TDD | C | io, loops |
| **Formatação e Leitura Robusta** | Casos com quebras de linha e espaços extras sutis para testar a robustez da leitura da entrada. | 1 | TDD | C | io |
| **Caso de Teste Exemplo** | Primeiro caso de teste apresentado no enunciado do problema, servindo como validação inicial. | 3 | TDD | D | io |

## Solutions
- **Solução de Referência em Python** (`a-optimal`)
  - Languages: `py, cpp, java`
- **Solução Sub-ótima em C++ o(n^2)** (`b-suboptimal`)
  - Languages: `cpp`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases