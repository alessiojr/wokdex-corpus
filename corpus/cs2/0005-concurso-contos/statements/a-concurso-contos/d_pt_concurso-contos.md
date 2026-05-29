# Maratona de Programação da SBC/2016

## B – Concurso de contos (Tutorial)

Este guia explica como implementar uma solução eficiente para o problema de diagramação de contos usando uma abordagem de simulação.

### Tutorial: Passo a Passo

O segredo deste problema é simular o processo de escrita palavra por palavra, preenchendo as linhas de forma "gulosa" (colocando o máximo possível em cada linha).

#### 1. Estrutura de Dados e Variáveis
Você precisará de três contadores principais:
- `paginas`: Começa em 1 (já que sempre haverá pelo menos uma página).
- `linhas_atuais`: Começa em 1 (a primeira página começa com a primeira linha).
- `caracteres_atuais`: Começa em 0 (espaço ocupado na linha atual).

#### 2. Processando as Palavras
Para cada palavra de comprimento `len`:

- **Se for a primeira palavra da linha**:
    O espaço ocupado será exatamente `len`.
- **Se não for a primeira palavra da linha**:
    O espaço ocupado será `len + 1` (devido ao espaço em branco obrigatório antes da palavra).

#### 3. Mudança de Linha e Página
Para cada palavra, verifique se ela cabe na linha atual:
- **Se cabe** (`caracteres_atuais + (primeira ? len : len + 1) <= C`): 
    Atualize `caracteres_atuais`.
- **Se NÃO cabe**:
    - A palavra deve ir para a próxima linha (`linhas_atuais++`).
    - O novo valor de `caracteres_atuais` será apenas o comprimento da palavra (`len`).
    - **Verificação de Página**: Se ao mudar de linha, o novo `linhas_atuais` ultrapassar o limite $L$:
        - Resetamos `linhas_atuais` para 1.
        - Incrementamos o contador de `paginas`.

#### Dica de Implementação
Em linguagens como C++ ou Java, você pode ler as palavras uma a uma usando `cin >> word` ou `Scanner.next()`. Isso facilita o processamento sem precisar lidar com a string completa do conto de uma vez.

---

### Entrada

- $N$: número de palavras.
- $L$: linhas por página.
- $C$: caracteres por linha.
- O conto: $N$ palavras separadas por espaços.

### Saída

O total de páginas calculado pela simulação.

### Exemplos de Entrada e Saída

| Entrada | Saída |
| :--- | :--- |
| 14 4 20<br>Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral | 2 |
| 16 3 30<br>No dia seguinte entrou a dizer de mim nomes feios e acabou alcunhando me Dom Casmurro | 1 |
| 5 2 2<br>a de i de o | 3 |
