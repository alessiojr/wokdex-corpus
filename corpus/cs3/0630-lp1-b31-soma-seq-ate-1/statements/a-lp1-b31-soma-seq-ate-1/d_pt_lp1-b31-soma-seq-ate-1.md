# Soma de Valores — Tutorial

## Como Resolver Passo a Passo

Esse é o clássico exercício introdutório de "Laço Condicional por Flag Sentinela". O padrão "Sentinela" ocorre quando nós não sabemos quantas leituras faremos (poderia ser uma, poderiam ser milhares), e o programa só sabe que deve parar quando encontra um "sinal/flag" — que neste caso é o número `-1`.

### Passo 1: As Variáveis
Crie a variável `int soma = 0` para atuar como nossa caixinha acumuladora de valores.
Crie também uma variável `int X;` que será usada para ler o número temporário em cada passo.

### Passo 2: O Laço Infinito
Para que um laço rode indefinidamente (até a gente ativamente pará-lo com um `break`), usaremos a estrutura `while`.
```cpp
while (true) {
    // Código infinito
}
```

### Passo 3: O Guardião Sentinela
O que fará o programa não rodar para todo o sempre é o que chamamos de Sentinela. Ele se posiciona logo após a leitura da variável, assim, se o sinal tocar, ele interrompe tudo imediatamente (inclusive impedindo que a variável lida `-1` vá parar dentro da `soma`).
```cpp
while (true) {
    cin >> X;          // Leia da entrada do console
    
    if (X == -1) {     // A Sentinela tocou! Fomos avisados pra parar!
        break;         // Quebra e destrói o laço imediatamente
    }
    
    soma = soma + X;   // Se não tocou, continue normalmente acumulando o número lido
}
```

### Passo 4: O Impresso
Fora do bloco `while`, ou seja, o ponto para qual o programa irá fugir quando o `break` for ativado, você apenas precisa imprimir a formatação exata que o professor pediu:
`cout << "A soma dos valores eh: " << soma << endl;`
E pronto!
