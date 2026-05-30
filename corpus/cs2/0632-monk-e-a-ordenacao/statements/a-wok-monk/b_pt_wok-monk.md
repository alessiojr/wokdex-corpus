# Logística Galáctica: Ordenação de Contêineres

![Hangar da Estação Espacial](../assets/monk_logistics.png)

Monk está organizando uma lista de $N$ códigos de naves espaciais para o Grande Desfile Intergaláctico. Cada nave possui um identificador numérico (identificador de até 18 dígitos). Para organizar a frota de forma eficiente, ele utiliza um algoritmo que processa os identificadores em blocos de 5 dígitos, da direita para a esquerda.

A cada passo $i$ (começando em $i=1$):
1. Extraia o $i$-ésimo bloco de 5 dígitos de cada identificador. O primeiro bloco compreende os dígitos das posições 1 a 5 (unidade a dezena de milhar), o segundo de 6 a 10, e assim por diante. Se um número não possuir dígitos em certas posições, considere-os como 0.
2. Se o valor do bloco extraído de **todos** os identificadores for igual a zero, o processo termina e o desfile está pronto.
3. Caso contrário, ordene a lista de naves de forma **estável** com base no valor do bloco extraído (pesos).
4. Imprima a configuração atual da frota após a ordenação.

Sua missão é automatizar este sistema de organização para Monk.

## Entrada

A primeira linha contém um inteiro $N$ ($1 \le N \le 10^6$), o número de naves.
A segunda linha contém $N$ inteiros $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$), os identificadores das naves.

## Saída

Imprima o estado do array de identificadores após cada iteração de ordenação. Cada estado deve estar em uma nova linha, com os elementos separados por espaço.

## Restrições

- $1 \le N \le 10^6$
- $-10^{18} \le A_i \le 10^{18}$
- Atenção ao tempo limite de execução.

## Exemplos

| Entrada | Saída |
| :--- | :--- |
| `3`<br>`213456789 167890 123456789` | `213456789 123456789 167890 `<br>`167890 123456789 213456789 ` |
