# Olimpíada Brasileira de Informática – OBI2010

## 0523 – Dentista

**Nome do arquivo fonte:** dentista.cpp

O dentista que atende em uma pequena cidade tem apenas um consultório. Ele atende no máximo um paciente por vez e as consultas sempre iniciam e terminam no mesmo dia. Ele já tem marcadas as consultas para o dia de hoje. No entanto, por um erro de sua secretária, algumas consultas podem estar marcadas para horários que se sobrepõem.

O dentista deseja atender o maior número possível de pacientes e, para isso, ele pode desmarcar algumas consultas, desde que as consultas restantes não se sobreponham.

### Entrada

A primeira linha contém um inteiro $N$ ($1 \le N \le 10.000$) que indica o número de consultas que a secretária marcou. Cada uma das $N$ linhas seguintes contém um par de inteiros $X$ e $Y$ separados por um espaço em branco ($0 \le X < Y \le 1.000.000$) que representam, respectivamente, o horário de início e de término da consulta. Considere que se uma consulta inicia no exato instante em que outra termina não há sobreposição. Os horários de início são fornecidos em ordem, podendo haver mais de uma consulta que inicie no mesmo horário.

### Saída

Seu programa deve imprimir uma única linha, contendo um inteiro que representa a quantidade máxima de consultas que podem ser atendidas sem que haja qualquer sobreposição.

### Informações sobre a pontuação

- Em um conjunto de casos de teste que totaliza 40 pontos, ($0 \le X < Y \le 1.000$).

| Entrada | Saída |
| --: | --: |
| 3 | 2 |
| 10 100 | |
| 40 130 | |
| 120 200 | |

| Entrada | Saída |
| --: | --: |
| 4 | 4 |
| 10 20 | |
| 20 30 | |
| 30 40 | |
| 40 50 | |

| Entrada | Saída |
| --: | --: |
| 5 | 3 |
| 10 30 | |
| 20 40 | |
| 30 60 | |
| 40 80 | |
| 60 100 | |

---

### Tutorial de Resolução

Este problema pode ser resolvido utilizando uma **abordagem gulosa** (*greedy*). Siga os passos abaixo:

1.  **Leitura e Estrutura de Dados**: Armazene as consultas em uma lista de objetos ou pares (Início, Término).
2.  **Ordenação Crucial**: Ordene todas as consultas pelo seu **horário de término** ($Y$). Este é o passo mais importante: escolher o que termina mais cedo maximiza o espaço para o restante do dia.
3.  **Seleção de Itens**:
    -   Mantenha um contador (`consultas_atendidas = 0`).
    -   Mantenha o horário em que a última consulta escolhida termina (`fim_ultima_escolhida = 0`).
    -   Percorra a lista ordenada:
        -   Se o horário de **início** da consulta atual for maior ou igual a `fim_ultima_escolhida`, então essa consulta pode ser atendida.
        -   Incremente o contador e atualize `fim_ultima_escolhida` para o horário de **término** dessa consulta.
4.  **Resultado**: O valor final do contador é a resposta.

**Exemplo Prático (Amostra 1):**
Consultas: (10, 100), (40, 130), (120, 200)

1.  Ordenadas pelo término: (10, 100), (40, 130), (120, 200).
2.  Escolhemos (10, 100). Fim atual = 100. Contador = 1.
3.  Próxima consulta: (40, 130). Início (40) < Fim atual (100). Ignoramos.
4.  Próxima consulta: (120, 200). Início (120) >= Fim atual (100). Escolhemos. Fim atual = 200. Contador = 2.
5.  Resultado = 2.
