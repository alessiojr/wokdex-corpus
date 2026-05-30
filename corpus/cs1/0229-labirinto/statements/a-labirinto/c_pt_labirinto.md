# CTBC / Unitri - Maratona de Programação (2009)

## B – Labirinto (Edição Educacional)

**Nome do arquivo fonte:** labirinto.c, labirinto.cpp ou labirinto.java

Este problema desafia sua capacidade de processamento de strings e interpretação de regras de codificação simples para gerar saídas visuais.

### O Desafio

Você deve reconstruir um labirinto a partir de uma linha de entrada comprimida. Cada caractere no labirinto é precedido por um ou mais dígitos que indicam sua contagem.

### Dica de Estratégia: Processamento Sequencial

A estratégia ideal para este problema é o **processamento sequencial (greedy)** da string de entrada:

1.  **Acumulação de Dígitos**: Ao encontrar um dígito, converta-o para valor numérico e adicione-o a um acumulador (`total`). Se houver múltiplos dígitos seguidos (ex: `12A`), o total será a soma (`1+2=3`, resultando em `AAA`).
2.  **Expansão de Caracteres**: Ao encontrar um caractere (não dígito), repita-o na saída `total` vezes. 
    *   **Importante**: Se o acumulador for zero ao encontrar um caractere, esse caractere deve ser ignorado.
3.  **Delimitadores de Linha**: O caractere `!` indica que uma **única** nova linha deve ser iniciada no labirinto impresso (mesmo se houver números antes dele).
4.  **Tratamento de Espaços**: Lembre-se que `b` deve ser traduzido como espaço (' ').

### Complexidade Esperada

A solução deve processar a entrada em uma única passagem. A complexidade de tempo é **O(N)**, onde N é o comprimento da string de entrada somado ao número de caracteres gerados na saída.

### Caso Especial: Entrada Vazia

Se após processar toda uma linha de entrada nenhum caractere for impresso (por falta de dígitos ou formato inválido), o programa deve imprimir a mensagem: `Entrada errada`.

---

### Exemplos de Entrada e Saída

| Entrada | Saída |
| --: | --: |
| 11X21b1X!4X1b1X | XX   X |
| | XXXX X |
| | ------------- |

| Entrada | Saída |
| --: | --: |
| ddddddddd | Entrada errada |
| | ------------- |
