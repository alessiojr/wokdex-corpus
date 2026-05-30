# Bakugan (Nível C — Educacional)

Neste problema, o objetivo é simular uma partida de Bakugan entre Mark e Leti e determinar o vencedor após $R$ rodadas.

### Dica Estratégica: Simulação Direta

Como o número de rodadas $R$ pode ser de até $10^5$, e para cada rodada fazemos apenas operações simples, uma **Simulação Direta** ($O(R)$) é a abordagem ideal.

1.  **Pontuação Base**: Em cada rodada, cada jogador ganha o número de pontos do monstro que liberou.
2.  **O Bônus de 30 Pontos**: Este é o ponto crucial. Você deve identificar quem completa três rodadas seguidas com o mesmo monstro **primeiro**.
    -   Se Mark conseguir isso na rodada $i$ e Leti ainda não conseguiu, Mark ganha o bônus.
    -   Se Leti conseguir na rodada $i$ e Mark ainda não conseguiu, Leti ganha o bônus.
    -   **Importante**: Se ambos conseguirem pela primeira vez **na mesma rodada $i$**, ninguém ganha o bônus de 30 pontos.

**Complexidade Sugerida**: $O(R)$ no tempo e $O(R)$ no espaço (para armazenar as jogadas).
