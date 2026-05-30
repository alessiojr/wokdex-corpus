# Toca do Saci

Para resolver o problema perfeitamente em $O(N \times M)$ sem dar erros de compilação ou de estourar a matriz, siga esta receita:

1. **Leitura e Guarda de Matriz:** Crie uma matriz gigante e a preencha. Durante a leitura, anote as coordenadas X e Y onde você encontrou o valor `3` (Saída). 
   *Por que começar da saída e ir pra Emília?* Porque dá no mesmo! O caminho é único, a quantidade de passos é igual e você encerra quando pisar numa célula de valor `2`.
2. **Vetores de Direção:** Evite fazer 4 grandes `if`s (cima, baixo, esquerda, direita). Use a técnica dos Vetores de Movimento. Dois pequenos arrays: `X_direcoes = {0, 0, 1, -1}` e `Y_direcoes = {1, -1, 0, 0}`.
3. **Pão de Migalhas:** Em cada passo válido, destrua a sala atual fazendo com que ela vire `0`. Isso impede o seu código de andar para trás e ficar num loop infinito voltando para a sala anterior!
