# Cartas — Tutorial

## Como Resolver Passo a Passo

O problema testa os conhecimentos básicos de estruturas de controle e condicionais `if / else`. Você possui apenas três variáveis e precisa descobrir quem é a "diferente" (já que o jogo te garante que existem 2 pares e você já puxou 3 cartas, então com certeza 2 das cartas que você puxou formam o primeiro par).

### O Teste Lógico
Basta ler as três variáveis inteiras $A$, $B$ e $C$.
A estrutura do `if/else` deve cobrir exatamente os 3 cenários de organização das cartas:

```cpp
// Cenário 1: Se a 1ª e a 2ª carta formam o par, 
// a "diferente" é a 3ª.
if (A == B) {
    imprime C;
}
// Cenário 2: Se a 1ª e a 3ª carta formam o par, 
// a "diferente" é a 2ª.
else if (A == C) {
    imprime B;
}
// Cenário 3: Se não for nenhuma das opções acima,
// as cartas que formam o par são obrigatoriamente
// a 2ª e a 3ª. Logo, a "diferente" é a 1ª.
else {
    imprime A;
}
```

### O Truque Supremo do XOR
Se você já domina operações a nível de Bits (Bitwise), o operador XOR (`^`) resolve esse problema em uma linha!
O XOR possui uma propriedade matemática incrível: todo número submetido a um XOR com ele mesmo se anula e vira zero ($X \oplus X = 0$). Todo número submetido a XOR com Zero continua ele mesmo ($X \oplus 0 = X$).
Portanto, as duas cartas iguais vão se anular e só vai sobrar a carta faltante.

Basta fazer a operação:
`imprima A ^ B ^ C`
