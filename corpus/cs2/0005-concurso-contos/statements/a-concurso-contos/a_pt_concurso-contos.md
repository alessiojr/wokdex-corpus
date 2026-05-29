# Maratona de Programação da SBC/2016

## B – Concurso de contos

**Nome do arquivo fonte:** concurso-contos.cpp

Machado gosta muito de escrever. Já escreveu muitos contos, resenhas, relatos de viagens que fez, além de um pequeno romance. Agora Machado quer participar de um concurso de contos, que tem regras muito rígidas sobre o formato de submissão do conto.

As regras do concurso especificam o número máximo de caracteres por linha, o número máximo de linhas por página, além de limitar o número total de páginas. Adicionalmente, cada palavra deve ser escrita integralmente em uma linha (ou seja, a palavra não pode ser separada silabicamente em duas linhas). Machado quer escrever um conto com o maior número de palavras possível, dentro das regras do concurso, e precisa de sua ajuda.

Dados o número máximo de caracteres por linha, o número máximo de linhas por página, e as palavras do conto que Machado está escrevendo, ele quer saber o número mínimo de páginas que seu conto utilizaria seguindo as regras do concurso.

### Entrada

A primeira linha da entrada contém três inteiros $N$, $L$ e $C$ ($2 \le N \le 1000$, $1 \le L \le 30$ e $1 \le C \le 70$) que indicam, respectivamente, o número de palavras do conto de Machado, o número máximo de linhas por página e o número máximo de caracteres por linha. O conto de Machado é inovador e não contém nenhum caractere além de letras maiúsculas e minúsculas e espaços em branco, sem letras acentuadas e sem cedilha. A segunda linha contém o conto de Machado, composto de $N$ palavras separadas por espaços em branco; há espaço em branco somente entre duas palavras, e entre duas palavras há exatamente um espaço em branco. Cada palavra é composta por no mínimo uma e no máximo $C$ letras.

### Saída

Seu programa deve produzir uma única linha, contendo um único número inteiro, indicando o número mínimo de páginas que o conto de Machado ocupa, considerando as regras do concurso.

| Entrada | Saída |
| --: | --: |
| 14 4 20 | 2 |
| Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral | |

| Entrada | Saída |
| --: | --: |
| 16 3 30 | 1 |
| No dia seguinte entrou a dizer de mim nomes feios e acabou alcunhando me Dom Casmurro | |

| Entrada | Saída |
| --: | --: |
| 5 2 2 | 3 |
| a de i de o | |
