# Prefixa, Infixa e Posfixa

Mapear a estrutura exata de uma árvore binária a partir de percursos é um desafio comum em recuperação de dados. 

Existem três formas principais de atravessar e registrar os nós de uma árvore binária:
1. **Prefixa (Pre-order)**: Visita-se a Raiz, depois a sub-árvore Esquerda, e depois a sub-árvore Direita.
2. **Infixa (In-order)**: Visita-se a sub-árvore Esquerda, depois a Raiz, e depois a sub-árvore Direita.
3. **Posfixa (Post-order)**: Visita-se a sub-árvore Esquerda, depois a sub-árvore Direita, e por fim a Raiz.

Sua tarefa de hoje é atuar como um decodificador de redes: dadas as travessias Prefixa e Infixa de uma árvore binária desconhecida, você deve descobrir e imprimir qual seria a sua travessia Posfixa!

## Entrada
A primeira linha de entrada contém um número positivo $C$ ($C \le 2000$), que indica o número de casos de teste. 
Seguem $C$ linhas, uma para cada caso de teste. 
Cada caso de teste inicia com um número $N$ ($1 \le N \le 52$), que é a quantidade de nós na árvore. Depois haverá duas strings separadas por espaço, `S1` e `S2`, que representam as travessias Prefixa e Infixa, respectivamente.
Os nós da árvore são nomeados com caracteres distintos (sem repetições) entre 'a'...'z' e 'A'...'Z'.

## Saída
Para cada conjunto de entrada, você deve imprimir uma linha contendo a travessia posfixa da árvore binária em questão.

## Exemplos
### Exemplo de Entrada
```
3
3 xYz Yxz
3 abc cba
6 ABCDEF CBAEDF
```

### Exemplo de Saída
```
Yzx
cba
CBEFDA
```
