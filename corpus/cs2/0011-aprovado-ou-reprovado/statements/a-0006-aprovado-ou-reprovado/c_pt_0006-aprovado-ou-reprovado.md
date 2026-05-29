# Aprovado Reprovado

No colégio Barias Frito (BF) um aluno é aprovado por média se ele obtiver uma média final maior ou igual a 7, caso o aluno tenha uma média menor que 7 mas maior ou igual a 4 ele está de recuperação, caso ele tenha uma média menor que 4 o aluno está reprovado.

A média é calculada com a nota das duas **provas** aplicadas no semestre e corresponde simplesmente a média aritmética das duas notas.

Baseado nas duas notas do aluno, indique o resultado final do aluno: "Aprovado", "Reprovado" ou "Recuperacao".

## Entrada

A entrada consiste de apenas uma linha com as notas A e B, que correspondem as duas notas que o aluno conquistou esse semestre.

## Saída

A saída do seu programa deve ser apenas uma linha. Caso o aluno tenha sido aprovado informe "Aprovado", caso o aluno tenha sido reprovado informe "Reprovado" e caso ele esteja de recuperação informe "Recuperacao".

## Exemplos

| Entrada | Saída |
| :--- | :--- |
| `10.0 10.0` | `Aprovado` |

| Entrada | Saída |
| :--- | :--- |
| `2.2 4.2` | `Reprovado` |

| Entrada | Saída |
| :--- | :--- |
| `5.0 5.0` | `Recuperacao` |

## Solução e Complexidade

Este problema exige o uso de estruturas de controle condicionais (`if`, `else if`, `else`) para analisar limites numéricos e determinar o estado do aluno com base no cálculo de sua média.

A estratégia educacional consiste nos seguintes passos:
1. Obter valores das duas respecitvas notas (separadas por espaço na mesma linha).
2. Calcular a média: `(A + B) / 2`.
3. Validar se a média satisfaz `>= 7`. Caso não passe, avaliar `>= 4` (como já garantimos não ser `7`, não precisamos de limite superior nessa fase) e no final a opção que sobrou.

**Complexidade Esperada**:
- **Tempo:** $O(1)$ — Como é apenas um processamento aritmético direto com verificações numéricas em tempo contínuo que nunca mudará de ritmo em decorrer dos valores de nota avaliados.
- **Espaço:** $O(1)$ — Precisamos alocar apenas um número pequeno de variáveis flutuantes na memória, o que garante armazenamento contínuo e estritamente básico.
