# Maratona de Programação da SBC 2009

## 0345 – Bakugan

**Nome do arquivo fonte:** bakugan.c

Mark e Leti adoram brincar com suas bolas Bakugan. Essas bolas são pequenas esferas de plástico com um pequeno brinquedo-monstro dentro. Quando jogada ao chão, a bola Bakugan se abre, fazendo um som incrível e liberando um monstro Bakugan assustador. Mark e Leti adoram brincar com seus monstros, mas abrir as bolas Bakugan também é bem divertido.

Cada um deles recebeu uma bolsa com bolas Bakugan e eles inventaram um jogo para abrir as bolas. Existem 10 monstros diferentes, e para o jogo Mark e Leti associaram cada monstro a um inteiro diferente de 1 a 10, de acordo com o nível de feiura do monstro. O jogo é composto de $R$ rodadas. A cada rodada:

*   Os dois jogadores jogam suas bolas ao chão simultaneamente;
*   Cada jogador acumula um número de pontos coincidente com o número associado ao monstro liberado por sua bola;
*   O primeiro (e apenas o primeiro) jogador que liberar o mesmo monstro em três rodadas consecutivas ganha 30 pontos adicionais; se essa condição acontecer na mesma rodada para ambos os jogadores então ninguém ganha pontos extras.

O vencedor do jogo é o jogador que acumular mais pontos. Por favor ajude Mark e Leti a anunciar o vencedor do jogo!

### Entrada

Cada caso de teste é descrito por três linhas. A primeira linha contém um inteiro $R$ indicando o número de rodadas do jogo ($1 \le R \le 10^5$). A segunda linha contém $R$ inteiros $M_i$ indicando os monstros liberados por Mark a cada rodada ($1 \le M_i \le 10$, para $1 \le i \le R$). A terceira linha contém $R$ inteiros $L_i$ indicando os monstros liberados por Leti a cada rodada ($1 \le L_i \le 10$, para $1 \le i \le R$).

O último caso de teste é composto por uma linha contendo zero.

### Saída

Para cada caso de teste imprima uma linha com um caractere representando o resultado do jogo: "M" caso o vencedor seja Mark, "L" caso o vencedor seja Leti, ou "T" caso haja um empate (tie).

| Entrada | Saída |
| --: | --: |
| 10 | M |
| 4 2 2 2 5 6 7 8 1 1 | |
| 1 4 4 4 1 1 1 1 2 3 | |

| Entrada | Saída |
| --: | --: |
| 5 | T |
| 3 3 3 3 2 | |
| 8 9 9 9 9 | |

| Entrada | Saída |
| --: | --: |
| 10 | L |
| 8 4 7 1 1 9 5 2 4 3 | |
| 5 6 9 7 9 4 2 3 7 4 | |

| Entrada | Saída |
| --: | --: |
| 0 | |
