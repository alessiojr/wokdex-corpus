# Cartas

Um novo game de realidade aumentada tem um mini-game de memória para ganhar pontos bônus. O jogo possui quatro cartas, formando exatamente dois pares de cartas iguais (duas cartas com um valor inteiro $N$ e duas com o valor $M$, sendo $N \neq M$).

Você já virou três das cartas. Como você sabe a regra de que existem dois pares, a carta que falta virar vai formar par com uma das três que já estão viradas. Implemente um programa que descobre qual é o número que está na carta oculta!

## Entrada
A entrada é composta por três linhas.
- A primeira contém o valor da carta $A$.
- A segunda contém o valor da carta $B$.
- A terceira contém o valor da carta $C$.
Os valores estão entre $0$ e $100$.

## Saída
Seu programa deve imprimir uma única linha contendo o número que está faltando para completar o segundo par.

## Exemplos

| Entrada | Saída |
| :-- | :-- |
| 40<br>11<br>40 | 11 |
| 8<br>8<br>96 | 96 |
