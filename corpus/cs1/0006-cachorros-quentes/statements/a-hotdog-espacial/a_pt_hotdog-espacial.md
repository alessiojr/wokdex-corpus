# Índice de Consumo Estelar

Na borda da galáxia WOK, a estação orbital **Gamma-BBQ** organiza todo ciclo
uma competição curiosa: quem consegue devorar mais unidades de *dogs cósmicos*
em tempo recorde.

Centenas de espécies diferentes participam: pilotos humanos, androides de carga,
criaturas gasosas e até enxames de nano-robôs. Ao final de cada edição, o
Conselho Gastronômico Intergaláctico precisa registrar um único número para
comparar eventos de diferentes sistemas estelares: o **Índice Médio de Consumo
Estelar (IMCE)** daquele torneio.

Os sensores da estação registram com precisão:

- o número total de unidades de dogs cósmicos consumidas durante a competição;
- o número total de participantes ativos naquele evento.

Você recebe, para um único torneio da Gamma-BBQ, exatamente esses dois valores
agregados. Os registros detalhados de quem comeu quanto foram perdidos após
uma tempestade de partículas solares — mas o Conselho insiste em saber o IMCE
com precisão suficiente para entrar no Almanaque Gastronômico da galáxia.

Sua missão é descobrir qual deve ser o valor desse índice médio, no formato
exigido pelos auditores intergalácticos.

## Entrada

A entrada consiste em uma única linha contendo dois inteiros `H` e `P`
(`1 ≤ H, P ≤ 1000`), onde:

- `H` é o total de unidades de dogs cósmicos consumidas no torneio;
- `P` é o número total de participantes.

## Saída

Imprima uma única linha contendo o valor do **Índice Médio de Consumo Estelar**
para esse torneio, representado por um número racional com **exatamente dois
algarismos** após o ponto decimal.

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

# Análise de Desempenho Digestivo

A Organização Mundial de Esportes Gastronômicos (OMEG) está implementando um novo sistema de métricas para avaliar a eficiência de competições de alimentação em alta velocidade. O objetivo é estabelecer um "Índice de Saturação Média" (ISM) para cada evento registrado no calendário oficial.

Os relatórios recebidos contêm uma grande quantidade de dados, incluindo temperatura local, umidade relativa do ar e marcas de patrocinadores. No entanto, para o cálculo do ISM, os analistas identificaram que apenas duas variáveis são fundamentais: a massa total de alimento consumida (neste caso, contabilizada em unidades padronizadas de "cachorros-quentes") e a cardinalidade do conjunto de competidores ativos.

Sua tarefa, como engenheiro de dados júnior, é processar esses fluxos de informação crua. Você deve ignorar os metadados irrelevantes (que sequer são fornecidos na entrada simplificada deste problema) e focar estritamente na derivação do ISM. O índice é definido matematicamente como a razão entre o volume total consumido e a população de participantes, devendo ser apresentado com uma precisão de duas casas decimais para manter a consistência com os registros históricos.

## Entrada

A entrada consiste de uma única linha contendo dois números inteiros $H$ e $P$ ($1 \leq H, P \leq 1000$). O valor $H$ representa a quantidade total de unidades de cachorros-quentes consumidas durante o evento, e $P$ representa o número total de participantes inscritos e ativos na competição.

## Saída

Seu programa deve produzir uma única linha contendo o valor do Índice de Saturação Média (ISM). Este valor deve ser um número racional formatado com **exatamente dois dígitos** após o ponto decimal. Realize o arredondamento padrão se necessário.

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
