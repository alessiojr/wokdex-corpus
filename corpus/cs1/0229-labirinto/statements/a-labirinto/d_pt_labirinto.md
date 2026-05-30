# CTBC / Unitri - Maratona de Programação (2009)

## B – Labirinto (Tutorial / Novo Editorial)

**Nome do arquivo fonte:** labirinto.c, labirinto.cpp ou labirinto.java

Nível: Iniciante. Este tutorial explica passo a passo como implementar o desenhador de labirintos.

### Passo 1: Leitura da Entrada até o EOF

O programa deve ler cada linha da entrada até o final do arquivo (EOF). Use uma estrutura como `while(scanf("%[^\n]", linha) != EOF)` em C ou `input().splitlines()` em Python para ler o dump.

### Passo 2: Estrutura de Repetição com Acumulador

Para cada linha lida, percorra-a caractere por caractere. Você precisará de uma variável **acumuladora** (ex: `total = 0`) para guardar o número de repetições.

- **Se o caractere for um dígito ('0'-'9')**: Converta-o para número e **some** ao seu `total`. 
  - Exemplo: `11X` → `total = 1 + 1 = 2`.
- **Se o caractere for uma letra ou símbolo**: Imprima esse caractere `total` vezes na tela e **resete** o `total` para zero antes de continuar.
  - Caractere 'b' → Imprima espaços (' ').
  - Caractere '!' → Imprima uma **única** quebra de linha ('\n') e ignore qualquer acumulador anterior.

### Passo 3: Identificando Entradas Vazias

Crie uma variável sinalizadora (ex: `teve_saida = falso`). Sempre que você imprimir qualquer caractere do labirinto, mude essa variável para **verdadeiro**. Se ao final da linha ela ainda for **falso**, significa que a entrada não gerou nenhum desenho. Nesse caso, imprima: `Entrada errada`.

### Passo 4: O Separador Final

Independente de a entrada ser válida ou errada, **sempre** após processar uma linha completa, imprima uma quebra de linha seguida de 13 hifens e outra quebra de linha:
`-------------`

---

### Exemplo de Lógica: `11X21b1X`

1.  Lê '1': `total = 1`.
2.  Lê '1': `total = 1 + 1 = 2`.
3.  Lê 'X': Imprime `XX`. Reseta `total = 0`. `teve_saida = verdadeiro`.
4.  Lê '2': `total = 2`.
5.  Lê '1': `total = 2 + 1 = 3`.
6.  Lê 'b': Imprime três espaços (`   `). Reseta `total = 0`.
7.  Lê '1': `total = 1`.
8.  Lê 'X': Imprime `X`. Reseta `total = 0`.
9.  Fim da linha: Imprime o separador.

| Entrada | Saída |
| --: | --: |
| 11X21b1X | XX   X |
| | ------------- |
| ddddddddd | Entrada errada |
| | ------------- |
