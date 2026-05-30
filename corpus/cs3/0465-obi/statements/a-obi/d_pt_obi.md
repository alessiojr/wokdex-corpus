# OBI — Tutorial

## Como Resolver Passo a Passo

Problemas que exigem contagem de quantos elementos cumprem uma certa condição são o padrão mais comum e clássico de introdução ao mundo da programação e aos "Laços de Repetição" (Loops). Não é necessário gravar as notas de todos os alunos em Array ou Lista, basta julgar as notas "ao vivo" logo quando elas chegam para economizar memória!

### Passo 1: Lendo as Variáveis Base
Leia da entrada padrão os primeiros dois inteiros, chamando-os de `N` (quantidade de alunos a serem lidos) e `P` (pontuação mínima).
Em seguida, inicialize uma variável `int contagem = 0` para guardar seus aprovados.

### Passo 2: O Laço de Repetição
Crie um bloco de repetição `for(int i = 0; i < N; i++)`. 
Note que este laço executará o seu interior exatamente $N$ vezes, que é a quantidade de alunos que precisamos processar.

### Passo 3: Avaliando cada competidor
Dentro do seu loop `for`, crie duas variáveis locais `X` e `Y` e as leia da entrada padrão.
Imediatamente abaixo, faça um comando `if (X + Y >= P)` (onde testamos se a soma supera ou *empata* com a nota de corte). Se a condição for verde, incremente a sua contagem: `contagem++`.

### Passo 4: O Gran-Finale
Após o término do seu bloco `for` (ou seja, fora das chaves de repetição), simplesmente dê um comando para imprimir a variável `contagem`.
Isso vai resultar na exata quantidade final de aprovados.
