# Bakugan (Nível D — Tutorial)

Para resolver o problema **Bakugan**, vamos seguir um passo a passo para calcular as pontuações e o bônus de 30 pontos.

### Lógica Passo a Passo

1.  **Entrada**: Leia o número de rodadas $R$. Crie dois vetores (ou listas) para armazenar os monstros de Mark e Leti em cada rodada. Continue lendo até que $R = 0$.
2.  **Soma Inicial**: Some todos os valores do vetor de Mark para obter a pontuação base dele. Faça o mesmo para Leti.
3.  **Localizar o Bônus**: Precisamos encontrar a primeira rodada $i$ onde alguém consegue três monstros iguais seguidos. Percorra as rodadas de $3$ até $R$:
    -   Verifique se Mark tem bônus na rodada $i$: `M[i] == M[i-1]` e `M[i] == M[i-2]`.
    -   Verifique se Leti tem bônus na rodada $i$: `L[i] == L[i-1]` e `L[i] == L[i-2]`.
4.  **Decidir quem ganha o bônus**:
    -   Se **apenas Mark** conseguiu o bônus na rodada $i$, adicione 30 pontos ao total de Mark e pare a busca (o bônus é dado apenas uma vez).
    -   Se **apenas Leti** conseguiu o bônus na rodada $i$, adicione 30 pontos ao total de Leti e pare a busca.
    -   Se **ambos** conseguiram o bônus na mesma rodada $i$ pela primeira vez, então ninguém ganha os 30 pontos. Pare a busca.
5.  **Resultado**: Compare os totais finais:
    -   Se `Total_Mark > Total_Leti` $\rightarrow$ imprima "M".
    -   Se `Total_Leti > Total_Mark` $\rightarrow$ imprima "L".
    -   Se for igual $\rightarrow$ imprima "T".

### Exemplo Prático

Mark: `4 2 2 2 ...`
Na rodada 3, Mark tem `M[1]=4, M[2]=2, M[3]=2`. Não são iguais.
Na rodada 4, Mark tem `M[2]=2, M[3]=2, M[4]=2`. **Bônus detectado!**
Se Leti não tiver conseguido o bônus na rodada 3 nem na rodada 4, Mark ganha os 30 pontos extras.
