# Computação de Dobra Espacial

A nave estelar Wok-Enterprise está prestes a saltar para o hiperespaço. O motor de dobra opera dobrando o tecido do espaço-tempo, criando uma ponte de Einstein-Rosen.

Para calcular a energia necessária em MegaJoules, o computador de bordo precisa somar as distâncias vetoriais relativísticas de dois setores adjacentes. Devido à dilatação temporal em velocidades próximas à da luz ($c \approx 3 \times 10^8 m/s$), as coordenadas podem parecer confusas, mas para este salto de curto alcance, podemos ignorar o Tensor de Ricci e a Curvatura de Riemann.

O Capitão precisa apenas da distância linear total de viagem (Sector X + Sector Y) para autorizar a ignição. Ignore as flutuações quânticas do vácuo.

## Entrada
O computador fornece dois valores inteiros $X$ e $Y$, representando a distância em anos-luz dos dois setores.
*Domínio: $-10^4 \leq X, Y \leq 10^4$*

## Saída
Um único número inteiro representando a distância total do salto.

## Exemplos
| Entrada | Saída |
| :--- | :--- |
| 2<br>7 | 9 |

| Entrada | Saída |
| :--- | :--- |
| 10<br>5 | 15 |
