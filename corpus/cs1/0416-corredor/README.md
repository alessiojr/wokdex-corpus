# 0416 - Corredor | **Version**: 1.0
`corredor` | Difficulty: **D** | **Updated**: 2026-05-07 08:45:43


## Overview
Nesta aventura, você precisa ajudar o personagem de Bruninho a atravessar um corredor repleto de salas consecutivas. Cada sala possui uma porta de entrada e saída, e passar por ela pode conceder vidas extras ou infligir dano! Sabendo os valores de vida de todas as salas, seu objetivo é descobrir qual a quantidade máxima possível de vidas que o personagem consegue acumular percorrendo um trecho contínuo em uma única passagem.

## Metadata
- **Editorial Author**: alessio
- **Editorial**: **Briefing do Professor:**
Este problema é a introdução perfeita à Programação Dinâmica unidimensional clássica, focado no problema da Subsequência Contígua de Soma Máxima. O aluno precisa de conhecimentos básicos sobre arrays e laços de repetição. É excelente para ser aplicado no início do módulo de Programação Dinâmica (DP) ou Algoritmos Gulosos, ajudando a construir a intuição de sobreposição de subproblemas e subestrutura ótima de forma palpável, encaixando-se perfeitamente em um nível intermediário na grade de algoritmos.

**Resumo da Estratégia:**
A intuição chave é perceber que testar todos os trechos possíveis (pares de início e fim) levaria a uma complexidade quadrática O(N^2), inviável para N = 50000. A solução correta exige o Algoritmo de Kadane. O raciocínio é simples: processamos as salas de forma linear, da esquerda para a direita, mantendo um acumulador (`soma_atual`) e o melhor valor global (`soma_maxima`). A cada sala, somamos a respectiva vida ao acumulador. O 'pulo do gato' é que, caso o acumulador se torne negativo, significa que o trecho contíguo atual dá mais prejuízo do que lucro; logo, devemos reiniciar a soma a partir de zero na sala seguinte. Isso garante a resposta ótima em tempo O(N) e espaço auxiliar O(1).
*Para os detalhes completos de implementação e dedução da lógica, consulte o statement de nível D.*

- **Success Msg**: Incrível! Você sobreviveu ao corredor perigoso e maximizou suas vidas com máxima eficiência!

| Time Limit | Memory Limit | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| 1s | -MB | O(N) | - |

## Stats
| Metric | Count |
| :--- | :--- |
| Test Scenarios | 41 |
| Solutions | 2 |

## Statements
| ID | Status | Level | Natural Languages | Skills |
| :--- | :--- | :--- | :--- | :--- |
| `a-corredor` | ✅ | A | pt | games |

## Test Scenarios
| Name | Description | Count | Type | Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Teste de Carga e Desempenho** | Casos de teste com N máximo (50000) e valores intercalados para forçar TLE em algoritmos O(N^2). | 14 | Performance | A | dynamic-programming |
| **Fuzzing com Valores Aleatórios** | Casos de teste com tamanhos variados e valores aleatórios entre -100 e 100 para evitar heurísticas engessadas. | 17 | Input | B | arrays, dynamic-programming |
| **Casos Extremos (Edge Cases)** | Casos pequenos com N=1, N=2, todos negativos exceto um positivo, etc. | 6 | TDD | C | arrays |
| **Padrões Específicos** | Casos onde todos os valores são crescentes ou decrescentes, garantindo que algoritmos gulosos não parem antes da hora. | 2 | TDD | C | dynamic-programming |
| **Exemplos** | Casos de teste de exemplo do statement. | 2 | TDD | D | dynamic-programming |

## Solutions
- **Algoritmo de Kadane Clássico** (`a-otima-kadane`)
  - Languages: `c, cpp, java`
- **Força Bruta O(N^2)** (`b-forca-bruta`)
  - Languages: `python`

## Components
- ✅ Statements
- ✅ Solutions
- ✅ Test Cases