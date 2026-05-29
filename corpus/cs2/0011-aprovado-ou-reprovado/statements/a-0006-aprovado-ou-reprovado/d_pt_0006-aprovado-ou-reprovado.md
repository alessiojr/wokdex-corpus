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

## Tutorial de Resolução

Neste problema, nós precisamos realizar uma continha matemática simples (obter a média aritmética) e utilizarmos **Estruturas Condicionais** para validar as diretrizes ditadas e obter a classificação correta para as notas dos alunos.

Observe de forma progressiva o fluxo desse algoritmo:

### Etapa 1: Leitura e Associação de Variáveis
As linguagens de programação capturam a linha da entrada e separam esse modelo de entrada através de espaços de acordo com implementações clássicas (como o `cin` no C++, `input().split()` no Python ou `Scanner` no Java). Crie duas variáveis flutuantes na sua linguagem respectiva do banco (`float` / `double`) e preencha-as com a primeira nota sendo `A` e a segunda nota sendo `B`.

### Etapa 2: Realize as Operações
Tendo as duas notas em formato numeral decimal com as casas preservadas (flutuantes), elabore uma média aritmética pura. Use uma variável como `media` recendo o valor de `(A + B) / 2.0` (sempre mantenha a base do divisor como float para algumas linguagens fortemente tipadas não cortarem a precisão para um inteiro antes da conversão e estragar o caso como o limpo `3.5`).

### Etapa 3: Aplicar as Condicionais de Classificação
O limitador condicional (`if`) cria o escopo correto da execução pra cada caso. Como as nossas regras excluem umas as outras (um aluno não pode ser reprovado e estar de recuperação ao mesmo tempo), certifique-se de empilhar no comportamento seletivo `if-else`:
1. `if (media >= 7.0)` -> Significa limite seguro, por favor mostre `Aprovado`.
2. `else if (media >= 4.0)` -> Ao alcançar esta estrutura, assumimos implicitamente pelas leis básicas das seleções que se não obedeceu a primeira (não é maior ou igual 7), logo obrigatoriamente já satisfaz essa metade da instrução de que a média é *menor do que 7*. Com a segunda parte checada "é maior ou igual a 4?" o retorno se aprova, mostre `Recuperacao`. Assegure que as saídas não possuem caracteres acentuados ou cedilha neste passo.
3. `else` -> Todo o comportamento contíguo restante recai sobre "média não foi validada como maior que 7... e nem ao menos maior que 4". Ele então logicamente só pode ser menor do que 4 totalizando a derrota, caindo na validação final para mostrar e imprimir `Reprovado`.

### Resumo de Estrutura em Código (Pseudocódigo)
```text
ler A, B em float

media = (A + B) / 2.0

se (media >= 7.0) entao:
    imprimir("Aprovado")
senao se (media >= 4.0) entao:
    imprimir("Recuperacao")
senao:
    imprimir("Reprovado")
```

Através desses passos você conseguirá submeter uma instrução segura e passar no avaliador.
