# Cachorros-quentes

Em 2012 foi alcançado um novo recorde mundial na famosa Competição de Cachorros-Quentes do Nathan: o campeão, Joey Chestnut, devorou 68 cachorros-quentes em dez minutos, um aumento incrível em relação aos 62 sanduíches devorados pelo mesmo Chestnut em 2011.

O restaurante Nathan's Famous Corporation, localizado no Brooklyn, NY, é o responsável pela competição. Eles produzem deliciosos cachorros-quentes, mundialmente famosos, mas quando o assunto é matemática eles não são tão bons. Eles desejam ser listados no Livro de Recordes do Guinness, mas para isso devem preencher um formulário descrevendo os fatos básicos da competição. Em particular, eles devem informar o número médio de cachorros-quentes consumidos pelos participantes durante a competição.

Você pode ajudá-los? Eles prometeram pagá-lo com um dos seus saborosos cachorros-quentes. Dados o número total de cachorros-quentes consumidos e o número total de participantes na competição, você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos participantes.

### Passo a Passo

O desafio requer simplesmente o cálculo da **média** de cachorros-quentes por participante. O cálculo matemático de uma média básica dadas as somas é clássico: `Média = Total de itens / Quantidade de participantes`. 

Mas preste atenção à construção do fluxo do código:

1. **Leitura**: Você irá receber num único momento dois números. O primeiro é `H` (o total devorado) e o segundo é `P` (quantos competidores haviam). Comece lendo-os para variáveis no seu código.
2. **A Divisão (O Cuidado Crítico)**: A maioria das linguagens de programação fortemente tipadas (como C, C++ ou Java), ao dividir dois Inteiros (ex: 10 / 90), vai assumir que você também quer um resultado Inteiro de volta. Isso causaria o corte das frações e o retorno de resultado truncado (Zero, nesse exato exemplo). Para ter os decimais precisos, você deve aplicar o *casting*, transformando pelo menos uma das variáveis para real (como `float` ou `double`) no exato momento da divisão (ex: `(double)H / P`). Observação: em linguagens mais dinâmicas como Python e JS, ou dividindo com operadores específicos, este corte automático não ocorre.
3. **Formatação e Arredondamento da Saída**: O resultado precisa ser exibido obedecendo a regra imposta: na tela, devem saltar exatamente 2 dígitos após a vírgula/ponto, não importando a dízima. Lembre-se, as linguagens já fazem o arredondamento ideal por baixo dos panos se você mandar imprimir o ponto flutuante limitando nas casas decimais usando a saída parametrizada padrão (exemplo no C ou Java: `.printf("%.2f\n", media)`).
4. Ao final, jogue o resultado no console com a quebra de linha necessária.

## Entrada

A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤ H, P ≤ 1000) indicando respectivamente o número total de cachorros-quentes consumidos e o número total de participantes na competição.

## Saída

Seu programa deve produzir uma única linha com um número racional representando o número médio de cachorros-quentes consumidos pelos participantes. O resultado deve ser escrito como um número racional com exatamente dois dígitos após o ponto decimal, arredondado se necessário.

| Entrada | Saída |
| :-- | :-- |
| 10 90 | 0.11 |

| Entrada | Saída |
| :-- | :-- |
| 840 11 | 76.36 |

| Entrada | Saída |
| :-- | :-- |
| 1 50 | 0.02 |

| Entrada | Saída |
| :-- | :-- |
| 34 1000 | 0.03 |

| Entrada | Saída |
| :-- | :-- |
| 35 1000 | 0.04 |

| Entrada | Saída |
| :-- | :-- |
| 36 1000 | 0.04 |
